# Working on this learning repository

Read README.md, docs/VERIFICATION.md, CONTRIBUTING.md and progress/LEARNING_TRACKER.md before continuing a learning task.

- Use docs/PROJECT_PLANNING.md and docs/AZURE_BOARDS_SETUP.md before substantive work. Azure Boards is selected; until its migration is verified, use roadmap issue #2 and the existing GitHub tasks. Find or create the work item, read prerequisites and criteria, and keep one task In progress. A backlog does not authorise every future item at once.
- Do not create the superseded GitHub Projects board. Never invent Azure IDs or treat a CSV as a live import. After verified handover, use Azure Boards as the sole live tracker and link actual IDs with AB# references.
- Keep issue/board status, PR links and evidence current during the selected task. Do not treat a develop merge as a production deployment or rely on default-branch closing keywords to close develop tasks.
- Teach one concept and one practical step at a time. Record only observed learning progress; acknowledgement alone is not proof of mastery.
- Distinguish the deterministic offline lab, the upstream AI application and proposed MCP/cloud work. Label simulated data and planned capabilities explicitly.
- Use a focused feature or bug-fix branch and a pull request following docs/BRANCHING_AND_RELEASES.md. Check the current branch and worktree before edits. Preserve unrelated user changes.
- Keep upstream/cold-chain pinned and unchanged unless the user specifically requests an upstream version update. Teaching adaptations belong in our code or the ignored work copy.
- Run the relevant checks before claiming success: `python -m unittest discover -s tests -v`, `python -m lab demo`, and `python scripts/check_docs.py`.
- Keep credentials, private notes and generated runtime files out of commits. Use synthetic data in examples and test reports.
- For MCP or provider-specific changes, check the current official protocol/SDK documentation and record the tested versions. Tool descriptions do not replace input validation or permissions.
- Explain the change, test evidence and remaining limitations in the PR. Keep planned deployments and completed deployments distinct.
