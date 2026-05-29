---
name: amazon-upload-kit
description: >-
  Generates the complete Amazon KDP upload metadata package for Kindle
  publishing — an HTML-formatted book description (under 4,000 characters),
  7 strategic keyword phrases (each under 50 characters), and 3 recommended
  Kindle browse categories for Kindle Unlimited placement. Output:
  amazon-upload-kit.md. Terminal step of the pipeline.
---

# Amazon Upload Kit

The final pipeline step. Generates everything needed to upload the book to Amazon KDP. Nothing here is creative prose — it is marketing infrastructure. The goal is discoverability: the right words in the right fields so the right readers find the book.

---

## Before You Begin

Read:

- `[plugin-root]/plugin.json` — `config.authorName`
- `story-config.md` — sub-genre and stacked plot archetypes
- `story-seed.md` — characters, world, conflict, and tone
- `3-act-outline.md` — arc, themes, and stakes
- `book-title.md` — `Final Title:` line

**Finding the title folder:** Read `book-title.md` at the book root, extract the `Final Title:` value, sanitize it (replace `:` with ` -`, remove `< > " / \ | ? *`).

---

## Amazon KDP Field Limits

| Field | Limit |
|---|---|
| Description | 4,000 characters maximum (HTML tags count toward the limit) |
| Keyword fields | 7 fields, each maximum 50 characters including spaces |
| Categories (during upload) | 3 categories selectable at upload time |


---

## Step 1: Write the Amazon Description

### What the description must do

A reader who finds the book on Amazon will see the first 400 characters before clicking "Read more." Those first 400 characters are the make-or-break moment. The description must answer three questions immediately: Who is this about? What do they want? What stands in the way?

### Structure

```
[HOOK — one or two sentences. Protagonist + situation + the thing that changes everything.]

[STAKES PARAGRAPH — what the protagonist must do, what happens if they fail, what they stand to lose.]

[CONFLICT PARAGRAPH — the key relationship or opposition driving the story. Internal and external tension.]

[CLOSING LINE — ends without resolution. Creates urgency. Does not spoil.]

[COMP LINE — "For fans of [Title] and [Title]."]
```

### HTML formatting

KDP supports these tags in descriptions. Use them:

- `<b>` — bold, for the hook line or a single key phrase
- `<i>` — italic, for comp titles and the comp line
- `<br><br>` — paragraph break (use this between every section)
- `<p>` — paragraph (alternative to `<br><br>`)

Do not use: `<h1>`, `<h2>`, `<h3>`, `<div>`, `<span>`, `<a>`, `<img>`

### Rules

- Write in present tense ("Mara discovers" not "Mara discovered")
- Do not reveal the resolution or the climax outcome
- Do not use review quotes — those go in Editorial Reviews, not the description
- Count the characters after writing. Include the count in the output. Stay under 4,000.
- If the count exceeds 4,000, trim the stakes or conflict paragraph first — never the hook

---

## Step 2: Generate 7 Keywords

### How Amazon uses keywords

Keywords appear in the book's metadata. Amazon matches them against what readers type into the search bar. They also influence "customers also bought" and browse recommendations. The title and author name are already indexed by Amazon separately — do not repeat them in keyword phrases.

### What works

Amazon readers search by:

| Search type | Example phrases |
|---|---|
| **Trope** | "enemies to lovers fantasy", "chosen one dark fantasy" |
| **Setting + genre** | "dark academy magic system fantasy", "post-apocalyptic survival series" |
| **Mood/tone** | "fast paced fantasy series", "dark gritty fantasy novel" |
| **Comp-style** | "books like fourth wing", "fantasy adventure series" |
| **Character type** | "female warrior fantasy", "antihero redemption arc fantasy" |
| **Series signal** | "book one complete series fantasy", "standalone dark fantasy" |
| **Sub-genre specific** | LitRPG: "progression fantasy leveling system"; romantasy: "fae court enemies to lovers" |

### Rules

- Each phrase ≤ 50 characters (count them — show the count)
- Use lowercase (Amazon normalizes case anyway)
- Use 3–5 word phrases, not single words
- Do not repeat any word from the book title
- Do not use competitor author names or specific comp titles (Amazon policy violation)
- Do not use misleading terms or genres the book doesn't fit

Generate all 7. After each phrase, show the character count in parentheses.

---

## Step 3: Recommend 3 Categories

### How categories drive Kindle Unlimited traffic

For Kindle Unlimited authors, category placement determines browse visibility. A book ranked #1 in a niche category gets a "Best Seller" or "#1 New Release" badge, which drives organic clicks. Being ranked #200 in a mega-category ("Fantasy") gets nothing.

The strategy: find the most specific category that accurately describes the book, not the most prestigious one.

### How to select categories

1. Start with the exact sub-genre from `story-config.md`
2. Navigate Amazon's Kindle browse tree to the most specific matching category
3. Avoid top-level categories unless the book already has significant reviews and velocity
4. For the cross-genre recommendation, find a category that captures secondary genre elements (romance subplot → a romance sub-category; horror elements → a horror sub-category)

### Format

Write each recommendation as the full Amazon browse path:

```
Kindle Store > Kindle eBooks > Science Fiction & Fantasy > Fantasy > Epic Fantasy
```

Rank the three recommendations:

1. **Primary** — most precise match to the book's sub-genre
2. **Secondary** — slightly broader category in the same genre space (fallback if the primary is too crowded or the book doesn't qualify)
3. **Cross-genre** — captures a secondary genre element or tone

For each, write one sentence: why it fits and whether it is a crowded or niche category.

---

## Output

Write everything to `[title-folder]/amazon-upload-kit.md`. This file is designed to be opened and copied directly into KDP upload fields — no editing required.

```markdown
# Amazon Upload Kit — [Final Title]
*Author: [config.authorName]*

---

## Description
**Character count: [N] / 4,000**

[HTML-formatted description — paste directly into the KDP description field]

---

## Keywords
*(Each field: max 50 characters. Paste one phrase per KDP keyword box.)*

1. [keyword phrase] ([N] chars)
2. [keyword phrase] ([N] chars)
3. [keyword phrase] ([N] chars)
4. [keyword phrase] ([N] chars)
5. [keyword phrase] ([N] chars)
6. [keyword phrase] ([N] chars)
7. [keyword phrase] ([N] chars)

---

## Categories

**Primary:**
Kindle Store > [full browse path]
*[One sentence: why it fits + crowded vs. niche]*

**Secondary:**
Kindle Store > [full browse path]
*[One sentence: why it fits + crowded vs. niche]*

**Cross-genre:**
Kindle Store > [full browse path]
*[One sentence: why it fits + crowded vs. niche]*

```

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after the kit is written end with the exact line:

> **Step 14 complete. Output: `[book-folder]/[sanitized-title]/amazon-upload-kit.md`**

The orchestrator will then run `pipeline_validator.py --step 14` and report the pipeline complete. This is the terminal step — no further skills follow. When invoked manually, end as described in the Output section above.
