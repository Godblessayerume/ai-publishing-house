---
name: novel-proofreader
description: >-
  Final mechanical pass on the compiled manuscript-final.md — catches duplicate
  words, unclosed formatting, chapter heading inconsistencies, and typographic
  errors introduced during compilation. Edits manuscript-final.md in place and
  produces proofread-report.md. The next step is /book-cover-prompt-generator.
---

# Novel Proofreader

The last pass before the book is finished. Proofreading runs after compilation — it works on `manuscript-final.md`, not on individual chapter files. Its scope is narrow and mechanical: it catches what slipped through copyediting and what compilation itself may have introduced.

---

## Before You Begin

Confirm:

- `[title-folder]/manuscript-final.md` — produced by `/novel-publisher`

**Finding the title folder:** Read `book-title.md` at the book root, extract the `Final Title:` value, sanitize it (replace `:` with ` -`, remove `< > " / \ | ? *`).

---

## What Proofreading Catches

### Duplicate words
Any word repeated twice in a row: "the the", "and and", "had had", "a a", "of of". Fix by removing the duplicate. Flag cases where the repetition might be intentional (diacope — "Bond. James Bond." — do not fix).

### Typographic errors
- Double spaces between words — fix to single space
- Space before punctuation (" ," " ." " !" " ?") — remove the space
- Missing space after punctuation where required

### Unclosed Markdown formatting
- Italics opened but not closed (`*text` with no closing `*`)
- Bold opened but not closed (`**text` with no closing `**`)
Fix by closing the formatting at the nearest logical boundary.

### Chapter heading consistency
Every chapter heading should follow one consistent format. Identify the format used in the first chapter (e.g., `# Chapter 1: Title` or `# Chapter 1 — Title`) and flag any heading that deviates from it. Do not auto-fix heading format — flag for review.

### Table of Contents accuracy
If the manuscript includes a generated TOC, check that every TOC entry matches its corresponding chapter heading exactly. If a heading was changed during editing and the TOC wasn't updated, flag the mismatch.

### Orphaned punctuation
- A closing quotation mark with no matching opening mark in the same paragraph
- A closing parenthesis with no opening parenthesis
Flag these — do not auto-fix, as the correct fix depends on intent.

---

## How the Proofread Pass Works

1. Read `manuscript-final.md` in full
2. Scan for all issue categories above in sequence
3. Fix what can be safely auto-fixed (duplicate words, double spaces, space-before-punctuation)
4. Flag what requires judgment (heading inconsistencies, TOC mismatches, unclosed formatting that spans sections, orphaned punctuation)
5. Write the corrected manuscript back to `manuscript-final.md`
6. Write `proofread-report.md` to the title folder

---

## Output

Write `[title-folder]/proofread-report.md`:

```markdown
## Proofread Report

**Fixes applied:**
- [N] duplicate word instances removed
- [N] double-space corrections
- [N] space-before-punctuation corrections
- [N] unclosed formatting pairs closed

**Flagged for review:**
- [Heading inconsistencies, TOC mismatches, orphaned punctuation, or ambiguous duplicates]

**Manuscript status:** Ready for upload
```

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after the manuscript is proofread and the report is written, end with the exact line:

> **Step 12 complete. Output: `[book-folder]/[sanitized-title]/proofread-report.md` (manuscript-final.md proofread)**

The orchestrator will then run `pipeline_validator.py --step 12` and route to Step 13 (`/book-cover-prompt-generator`). When invoked manually, end as described in the Output section above.
