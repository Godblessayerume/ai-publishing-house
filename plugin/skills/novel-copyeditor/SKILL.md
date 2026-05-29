---
name: novel-copyeditor
description: >-
  Copyedits every chapter in sequence — fixes grammar, punctuation, spelling,
  tense consistency, POV consistency, and character name/detail consistency
  against the world-building files. Edits chapters in place and produces
  copyedit-report.md. The next step is /novel-publisher.
---

# Novel Copyeditor

A mechanics-focused pass. It does not touch creative choices — rhythm, voice, dialogue style, and scene structure are already locked by the line editor. It fixes only what is wrong: grammar errors, punctuation errors, spelling errors, consistency errors, and POV slippage.

---

## Before You Begin

Confirm all of the following exist:

- All chapter files in `[title-folder]/chapters/` — produced and line-edited by `/novel-editor`
- `world/characters/bios/` — for correct character name spellings and physical details
- `world/settings/` — for correct setting names and geography
- `[title-folder]/[book-title]-chapter-map.md` — for the POV character per chapter

**Finding the title folder:** Read `book-title.md` at the book root, extract the `Final Title:` value, sanitize it (replace `:` with ` -`, remove `< > " / \ | ? *`). The title folder was created by Step 6.

---

## Building the Consistency Reference

Before reading any chapter, load:

1. Every character bio from `world/characters/bios/` — note the canonical spelling of each character's name, their physical description (hair, eyes, height, distinguishing marks), and any details that could be inconsistently described across chapters.
2. Every setting file from `world/settings/` — note canonical place names and any directional or geographic facts.

This reference is the source of truth for consistency checks.

---

## What Copyediting Fixes

### Grammar
- Subject-verb agreement errors
- Pronoun case errors (him/he, her/she misused as subject or object)
- Dangling and misplaced modifiers
- Unintentional sentence fragments (intentional fragments used for rhythm are preserved — see note below)

### Punctuation
- Comma splices (two independent clauses joined by a comma with no coordinating conjunction) — fix unless the comma splice is clearly intentional for rhythm
- Missing apostrophes in contractions and possessives
- Unclosed or mismatched quotation marks
- Hyphens used where em dashes belong in narrative prose (-- or - replacing —)

### Spelling
- Misspelled common words
- Inconsistent spelling of character names across chapters (canonical spelling from the bio)
- Inconsistent spelling of invented place names (canonical spelling from the setting file)

### Tense consistency
- Identify the manuscript's established tense (past or present) from the first chapter
- Flag and fix any paragraph that slips into the other tense without clear flashback framing
- Do not change deliberate tense shifts that serve a narrative purpose (clearly framed flashbacks, quoted text, etc.)

### POV consistency
- Each chapter has a POV character (from the chapter map)
- Fix any passage where the narration slips into another character's internal thoughts or perceptions (head-hopping)
- The fix is to externalize the observation — what the POV character can see, hear, or infer — rather than deleting the information

### Character and world consistency
- If a chapter describes a character's physical detail inconsistently with their bio (wrong eye color, wrong hair), fix the chapter to match the bio
- If a chapter places a setting geographically inconsistently with the world-map description, flag it in the report but do not auto-fix — geography contradictions may have plot implications

---

## Intentional Exceptions — Do Not Fix These

The line editor made deliberate choices that may look like errors:

- **Intentional fragments** — a one-word or two-word paragraph used for rhythm or emphasis
- **Intentional comma splices** — short clauses run together for breathlessness
- **Intentional run-ons** — a long sentence used for the "violin solo" or overwhelm effect (Rule #3)
- **Unconventional punctuation** — ellipses, em dashes, or unconventional capitalization used as a stylistic device

If something looks like an error but might be intentional, leave it and flag it in the report as "possible intentional choice — not fixed."

---

## How the Copyedit Pass Works

1. Load the consistency reference (all bios and settings)
2. Tell the user: "Copyediting [N] chapters. Starting now."
3. Copyedit each chapter in sequence without pausing
4. After all chapters are processed, write the report and confirm

Do not stop between chapters.

---

## For Each Chapter

1. Read the chapter file
2. Check the chapter map for the POV character
3. Apply fixes from all categories above
4. Write the edited chapter back to the same file path (`[title-folder]/chapters/chapter-[NN].md`)
5. Record for the report: chapter number, fix category, brief description

---

## Output

After all chapters are processed, write `[title-folder]/copyedit-report.md`:

```markdown
## Copyedit Report

| Chapter | Category | Fix Applied |
|---|---|---|
| Chapter 01 | Spelling | "Mira" corrected to "Mara" (3 instances) |
| Chapter 03 | Punctuation | Comma splice fixed (paragraph 2) |
| Chapter 07 | POV | Head-hop removed — externalized as POV character's inference |
| ... | ... | ... |

**Total chapters processed:** [N]
**Total fixes applied:** [X]

**Flagged (not auto-fixed):**
- [Any geography/plot-level inconsistencies, possible intentional choices, or issues needing author review]
```

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after all chapters are copyedited and the report is written, end with the exact line:

> **Step 10 complete. Output: `[book-folder]/[sanitized-title]/copyedit-report.md` ([N] chapters copyedited)**

The orchestrator will then run `pipeline_validator.py --step 10` and route to Step 11 (`/novel-publisher`). When invoked manually, end as described in the Output section above.
