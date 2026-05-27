---
name: book-title-generator
description: >-
  Step 6 of the pipeline. Reads the accumulated story files (genre, seed,
  outline, world-building) and generates compelling book title candidates using
  proven formulas. Output: book-title.md. The next step is /novel-chapter-mapper.
---

# Book Title Generator

Step 6 — the bridge between world-building and chapter structure. By now the story has a locked genre, a full story seed, a seasoned 3-act outline, and a built world. That is everything needed to generate a title that truly fits the book — not a guess, but a decision backed by full story context.

This skill does not ask the user to invent a title from nothing. It reads all the accumulated files, extracts the most potent story material, and generates 8–10 candidates using proven title formulas. The user picks, refines, or asks for more options until the title feels right.

---

## Before You Begin

All five previous steps must be complete. Check that these files exist in the active book's folder before proceeding:

| Required file | Produced by |
|---|---|
| `story-config.md` | `/novel-genre-picker` |
| `story-seed.md` | `/novel-story-seed-writer` |
| `3-act-outline.md` (with `## Macro Architecture` section) | `/novel-3-act-outliner` + `/outline-architect` |
| `world/world-map.md` | `/build-the-world` |

If any are missing, stop and direct the user to the upstream skill.

---

## What Makes a Book Title Work

A strong title does four things simultaneously:

1. **Intrigues** — creates curiosity or raises a question without being confusing
2. **Signals the genre** — readers browsing a shelf or Amazon page know what kind of story this is
3. **Is memorable and searchable** — readers can recall it, spell it, and find it by searching
4. **Works at thumbnail size** — legible and distinctive on a digital cover no bigger than a postage stamp

---

## Title Formulas by Approach

Read these formulas before generating candidates. Each title you generate must be tagged with which formula it uses and one sentence explaining why it fits this specific story.

### Formula A — Character Name
Use the protagonist's name alone, or with a descriptor.
> *Jane Eyre*, *Eragon*, *Jude the Obscure*

Best for: character-driven stories where the protagonist IS the story.

---

### Formula B — Setting or World
Use the place, realm, or world that defines the story.
> *Middlemarch*, *Dune*, *Picnic at Hanging Rock*

Best for: stories where the setting is as central as the character.

---

### Formula C — "The [N] of [N]"
Two nouns connected by "of." One abstract, one concrete — or both symbolic.
> *The Name of the Wind*, *Throne of Glass*, *Words of Radiance*

Best for: epic fantasy, literary fiction. Creates instant gravitas.

---

### Formula D — "A [N] of [N] and [N]"
Three nouns. The "and" signals layered conflict or duality.
> *A Court of Thorns and Roses*, *A Game of Thrones*, *A Little Life*

Best for: romantasy, epic fantasy, literary fiction. Signals scope.

---

### Formula E — Central Symbol or Theme
Pull the central object, image, or metaphor from the story.
> *To Kill a Mockingbird*, *The Scarlet Letter*, *The Handmaid's Tale*

Best for: stories with a strong recurring symbol or thematic image.

---

### Formula F — Implicit Question
A title that poses an unspoken question — what happened? who is this? how does this end?
> *Do Androids Dream of Electric Sheep?*, *Gone Girl*, *The Curious Incident of the Dog in the Night-Time*

Best for: thrillers, mysteries, speculative fiction.

---

### Formula G — Dual Element / "[X] and [Y]"
Two opposing or complementary things linked together.
> *War and Peace*, *Pride and Prejudice*, *Fire and Ice*

Best for: stories with two warring forces, dual POVs, or a central duality.

---

### Formula H — Single Evocative Word
One word — but it must carry enormous weight and be genre-distinctive.
> *Dune*, *Beloved*, *Frankenstein*, *Neuromancer*

Use sparingly. Only when the word is unique enough to own in search.

---

### Formula I — Genre-Specific Patterns

**Epic Fantasy:** Realm names, artifact names, ancient titles. "The [Adjective] [Sword/Crown/Throne]"

**Grimdark:** Hard, brutal nouns. Broken or corrupted things.
> *The Blade Itself*, *Best Served Cold*, *Prince of Thorns*

**Romantasy:** Courts, shadows, flowers, bargains, fae. Formulas C and D dominate.
> *The Midnight Court*, *A Shadow of Vows*

**Dark Fantasy:** Something forbidden, cursed, or corrupted. Implied dread in every word.

**Space Opera:** Ship names, empire-scale proper nouns, stellar geography.

**Hard Sci-Fi:** Scientific concepts elevated to poetry. Precision as atmosphere.

**Cozy Fantasy:** Warm, inviting. A place + a feeling. Community-centered nouns.

**LitRPG:** Game mechanics vocabulary — class names, level/rank terminology.

---

## The Process

### Step 1: Read the Story Files

Read all four prerequisite files:
- `story-config.md` — sub-genre, primary archetype, secondary archetypes, stack summary
- `story-seed.md` — premise, protagonist, central conflict, setting, tone
- `3-act-outline.md` — key beats, the Macro Architecture section, thematic throughline
- `world/world-map.md` — world name, defining locations, core tension of the world

Extract the most potent material: the protagonist's name, the world's most distinctive noun, the central conflict in a few words, the key symbol or image, the thematic core. These are the raw materials for title generation.

---

### Step 2: Generate Candidates

Using the extracted material and the formula list above, generate **8–10 title candidates** drawing from at least 4 different formulas. For each title:

- Show the title
- Tag the formula (e.g., *Formula C — "The [N] of [N]"*)
- One sentence explaining why it fits this specific story — use concrete details from the files

Example format:

> **1. The Ashborn Throne** *(Formula C — "The [N] of [N]")*
> Pulls the ash-and-ruin imagery from your world-map and the succession conflict from Act 2 Beat 4.
>
> **2. A Court of Smoke and Silence** *(Formula D — "A [N] of [N] and [N]")*
> Romantasy signal is immediate; smoke references your magic system, silence references your protagonist's secret.

---

### Step 3: Refine

After presenting the list, ask:

> "Do any of these feel right? Tell me which ones you like and why — or what's missing — and I'll generate more in that direction."

Keep refining until the user commits to one title. They may mix elements from different candidates. Work with it.

---

### Step 4: Validate

Before writing the output, check the title against this list:

1. Does it intrigue without confusing?
2. Does it signal the genre clearly?
3. Can a reader remember it, spell it, and search for it?
4. Does it work as spine text or a thumbnail label?
5. Is it Amazon-safe? (No vulgarity, no trademarked terms, no "bestselling" or "free")
6. Does it sound natural when said aloud to a stranger?

Flag any failure to the user and offer a fix before writing.

---

### Step 5: Confirm and Write

Confirm with the user:

> "Your title is: **[Title]**. Ready to lock it in?"

Once confirmed, do both of the following:

1. **Write `book-title.md` to the book root** (the pipeline validator reads it here):

   ```
   Final Title: [Chosen Title]
   ```

2. **Create the title folder** — a subfolder inside the book's working directory named after the chosen title, sanitized for Windows:
   - Replace `:` with ` -` (e.g., `System: Reborn` → `System - Reborn`)
   - Remove any characters illegal on Windows: `< > " / \ | ? *`
   - Trim extra whitespace
   
   Example: `The Iron Throne: A Beginning` → `The Iron Throne - A Beginning`

   This **title folder** is where every file from Step 7 (Chapter Map) through Step 11 (Cover Prompt) will be written. It keeps all draft files for this title grouped together, separate from the story scaffolding files (Steps 1–5) at the book root.

The next step is `/novel-chapter-mapper`, which will write its chapter map into the title folder.

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after the user locks in their chosen title, `book-title.md` is written, and the title folder is created, end with the exact line:

> **Step 6 complete. Output: `[book-folder]/book-title.md` | Title folder: `[book-folder]/[sanitized-title]/`**

The orchestrator will then run `pipeline_validator.py --step 6` and route to Step 7 (`/novel-chapter-mapper`). When invoked manually by the user, end as described in the Output section above.
