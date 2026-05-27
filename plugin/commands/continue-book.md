---
description: Resume an in-progress novel — auto-detects which book you were working on and picks up at the first pending step.
argument-hint: "[optional: book-folder-name]"
---

The user wants to continue an existing novel.

Invoke the `ai-publishing-house` skill via the Skill tool with the following context:

- **Intent**: `continue`
- **Mode**: Active auto-chain (resume)
- **Vault scan**: Required

Workflow:

1. List all folders in `vaultPath` (each is a book).
2. If the user passed a specific book slug as an argument, use that one. If exactly one book exists, use it. If multiple, present a numbered list and ask the user which.
3. Run `pipeline_validator.py --check-state` to find the first pending step.
4. If state is `complete`, report success and the manuscript path. Stop.
5. Otherwise enter the auto-chain loop at the reported next step.
6. **Partial-chapter recovery**: If the reported step is 8 with N chapters already drafted out of M total, pass resume context to the chapter drafter so it begins at chapter [N+1] and skips existing files.

Pause only at the 5 decision points. Validate output between every step. If any validation fails, stop and report.

Begin now by invoking the orchestrator skill.
