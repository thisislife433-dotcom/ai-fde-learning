# Set up Azure Boards for AI FDE learning

**Selected 16 October 2026. Status: prepared; live setup awaits account access and the destination organisation.** The Microsoft sign-in prompt was declined. No Azure project, work items, board settings or GitHub integration have been created or verified.

[P00 / GitHub issue #3](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3) owns this transfer. Existing issues remain the temporary tracker until every Azure item and link is verified. The earlier GitHub Projects proposal is superseded.

## Project choices

| Setting | Choice |
|---|---|
| Organisation | User-selected personal/learning destination; not yet known |
| Project | ai-fde-learning |
| Visibility | Private |
| Work-item process | Agile |
| Access licence | Basic, within the first-five-user free allowance |
| Code and PRs | Existing thisislife433-dotcom/ai-fde-learning GitHub repository |
| CI/CD | Keep current GitHub Actions; Azure Pipelines is a separate learning decision |
| Dates and iterations | Agree session availability first |

Use a personal learning organisation or another destination the user explicitly chooses. Do not create this project in an employer's organisation merely because it appears after sign-in.

Microsoft currently requires an active Azure subscription for a new organisation; existing organisations and free limits are unaffected. First five Basic users remain free. Extra users, paid add-ons, excess pipeline/artifact usage, hosting and model calls are separate. A free board does not authorise paid services or a billing commitment.

## Backlog structure

The [import file](../planning/azure-boards-import.csv) has **31 new items**: one Epic, six phase Features, 23 User Stories and one Bug. These represent the original **24 tasks**, plus seven containers; they are not 31 lessons.

| Phase Feature | Original task codes | Tasks |
|---|---|---:|
| 0: Planning | P00 | 1 |
| 1: Foundations | L01–L06 | 6 |
| 2: Features and MCP | B01, F01, M01, M02 | 4 |
| 3: AI application | Q01, A01, A02, Q02 | 4 |
| 4: Azure dev | C01, I01, I02, I03 | 4 |
| 5: Release and operations | R01, O01, O02, Z01, O03 | 5 |

Hierarchy: Epic → phase Feature → User Story/Bug. Add small implementation Tasks when starting an outcome. B01 addresses a reproduced defect. Other rows describe learning/delivery outcomes, not completed implementations.

Each original task retains its code, full criteria, prerequisites, proposed branch/review path and source GitHub link. P00 reflects the Azure decision. The CSV is a dated transfer snapshot, not a live status source.

## Create and import

1. Sign in and select the intended organisation. The user resolves any new-account, subscription and terms steps.
2. Create the private project using **Agile**. Verify destination, visibility, process and Basic licence.
3. Check target field names/types against a sample/export. The CSV uses indented Title columns, Description and Priority; it omits IDs, assignees, State, dates and area paths.
4. Use **Boards → Queries → Import work items**, select the CSV, inspect the 31-row preview, then **Save items**.
5. Resolve validation errors. Criteria are in Description. For B01, copy the retained reproduction/criteria into the visible Bug fields if its form does not display Description.
6. Export the assigned Azure IDs. Verify every original task code, phase parent and Epic relationship.

Do not blindly repeat a new-item import: it can duplicate work. After a partial save, query/export existing codes and IDs, then import only missing rows. Use assigned Azure IDs for later updates.

## Finish the board and links

- Show Bugs with requirements on the team backlog, so B01 appears with User Stories.
- Map Backlog/New, Ready/New, In progress/Active, Review/Resolved and Done/Closed. Use a Blocked tag with the actual blocker; retain State. This changes the team board, not process states.
- Put L01 and L02 in Ready. P00 stays active during setup; tag it Blocked if access or another dependency interrupts work. Other tasks stay in Backlog. Import does not complete a lesson.
- Use phase parents and retained type/learning notes for context; retain priorities 1 or 2. Add phase/type tags if useful after checking team conventions.
- Use assigned IDs to create native Predecessor/Successor links for prerequisites. The CSV preserves references but cannot create these non-parent links. A prerequisite is the selected task's Predecessor.
- Save a backlog view and open-work query with ID, type, title, State, Priority and Tags. Check counts and next Ready items; keep one item In progress.
- Connect only this GitHub repository through the Azure Boards app and review requested permissions. Verify a link-only `AB#<actual-id>` in PR #1 against P00 and its reverse PR link. Do not enable automatic completion of learning items on merge. Ordinary hyperlinks help during pending authorisation but do not prove app integration works.

## Complete the handover

- [ ] Verify all 31 saved items, 24 task mappings, criteria, priorities and parent links.
- [ ] Verify native prerequisite links and initial board positions; infer no learner completion.
- [ ] Replace repository task links with actual Azure URLs, retaining source GitHub links as provenance.
- [ ] Add a migration notice and correct Azure link to each original GitHub issue. Retire them as transferred, not completed; preserve their history.
- [ ] Update roadmap/repo to say Azure Boards is live; remove old GitHub Status lines.
- [ ] Verify GitHub linking, record the board URL/evidence in P00.
- [ ] Have the learner identify L01/L02 and explain how to find the next task. Finish P00 only after all criteria are met.

Until these checks pass, existing GitHub issues remain authoritative.

## Official references checked 16 October 2026

- [Organisation creation and subscription requirement](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/create-organization?view=azure-devops)
- [Azure DevOps pricing](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)
- [CSV import and hierarchy](https://learn.microsoft.com/en-us/azure/devops/boards/queries/import-work-items-from-csv?view=azure-devops)
- [Agile workflow](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/agile-process-workflow?view=azure-devops)
- [Work-item fields](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/work-item-field?view=azure-devops)
- [Connect GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops)
- [GitHub work-item links](https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github?view=azure-devops)
