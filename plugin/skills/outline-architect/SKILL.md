---
name: outline-architect
description: >-
  Takes a completed Story Seed, 3-Act Outline, and world/ folder and upgrades
  3-act-outline.md in place — adding MICE threads, FILO closure cascade, Mirror
  Rule, and elastic position directly to the existing beats. Phase 1 audits
  characters and settings for on-page weight and recalculates the honest word
  budget. Phase 2 seasons the existing outline without creating a new file. The
  next step is /novel-chapter-mapper.
---

# Outline Architect

A skill for taking a beat-level novel outline and cooking the MICE Quotient framework and Try-Fail cycles into it as structural seasoning — producing a Version 2 outline that is writing-ready, with threads explicitly mapped, the FILO closure cascade verified, and the mirror rule applied between opening and closing beats.

This skill operates on a clear principle: **the story is the soup. MICE threads and Try-Fail cycles are the spices. Chapters are the dishing.**

This skill handles the cooking. `/novel-chapter-mapper` handles the dishing.

---

## Before You Begin

Confirm you have the following locked in from earlier pipeline steps:

- The completed **Story Seed** (C/W/D/A/C outline + 1-sentence seed + expanded seed)
- The completed **3-Act Outline** (all 9 beats)
- The completed **world/** folder from `/build-the-world` (world-map, all settings, character list, all character bios)

If any of the above are missing, stop and complete those steps first.

---

## The MICE Quotient Framework

The MICE Quotient (originated by Orson Scott Card, evolved by Mary Robinette Kowal) is a story architecture framework. Every story longer than flash fiction contains multiple MICE threads woven together. Understanding which threads are open, how long they've been stretched, and what order they close in determines whether a story feels satisfying or fizzles.

**The MICE framework describes what a story is doing. It does not control what the story does.**

When mapping an outline with MICE:
- The story tells you where threads open and close
- You annotate what the story is doing
- You do NOT impose a tidy or symmetrical structure
- You do NOT force the story to fit a template

If the story does something asymmetric or unusual, document it that way. The framework's job is to make the story's existing structure visible.

---

### The Four MICE Thread Types

#### M — Milieu (Place)

A thread about a world or specific location.
- **Opens when:** A character enters (or struggles to enter) a place
- **Closes when:** They exit (or decide to stay)
- **Source of conflict:** Difficulty navigating or surviving the space, pressure from the environment, being trapped, etc.

#### I — Inquiry (Information)

A thread driven by a question.
- **Opens when:** A character asks "Huh?" or "What's going on?"
- **Closes when:** The character reaches "Aha!" or "Now I understand"
- **Source of conflict:** Red herrings, lies, dead ends, misunderstood clues, etc.

#### C — Character (Internal Change)

A thread driven by identity and self-definition.
- **Opens when:** A character experiences identity dissatisfaction ("Who am I?")
- **Closes when:** Self-redefinition or reconciliation ("Oh, this is who I am")
- **Source of conflict:** Self-loathing, internal contradiction, backfiring attempts at change, etc.

#### E — Event (External Change)

A thread driven by disruption of normal status quo.
- **Opens when:** The status quo breaks ("normal" breaks)
- **Closes when:** A new status quo is established (even if "everyone dies" — that's a stable end state)
- **Source of conflict:** External action — fights, chases, escalating disasters, betrayals, etc.

---

### The Nesting Rule

Every opened thread must close inside its parent thread.

Threads can be:
- **Sequential** (one closes, another opens, both inside a parent)
- **Recursive** (a same-type thread opening at a deeper level — C1 can wrap C2)
- **Parallel siblings** (multiple threads inside one parent, closing in any order — not required to be strict reverse order)

What is NOT allowed: a child thread closing OUTSIDE its parent. This produces the "story ended three times" failure or the "fizzle" failure.

**Example: A Recursive Nested Structure:**

```
<C1: Outer character arc>
  <I1: Outer inquiry>
    <E1: Outer event>
      <M1: Primary location>
        <C2: Inner character beat>
          <I2: Inner inquiry>
            <E2: Inner event>
            </E2>
            <M2: Sub-location>
            </M2>
          </I2>
        </C2>
      </M1>
    </E1>
  </I1>
</C1>
```

E2 closes before M2 opens — both are siblings inside I2, and sibling order is flexible.

---

### Same-Type Nesting and Consolidation

Threads of the same type often work better as escalating obstacles inside one thread, not as separate threads.

Example: an antagonist's pressure on the protagonist's existing arc is usually *baked into* the existing thread, not a parallel arc. An antagonist's institutional pressure is not E2 (a separate Event thread) — it's part of E1, functioning as escalating obstacles in Try-Fail cycles.

Apply this judgment when designing the master structure: a "parallel" antagonist is often actually salt in the existing soup, not a separate dish.

---

### The Elastic Band Principle

Kowal's central pacing claim: the longer a thread is stretched without breaking, the more cathartic its release.

Mechanism: emotional energy accrues with sustained anticipation. A thread opened in chapter one and closed in chapter forty has accumulated forty chapters of investment; its release produces a cathartic burst proportional to that accumulation.

Practical consequence: **the most important emotional moment of your novel should be the closure of the thread you opened first.**

---

### FILO Closure Order

First In, Last Out. The deepest catharsis (the outermost thread, opened first) closes last, after all inner threads have already discharged. Each prior closure primes the reader for the next, larger one.

This produces what readers experience as "completeness." Wrong-order closures produce the multiple-endings failure (*Return of the King* problem) or the wrong-type-ending failure.

---

## Try-Fail Cycles

The engine of the middle. Brandon Sanderson learned these from Dave Wolverton; Kowal integrated them with MICE.

| Outcome | Function | Use |
|---|---|---|
| **Yes, but…** | Partial success + new complication | sustain tension |
| **No, and…** | Failure + things get worse | sustain tension, build sympathy |
| **Yes, and…** | Success + bonus | Climax/closure; deliver payoff |
| **No, but…** | Failure + consolation or step toward resolution or gain knowledge | redirect or settle |

The "Yes, but / No, and" pair extends a thread. The "Yes, and / No, but" pair closes it.

---

### The Yes-And-But-Cost Climax

The most powerful single climax structure: the protagonist wins AND pays a price that retroactively defines what the wanting meant.

Examples: Dorothy returns home (she gets what she wanted, and the magical world is gone forever). Frodo destroys the Ring (he wins, and he cannot stay in the Shire). Raskolnikov confesses (he is free of the lie, and he is in Siberia).

The structure: Yes (success) + and (bonus) + but (cost). The cost is not external — it is the protagonist's identity from page one, transformed by the act of winning.

---

### The Mirror Rule

The ending should mirror the opening — revisit the same Who, Where, Genre/Mood, transformed.

Dorothy opens in Kansas and ends in Kansas; the character has changed but the frame returns. This is what produces the symmetry humans subconsciously recognize as completeness.

When applying this rule: identify specific opening elements (often listed quantitatively or visually in Beat 1) and find their inverted counterparts in the closing beat.

---

### The Word Budget Formula

`L = ((C + S) × 750 × M) / 1.5`

Where:
- C = effective on-page characters (Primary = 1.0, World-Building Only = 0)
- S = effective on-page settings/stages (same weighting; count sub-stages within a major setting)
- M = number of MICE threads

The 750 represents the midpoint of the 500–1,000-word range to "do a character or setting justice." Division by 1.5 accounts for overlap.

Worked examples:
- 5 characters + 6 settings + 4 threads = 22,000 words
- 8 characters + 8 settings + 5 threads = 40,000 words
- 12 characters + 25 settings + 6 threads = 111,000 words

The formula is diagnostic, not prescriptive. Use it to check whether scope matches target.

---

# Phase 1: Audit

The audit is the pre-cooking step. It recalibrates the word budget formula against the actual outline by categorizing every character and setting by their real dramatic presence.

## Why This Matters

The word budget formula assumes every character and setting carries full dramatic weight on the page. In practice, most novel projects have:
- A handful of on-page primary characters (who drive scenes)
- A larger world-building cast (who exist for atmosphere but never appear on-page)

Same with settings. A 25-setting world-building catalog usually translates to 5–10 on-page stages in the actual novel.

Running the formula with the iceberg counts produces a misleading word count. Running it with the on-page counts produces the honest target.

## How to Categorize

Read the beat outline carefully. For each character in `world/characters/character-list.md` and their bios:

1. Search the outline for the character's name
2. Note every beat where they appear
3. Determine: do they drive any scenes? Speak dialogue? Carry plot weight?
4. Categorize accordingly

For each setting in `world/settings/`:

1. Search the outline for the setting's name
2. Note every beat where action occurs there
3. Determine: is this a stage where scenes happen, or just a name dropped in atmosphere?
4. Categorize accordingly

Also: identify **sub-stages within major settings**. A city may contain 5–6 distinct scene locations (office, apartment, archive, streets, etc.). Count these as effective stages, not the city as one.

---

### The Two-Tier Categorization System

#### PRIMARY (P) — Full dramatic presence

The character or setting:
- Has scenes (multiple beats)
- Has dialogue (for characters) or is the stage for action (for settings)
- Drives plot
- The reader experiences them directly

Word-budget cost: full (1.0)

#### WORLD-BUILDING ONLY (W) — No on-page presence

The character or setting:
- Never appears on-page in this novel
- Exists in the world for atmosphere or future-book purposes
- May be mentioned in passing reference only

Word-budget cost: zero (0)

---

## Step 0: Gather Project Material

Read the following files:
- Story seed file
- 3-Act beat outline file
- `world/world-map.md`
- All files in `world/settings/`
- `world/characters/character-list.md`
- All files in `world/characters/bios/`

Confirm what's available. If the outline or character/location inventory is missing, stop and tell the user what's missing before proceeding.

## Step 1: On-Page Weight Categories

Apply the two-tier definitions (Primary, World-Building Only) with their word-budget costs.

## Step 2: Characters Audit

For each character, produce a table row:
- Character name
- On-Page Weight (P/W)
- Appears In (which beats)
- Justification (one-sentence explanation)

State the total counts (how many Primary, how many World-Building Only) and the effective character count for the formula.

## Step 3: Settings Audit

For each setting, produce a table row with the same structure. Note sub-stages within major settings as effective stages.

State the total counts and the effective setting count.

## Step 4: Recalculated Word Budget

Show:
- Original (theoretical) formula application using the full catalog counts
- Honest formula application using the on-page weighted counts
- The gap between the two

## Step 5: The Recommended Ingredient List

The final list of ingredients for cooking Phase 2:
- **On-Page Characters** (primary recommended additions)
- **On-Page Stages** (primary recommended additions)
- **MICE Threads** (count and naming if already clear from outline)

Revised word budget calculation with the final ingredient counts.

---

# Phase 2: Cooking the V2 Outline

Phase 2 takes the confirmed ingredient list and the original beat outline and produces the V2 outline — the seasoned soup, ready to write from.

## The Operating Principle

**Story first, framework second.** The original outline prose is preserved exactly. The MICE architecture is added as a *seasoning layer* — never replacing the story, only making its structural patterns visible.

---

**Step 2.1: Identify the Beat Structure**

Read the user's beat outline exactly. Note:
- The Act divisions
- The beat count (typically 9, but adapt — could be 15 for Save the Cat, 12 for Hero's Journey, 8 for Story Circle, custom for others)
- The position of each beat in the structure

The skill adapts to whatever structure exists. Do not force a 9-beat fit if the outline uses something else.

**Step 2.2: Identify the Macro MICE Threads**

Read the outline carefully. Determine, based on what the story actually does:

- **What is the primary thread carrying the whole novel?** (Character, Inquiry, Event, or Milieu?) Determine by what the story actually does, not by what type of book it should be.
- **What sub-threads open and close at various points?**

**Critical rule:** Same-type threads (e.g., two Event threads) often work better as escalating obstacles within one thread, not as separate threads. If an antagonist's pressure is *on the protagonist's existing arc* rather than *a parallel arc*, bake it into the existing thread.

**Step 2.3: Build the Master Nested Structure**

Output the macro thread structure for the WHOLE NOVEL using tag notation. Nesting is recursive and non-linear. Threads of the same type can re-open at deeper levels. Sibling threads inside the same parent can close in any order. The only rule: **every thread must close inside its parent thread.**

Format the master nested structure as a code block with thread codes (C1, M1, I1, E1, C2, etc.), descriptions, and explicit open/close beat positions.

**Step 2.4: Build the Thread Registry**

Build a table with columns:
- Code (C1, M1, etc.)
- Type (Character, Milieu, Inquiry, Event)
- Description (one line)
- Carrier (which character drives it)
- Opens at (which beat)
- Closes at (which beat)

**Step 2.5: Map the Mirror Rule**

The ending should mirror the opening — Who, Where, Genre/Mood revisited, transformed. Identify how the opening beat (typically Beat 1) and closing beat (typically the final beat) mirror each other. Document the specific elements that recur with inverted polarity.

**Step 2.6: For each beat, write the seasoning layer**

Beneath each beat's original prose, add a `#### 🧂 MICE Layer` section containing:

- **Threads opening this beat** (with code, type, and the line/event where they open)
- **Threads sustaining this beat** (with code and one-line note on how each is sustained)
- **Threads closing this beat** (with code, type, and the specific line/moment of closure)
- **Elastic position** (which threads are stretched, how taut, what's about to release)

**Special handling for specific beats:**

- **Opening Beat (Beat 1):** Note any gaps (e.g., "Where" not yet anchored to sensory detail) with drafting recommendations
- **Final Beat (typically Beat 9):** Include the **mirror complete** table — Beat 1 elements ↔ final beat elements, side by side, showing the polarity inversion.

**Step 2.7: Build the Final Verification Section**

At the end of the V2 document, add:

1. **Thread architecture diagram** — visual sequence showing openings and closings by beat
2. **Mirror confirmation** — two-column table showing Beat 1 elements ↔ final beat elements
3. **Word budget** — formula re-applied with confirmed numbers
4. **What's cooked in** — summary of all structural ingredients now in the outline

---

## How the Upgrade Works

This skill edits `3-act-outline.md` directly. It does not create a new file. The original beat prose is never touched — only new sections are added.

### Addition 1: Macro Architecture section (inserted at the top, before the beats)

**1a. The Master Nested Structure** — code block with tag notation

**1b. The Thread Registry** — table

**1c. The Mirror** — short paragraph identifying how opening and closing beats mirror each other

### Addition 2: MICE Layer (added beneath each beat's existing prose)

For each beat, a `#### 🧂 MICE Layer` section is added immediately after the beat's prose. The original beat content is not rewritten or removed.

### Addition 3: Final Verification (appended at the bottom of the file)

Thread architecture diagram, mirror confirmation table, word budget, what's cooked in.

---

## Output

Upgrade `3-act-outline.md` in the active book's working directory by adding the three sections above. Do not rewrite or remove any original content.

Once the file is upgraded, confirm to the user that the outline has been seasoned and list what was cooked in. The next step is `/novel-chapter-mapper`.

---

## Operating Principles

1. **Read the entire outline first.** Don't start writing the V2 until you've read all beats and built a mental model of the thread structure.
2. **Identify the master architecture before doing beat-by-beat.** The upfront architecture drives the beats. Don't write the beats first.
3. **Preserve the story.** Never edit the original prose. The seasoning layer goes beneath it. If the original beat doesn't do what the research recommends, flag it as a recommendation — don't rewrite it.
4. **Be specific.** Generic notes are useless. Identify the specific line where a thread opens, sustains visibly, or closes. Quote it where possible.
5. **Story first, framework second.** The outline is the source of truth. MICE notation describes what's happening; it does not redesign the story.
6. **Don't invent.** Use only what's already in the project files. If something's missing, name it.
7. **Same-type threads usually consolidate.** Antagonist pressure is typically baked into the protagonist's existing thread, not a parallel thread.
8. **The mirror rule is non-negotiable.** Every seasoned outline must map opening ↔ ending elements explicitly.

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after upgrading `3-act-outline.md` in place end with the exact line:

> **Step 5 complete. Output: `[book-folder]/3-act-outline.md` (upgraded with Macro Architecture)**

The orchestrator will then run `pipeline_validator.py --step 5` and route to Step 6 (`/book-title-generator`). When invoked manually by the user, end as described in the Output section above.
