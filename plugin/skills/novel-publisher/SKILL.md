---
name: novel-publisher
description: >-
  Compiles individual edited chapter files into a beautifully formatted master manuscript (Markdown or HTML) with an automated Table of Contents.
---

# Novel Publisher

## Overview
This skill compiles individual approved chapter files into a single, cohesive book manuscript. It automatically generates a Table of Contents (TOC) and packages the book into standard Markdown or highly styled HTML ready for digital publishing platforms.

## Dependencies
- `novel-editor`: Requires individual chapter drafts to be edited and approved before compiling.
- `uv`: Requires the Python environment to run the compiler script.

## Utility Scripts
This skill relies on the compiler script located at:
`[plugin-root]/scripts/manuscript_compiler.py`

### Compiler Commands
The compiler is run from inside the **title folder** (created by Step 6 — see below). All chapters and the output manuscript live there.

**Finding the title folder:** Read `book-title.md` at the book root, extract the `Final Title:` value, sanitize it (replace `:` with ` -`, remove `< > " / \ | ? *`). That sanitized string is the subfolder name.

```bash
# Compile all chapters in the title folder to a Markdown master manuscript
cd "[book-root]/[sanitized-title]"
uv run [plugin-root]/scripts/manuscript_compiler.py --output manuscript-final.md

# Compile to a styled HTML document
uv run [plugin-root]/scripts/manuscript_compiler.py --output index.html --format html

# Compile using a custom JSON chapter index to enforce a strict chapter order
uv run [plugin-root]/scripts/manuscript_compiler.py --output manuscript-final.md --index chapters_index.json
```

## Workflow

### Step 1: Prepare Chapter Order
- If chapter files are named in standard sequential order (e.g. `chapter_1.md`, `chapter_2.md`), the compiler will auto-discover and naturally sort them correctly.
- If they have custom names, create a `chapters_index.json` file in the workspace directory to specify the compilation order:
  ```json
  {
    "chapters": [
      "chapter_1.md",
      "special_interlude.md",
      "chapter_2.md"
    ]
  }
  ```

### Step 2: Run Compiler
Execute the compilation command in the workspace directory. Select `markdown` for a master editing manuscript, or `html` for a reading draft.

### Step 3: Validate Outputs
Verify that:
1. The Table of Contents (TOC) is dynamically generated and links to all chapters correctly.
2. Frontmatter is stripped from individual chapters so they integrate seamlessly without scattered meta headers.
3. No duplicate chapter titles exist (the compiler automatically strips inner H1 headers to prevent duplicates).

## Common Mistakes
- **Compiling Unfinished Chapters**: Compiling drafts before they have passed the linter checks in `novel-editor`. Ensure all components are marked as approved first.
- **Skipping Natural Sort Order**: Naming files inconsistently (e.g., `ch_1.md` and `chap2.md`), which confuses the auto-discovery sorting. Stick to `chapter_1.md`, `chapter_2.md` syntax.

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after the manuscript is compiled end with the exact line:

> **Step 10 complete. Output: `[book-folder]/[sanitized-title]/manuscript-final.md`**

The orchestrator will then run `pipeline_validator.py --step 10` and route to Step 11 (`/book-cover-prompt-generator`). When invoked manually by the user, end as normal.
