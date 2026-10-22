# Verification record

**Prepared and checked: 24 September 2026.** Update this file when a new environment or live integration is actually exercised. Do not infer a pass from another layer's test.

| Item | Evidence | Status |
|---|---|---|
| Upstream identity | Git checkout at `ef6633928950ef9c13115fb77439ccab40397790` | Confirmed |
| Offline Python lab | Executed with Python 3.12.14 on Linux x86-64 | Passed |
| Behavioural tests | 12 unittest cases: thresholds, stale/future/missing data, repeat seeding, query parameter handling, mutation refusal, routing and trace preservation | Passed |
| Demo scenario | Three Melbourne results: breach, within fictional limits, unknown current status | Passed |
| Preparation helper | Created isolated working copy; source left clean; parsed all copied Python files without executing them | Passed |
| Preparation controls | Refuses overwrite; confines outputs to `work/`; generated credentials are in ignored local files | Checked |
| Recall-card format and content | 28 unique cards; list/review commands exercised | Checked |
| Cost calculator | Default scenario US$1.62 / AU$2.51 with documented assumptions | Checked |
| Relative companion links | `python scripts/check_docs.py` | Checked before delivery |
| Source supporting material | Code, dataset schema/count, original notes and extracted design/business text reviewed | See source scope |
| Full stack dependency installation | Large upstream requirements not installed in this runtime | Not verified |
| SQL Docker/ODBC integration | Docker unavailable in this runtime | Not verified |
| Pinecone ingestion/retrieval | Requires user's provider account and configured index | Not verified |
| Paid model calls/tool selection | Requires user's API access and evaluation cases | Not verified |
| Streamlit full-stack UI | Depends on the unverified services above | Not verified |
| Cloud or Azure deployment | No resources provisioned | Not performed |
| GitHub workflow run | [Run #1](https://github.com/thisislife433-dotcom/ai-fde-learning/actions/runs/36014466608) on commit `0d06034`: Ubuntu runner with Python 3.12; tests, demo and relative-link check all succeeded | Passed |

## Delivery learning track: 15 October 2026

The extension adds the agent/MCP and dev-to-prod learning path, contribution instructions, PR/issue templates, a broader relative-link check and CI triggers for documentation changes. The 12 existing tests, offline demo and expanded link check passed locally after these changes. Remote check evidence is available in the learning-path PR's Checks tab.

The singular/plural truck-routing defect described in [D5](DELIVERY_PATH.md) was reproduced and remains an open learning exercise. The existing suite does not cover that case. No custom MCP server, HTTP service, container build, Azure infrastructure, branch protection or deployment approval configuration is claimed as implemented by this extension.

## Project planning: 16 October 2026

A [master roadmap](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/2) and 24 task issues now cover the remaining lessons, agent/MCP work, a feature, a regression fix, CI, Azure dev, learning production, recovery and cleanup. Each issue records prerequisites, completion criteria and evidence to collect. [Project planning](PROJECT_PLANNING.md) and the [task index](../progress/WORK_BACKLOG.md) define how to use them.

After these documentation/template changes, all 12 existing unit tests, the offline demo, the relative-link check and `git diff --check` passed locally. No application behaviour or upstream source changed. The learner's checklist remains incomplete. At that initial checkpoint, native Projects board setup was still tracked in [P00](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3), because the browser was signed out. This historical GitHub Projects proposal was superseded by Azure Boards; see the live setup record below.

## Azure Boards decision and prepared transfer: 16 October 2026

The user selected Azure DevOps Boards, replacing the earlier GitHub Projects proposal. [Setup instructions](AZURE_BOARDS_SETUP.md) and the [CSV](../planning/azure-boards-import.csv) are prepared in the existing draft PR. Code and CI remain in GitHub.

Local import checks found 31 rows: one Epic, six phase Features, 23 User Stories and one Bug. All 24 source task codes, 123 acceptance-checklist entries, prerequisite hyperlinks and priorities are retained; title-column hierarchy counts are 1/6/4/4/4/5 tasks per phase. The new-item file excludes IDs, State, assignees and organisation-specific paths.

All 12 existing unit tests, the offline demo, relative-link check and diff check passed. These checks do not exercise Azure's importer. At this preparation checkpoint, Microsoft sign-in was incomplete and the live import and integration had not been verified. That access blocker was subsequently resolved; see the live setup record below. Existing GitHub tasks remain the temporary tracker. No Azure resource or paid service was provisioned, and no learner milestone was marked complete.

## Live Azure Boards setup and repository checkpoint: 16–22 October 2026

The selected destination is the private **aipoc** project. An unrestricted query found no existing items before Basic was changed to Agile. The importer saved 31 work items. The saved export matched titles, types, descriptions, priorities and parent links for every row, retaining 24 task outcomes and 123 criteria. B01's reproduction and criteria were additionally placed in its visible Repro Steps field.

All 39 native predecessor links across 21 tasks were saved and checked. Stories and Bugs use Backlog/New, Ready/New, In progress/Active, Review/Resolved and Done/Closed. WIP is one; P00 is active, L01/L02 are Ready, and the remaining tasks are in Backlog. The Stories backlog showed all 24 tasks. Shared all-work and open-work queries were saved; the latter excludes Closed and Removed and includes Priority and Board Column. One Basic user was observed without changing licences or billing.

On 22 October, the board reopened successfully with the recorded initial positions. [Setup evidence](AZURE_BOARDS_SETUP.md), the [task index](../progress/WORK_BACKLOG.md) and [ID map](../planning/azure-work-item-map.json) now identify the live destinations. The CSV records the actual import snapshot; do not repeat that new-item import. Raw exports and private account details are not committed.

All 12 existing unit tests, the offline demo, documentation-link checks and git diff --check passed after this repository update. These checks do not establish GitHub app integration.

At that repository checkpoint, GitHub app authorisation, native PR linking and final source-issue retirement were pending. Ordinary URLs alone were not proof of app integration. The later verification below supersedes that blocker.

## GitHub integration and tracker handover: 22 October 2026

After the user completed sign-in and installation, Azure displayed a successful GitHub App connection. GitHub's saved installation settings were restricted from all repositories to the single `thisislife433-dotcom/ai-fde-learning` repository and reopened to verify the scope. No separate broad OAuth grant was accepted.

Updating draft PR #1 with the link-only `AB#3` reference produced a native **GitHub Pull Request** relation in Azure P00's Development section. The relation showed the correct PR title, #1, target develop and Draft status; Azure Boards appeared as the updating identity. P00 remained Active.

All 25 source GitHub records received exact Azure destinations. Roadmap #2 and task issues #4–26 were retired as transferred with `state_reason=not_planned`, preserving their original content. GitHub P00 (#3) remains open for the outstanding learner check, matching Azure P00. Azure Boards is now the live tracker. Repository planning, contribution and task templates use verified Azure IDs.

Azure's connection-list display still included seven old repository names after the saved GitHub restriction; its display cleanup remains recorded in [P00 setup evidence](AZURE_BOARDS_SETUP.md). The active app permission scope is one selected repository. The optional sample-story and badge-PR wizard was skipped.

All 12 existing unit tests, the offline demo, documentation-link checks and diff checks passed after the handover documentation changes. PR #1 stays draft and unmerged for L01. No learner demonstration, live AI/MCP integration, Azure deployment or paid resource is claimed complete.

## Reproduce local checks

```bash
python -m unittest discover -s tests -v
python -m lab demo
python scripts/review.py --list
python scripts/cost_estimator.py
python scripts/check_docs.py
python scripts/doctor.py
```

Run `python scripts/prepare_full_project.py` only to create a new local teaching copy. It does not execute the original app. A prepared copy is not the same as a fully running integration.

## What the tests establish

The tests check the companion's deterministic behaviour with synthetic records. They do not measure an LLM's accuracy, an embedding model's retrieval quality or production security. The original project's identified limitations remain documented even after convenience patches are applied.

## Evidence to add after your first live run

Record operating system, Python version, dependency lock, SQL container digest, ODBC version, model/deployment, index dimension, date, test cases and outcomes. Never record API keys or passwords. Link a reviewed commit or sanitised test report when useful.
