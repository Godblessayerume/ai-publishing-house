---
description: Start a new novel — auto-chains through the full creation pipeline from genre selection to published manuscript.
---

The user wants to start a brand-new novel.

Invoke the `ai-publishing-house` skill via the Skill tool with the following context:

- **Intent**: `new`
- **Mode**: Active auto-chain
- **Skip vault scan**: Yes (we're starting fresh)
- **First action**: Invoke `/novel-genre-picker` in auto-chain mode (it will create the book folder from the user-provided project slug)

Then enter the auto-chain loop as described in the orchestrator skill. Pause only at the 5 decision points:
1. Sub-genre + project slug (in genre picker)
2. Archetype stack confirmation (in genre picker)
3. Story sketch (in story seed writer)
4. World name pick (in world builder)
5. Title pick (in title generator)

Between decision points, run every skill end-to-end. Validate output between every step using `pipeline_validator.py`. If any validation fails, stop and report the reason.

Begin now by invoking the orchestrator skill.
