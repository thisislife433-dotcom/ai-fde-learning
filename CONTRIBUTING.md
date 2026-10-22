# Make one change from start to finish

This repository is a teaching project. The workflow is part of what we are learning. Start with [the first offline run](docs/START_HERE.md), then use [the delivery track](docs/DELIVERY_PATH.md).

## Plan the task first

Read [Project planning](docs/PROJECT_PLANNING.md) and choose the existing Azure work item from the [work backlog](progress/WORK_BACKLOG.md), or create a focused new one in Azure Boards. The [handover](docs/AZURE_BOARDS_SETUP.md) is verified; original GitHub issues preserve history. Define the result, prerequisites, criteria and checks before changing files. Keep one task In progress. Include its stable task code in a descriptive branch name.

## Start a feature

From a clean checkout, fetch the current development branch and create your own branch:

```bash
git fetch origin
git switch -c feature/describe-your-change origin/develop
```

Use `bugfix/describe-the-defect` for an ordinary bug fix. Choose a new descriptive branch name each time. Start from `origin/main` only for a production hotfix; follow [the release guide](docs/BRANCHING_AND_RELEASES.md).

## Implement, check and commit

1. Describe the expected behaviour and one way to verify it.
2. Make a focused change. For a defect, reproduce it and add a regression test that fails before the fix.
3. Run the relevant checks:

```bash
python -m unittest discover -s tests -v
python -m lab demo
python scripts/check_docs.py
git diff --check
git diff
git status --short
```

4. Stage only the intended paths with `git add`, inspect `git diff --cached`, then commit with a specific message such as `fix: handle singular truck in policy routing`.
5. Push with `git push -u origin HEAD` and open a pull request with **base: develop**. Use a link-only `AB#<actual-azure-id>` plus its URL. GitHub and Azure numbers are different. Record the problem, result and checks, and verify the native GitHub PR relation in the Azure work item's Development section.
6. Inspect the diff and CI output. Resolve review feedback before merging. A passing check does not replace understanding the change.

Use a squash merge for an individual feature or bug-fix PR. Preserve history with a merge commit for `develop` to `main` release PRs and `main` back to `develop` synchronization PRs. See [branching and releases](docs/BRANCHING_AND_RELEASES.md) for the reasons and release conditions.

## Record evidence

After review and merge, verify the work item's criteria before closing it. Avoid automatic closing/state-transition commands for Azure learning and release items. GitHub's closing keywords target the default branch; do not assume merging into develop closes an issue or deploys a feature. Release and deployment tasks require their own observed environment checks.

Update [your tracker](progress/LEARNING_TRACKER.md) after doing the exercise. Record its PR, commands and result. The offline test workflow is available now. MCP, container and deployment checks will be added in their own exercises.

Do not commit `.env`, `runtime/`, `work/`, or `progress/private/`. Original source attribution and its pinned submodule remain intact.
