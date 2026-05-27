---
name: novel-chapter-mapper
description: >-
  Takes the seasoned 3-act-outline.md (upgraded by /outline-architect) and
  breaks it into a complete chapter-by-chapter map — every chapter gets a
  working title, beat, setting, word target, opening style, ending style, MICE
  thread annotation, and Try-Fail cycle. This is the final pre-writing step
  before prose drafting with /novel-chapter-drafter. Output: [story-title]-chapter-map.md.
---

# Novel Chapter Mapper

A skill for taking the seasoned 3-act outline and breaking it into a complete chapter-by-chapter map — the writer's guide for prose drafting. Every chapter entry contains everything needed to sit down and write.

This skill operates on a clear principle: **the soup is cooked (`/outline-architect`). This skill is the dishing — how the soup is served.**

The dishing does not affect the cooking. The story is what it is. The chapters are how it's plated. The chapter count, the chapter lengths, the opening styles, the ending styles — these are presentation decisions, not story decisions. The MICE threads don't change. The beats don't change. The characters and settings don't change.

---

## Before You Begin

Confirm you have the following locked in:

- The **seasoned 3-act outline** (`3-act-outline.md`) upgraded by `/outline-architect` — confirmed by the presence of a `## Macro Architecture` section at the top of the file

If the Macro Architecture section is missing, stop and run `/outline-architect` first.

---

## Chapter Titles

Working titles, not final titles. They should be:
- Evocative (what this chapter is *about*, not what *happens*)
- Short (one to four words typically)
- Slightly oblique (titles that work better in retrospect than in prospect)

Avoid titles that are too on-the-nose ("Character Discovers the Secret") or too vague ("The Decision").

---

## The Chapter-by-Chapter Mapping Process

### Step 1: Read the Seasoned Outline

Read:
- `3-act-outline.md` — the outline upgraded by `/outline-architect`, containing the original beats plus the Macro Architecture section and MICE layers

If the `## Macro Architecture` section is not present in the file, stop and tell the user to run `/outline-architect` first.

---

### Step 2: Extract the Architecture

From the V2 outline, identify and note:
- Total beats and their Act positions
- The MICE threads with their open/close beats
- The pivot beat
- The FILO closure cascade order
- The mirror elements (Beat 1 ↔ final beat)
- The target word count

---

### Step 3: Calculate Chapter Count

Apply:
`Chapter count = target word count ÷ preferred chapter length`

Default preferred chapter length: **1,200 words**

Adjust for:
- Beat complexity (beats with multiple Try-Fail cycles need more chapters than single-cycle beats)
- Structural beats that require space (the pivot beat, the pre-loaded elastic closure, the Yes-and-but-cost climax)

State the final chapter count and the reasoning.

---

### Step 4: Distribute Chapters Across Beats

Allocate chapters to beats based on:
- Word weight of each beat (how much happens)
- Try-Fail cycle count in the beat (each major cycle typically warrants its own chapter)

Adapt this distribution to the actual outline.

---

### Step 5: Assign Opening and Ending Styles

Read `references/author-voice-guide.md` and apply **Rule #1 and Rule #5** (alternate opening and ending styles) across all chapter openings.

For every chapter, assign an opening style and ending style.

**Never the same opening style in two consecutive chapters.**
**Never the same ending style in two consecutive chapters.**

---

### Step 6: Assign Chapter MICE Thread

The mini-thread that operates at chapter scale, nested inside the novel's macro threads. Format as tag notation:

```
<I: [Question asked] OPENS/CLOSES — the chapter-scale inquiry that opens and resolves here>
```

Or for a chapter where a macro thread has significant activity:

```
<I1: SUSTAINS — the main inquiry escalates through the anomaly discovery>
<C1: STRETCHES — the identity arc tightens as the cost becomes visible>
```

For closure chapters:
```
<C2: CLOSES — the recognition beat; the elastic releases here>
```

The chapter MICE should reflect what the chapter actually does structurally — not just what the characters do narratively.

---

### Step 7: Assign Try-Fail Cycle

State the type clearly: **Yes, but** / **No, and** / **Yes, and** / **No, but** / **Yes-and-but-cost** (for climax chapters) / **None**.

Then describe:
- **Try:** What the protagonist specifically attempts in this chapter
- **Outcome:** What the result is and what it produces next

The Try-Fail must serve a macro thread. It should feel like a cause that produces an effect, not a scene that happens.

If the chapter has multiple distinct Try-Fail cycles, label them:
- **Cycle 1:** Yes, but — [description]
- **Cycle 2:** No, and — [description]

---

### Step 8: Write Every Chapter Entry

For each chapter from 1 to N, produce a full entry using this template:

```markdown
### Chapter [N]: "[Working Title]"
**Beat:** [Beat number and name]
**Setting:** [Specific location/geography from the world-building]
**Target:** ~[X] words

**Opening style: [Code]** — [One-sentence description of how the chapter opens]
**Ending style: [Code]** — [One-sentence description of how the chapter ends]

**Chapter MICE:**

<[Thread type]: [Description] OPENS / SUSTAINS / CLOSES>

**Try-Fail:** **[Yes-but / No-and / Yes-and / No-but / Yes-and-but-cost / None]**
- Try: [What the protagonist/character attempts]
- Outcome: [The result and its immediate consequence]
```

---

### Step 9: Final Numbers

Produce a summary table:
- Total chapters
- Act 1 / Act 2 / Act 3 chapter counts
- Estimated word count (baseline from chapter allocations)
- Estimated word count with dramatized Try-Fails

---

## Output

Write the complete chapter map to: `[story-title]-chapter-map.md` in the active book's working directory.

Once the file is written, confirm to the user that the chapter map is complete and list the total chapters per act. The next step is `/novel-chapter-drafter`.

---

## Operating Principles

1. **Dishing follows cooking.** Never run this skill without a seasoned V2 outline. If the outline hasn't been cooked, stop and redirect to `/outline-architect`.
2. **Story-first.** The dishing doesn't change the story. If a chapter allocation feels forced, reconsider the distribution — the story tells you where the chapters should break, not the other way around.
3. **Never the same style twice in a row.** Opening style and ending style must alternate across consecutive chapters.
4. **Try-Fail must serve a macro thread.** Don't introduce Try-Fail cycles that don't advance the novel's macro threads.
5. **One file at the end.** No partial files. One master chapter map MD file written to the working directory.

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after writing the chapter map end with the exact line:

> **Step 7 complete. Output: `[book-folder]/[book-title]-chapter-map.md`**

The orchestrator will then run `pipeline_validator.py --step 7` and route to Step 8 (`/novel-chapter-drafter`). When invoked manually by the user, end as described in the Output section above.
