---
name: novel-genre-picker
description: >-
  The first step in every new book. Locks in the sub-genre and stacks 2–4 plot
  archetypes from the 100 Plot Archetypes reference. Output: story-config.md.
  The next step is /novel-story-seed-writer.
---

# Novel Genre Picker

The first creative decision for any new book. This skill locks in two things before any writing begins:

1. **The sub-genre** — the specific flavor of fiction this story lives in
2. **The stacked plot archetypes** — the 2–4 structural engines that will drive the plot

Everything downstream (story seed, outline, world-building, chapter drafting) reads from this config. Get it right here and the whole pipeline flows cleanly.

---

## Before You Begin

No prerequisites. This is the first step of the pipeline — the starting point for every new book.

---

## What Is Plot Stacking?

A single plot archetype gives a story one engine. Stacking 2–4 archetypes gives a story multiple engines running simultaneously — each one pulling the reader forward in a different way.

**Example stacks:**
- Hero's Journey (#1) + Redemption (#14) + War (#21) — a war novel about a soldier trying to atone while completing a mission
- Coming of Age (#2) + Forbidden Love (#5) + Betrayal (#11) — a YA romance with a backstabbing friend arc
- Dystopia (#17) + Rebellion (#27) + Chosen One (#12) — a classic YA dystopian trilogy setup

**Rules for stacking:**
- One **primary archetype** — this drives the main plot
- 1–3 **secondary archetypes** — these add sub-plots, thematic layers, or emotional depth
- Primary and secondary archetypes should create tension with each other, not pile on more of the same thing

---

## The Process

### Step 1: Create the Book Folder

Ask the user two questions together:

> "What sub-genre is this story? And what should we call this project? (The project name becomes the working folder — use something short, e.g. `the-king-project` or `iron-court`. The real book title is decided later at Step 6.)"

- Accept the sub-genre exactly as stated. Do not modify or rephrase it.
- Convert the project name to a folder sub-genre: lowercase, spaces to hyphens, remove punctuation.

Confirm with the user:

> "Got it — sub-genre: **[sub-genre]**. Working folder: `[vaultPath]/[sub-genre]/`. Creating it now."

Create the folder at `[vaultPath]/[sub-genre]/`. All output files for this book go inside this folder. The folder is created here — no other skill creates it.

---

### Step 2: Stack the Plot Archetypes

#### Part A — Get a Story Sketch

Before recommending archetypes, ask:

> "Give me 2–3 sentences about the story — what is it basically about? Who is the main character and what do they want or face?"

Accept whatever they provide. This sketch is the lens for your recommendations. If they have nothing yet, ask them to describe even the roughest idea — a feeling, a setting, a conflict — anything.

---

#### Part B — Recommend Archetypes

Read `references/The 100 Plot Archetypes.md`. Based on the sub-genre and the story sketch, recommend:

1. A **primary archetype** — the one that carries the main plot
2. **1–3 secondary archetypes** — the ones that layer in sub-plots or thematic depth

For each recommendation, give one sentence of reasoning that ties it specifically to their sub-genre and story sketch.

Present the recommendation in this format:

> **Based on [sub-genre] and your story, here's what I recommend:**
>
> **Primary:** #[N] — [Archetype Name]
> *[One sentence: why this archetype fits their story]*
>
> **Secondary:**
> - #[N] — [Archetype Name]: *[why it fits]*
> - #[N] — [Archetype Name]: *[why it fits]*
>
> Do you want to go with these, or swap any out?

If they want to swap, let them choose from the full list in `references/The 100 Plot Archetypes.md`. Accept their changes without resistance.

---

#### Part C — Clarify Each Archetype

Once the user accepts the final archetype stack, go through each one individually.

For each archetype, ask the clarifying question **and** offer 1–2 concrete story ideas drawn from their sketch:

> **How does [Archetype Name] show up in your story specifically?**
>
> Here are two ways it could work given what you've told me:
> 1. [Concrete idea rooted in their story sketch — specific characters, situation, or moment]
> 2. [Alternate concrete idea — a different angle on the same archetype]
>
> Use one of these, combine them, or describe your own version.

Do this for every archetype in the stack — primary first, then each secondary in order. The goal is intentionality: not "I like this archetype" but "this archetype shows up when [specific story moment]."

---

### Step 3: Confirm and Summarize

Once all archetypes have been clarified, write a short **Stack Summary** (1 paragraph) describing how the chosen archetypes interlace. This is not a story pitch — it is a structural description: what engine each archetype provides, how each one shows up concretely in this story (using the answers from Part C), and how they create productive friction with each other.

Read the summary back to the user and ask for confirmation before writing the output file.

---

## Output

Write to: `story-config.md` in the active book's working directory.

Format:
```markdown
# Story Configuration

## Sub-Genre
[The confirmed sub-genre label]

## Plot Archetypes

**Primary:** #[number] — [Archetype Name]
[One sentence: how this archetype drives the main plot]

**Secondary:**
- #[number] — [Archetype Name]: [One sentence: how it layers]
- #[number] — [Archetype Name]: [One sentence: how it layers]

## Stack Summary
[1-paragraph structural description of how the archetypes interlace and what tension they create with each other]
```

Once the file is written, confirm to the user that the story configuration is locked. The next step is `/novel-story-seed-writer`.

---

## Operating Principles

1. **Accept the sub-genre as given.** The user knows their genre. Lock in exactly what they provide without modification. Only offer alternatives if they explicitly ask for help.
2. **Recommend, don't just list.** Use the sub-genre and story sketch to make specific, reasoned recommendations. The user should not have to browse 100 archetypes alone — your job is to surface the 3–4 most likely fits and explain why.
3. **Primary archetype first.** Recommend and confirm the primary archetype before introducing the secondaries. The stack should reinforce and complicate the primary, not compete with it.
4. **Concrete ideas in every clarifying question.** When asking "how does [archetype] show up in your story?", always offer 1–2 story-specific ideas. Never leave the user staring at a blank question. The ideas should be grounded in what they told you in the story sketch.
5. **Intentional stacking only.** Each secondary archetype must produce a concrete answer to "how does this show up?" If the user can't answer, prompt with more ideas — or drop it from the stack.
6. **No more than 4 archetypes total.** More than 4 and the story loses focus. A 2-archetype stack is often stronger than a 4-archetype stack.
7. **Confirm before writing.** Read the Stack Summary back to the user and get a yes before writing `story-config.md`.

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after writing `story-config.md` end with the exact line:

> **Step 1 complete. Output: `[book-folder]/story-config.md`**

The orchestrator will then run `pipeline_validator.py --step 1` and route to Step 2 (`/novel-story-seed-writer`). When invoked manually by the user, end as described in the Output section above.
