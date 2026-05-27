---
name: novel-chapter-drafter
description: >-
  Drafts all chapters in sequence as a production run — reads the chapter map,
  loads the relevant character bios, world settings, and Author Voice Guide for
  each chapter, then writes every chapter to chapters/chapter-NN.md without
  stopping. The next step is /novel-editor.
---

# Novel Chapter Drafter

A production-run skill. It does not stop between chapters. It reads the chapter map, loads what it needs for each chapter, drafts the prose, writes the file, and moves immediately to the next chapter. When it finishes, every chapter file exists and is ready for editing.

---

## Before You Begin

Confirm all of the following exist in the active book's working directory:

- `story-config.md` — sub-genre and plot archetypes
- `story-seed.md` — C/W/D/A/C breakdown and expanded seed
- `3-act-outline.md` — seasoned outline (confirmed by `## Macro Architecture` section)
- `[book-title]-chapter-map.md` — complete chapter-by-chapter map from `/novel-chapter-mapper`
- `world/characters/character-list.md` and all files in `world/characters/bios/`
- All setting files in `world/settings/`

If any are missing, stop and name what is missing before proceeding.

---

## How the Production Run Works

1. Read `[book-title]-chapter-map.md` in full — all chapters, all entries
2. Count the total chapters
3. Tell the user: "Drafting [N] chapters. Starting now."
4. Draft each chapter from Chapter 1 to Chapter N in order, without pausing
5. After all chapters are written, report the summary

Do not stop between chapters to ask for feedback or approval. This is a drafting run, not a review session. The editing pass comes after.

---

## For Each Chapter

### Step 1: Load the Chapter Map Entry

From `[book-title]-chapter-map.md`, read the entry for this chapter:
- Working title
- Beat assignment
- Setting (specific location)
- Target word count
- Opening style
- Ending style
- Chapter MICE thread
- Try-Fail cycle (type + Try + Outcome)

### Step 2: Load the Character Bios

Identify which characters appear in this chapter based on the beat and Try-Fail. Load their biography files from `world/characters/bios/[character-name].md`.

Focus on:
- Their contradiction (this creates tension in the scene)
- Their want (this drives their behavior)
- Their dialogue patterns and quirks
- Their most prized possession (use as an object of vulnerability if relevant)

### Step 3: Load the Setting File

Load `world/settings/[location-name].md` for the chapter's assigned setting.

Use the setting's physical details to anchor the chapter's sensory layer — geography, architecture, climate, sounds, smells. The setting should feel lived-in, not described.

### Step 4: Read the Author Voice Guide

Read `references/author-voice-guide.md` — all 14 rules. Apply them throughout the draft.

Key rules to apply at the chapter level:
- **Rule #1** — The first sentence is the assigned opening style: a single sentence that establishes Who, Where, and Genre/Mood
- **Rule #5** — The final sentence matches the assigned ending style
- **Rule #7** — Dialogue moves past each other, not at each other. Characters do not explain the plot to each other.
- **Rule #14** — Pronouns disappear the character. Use character names, not she/he, where possible.

---

## Writing the Chapter

### Word Count

Hit the target word count from the chapter map. Default is ~1,200 words. Do not pad — earn every word.

### Structure

The chapter's structure is driven by the Try-Fail cycle:
- **Try** — the protagonist attempts what the chapter map specifies
- **Outcome** — the result lands as the chapter map specifies (Yes-but / No-and / Yes-and / No-but / Yes-and-but-cost)

The Try-Fail is not the entire chapter. It is the spine. Build the scene around it: establish the setting, bring the characters in, raise the stakes, execute the Try, land the Outcome.

### MICE Thread

The chapter's MICE annotation (from the chapter map) tells you what structural work this chapter does:
- **OPENS** — introduce the thread's question or disruption early in the chapter
- **SUSTAINS** — escalate, complicate, or stretch the thread through the chapter's action
- **CLOSES** — resolve the thread's question or establish the new status quo by the chapter's end

### Prose Quality

Apply all 14 Author Voice Guide rules. Specifically:
- Use the 15 poetry mechanisms (Rule #4) at moments of emotional weight — not throughout, but at peaks
- Use objects, moments, and small actions as emotional proxies (Rule #8) — do not state feelings directly
- Capture subculture and inside perspective (Rule #9) — the character's world has its own language and hierarchy
- Vary sentence rhythm (Rule #3) — short sentences at peaks, longer sentences in the flow

---

## Output

Write each chapter to: `chapters/chapter-[NN].md` in the active book's working directory.

Use zero-padded numbering: `chapter-01.md`, `chapter-02.md`, ..., `chapter-12.md`.

Format for each file:
```markdown
# Chapter [N]: [Working Title]

[Chapter prose — no metadata, no notes, no headers within the chapter body]
```

Write the file immediately after drafting each chapter. Then move to the next chapter without stopping.

---

## End of Production Run

After all chapters are written, report:

| | |
|---|---|
| **Total chapters drafted** | [N] |
| **Total estimated word count** | ~[X] words |
| **Chapter files written** | `chapters/chapter-01.md` → `chapters/chapter-[NN].md` |

The next step is `/novel-editor`.

---

## Operating Principles

1. **Production run — no stopping.** Draft all chapters in sequence. Do not pause for review. The editing pass is a separate skill.
2. **Chapter map is the blueprint.** Every structural decision (setting, Try-Fail, MICE, opening/ending style) comes from the chapter map. Do not deviate from it.
3. **Author Voice Guide is the writing standard.** Every sentence should be held against it.
4. **Show, don't state.** Use objects, actions, and dialogue to carry emotion. Never write "she felt sad" when an action can carry it.
5. **The setting is active, not described.** Characters move through settings. Settings create obstacles, pressure, and atmosphere. They are not backdrops.
6. **Dialogue past each other.** Characters have agendas. They do not cooperate to explain the story to the reader.

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after all chapters are drafted end with the exact line:

> **Step 8 complete. Output: `[book-folder]/chapters/chapter-01.md` through `chapter-NN.md` ([N] chapters drafted)**

If the orchestrator passed in a partial-resume context (e.g., "resume from chapter-06"), begin drafting at that chapter rather than chapter-01 and skip any chapters that already exist.

The orchestrator will then run `pipeline_validator.py --step 8` and route to Step 9 (`/novel-editor`). When invoked manually by the user, end as described in the End of Production Run section above.
