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

After these documentation/template changes, all 12 existing unit tests, the offline demo, the relative-link check and `git diff --check` passed locally. No application behaviour or upstream source changed. The learner's checklist remains incomplete. Native Projects board setup is still tracked in [P00](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3), because the browser was signed out; no native board or board automation is claimed as configured.

## Azure Boards decision and prepared transfer: 16 October 2026

The user selected Azure DevOps Boards, replacing the earlier GitHub Projects proposal. [Setup instructions](AZURE_BOARDS_SETUP.md) and the [CSV](../planning/azure-boards-import.csv) are prepared in the existing draft PR. Code and CI remain in GitHub.

Local import checks found 31 rows: one Epic, six phase Features, 23 User Stories and one Bug. All 24 source task codes, 123 acceptance-checklist entries, prerequisite hyperlinks and priorities are retained; title-column hierarchy counts are 1/6/4/4/4/5 tasks per phase. The new-item file excludes IDs, State, assignees and organisation-specific paths.

All 12 existing unit tests, the offline demo, relative-link check and diff check passed. These checks do not exercise Azure's importer. Microsoft sign-in was declined; the destination organisation, live project, import validation, native dependency links, board views and GitHub integration remain unverified. Existing GitHub tasks remain the temporary tracker. No Azure resource or paid service was provisioned, and no learner milestone was marked complete.

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
