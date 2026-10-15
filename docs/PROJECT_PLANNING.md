# Plan the work before changing the project

**Agreed 16 October 2026.** Use GitHub Issues for the live backlog and GitHub Projects for the planned visual board. Tasks, code, pull requests and releases stay with this repository. We are learning the planning process as well as the software.

- [Master roadmap and current next steps](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/2)
- [Ordered task index](../progress/WORK_BACKLOG.md)
- [P00: planning and board setup](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3)
- [Personal learning checkpoint](../progress/LEARNING_TRACKER.md)

The issues are real work items. The visual board has its own setup acceptance criteria in P00; it is not created merely by adding these documents. The browser was signed out of GitHub when the initial backlog was prepared, so native board setup remains pending. No separate Jira subscription or Azure resource was created for this planning work.

## One source for each kind of evidence

| Record | What it owns |
|---|---|
| Master roadmap issue | Phase index, next task and significant planning changes |
| Individual issue | Scope, prerequisites, acceptance criteria, blockers and completion evidence |
| Issue Status line, until the board exists | Current work state |
| Native Projects Status field, after setup | Current work state; remove the old Status line from issue bodies when migrating |
| Pull request and CI run | Exact changes, review, checks and merge evidence |
| Release/deployment task | Tested artifact, environment, approval, configuration and observed release result |
| Learning tracker | What the learner personally ran, reviewed and can explain |

The task index in this repository is an ordered map, not a duplicate status board. Open the linked issue for current evidence. Keep descriptions and status consistent when work changes; do not infer completion from an issue title or a checked-in implementation alone.

## What every work item needs

Before starting a substantive lesson, feature, bug fix, infrastructure change or release, identify its existing issue or create a focused new one. Record:

1. The user or learning problem and the observable result we want.
2. Type, phase and priority. The initial backlog uses stable task IDs such as L01, F01 and B01.
3. Linked prerequisites and any concrete blocker.
4. Scope and acceptance criteria, including relevant failure behaviour.
5. A proposed branch or review path, plus meaningful verification.
6. Any account, environment or spending choice that must be resolved before execution.

Use P1 for the next foundation/learning batch and P2 for planned later work. P2 does not mean optional. Record an actual incident's urgency separately if one arises. Do not invent dates, sprint capacity or progress percentages. Agree session availability before assigning calendar targets.

Large future tasks are planning containers. Before implementation, split them into smaller linked issues if their changes cannot be reviewed and explained comfortably in one focused PR. Give each child its own acceptance criteria and update the parent with links.

## Work states

| State | Meaning and exit condition |
|---|---|
| Backlog | Agreed future scope; prerequisites or implementation detail remain unfinished |
| Ready | Prerequisites are met, scope/checks are clear and we can select the next practical step |
| In progress | This is the task we are actively doing; keep one task here at a time |
| Review | The result and evidence are ready to inspect; a PR being open alone is not enough |
| Blocked | A concrete prerequisite or external action prevents progress; record what will unblock it |
| Done | The issue's acceptance criteria are observed and linked, with the required review/merge/deployment complete |

An issue can return from Review to In progress when review finds a gap. Unblocking a task does not automatically mark it Done. Close a completed issue with the completed reason; close cancelled work with the appropriate not-planned reason and an explanation.

## Our session routine

1. Read the roadmap's current focus and the selected issue.
2. Review the previous checkpoint for a few minutes.
3. Explain one concept, do one practical step and inspect its result together.
4. Make a small branch/commit/PR when code or repository documents change.
5. Record what happened, what remains uncertain and the exact next action in the issue and learning tracker.

Phone-friendly work includes planning, reading files, examining PR diffs and checking CI results. L02 chooses the environment for terminal exercises. Do not assume a computer is configured or that the learner ran a command because the assistant ran it elsewhere.

The assistant can prepare work, test and explain it, and update the selected task's evidence during our sessions. A backlog is not an instruction to implement all tasks at once, provision paid resources, schedule reminders or mark every lesson complete.

## Connect the task to Git and releases

Follow [Contributing](../CONTRIBUTING.md) and [Branching and releases](BRANCHING_AND_RELEASES.md).

- Feature and ordinary bug-fix work starts from the latest develop. Include the task ID or issue number in a descriptive branch name.
- Reference the issue in commits when useful and put `Refs #<issue-number>` in the PR description. Add a reverse PR link to the issue so the relationship is easy to find.
- For the current existing learning-foundation PR, P00's documentation changes continue on feature/agent-delivery-learning-track. The draft remains the learner's first review exercise.
- GitHub closing keywords are evaluated for PRs targeting the default branch. Our default is main; feature PRs target develop. Therefore do not rely on `Closes` or `Fixes` to close a develop task automatically.
- After a develop PR merges, explicitly close its issue only if that issue's criteria are met. A release or deployed-behaviour issue remains open until its environment checks pass.
- A feature merged to develop is not proof of deployment. Dev and production have their own tasks, artifact digests, configuration and smoke-test evidence.
- Keep release and hotfix history, approval controls and artifact promotion consistent with the release guide.

## Completion evidence depends on the task

| Task type | Evidence to record |
|---|---|
| Learning | The learner's own explanation, command/result or reviewed diff; no automatic pass for saying OK |
| Feature | Expected behaviour, meaningful tests, reviewed PR and integration target |
| Bug | Reproduction, failing regression on the parent, passing result after the fix and reviewed PR |
| Model/MCP | Actual discovery/tool exchanges and evaluations, tested versions, evidence/citations and known limitations |
| Infrastructure | Reviewed resource changes, identity/access checks, cost decisions and observed deployment output |
| Release | Candidate source/tree, image digest, approval, environment/configuration and smoke checks |
| Recovery | Known-good artifact/configuration, observed rollback or hotfix result and synchronisation evidence |

Preserve the distinction between implementation completed by the assistant and a skill demonstrated by the learner. Record both honestly. Keep secrets, private logs and account identifiers out of public issues and commits.

## Planned native board configuration

P00 owns completion of this setup and its verified board URL:

- Name: **AI FDE - Learning and delivery**; link this repository.
- States: Backlog, Ready, In progress, Review, Blocked and Done.
- Fields: Phase, Priority and Type, populated from the task issues. Add dates only when actually agreed.
- Views: an ordered backlog table and a board grouped by Status. Keep the roadmap issue as a reference rather than counting it as implementation work.
- Add the task issues, map their current states, and verify both views before claiming setup is complete.
- Keep completed issue closure and board state consistent. Do not configure an automation that marks a learning task complete merely because a PR merges.
- After setup, add the board URL to the master roadmap, remove duplicate Status lines from the issue bodies and update P00 with evidence.

Until this is complete, the individual issue's Status line is the usable live tracker. Dependencies are explicitly linked in issue bodies; this does not claim that native GitHub milestone, sub-issue or blocking relationships have been configured.

## References

- [GitHub Projects: board, table and roadmap views](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [GitHub issue and PR links, including the default-branch closing rule](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
