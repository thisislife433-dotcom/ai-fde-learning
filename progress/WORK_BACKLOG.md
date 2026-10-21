# Work backlog

**Updated 22 October 2026.** This index links the saved Azure work items and preserves their original GitHub issues. The Azure board and prerequisites are verified; GitHub integration and final cutover remain pending. GitHub issues remain the temporary authority until that cutover. This index is not a duplicate status tracker.

- [Azure board](https://dev.azure.com/waseemjaleel0723/aipoc/_boards/board/t/aipoc%20Team/Stories)
- [Verified ID and prerequisite map](../planning/azure-work-item-map.json)

- [Master roadmap](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/2)
- [All project issues](https://github.com/thisislife433-dotcom/ai-fde-learning/issues)
- [Planning workflow](../docs/PROJECT_PLANNING.md)
- [Personal learning evidence](LEARNING_TRACKER.md)

[P00](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3) now tracks [Azure Boards setup](../docs/AZURE_BOARDS_SETUP.md). All 31 items are saved, including 24 task outcomes, with 39 native prerequisite links. The remaining setup is the GitHub app connection, source-issue handover and learner confirmation of the next Ready task.

## 0 — Planning

| Task | Work item | Prerequisites | Learning map | Source issue |
|---|---|---|---|---|
| [P00 / Azure #3](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/3/?view=edit) | Set up Azure Boards and the work-item-first workflow | None | Working agreement | [GitHub #3](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/3) |

## 1 — Foundations

| Task | Work item | Prerequisites | Learning map | Source issue |
|---|---|---|---|---|
| [L01 / Azure #5](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/5/?view=edit) | Review the first pull request on the phone | None | D1 review introduction | [GitHub #4](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/4) |
| [L02 / Azure #6](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/6/?view=edit) | Choose a development environment and run the offline lab | None | Lesson 0 | [GitHub #5](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/5) |
| [L03 / Azure #7](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/7/?view=edit) | Write the business brief through your first feature branch and PR | [L01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/5/?view=edit), [L02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/6/?view=edit) | Lesson 1 + D1 | [GitHub #6](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/6) |
| [L04 / Azure #8](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/8/?view=edit) | Inspect shipment data and define read-only tool contracts | [L02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/6/?view=edit) | Lessons 2 and 4 | [GitHub #7](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/7) |
| [L05 / Azure #9](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/9/?view=edit) | Draw the architecture and explain the business outcome | [L03](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/7/?view=edit), [L04](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/8/?view=edit) | Lesson 3 | [GitHub #8](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/8) |
| [L06 / Azure #10](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/10/?view=edit) | Design policy retrieval, versioning and reliable ingestion | [L04](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/8/?view=edit), [L05](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/9/?view=edit) | Lessons 5 and 6 | [GitHub #9](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/9) |

## 2 — Features and MCP

| Task | Work item | Prerequisites | Learning map | Source issue |
|---|---|---|---|---|
| [B01 / Azure #12](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/12/?view=edit) | Fix singular truck routing with a failing regression test | [L03](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/7/?view=edit), [L04](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/8/?view=edit) | D5, brought forward as the first small bug exercise | [GitHub #10](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/10) |
| [F01 / Azure #13](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/13/?view=edit) | Build a read-only shipment-status HTTP service | [B01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/12/?view=edit), [L05](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/9/?view=edit) | D2 | [GitHub #11](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/11) |
| [M01 / Azure #14](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/14/?view=edit) | Connect and inspect an existing documentation MCP server | [L02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/6/?view=edit) | D3 first connection | [GitHub #12](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/12) |
| [M02 / Azure #15](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/15/?view=edit) | Implement and test the shipment MCP adapter | [F01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/13/?view=edit), [M01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/14/?view=edit) | D3 custom server | [GitHub #13](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/13) |

## 3 — AI application

| Task | Work item | Prerequisites | Learning map | Source issue |
|---|---|---|---|---|
| [Q01 / Azure #17](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/17/?view=edit) | Define evaluation cases and access boundaries before model integration | [L05](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/9/?view=edit), [L06](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/10/?view=edit) | Lesson 9 preparation | [GitHub #14](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/14) |
| [A01 / Azure #18](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/18/?view=edit) | Run and document the original SQL, retrieval and Streamlit integration | [L02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/6/?view=edit), [L06](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/10/?view=edit), [Q01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/17/?view=edit) | Lesson 8 | [GitHub #15](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/15) |
| [A02 / Azure #19](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/19/?view=edit) | Connect the model-controlled assistant to the permitted MCP tools | [M02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/15/?view=edit), [A01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/18/?view=edit), [Q01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/17/?view=edit) | Lesson 7 + D4 | [GitHub #16](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/16) |
| [Q02 / Azure #20](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/20/?view=edit) | Run live agent evaluations and verify audit evidence | [A02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/19/?view=edit), [Q01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/17/?view=edit) | Lesson 9 + D4 verification | [GitHub #17](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/17) |

## 4 — Azure dev

| Task | Work item | Prerequisites | Learning map | Source issue |
|---|---|---|---|---|
| [C01 / Azure #22](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/22/?view=edit) | Build and test an immutable container artifact in CI | [F01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/13/?view=edit), [B01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/12/?view=edit) | D6 | [GitHub #18](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/18) |
| [I01 / Azure #23](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/23/?view=edit) | Agree Azure design, costs, identities and release controls | [L05](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/9/?view=edit), [C01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/22/?view=edit) | Lesson 10 + D7 preparation | [GitHub #19](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/19) |
| [I02 / Azure #24](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/24/?view=edit) | Provision Azure dev with Bicep and deploy through GitHub Actions | [I01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/23/?view=edit), [C01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/22/?view=edit) | D7 | [GitHub #20](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/20) |
| [I03 / Azure #25](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/25/?view=edit) | Validate the deployed agent, remote MCP and operational storage | [I02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/24/?view=edit), [Q02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/20/?view=edit), [M02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/15/?view=edit) | D7 operational validation | [GitHub #21](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/21) |

## 5 — Release and operations

| Task | Work item | Prerequisites | Learning map | Source issue |
|---|---|---|---|---|
| [R01 / Azure #27](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/27/?view=edit) | Promote the dev-tested release to learning production | [I03](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/25/?view=edit) | D8 | [GitHub #22](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/22) |
| [O01 / Azure #28](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/28/?view=edit) | Practise rollback and verify recovery | [R01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/27/?view=edit) | D9 rollback | [GitHub #23](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/23) |
| [O02 / Azure #29](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/29/?view=edit) | Deliver a hotfix and synchronise main back into develop | [O01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/28/?view=edit) | D9 hotfix | [GitHub #24](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/24) |
| [Z01 / Azure #30](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/30/?view=edit) | Complete an independent release and Azure architecture challenge | [O02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/29/?view=edit), [Q02](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/20/?view=edit) | Lesson 11 + D10 + final challenge | [GitHub #25](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/25) |
| [O03 / Azure #31](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/31/?view=edit) | Review running costs, retain useful notes and clean up the lab | [Z01](https://dev.azure.com/waseemjaleel0723/aipoc/_workitems/edit/30/?view=edit) | Operational handover | [GitHub #26](https://github.com/thisislife433-dotcom/ai-fde-learning/issues/26) |

## How to use the index

The initial phone-friendly learning task is **L01**, reviewing PR #1. **L02** chooses a development environment and verifies the first learner-run demo. No practical lesson is marked complete merely because the materials exist.

Dependencies are learning and delivery prerequisites; independent rows need not be executed strictly by issue number. Keep one task active, select the next Ready task together and split large future items into smaller linked tasks before implementation. B01 intentionally brings the documented D5 bug exercise forward as an early coding task.

P1 means the next learning/foundation batch; P2 means scheduled after prerequisites, not optional. No calendar dates or velocity claims are imposed before the learner's available session time is known.

Our baseline completion target is a synthetic-data learning production environment. Azure Boards migration is now selected under P00. Optional voice features, switching CI to Azure Pipelines and real business production use require separate work items and scope decisions.

