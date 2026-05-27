---
name: ai-publishing-house
description: >-
  The master orchestrator for the AI Publishing House plugin. Drives the novel
  creation pipeline end-to-end — checks vault state, validates outputs, invokes
  each skill in sequence via the Skill tool, and pauses only at the 5 user
  decision points. Trigger this first at the start of every session. Also use
  it to start a new book, switch between books, resume from any step, or
  check pipeline status.
---

# AI Publishing House — Master Orchestrator

The agentic driver for the novel-creation pipeline. This skill operates in three modes:

- **Active mode** — invoke each pipeline skill via the Skill tool, validate output between steps, pause only at decision points or on failure.
- **Status mode** — read the vault and report progress without chaining.
- **Resume mode** — pick up an in-progress book and continue active mode from the first pending step (including partial-chapter recovery in Step 8).

> **Maintainer note:** The Pipeline Registry below and `scripts/pipeline_validator.py` are the source of truth. When you add a skill, change an output filename, or add a decision point, update both together — they must stay in sync.

---

## The Fiction Library Vault

All book output files live in the Fiction Library vault. The vault path is set in `plugin.json` under `config.vaultPath` (default: `C:\Users\HP\Documents\Fiction Library`).

Each book has its own folder inside the vault. The folder is created by `/novel-genre-picker` (Step 1) using a working project slug.

```
Fiction Library/
└── [book-slug]/
    ├── story-config.md
    ├── story-seed.md
    ├── 3-act-outline.md
    ├── book-title.md
    ├── world/
    │   ├── world-map.md
    │   ├── settings/
    │   └── characters/
    │       ├── character-list.md
    │       └── bios/
    ├── [book-title]-chapter-map.md
    ├── chapters/
    │   ├── chapter-01.md
    │   └── ...
    ├── manuscript-final.md
    └── book-cover-prompt.md
```

---

## Pipeline Registry

Source of truth. Each row lists the step, skill to invoke, output file(s), whether it's a decision point (where the workflow MUST pause), and the validator step number.

| Step | Skill | Output file(s) | Decision point? | Validator step |
|---|---|---|---|---|
| 1 | `/novel-genre-picker` | `story-config.md` | YES (sub-genre + slug, then archetype stack) | 1 |
| 2 | `/novel-story-seed-writer` | `story-seed.md` | YES (story sketch input) | 2 |
| 3 | `/novel-3-act-outliner` | `3-act-outline.md` | No (auto) | 3 |
| 4 | `/build-the-world` | `world/world-map.md` + settings + character bios | YES (world name pick) | 4 |
| 5 | `/outline-architect` | `3-act-outline.md` upgraded with `## Macro Architecture` | No (auto) | 5 |
| 6 | `/book-title-generator` | `book-title.md` | YES (title pick) | 6 |
| 7 | `/novel-chapter-mapper` | `[book-title]-chapter-map.md` | No (auto) | 7 |
| 8 | `/novel-chapter-drafter` | `chapters/chapter-01.md` ... `chapter-NN.md` | No (production run — supports resume) | 8 |
| 9 | `/novel-editor` | `chapters/*` (edited in place) | No (production run) | 9 |
| 10 | `/novel-publisher` | `manuscript-final.md` | No (auto) | 10 |
| 11 | `/book-cover-prompt-generator` | `book-cover-prompt.md` | No (auto, terminal) | 11 |

Decision points (Steps 1, 2, 4, 6) are the ONLY moments where the agentic workflow pauses for user input. Between these, every skill runs end-to-end without manual confirmation.

---

## Intent Detection

Infer intent from how the orchestrator was invoked:

| Invocation | Intent | Behavior |
|---|---|---|
| `/start-book` | `new` | Skip vault scan. Invoke Step 1 immediately. |
| `/continue-book` | `continue` | Scan vault, pick book, enter auto-chain from first pending step. |
| `/check-progress` | `status` | Scan vault, report status table. Do NOT chain. |
| `/resume-from N` | `jump-to-N` | Scan vault, pick book, redo Step N. |
| User says "start a new book" | `new` | Same as `/start-book`. |
| User says "continue" / "where did I leave off" | `continue` | Same as `/continue-book`. |
| User asks "status" / "where am I" | `status` | Same as `/check-progress`. |

If intent is ambiguous, ask once:
> "Are you starting a new book, continuing an existing one, or just checking status?"

---

## Active Mode — The Auto-Chain Loop

Core agentic behavior. After detecting intent and the next pending step, run:

1. **Invoke the next skill via the Skill tool**, passing auto-chain context:
   > "Invoking `/[skill-name]` in auto-chain mode for book at `[book-folder]`. End with the agentic handoff line."
2. **Wait for the skill to return** with the canonical handoff line `Step [N] complete. Output: [filepath]`.
3. **Run the validator:**
   ```
   uv run [plugin-root]/scripts/pipeline_validator.py --book-dir "[book-folder]" --step [N]
   ```
4. **Branch on the result:**
   - Exit code 0 (OK): set N = N+1. If N > 11, report pipeline complete with final outputs. Otherwise loop back to step 1.
   - Exit code 1 (FAIL): STOP. Show the validator's reason. Ask the user whether to retry Step N or fix the file manually.

Decision-point skills (Steps 1, 2, 4, 6) handle their own user-input pauses internally — the orchestrator does not need separate logic, just wait for the handoff line.

---

## State Detection

To find the next pending step for any book:

```
uv run [plugin-root]/scripts/pipeline_validator.py --book-dir "[book-folder]" --check-state
```

Returns either a step number with skill name (e.g., `6 (book-title-generator)`) or the literal string `complete`.

For a full status report:

```
uv run [plugin-root]/scripts/pipeline_validator.py --book-dir "[book-folder]" --all
```

---

## Partial-Chapter Recovery (Step 8)

Step 8 (`/novel-chapter-drafter`) is the longest-running step. If a user stops mid-draft:

1. The validator counts files in `chapters/` and compares to the chapter map total.
2. If `chapters/` has N files and the map has M (N < M), the validator reports: `Resume from chapter-[N+1].md`.
3. When invoking `/novel-chapter-drafter`, pass this resume context:
   > "Invoking `/novel-chapter-drafter` in auto-chain resume mode. Existing chapters: chapter-01 through chapter-[N]. Resume from chapter-[N+1].md."
4. The drafter skips existing files and begins at chapter [N+1].

The same resume logic applies to Step 9 if the editor was interrupted (less common since editing per chapter is faster).

---

## Mode 1 — Starting a New Book (`new`)

1. Skip vault scan.
2. Invoke `/novel-genre-picker` in auto-chain mode. No book folder yet — the genre picker creates it from the user-provided slug.
3. The genre picker handles its two internal decision points (sub-genre+slug, then archetype stack).
4. When the genre picker returns with `Step 1 complete. Output: [book-folder]/story-config.md`, extract the book folder path.
5. Enter the auto-chain loop from Step 2 with that book folder.

---

## Mode 2 — Continuing an Existing Book (`continue`)

1. List all folders in `vaultPath` (each is a book).
2. If exactly one book exists, use it. If multiple, present a numbered list and ask the user which.
3. Run `--check-state` against that book folder.
4. If state is `complete`, report success and the manuscript path. Stop.
5. Otherwise enter the auto-chain loop starting at the reported next step.
6. If the reported step is 8 with partial chapters, pass the resume context to the drafter.

---

## Mode 3 — Status Check (`status`)

1. List all folders in `vaultPath`.
2. For each, run `--all` to build the per-book status table.
3. Display a summary: book name, current step, % complete (steps done / 11), last modified.
4. Do NOT invoke any pipeline skill.

---

## Mode 4 — Jump to a Specific Step (`jump-to-N`)

1. Pick a book (Mode 2 logic).
2. Confirm with user: "You want to redo Step N (`/skill-name`) for book `[name]`. This will overwrite the existing output file(s). Continue?"
3. If yes:
   - To redo just that step: invoke the single skill in auto-chain mode, validate, then stop.
   - To redo from that step onward: invoke the skill, then continue the auto-chain loop from Step N+1.
   - Ask the user which they want.

---

## Decision Points — Where the Workflow Pauses

The orchestrator pauses for user input ONLY at:

1. **Step 1, Part A** — sub-genre + project slug (inside `/novel-genre-picker`)
2. **Step 1, Part C** — archetype stack confirmation (inside `/novel-genre-picker`)
3. **Step 2** — story sketch input (inside `/novel-story-seed-writer`)
4. **Step 4** — world name pick from 20 options (inside `/build-the-world`)
5. **Step 6** — title pick from 8-10 candidates (inside `/book-title-generator`)

These pauses are handled by the child skills themselves. The orchestrator's job is to invoke the skill and wait for the handoff line — not to second-guess the pause logic.

Between these moments, every skill runs to completion without confirmation prompts. The orchestrator does not ask "are you ready for Step N?" — it just runs Step N.

---

## The Author Voice Guide

The Author Voice Guide lives at `[plugin-root]/references/author-voice-guide.md`. Every prose-writing skill reads it before execution. The orchestrator does not write prose — but if the user asks about voice or style, refer them there.

---

## What This Skill Does NOT Do

- It does not write prose or modify story files.
- It does not skip validation. If the validator fails, the chain stops.
- It does not invent decisions. Anything the user must decide (genre, title, world name, archetype stack, story sketch) is delegated to the child skill that owns that decision.
- It does not run all the way through silently — it reports what step it's on as it goes.
