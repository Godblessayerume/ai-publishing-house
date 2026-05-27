---
description: Redo a specific pipeline step (1-11) for an existing book. Overwrites the existing output file(s).
argument-hint: "<step-number> [book-folder-name]"
---

The user wants to redo a specific step in the pipeline.

Invoke the `ai-publishing-house` skill via the Skill tool with the following context:

- **Intent**: `jump-to-N` where N is the step number passed as an argument
- **Mode**: Active

Workflow:

1. Parse the step number from the command arguments. Valid range: 1-11.
2. If the user passed a book slug as a second argument, use that. Otherwise list vault folders and let the user pick.
3. Confirm with the user:
   > "You want to redo Step [N] (`/skill-name`) for book `[book-name]`. This will overwrite the existing output file(s). Do you want to:
   > (a) Redo just Step [N] and stop
   > (b) Redo Step [N] and continue auto-chaining through subsequent steps"
4. Based on the user's answer:
   - (a): Invoke the single skill in auto-chain mode, validate, then stop.
   - (b): Invoke the skill, then continue the auto-chain loop from Step N+1, pausing at any remaining decision points.

If no step number was passed, ask:
> "Which step do you want to redo? (1: genre, 2: seed, 3: outline, 4: world, 5: architect, 6: title, 7: chapter map, 8: drafter, 9: editor, 10: publisher, 11: cover prompt)"

Validate output after every step invocation. If validation fails, stop and report.

Begin now by invoking the orchestrator skill.
