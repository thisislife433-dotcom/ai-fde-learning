# Azure Boards for AI FDE learning

**Updated 22 October 2026. The board is configured and the backlog is saved. GitHub app integration and final tracker handover remain pending.**

- [Open the board](https://dev.azure.com/waseemjaleel0723/aipoc/_boards/board/t/aipoc%20Team/Stories)
- [Open work query](https://dev.azure.com/waseemjaleel0723/aipoc/_queries/query/f28ee6bc-c4af-47aa-85c8-bb1bd553addd/)
- [All work query](https://dev.azure.com/waseemjaleel0723/aipoc/_queries/query-edit/9a485013-01b0-4e54-9740-3347619e9acb/)
- [P00 setup item](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/3/?view=edit) and its [temporary GitHub issue](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3)
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

## Remaining GitHub connection and handover

1. Install/configure Microsoft's Azure Boards GitHub app for **only** thisislife433-dotcom/ai-fde-learning. Review the actual requested permissions before granting access. The GitHub connection has not been authorised or verified.
2. Connect the existing organisation/project above. Do not create another project or import the same backlog again.
3. Use link-only `AB#3` in [draft PR 1](https://github.com/thisislife433-dotcom/ai-fde-learning/pull/1), then verify the work-item link and reverse GitHub PR relation. An ordinary hyperlink does not prove integration. Avoid automatic completion commands.
4. Add the exact Azure destination to each source GitHub issue, retire it as **transferred, not completed**, and preserve its history. Only then declare Azure Boards the sole live tracker.
5. Ask the learner to locate the next Ready task and explain its purpose. Keep P00 open until all its criteria are met.

Until this handover is verified, the existing GitHub issues remain the temporary authority. Repository links provide access to the saved Azure items without claiming the cutover is complete.

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
