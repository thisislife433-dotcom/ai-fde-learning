# Work backlog

**Updated 16 October 2026.** Azure Boards is selected. This ordered index maps lessons and delivery work to the existing GitHub tasks, which remain the temporary tracker until verified transfer. Replace links with actual Azure IDs after import; the same numbers do not apply. This is not a duplicate status tracker.

- [Master roadmap](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/2)
- [All project issues](https://github.com/thisislife433-dotcom/ai-fde-learning/issues)
- [Planning workflow](../docs/PROJECT_PLANNING.md)
- [Personal learning evidence](LEARNING_TRACKER.md)

[P00](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3) now tracks [Azure Boards setup](../docs/AZURE_BOARDS_SETUP.md). The import is prepared; account access and the destination organisation are still needed. No live Azure board is claimed.

## 0 — Planning

| Task | Work item | Prerequisites | Learning map |
|---|---|---|---|
| [P00 / #3](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3) | Set up Azure Boards and the work-item-first workflow | None | Working agreement |

## 1 — Foundations

| Task | Work item | Prerequisites | Learning map |
|---|---|---|---|
| [L01 / #4](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/4) | Review the first pull request on the phone | None | D1 review introduction |
| [L02 / #5](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/5) | Choose a development environment and run the offline lab | None | Lesson 0 |
| [L03 / #6](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/6) | Write the business brief through your first feature branch and PR | [L01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/4), [L02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/5) | Lesson 1 + D1 |
| [L04 / #7](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/7) | Inspect shipment data and define read-only tool contracts | [L02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/5) | Lessons 2 and 4 |
| [L05 / #8](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/8) | Draw the architecture and explain the business outcome | [L03](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/6), [L04](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/7) | Lesson 3 |
| [L06 / #9](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/9) | Design policy retrieval, versioning and reliable ingestion | [L04](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/7), [L05](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/8) | Lessons 5 and 6 |

## 2 — Features and MCP

| Task | Work item | Prerequisites | Learning map |
|---|---|---|---|
| [B01 / #10](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/10) | Fix singular truck routing with a failing regression test | [L03](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/6), [L04](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/7) | D5, brought forward as the first small bug exercise |
| [F01 / #11](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/11) | Build a read-only shipment-status HTTP service | [B01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/10), [L05](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/8) | D2 |
| [M01 / #12](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/12) | Connect and inspect an existing documentation MCP server | [L02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/5) | D3 first connection |
| [M02 / #13](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/13) | Implement and test the shipment MCP adapter | [F01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/11), [M01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/12) | D3 custom server |

## 3 — AI application

| Task | Work item | Prerequisites | Learning map |
|---|---|---|---|
| [Q01 / #14](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/14) | Define evaluation cases and access boundaries before model integration | [L05](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/8), [L06](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/9) | Lesson 9 preparation |
| [A01 / #15](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/15) | Run and document the original SQL, retrieval and Streamlit integration | [L02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/5), [L06](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/9), [Q01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/14) | Lesson 8 |
| [A02 / #16](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/16) | Connect the model-controlled assistant to the permitted MCP tools | [M02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/13), [A01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/15), [Q01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/14) | Lesson 7 + D4 |
| [Q02 / #17](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/17) | Run live agent evaluations and verify audit evidence | [A02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/16), [Q01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/14) | Lesson 9 + D4 verification |

## 4 — Azure dev

| Task | Work item | Prerequisites | Learning map |
|---|---|---|---|
| [C01 / #18](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/18) | Build and test an immutable container artifact in CI | [F01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/11), [B01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/10) | D6 |
| [I01 / #19](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/19) | Agree Azure design, costs, identities and release controls | [L05](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/8), [C01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/18) | Lesson 10 + D7 preparation |
| [I02 / #20](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/20) | Provision Azure dev with Bicep and deploy through GitHub Actions | [I01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/19), [C01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/18) | D7 |
| [I03 / #21](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/21) | Validate the deployed agent, remote MCP and operational storage | [I02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/20), [Q02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/17), [M02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/13) | D7 operational validation |

## 5 — Release and operations

| Task | Work item | Prerequisites | Learning map |
|---|---|---|---|
| [R01 / #22](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/22) | Promote the dev-tested release to learning production | [I03](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/21) | D8 |
| [O01 / #23](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/23) | Practise rollback and verify recovery | [R01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/22) | D9 rollback |
| [O02 / #24](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/24) | Deliver a hotfix and synchronise main back into develop | [O01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/23) | D9 hotfix |
| [Z01 / #25](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/25) | Complete an independent release and Azure architecture challenge | [O02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/24), [Q02](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/17) | Lesson 11 + D10 + final challenge |
| [O03 / #26](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/26) | Review running costs, retain useful notes and clean up the lab | [Z01](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/25) | Operational handover |

## How to use the index

The initial phone-friendly learning task is **L01**, reviewing PR #1. **L02** chooses a development environment and verifies the first learner-run demo. No practical lesson is marked complete merely because the materials exist.

Dependencies are learning and delivery prerequisites; independent rows need not be executed strictly by issue number. Keep one task active, select the next Ready task together and split large future items into smaller linked tasks before implementation. B01 intentionally brings the documented D5 bug exercise forward as an early coding task.

P1 means the next learning/foundation batch; P2 means scheduled after prerequisites, not optional. No calendar dates or velocity claims are imposed before the learner's available session time is known.

Our baseline completion target is a synthetic-data learning production environment. Azure Boards migration is now selected under P00. Optional voice features, switching CI to Azure Pipelines and real business production use require separate work items and scope decisions.

