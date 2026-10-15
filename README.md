# AI FDE Learning Lab

A practical study companion for Krish Naik's **Complete End To End AI Forward Deployed Engineer (FDE) Project Implementation**. Learn the architecture, inspect the code, run small exercises, then revisit the material without rewatching five hours.

**Start here: [your first 30 minutes](docs/START_HERE.md).**

```bash
python -m lab demo
python -m unittest discover -s tests -v
python scripts/review.py
```

The first two commands need only Python 3.10 or newer. The offline lab makes **no network or AI API calls** and incurs no cloud/API fees. It is a deterministic teaching model, not the original AI agent. Electricity, hardware and internet are your existing costs.

## What is ready

| Material | Where to go |
|---|---|
| Short lessons with video timestamps, exercises and completion checks | [Study guide](docs/STUDY_GUIDE.md) |
| System diagram, agent loop and Azure mapping | [Architecture](docs/ARCHITECTURE.md) |
| Explanation of the original code, file by file | [Code walkthrough](docs/CODE_WALKTHROUGH.md) |
| Concrete gaps found in the original demo | [Review findings](docs/REVIEW_FINDINGS.md) |
| Setup for Windows, macOS and Linux | [Start here](docs/START_HERE.md) |
| Original SQL + Pinecone + LangGraph + Streamlit setup | [Full-project setup](docs/FULL_PROJECT_SETUP.md) |
| Running costs and a calculator | [Costs](docs/COSTS.md) |
| Quick recall, glossary and questions with answers | [Revision notes](docs/REVISION.md) |
| What to do when something fails | [Troubleshooting](docs/TROUBLESHOOTING.md) |
| What has actually been tested | [Verification](docs/VERIFICATION.md) |
| A place to record progress and resume later | [Learning tracker](progress/LEARNING_TRACKER.md) |
| AI agents, MCP, feature work, bug fixes and dev-to-prod delivery | [End-to-end delivery learning path](docs/DELIVERY_PATH.md) |
| Branches, pull requests, release promotion and rollback | [Branching and releases](docs/BRANCHING_AND_RELEASES.md) |
| Plan each task, define completion criteria and track its evidence | [Project planning workflow](docs/PROJECT_PLANNING.md) |
| Selected planning tool, import file and handover checks | [Azure Boards setup](docs/AZURE_BOARDS_SETUP.md) |
| Ordered issues for all remaining learning and delivery work | [Work backlog](progress/WORK_BACKLOG.md) and [master roadmap](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/2) |

## Develop and release the project

Every new piece of work starts with a work item. **Azure DevOps Boards is our selected planning tool; code and PRs stay in GitHub.** The [setup and import](docs/AZURE_BOARDS_SETUP.md) are prepared; live creation awaits account access and the destination organisation. Until verified transfer, use the existing [master roadmap](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/2) to select one Ready task, link its branch and PR, and record evidence before calling it Done. [P00](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3) tracks the transfer.

The original 12 lessons now have an additional practical delivery track. We will build features on `feature/*`, fix defects on `bugfix/*`, integrate through pull requests into `develop`, and promote tested releases to `main`. The planned cloud target is Azure Container Apps with GitHub Actions. Read [Contributing](CONTRIBUTING.md) before making a change.

The delivery track is a learning plan and repository workflow foundation. The custom MCP server, container service, Azure infrastructure and deployment pipelines are future exercises, not running services. The existing workflow checks the offline lab and documents; it does not deploy anything.

## Original project and attribution

- [Watch the video](https://www.youtube.com/watch?v=FSZhPDzESPU) on Krish Naik's channel.
- [Original project](https://github.com/nimowhyca/cold-chain-logistics-FDE-Project) by the upstream repository's contributors.
- The video credits its implementation mentor; this companion does not claim authorship of their work.
- `upstream/cold-chain` is a Git submodule fixed at **ef6633928950ef9c13115fb77439ccab40397790**.
- [Source register and review scope](docs/SOURCES.md) records what was inspected and the limits of that inspection.

To include the original code when cloning, use `git clone --recurse-submodules https://github.com/thisislife433-dotcom/ai-fde-learning.git`. If you already cloned, run:

```bash
git submodule update --init --recursive
```

GitHub's ZIP download does not include submodule contents. The original project keeps its own provenance; no new licence is applied to it here. The companion adds original lessons, examples, exercises and local setup helpers.

## Learning outcome

Explain why the system needs SQL, document retrieval and tools; trace a question through the agent; identify missing evidence; run and evaluate a small solution; and describe what an enterprise deployment still needs. Use [the final challenge](docs/STUDY_GUIDE.md#final-challenge) to check that you can do this independently.

**Prepared 24 September 2026.** No paid infrastructure has been provisioned. Live provider access, cloud deployment and the original project's complete integration run remain dependent on your accounts and machine; see the verification record.
