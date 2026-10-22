# Azure Boards for AI FDE learning

**Updated 22 October 2026. The board, GitHub app integration and tracker handover are verified. Azure Boards is the live tracker. P00 remains open for the learner's next-task check.**

- [Open the board](https://dev.azure.com/waseemjaleel0723/aipoc/_boards/board/t/aipoc%20Team/Stories)
- [Open work query](https://dev.azure.com/waseemjaleel0723/aipoc/_queries/query/f28ee6bc-c4af-47aa-85c8-bb1bd553addd/)
- [All work query](https://dev.azure.com/waseemjaleel0723/aipoc/_queries/query-edit/9a485013-01b0-4e54-9740-3347619e9acb/)
- [P00 setup item](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/3/?view=edit) and its [original GitHub issue](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3), retained open for the learner check
- [Task index](../progress/WORK_BACKLOG.md) and [verified ID/prerequisite map](../planning/azure-work-item-map.json)

## Project choices

| Setting | Verified choice |
|---|---|
| Organisation | waseemjaleel0723, selected by the user during sign-in |
| Project | aipoc |
| Visibility | Private |
| Process | Agile; changed from Basic while the project had no work items |
| Access | One Basic user observed on 16 October; no licence or billing change made |
| Code, branches and pull requests | thisislife433-dotcom/ai-fde-learning on GitHub |
| CI | Existing GitHub Actions checks; deployment work remains planned |
| Dates and capacity | No delivery dates or sprint capacity agreed |

The original process was **Basic**, with Epics, Issues and Tasks. We chose **Agile** to organise the project as Epic → Feature → User Story/ Bug → implementation Tasks and to track bugs separately. It fits our feature, defect and release exercises. We can use this as a Kanban board without introducing sprint ceremonies. The process choice is separate from the **Basic access licence** and does not itself change the pricing tier.

## What was saved and verified

On 16 October, an unrestricted query confirmed that the destination had no work items. The new-item import then saved **31 items**: one Epic, six Features, 23 User Stories and one Bug. These represent **24 tasks**, with seven grouping items.

The exported IDs, titles, types, descriptions, priorities and parent links matched the import. All 123 acceptance-checklist entries were retained. The bug form did not display its imported Description, so B01's reproduction steps and criteria were also copied into its visible Repro Steps field. All **39 native predecessor links across 21 tasks** were saved and checked. P00, L01 and L02 have no prerequisites.

| Phase | Feature ID | Task codes |
|---|---:|---|
| Planning | 2 | P00 |
| Foundations | 4 | L01–L06 |
| Features and MCP | 11 | B01, F01, M01, M02 |
| AI application | 16 | Q01, A01, A02, Q02 |
| Azure dev | 21 | C01, I01, I02, I03 |
| Release and operations | 26 | R01, O01, O02, Z01, O03 |

All phase Features belong to [Epic 1](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/1/?view=edit). GitHub issue numbers and Azure IDs are different: for example, L01 is GitHub issue 4 and Azure work item 5.

## Board workflow

| Column | Agile State | Initial placement |
|---|---|---|
| Backlog | New | Tasks with outstanding prerequisites |
| Ready | New | L01 (5), L02 (6) |
| In progress | Active | P00 (3); WIP limit 1 |
| Review | Resolved | Empty |
| Done | Closed | Empty |

The mappings apply to both User Stories and Bugs. Bugs appear alongside requirements. Epics are enabled in backlog navigation. The Stories backlog showed all 24 tasks, including B01. Shared all-work and open-work queries are saved; the open query excludes Closed and Removed without a date cutoff and includes Priority and Board Column.

The board was reopened on 22 October and still showed P00 In progress and L01/L02 Ready. Setup activity is not evidence that the learner has completed a lesson.

## GitHub connection and handover verified on 22 October

The user completed Google/GitHub sign-in and the Azure Boards GitHub App installation. Azure displayed a successful connection to the existing aipoc project. The optional sample-story and badge-PR wizard was skipped; the original backlog was retained.

The initial installation included all eight account repositories. GitHub's installation settings were changed to **Only select repositories**, with **thisislife433-dotcom/ai-fde-learning** as the one selected repository. Reopening those settings confirmed the saved restriction. No broader OAuth grant was accepted.

The link-only `AB#3` reference in [draft PR 1](https://github.com/thisislife433-dotcom/ai-fde-learning/pull/1) was processed by Azure Boards. [Azure P00](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/3/?view=edit) shows the native **GitHub Pull Request** relation, correct title, PR #1, target **develop** and **Draft** status. P00 remains Active; the reference did not complete it.

All 25 original GitHub records (roadmap #2 and tasks #3–26) have exact Azure destination notices. The roadmap and 23 task records are closed using GitHub's `not_planned` reason solely to retire duplicates as **transferred, not completed**. Their history and criteria are retained. The work remains planned in Azure. GitHub P00 (#3) remains open because automatic approval review enforced its outstanding learner check. Azure Boards owns all current task status and evidence.

### Remaining checks

- Ask the learner to locate **L01 — review PR #1 on the phone** in Ready and explain its purpose. Keep both P00 records open until this criterion is demonstrated.
- Azure's connection list still displayed the original eight repository names after the GitHub installation was restricted to one. The saved GitHub permission scope and working native link are verified; the older Azure list is a remaining display/cleanup discrepancy. Azure's Remove repositories action requested a separate broad OAuth grant, so that route was left unapproved. Do not broaden access merely to clean up the list.
- PR #1 remains draft and unmerged for L01. No lesson, live AI integration or deployment is complete merely because planning is connected.

## Import file and recovery

[azure-boards-import.csv](../planning/azure-boards-import.csv) is the dated new-item snapshot used for the import, not a current export. It deliberately has no IDs. **Do not import it again into aipoc:** that would create duplicates. Use the ID map to locate existing items; inspect a current query/export before any repair. The CSV can preserve parent hierarchy, but native non-parent links were added separately.

## Cost and scope

The observed one-user Basic allocation fits the first-five-user free allowance documented at setup. No paid licence, subscription, add-on, Azure app resource or model usage was provisioned by this work. Hosting, AI calls and any future paid services require their own cost decision under I01.

## Official references checked at setup

- [Basic to Agile](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/change-process-basic-to-agile?view=azure-devops)
- [Azure DevOps pricing](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)
- [CSV import and hierarchy](https://learn.microsoft.com/en-us/azure/devops/boards/queries/import-work-items-from-csv?view=azure-devops)
- [Install the Azure Boards GitHub app](https://learn.microsoft.com/en-us/azure/devops/boards/github/install-github-app?view=azure-devops)
- [Link GitHub work](https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github?view=azure-devops)
