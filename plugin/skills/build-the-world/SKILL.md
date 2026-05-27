---
name: build-the-world
description: >-
  A 5-step sequential world-building skill for fiction novels. Pauses once at
  Step 1 for the user to choose a world name, then automatically runs Steps 2
  through 5 without interruption — generating the map, all setting files, the
  character list, and all character biographies. Outputs separate .md files
  organized into a world/ folder.
---

# Build The World

## Overview

This skill runs world-building in 5 sequential steps. There is **only one decision point**: Step 1, where you choose the world name. After that, the AI completes Steps 2 through 5 automatically without stopping. Outputs are written as individual `.md` files organized into the following folder structure inside your active book's working directory:

```
world/
├── world-map.md                  ← Steps 1 & 2
├── settings/
│   ├── [location-name].md        ← Step 3 (one file per geography)
│   └── ...
└── characters/
    ├── character-list.md         ← Step 4
    └── bios/
        ├── [character-name].md   ← Step 5 (one file per character)
        └── ...
```

---

## Before You Begin

Confirm you have the following locked in from earlier pipeline steps:

- The **Sub-Genre** of the story
- The **Plot Archetype(s)** selected
- The completed **Story Seed** (C/W/D/A/C outline + 1-sentence seed + expanded seed)
- The completed **3-Act Outline** (all 9 beats)

If any of the above are missing, stop and complete those steps first using `/novel-story-seed-writer` and `/novel-3-act-outliner`.

---

## Step 1 — Name the World

Read the story's sub-genre, plot archetypes, and story seed to understand the tone, setting era, and feel of the world.

Generate **20 world name options** that:
- Feel native to the sub-genre and tone
- Are distinct, memorable, and easy to pronounce
- Reflect the geography, culture, or mythology implied by the story

Present the 20 names in a numbered list with a one-line explanation for each name.

**Pause here — this is the only decision point.** Ask the user to choose a name from the list. Once a name is chosen, proceed through Steps 2–5 automatically without stopping.

---

## Step 2 — Generate the World Map

Using the chosen world name and the story's context, build the world map.

### Map Structure

1. **The Continent** — give it a name and describe its 2-3 most distinct physical features (mountain ranges, seas, climate zones, etc.)
2. **4 Major Cities** — one in each cardinal direction (North, South, East, West). For each city:
   - Name it
   - Describe its most distinct features (make each city radically different from the others in culture, architecture, economy, or climate)
3. **Surrounding Towns** — for each major city, name 3-5 small towns surrounding it and describe their most distinct feature

### Output

Write everything above to: `world/world-map.md`

Format:
```
# [World Name] — World Map

## The Continent: [Continent Name]
[Description]

## Major Cities

### North: [City Name]
[Description]

### South: [City Name]
[Description]

### East: [City Name]
[Description]

### West: [City Name]
[Description]

## Surrounding Towns

### Towns near [North City]
- **[Town Name]:** [Description]
- ...

### Towns near [South City]
- ...
[etc.]
```

Proceed to Step 3.

---

## Step 3 — Describe Every Setting

Using the map from Step 2, build a full list of every named geography (continent, 4 cities, all towns). Describe each one using the 30 aspects below.

### The 30 Aspects

1. Geography
2. Climate
3. Flora and Fauna
4. History and Lore
5. Magic System
6. Rare Materials
7. Technology
8. Economy
9. Factions and Organizations
10. Religion and Belief Systems
11. Government and Political Structure
12. Laws and Legal System
13. Education System
14. Architecture and City Planning
15. Transportation and Infrastructure
16. Communication Systems
17. Social Hierarchy and Class Structure
18. Art, Music, and Culture
19. Fashion and Clothing
20. Food and Cuisine
21. Languages and Dialects
22. Races and Species
23. Family Structure and Relationships
24. Traditions and Customs
25. Calendar and Timekeeping
26. Currency and Trade
27. Health and Medicine
28. Science and Research
29. Exploration and Frontiers
30. Conflicts, Wars, and Quests

### How to Execute

Work through **one geography at a time**:

1. Describe that geography across all 30 aspects
2. Write the output to: `world/settings/[location-name].md`
3. Immediately move to the next geography without stopping
4. Repeat until every geography on the map has been described

### Output Format (per file)

```
# [Location Name]

## 1. Geography
[Description]

## 2. Climate
[Description]

[...continue through all 30 aspects...]
```

> Note: Not every aspect will apply to every setting. For aspects that don't apply (e.g. Magic System in a realistic fiction), write "N/A — [brief reason]" rather than skipping the field entirely. This keeps the document consistent and reminds the writer it was considered.

---

## Step 4 — Create the Character List

Using the story seed, 3-act outline, and world settings as context, generate the full cast.

### Cast Size

- **3–5 Main Characters**
- **5–8 Supporting Characters**

### Character Card (for each character)

- **Name** — fitting for the world and sub-genre
- **Origin** — where on the map they are from
- **Appearance** — 1–2 sentences describing what they look like
- **Contradiction** — 1 personality contradiction that makes them interesting (e.g. brave but deeply afraid of intimacy)
- **Want** — 1 specific thing they want in this story (tracks their arc)

### Output

Write all character cards to: `world/characters/character-list.md`

```
# Character List

## Main Characters

### [Character Name]
- **Origin:** [Location from map]
- **Appearance:** [1-2 sentences]
- **Contradiction:** [Their contradiction]
- **Want:** [Their goal in the story]

[...repeat for each main character...]

## Supporting Characters

[...same format...]
```

Once the character list is written to file, immediately proceed to Step 5.

---

## Step 5 — Write Character Biographies

Using the character list from Step 4, write a full biography for each character — one at a time.

### Biography Template (for each character)

- **What they look like** (expand on the character card)
- **How old they are**
- **Their biggest strength**
- **Their biggest weakness**
- **A recognizable personality quirk**
- **A strange habit they have**
- **A trait that makes them admirable and lovable**
- **A trait that makes the reader question their intentions**
- **Their most prized possession**
- **Their dream and goal in this story**
- **Their biggest fear** (if their goal doesn't get achieved)

### How to Execute

Work through **one character at a time**:

1. Write the full biography for that character
2. Write the output to: `world/characters/bios/[character-name].md`
3. Immediately move to the next character without stopping
4. Repeat until every character on the list has a biography

### Output Format (per file)

```
# [Character Name] — Biography

## Appearance
[Description]

## Age
[Age]

## Biggest Strength
[Description]

## Biggest Weakness
[Description]

## Personality Quirk
[Description]

## Strange Habit
[Description]

## What Makes Them Admirable and Lovable
[Description]

## What Makes the Reader Question Their Intentions
[Description]

## Most Prized Possession
[Description]

## Dream and Goal in This Story
[Description]

## Biggest Fear
[Description]
```

---

## World-Building Complete

When all 5 steps are done, confirm to the user that world-building is complete and list all the files generated. The next step in the pipeline is `/outline-architect`.

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after all 5 world-building steps are done end with the exact line:

> **Step 4 complete. Output: `[book-folder]/world/world-map.md` (+ settings and character bios)**

The orchestrator will then run `pipeline_validator.py --step 4` and route to Step 5 (`/outline-architect`). When invoked manually by the user, end as described in the Output sections above.
