# Working on this learning repository

Read README.md, docs/VERIFICATION.md, CONTRIBUTING.md and progress/LEARNING_TRACKER.md before continuing a learning task.

- Teach one concept and one practical step at a time. Record only observed learning progress; acknowledgement alone is not proof of mastery.
- Distinguish the deterministic offline lab, the upstream AI application and proposed MCP/cloud work. Label simulated data and planned capabilities explicitly.
- Use a focused feature or bug-fix branch and a pull request following docs/BRANCHING_AND_RELEASES.md. Check the current branch and worktree before edits. Preserve unrelated user changes.
- Keep upstream/cold-chain pinned and unchanged unless the user specifically requests an upstream version update. Teaching adaptations belong in our code or the ignored work copy.
- Run the relevant checks before claiming success: `python -m unittest discover -s tests -v`, `python -m lab demo`, and `python scripts/check_docs.py`.
- Keep credentials, private notes and generated runtime files out of commits. Use synthetic data in examples and test reports.
- For MCP or provider-specific changes, check the current official protocol/SDK documentation and record the tested versions. Tool descriptions do not replace input validation or permissions.
- Explain the change, test evidence and remaining limitations in the PR. Keep planned deployments and completed deployments distinct.
