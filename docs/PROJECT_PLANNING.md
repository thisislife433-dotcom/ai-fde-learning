# Plan the work before changing the project

**Decision, 16 October 2026:** use **Azure DevOps Boards** for planning and keep code, branches, pull requests and existing CI in **GitHub**. Azure Boards replaces the earlier GitHub Projects proposal.

**Azure Boards is the sole live tracker after the verified 22 October 2026 handover.** The private aipoc project has 31 saved items representing 24 tasks, with 39 verified native prerequisite links. [Open the board](https://dev.azure.com/waseemjaleel0723/aipoc/_boards/board/t/aipoc%20Team/Stories). GitHub PR #1 has a verified native relation to Azure P00 through `AB#3`. Original GitHub issues now point to their Azure destinations. Do not create the superseded GitHub Projects board or repeat the new-item import.

- [Azure Boards setup and handover evidence](AZURE_BOARDS_SETUP.md)
- [Azure roadmap Epic](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/1/?view=edit)
- [Ordered task index](../progress/WORK_BACKLOG.md)
- [P00: current setup task](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/3/?view=edit)
- [Personal learning checkpoint](../progress/LEARNING_TRACKER.md)

## One source for each kind of evidence

| Record | What it owns |
|---|---|
| Original GitHub issues | Historical scope and transfer notices; follow each Azure destination |
| Azure roadmap Epic and phase Features | Overall outcome, phases and planning decisions |
| Azure User Story or Bug | Scope, prerequisites, criteria, blockers and evidence |
| Azure board column and work-item State | Current state; use a Blocked tag for an obstacle |
| GitHub PR and CI run | Exact changes, review, checks and merge evidence |
| Release work item | Tested artifact, environment, approval and observed release result |
| Learning tracker | What the learner personally ran, reviewed and can explain |

The task index and CSV are maps and transfer material, not duplicate live trackers. Handover notices preserve the original GitHub issue history. The roadmap and 23 task issues are closed as transferred using GitHub's `not_planned` reason; the work remains planned in Azure. GitHub P00 (#3) stays open until the learner identifies the next Ready task, as does Azure P00. Moving a task does not complete it.

## What every work item needs

Before a lesson, feature, bug fix, infrastructure change or release, select its existing item or create a focused one. Record the problem, expected result, type, phase, priority, prerequisites, criteria, branch/review path and meaningful checks. Resolve account, environment and spending choices before execution.

Keep stable task codes such as L01, F01 and B01 when Azure assigns numeric IDs. A GitHub issue number is not an Azure work-item ID. P1 means the next foundation batch; P2 means later work, not optional. Do not invent dates, sprint capacity or progress percentages.

Split large future outcomes into smaller linked Tasks before implementation when one PR cannot comfortably deliver and explain the result. Each child needs criteria; the parent's outcome and learning checks still apply.

## Work states

Use the standard **Agile process** and this team board mapping. The project process is separate from the Basic access licence.

| Column / marker | Agile State | Meaning |
|---|---|---|
| Backlog | New | Prerequisites or implementation detail remain outstanding |
| Ready | New | Clear scope and checks; prerequisites met |
| In progress | Active | Selected work; keep one item here at a time |
| Review | Resolved | Result and evidence ready for review |
| Done | Closed | Criteria, review and applicable deployment/learning evidence verified |
| Blocked tag | Retain current State | Record the obstacle and next unblocking action |

Ready and Backlog are board columns sharing New, not extra process states. Blocked is a tag. Check the mapping for User Story and Bug. An open PR alone is not enough for Review; a merge alone is not enough for Done. Reopen work if evidence reveals a gap.

## Our session routine

1. Read the roadmap and select one Ready item.
2. Review the previous checkpoint.
3. Explain one concept, do one practical step and inspect it together.
4. Use a focused branch, commit and PR when repository changes are needed.
5. Record evidence, blockers and the next action in the live item and learning tracker.

Phone work includes planning, reading files, PR diffs and CI. L02 chooses the environment for terminal exercises. Do not assume the learner ran a command because the assistant ran it elsewhere. Saying OK is not proof of mastery.

A backlog does not authorise every future implementation, paid provisioning, reminders or marking lessons complete. Calendar targets follow agreed availability.

## Connect work to Git and releases

Follow [Contributing](../CONTRIBUTING.md) and [Branching and releases](BRANCHING_AND_RELEASES.md).

- Start feature and ordinary bug-fix branches from latest develop; include a stable task code.
- Use a link-only `AB#<actual-azure-id>` and the work-item URL. Never substitute a GitHub number for an Azure ID.
- Add the reverse PR link and checks to the live item. Avoid automatic closing/state-transition commands for learning and release work; check criteria explicitly.
- P00 documentation continues in the existing feature/agent-delivery-learning-track draft PR #1, the learner's first review exercise.
- GitHub closing keywords target default branch main; do not assume a PR into develop closes its issue. With either tracker, develop integration is not deployment.
- Release work stays open until its environment, artifact, configuration and smoke checks pass. Use the release guide for promotion, rollback and hotfix synchronisation.

## Completion evidence

| Type | Evidence |
|---|---|
| Learning | Learner explanation, command/result or reviewed diff |
| Feature | Expected behaviour, meaningful checks, reviewed PR and integration target |
| Bug | Reproduction, failing regression before fix, passing result after it and reviewed PR |
| Model/MCP | Actual tool exchanges/evaluations, tested versions and limitations |
| Infrastructure | Reviewed resources, identity checks, cost decisions and deployment result |
| Release | Candidate source/tree, image digest, approval, environment and smoke checks |
| Recovery | Known-good artifact/configuration and observed rollback or hotfix result |

Record assistant implementation and learner demonstration separately. Keep secrets, private logs and account details out of this public repository.

## References

- [Azure Boards Agile workflow](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process-workflow?view=azure-devops)
- [Azure Boards links to GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github?view=azure-devops)
- [GitHub issue closing rules](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
