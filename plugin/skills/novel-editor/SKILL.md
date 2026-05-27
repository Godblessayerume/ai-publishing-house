---
name: novel-editor
description: >-
  Edits every drafted chapter in sequence against all 14 Author Voice Guide
  rules — rewrites sentences and paragraphs that violate the rules, edits
  in place, and reports what changed per chapter. The next step is
  /novel-publisher.
---

# Novel Editor

An editing-pass skill. It reads each chapter file, checks it against all 14 rules in the Author Voice Guide, rewrites violations, saves the file in place, and reports what changed. It does not add new content — it refines what exists.

---

## Before You Begin

Confirm all of the following exist in the active book's working directory:

- All chapter files in `[title-folder]/chapters/` — produced by `/novel-chapter-drafter`
- `references/author-voice-guide.md` — the 14 rules
- `[title-folder]/[book-title]-chapter-map.md` — to verify opening style, ending style, and Try-Fail for each chapter

**Finding the title folder:** Read `book-title.md` at the book root, extract the `Final Title:` value, sanitize it (replace `:` with ` -`, remove `< > " / \ | ? *`). The title folder was created by Step 6.

If any chapter files are missing, stop and run `/novel-chapter-drafter` first.

---

## How the Editing Pass Works

1. List all files in `[title-folder]/chapters/` in order (`chapter-01.md` → `chapter-NN.md`)
2. Tell the user: "Editing [N] chapters. Starting now."
3. Edit each chapter in sequence without pausing
4. After all chapters are edited, report the full summary

Do not stop between chapters. This is a pass, not a review session. The user reviews after the full pass is complete.

---

## For Each Chapter

### Step 1: Read the Chapter

Read the full chapter file.

### Step 2: Read the Chapter Map Entry

From `[title-folder]/[book-title]-chapter-map.md`, read this chapter's entry. Confirm:
- Assigned opening style (Rule #1 check)
- Assigned ending style (Rule #5 check)
- Try-Fail type (Rule #13 check for climax chapters)

### Step 3: Check Against All 14 Rules

Read `references/author-voice-guide.md`. Apply each rule as a lens:

**Rule #1 — Single-sentence opener**
The first sentence must be a single sentence establishing Who, Where, and Genre/Mood. Check: does it match the assigned opening style from the chapter map? If not, rewrite it.

**Rule #2 — Action/Explanation/Description combinations**
Prose should combine action, explanation, and description in the right ratio for the scene's tempo. Rewrite passages that are pure description with no action, or pure action with no grounding.

**Rule #3 — Rhythm and pacing**
Short sentences at dramatic peaks. Longer sentences in flowing passages. Check for monotonous sentence length — if five consecutive sentences are the same length, vary them.

**Rule #4 — Poetry mechanisms**
Check that at least 3–5 of the 15 mechanisms (alliteration, polyptoton, antithesis, merism, blazon, synesthesia, aposiopesis, hyperbaton, anadiplosis, periodic sentences, parataxis, hypotaxis, diacope, rhetorical question, hendiadys) appear at emotional peaks. Do not force them throughout — only at peaks.

**Rule #5 — Ending style**
The final sentence must match the assigned ending style from the chapter map. If it doesn't, rewrite the closing line.

**Rule #6 — Voice blend**
Check that the prose blends the voice percentages: 50% Patterson (short, punchy, propulsive), 20% Nabokov (precise, sensory, layered), 20% Hemingway (restrained, iceberg, earned), 10% DFW (inside-perspective, footnote-consciousness, meta-awareness). Rewrite passages that are too far in any one direction.

**Rule #7 — Dialogue past each other**
Check every dialogue exchange. Characters must not explain the plot to each other or cooperate to deliver information to the reader. If a dialogue exchange feels like an info dump, rewrite it so characters pursue their own agendas.

**Rule #8 — Objects and actions as vulnerability**
Check that emotional moments are carried by objects, physical actions, or small gestures — not stated feelings. Rewrite any instance of "she felt," "he was sad," "she was nervous" with a physical or behavioral proxy.

**Rule #9 — Subculture inside perspective**
Check that the POV character's internal voice uses the language, hierarchy, and assumptions of their world. Rewrite generic observations into specific inside-perspective ones.

**Rule #10 — Chapter length**
Verify the chapter is within 10% of its target word count from the chapter map. If significantly over, tighten. If significantly under, flag it — do not pad.

**Rule #11 — Genre-specific visual formatting**
Check that formatting matches the sub-genre. Scene breaks, white space, and visual rhythm should feel native to the genre.

**Rule #12 — Mirror Principle**
For Chapter 1 and the final chapter only: check that the closing chapter mirrors the opening chapter's Who, Where, and Genre/Mood — transformed. This is not applicable to middle chapters.

**Rule #13 — Yes-And-But-Cost**
For the climax chapter only: confirm the Try-Fail is structured as Yes-and-but-cost. If it reads as a clean win with no cost, rewrite the landing to add the cost.

**Rule #14 — Pronouns disappear the character**
Scan for overuse of she/he/they in reference to named characters. Where the pronoun is the subject of a sentence and the named character could be used instead, replace the pronoun. Do not replace every pronoun — only where the character name is more precise and less repetitive.

### Step 4: Rewrite Violations

Rewrite the passages that violate the rules. Preserve all content and story beats — only the execution changes, not the substance.

### Step 5: Save the File

Write the edited version back to the same file path (`[title-folder]/chapters/chapter-[NN].md`). The original is replaced.

### Step 6: Run the Brand Voice Linter

After saving, run the linter against the edited file:

```bash
uv run [plugin-root]/scripts/brand_voice_linter.py [title-folder]/chapters/chapter-[NN].md
```

The linter mechanically checks three rules:
- **Blocky opener** — first paragraph must be a single sentence (Rule #1)
- **Blocky paragraph** — no paragraph longer than 4 sentences (Rule #10)
- **Pronoun density** — pronoun ratio must stay under 15% per paragraph (Rule #14)

If the linter reports any `[WARNING]` violations, fix them before moving to the next chapter. `[INFO]` suggestions are advisory — use your judgement.

### Step 7: Record the Edit Log Entry

For this chapter, note:
- Rules triggered (which rules flagged violations)
- What was changed (one line per change)

---

## End of Editing Pass

After all chapters are edited, report:

```
## Edit Pass Complete

| Chapter | Rules Triggered | Changes Made |
|---|---|---|
| Chapter 01: [Title] | Rule #1, Rule #7 | Rewrote opener; rewrote 2 dialogue exchanges |
| Chapter 02: [Title] | Rule #8 | Replaced 3 stated emotions with physical proxies |
| ... | ... | ... |

**Total chapters edited:** [N]
**Most common violation:** [Rule #X — description]
```

The next step is `/novel-publisher`.

---

## Operating Principles

1. **Refine, don't replace.** The drafter wrote the story. The editor refines the execution. Do not change plot, characters, or beats — only the prose quality.
2. **Rules serve the story.** If applying a rule would make a sentence worse, don't apply it. Rules are guidelines, not laws. Flag the exception instead of forcing the change.
3. **Emotional peaks get the poetry.** Do not sprinkle Rule #4 mechanisms throughout. Concentrate them at the moments of highest emotional weight.
4. **Edit in place.** Overwrite the chapter file. The original draft is not kept. The chapter drafter can be re-run if needed.
5. **Report what changed.** The edit log is for the writer's awareness. Be specific — "rewrote opener" is better than "made changes."

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after all chapters are edited end with the exact line:

> **Step 9 complete. Output: `[book-folder]/[sanitized-title]/chapters/*` (edited in place, [N] chapters)**

The orchestrator will then run `pipeline_validator.py --step 9` and route to Step 10 (`/novel-publisher`). When invoked manually by the user, end as described in the End of Editing Pass section above.
