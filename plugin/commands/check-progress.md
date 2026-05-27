---
description: Show pipeline status for all books in the vault — does NOT chain skills.
---

The user wants a passive status report. Do NOT chain skills or invoke any pipeline step.

Invoke the `ai-publishing-house` skill via the Skill tool with the following context:

- **Intent**: `status`
- **Mode**: Status only (read-only)

Workflow:

1. List all folders in `vaultPath`.
2. For each book folder, run:
   ```
   uv run [plugin-root]/scripts/pipeline_validator.py --book-dir "[book-folder]" --all
   ```
3. Build a summary table showing for each book: name, current pending step, completion percentage (X/11 steps done), last modified date.
4. Report the summary to the user.
5. Suggest the next action per book (e.g., "To resume `book-X`, run `/continue-book book-X`").

Do NOT invoke any pipeline skill. This command is read-only.

Begin now by invoking the orchestrator skill.
