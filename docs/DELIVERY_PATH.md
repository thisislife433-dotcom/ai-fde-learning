# Learn AI agents, MCP and delivery from feature to production

**Added 15 October 2026.** This extends the original [12 application lessons](STUDY_GUIDE.md). We will use this same cold-chain project to learn how a team develops, tests, releases and operates an AI application.

The intended outcome is that you can trace one requirement through an issue, branch, commit, PR, test run, container image, dev deployment, production promotion and rollback. You should also be able to explain exactly which part the AI agent performed.

## What exists and what we will build

| Available foundation | Future practical work |
|---|---|
| Offline Python lab, synthetic records, tests and revision material | HTTP service, container image and service smoke tests |
| Pinned upstream SQL/Pinecone/LangGraph/Streamlit implementation | Verified integration using your configured provider accounts |
| CI for offline tests, demo and documentation links | Container build, MCP contract checks, AI evaluations and deployment jobs |
| Contribution guide, PR/issue templates and branch workflow | Enforced branch rules, GitHub deployment environments and Azure identities |
| A reproducible routing defect for the bug-fix exercise | Regression test and fix delivered through their own PR |

The companion does not currently expose an MCP server or run a model-controlled agent. The upstream Python tool functions are not automatically MCP tools. No Azure dev or production environment is created by this documentation change. A branch called `develop` is a code reference, not a running dev environment.

## Model, agent, tool and MCP

| Term | Meaning in this project |
|---|---|
| Model | Generates responses and can request tool calls from the supplied context |
| Agent | The application loop that gives the model instructions and tools, executes permitted calls and returns their results |
| Tool | A function such as retrieving shipment details or searching policy |
| MCP | Model Context Protocol: a standard way for a client and server to exchange tool definitions, calls and context |
| MCP server | Exposes capabilities; it can wrap our existing business functions |
| MCP client/host | The client connection sits inside the application that uses those capabilities |

MCP can expose tools, resources and prompts. We will begin with local stdio, then study authenticated Streamable HTTP for remote access. Use a compatible official SDK and record the actual client, server and protocol versions; validate tool discovery and calls without a model first. The [protocol architecture](https://modelcontextprotocol.io/docs/learn/architecture) is the reference for these concepts.

We will use agents in two distinct jobs:

| Agent | Example task | Tools and authority |
|---|---|---|
| Shipment assistant | Explain why a delivery needs review | Read shipment facts and policy; return dated evidence and recommendations |
| Development assistant | Implement a feature, inspect a failing check, prepare a PR | Read/edit the checkout, run tests and use authorized repository tools |

Git itself and GitHub Actions work without MCP. A coding agent can run the local Git CLI or use a connected GitHub tool. MCP supplies a connection interface; repository permissions and deployment rules still control what happens. Our runtime shipment assistant should not inherit the development assistant's release permissions.

## The ten practical units

Complete the [first offline run](START_HERE.md) before D1. The order below is a teaching sequence; later units depend on earlier implementations and the original application lessons. Each unit has its own small branch and PR.

| Unit | What you will do | Evidence of completion |
|---|---|---|
| D1. Git and review | Inspect our first learning-path PR; create your own small feature branch from develop, commit, push, review and merge | You explain working tree, staging, commit, remote, PR base/head and merge result |
| D2. A real feature | Add a small shipment-status HTTP service on `feature/shipment-status-api` | Success, unknown ID and bad-input cases tested; merged PR linked |
| D3. MCP | Connect a read-only documentation MCP; implement our shipment MCP adapter on `feature/shipment-mcp` | Tool discovery and successful/invalid calls through a real client recorded |
| D4. Agent integration | Let a model select the read-only tools; retain deterministic mode for comparison | Tool trace, citations, stale-data answer, missing-data answer and cost recorded |
| D5. Bug fix | Reproduce the singular/plural routing defect on `bugfix/singular-truck-routing` | A regression test fails on the parent commit and passes with the fix |
| D6. Container and CI | Add a Dockerfile, dependency lock and build checks on `feature/container-ci` | Tested image digest, source commit and CI run recorded |
| D7. Azure dev | Add Bicep infrastructure and a dev deployment workflow on `feature/azure-dev` | IaC review, OIDC login, deployment, health checks and functional checks observed |
| D8. Production promotion | Promote the dev-tested image to a separate learning production environment | Release PR, approval, matching digest, configuration and smoke results recorded |
| D9. Operations | Roll back to a known good artifact; practise a scoped hotfix and sync it into develop | Recovery check and synchronization PR linked; no fixes lost |
| D10. Independent release | Repeat a small requirement-to-production change with reduced assistance | You explain the complete chain and its failure/recovery decisions |

The separate learning production environment uses synthetic data. Serving real business users would require additional operational, access and data reviews; its name alone does not establish production readiness.

## D1: start with the workflow we can inspect now

Open the learning-path PR in GitHub. Identify the base branch `develop` and head branch `feature/agent-delivery-learning-track`. Look at **Files changed** and **Checks**. Explain why the main branch has not changed merely because a PR exists.

Then follow [Contributing](../CONTRIBUTING.md) for your own small change. A useful first change is adding your five-line business brief. Keep the PR small enough that you can explain every changed line. We will inspect it together before you perform the merge. The learning checkpoint remains incomplete until you have done and understood these steps.

## D2: the feature specification

Add a service around the existing assessment functions; do not duplicate their business rules. The initial contract will include `GET /health` and `GET /shipments/{id}/assessment`.

- A known synthetic ID returns its assessment, observation timestamp, policy version, `as_of` time and explicit synthetic-data label.
- An unknown ID returns a documented 404 response; malformed inputs return a documented client error.
- The fixture clock remains explicit so the offline examples are reproducible. A future live mode must use real dated readings and an appropriate current clock.
- The initial service is read-only. Parameterized queries and input validation remain in the implementation.

The checked-in lab policy is **0-4 C**, with its own freshness rule in `lab/data/policies.json`. Earlier spoken examples used illustrative limits; automated checks must use the actual fixture policy. These are exercise rules, not universal food or medicine guidance.

## D3: first use MCP, then build our own

For a machine with the Codex CLI already installed, the official OpenAI documentation server offers a small first connection:

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

Ask the coding agent to retrieve and cite the documentation for MCP tool configuration. Inspect the tool result. Registration alone does not prove the server was reached. This server reads documentation; it does not run model API requests for you. These commands are for the CLI/IDE setup, not commands to paste into a ChatGPT message. See [official OpenAI documentation](https://developers.openai.com/learn/docs-mcp).

Next, wrap the existing lab functions in three proposed MCP tools: `get_shipment(shipment_id)`, `search_policy(query)` and `assess_shipment(shipment_id)`. Return structured results and source labels. Test discovery, invalid IDs, bad argument types, missing data and unavailable dependencies. Choose the SDK/version during implementation and lock it after exercising a real client/server exchange.

For remote deployment, add authentication and authorization, bounded requests, timeouts and per-environment configuration. Retrieved policy text is input data, not permission to execute commands. A tool annotation claiming read-only does not enforce read-only access. The adapter and its underlying data permissions must enforce the contract.

## D4: observe the agent instead of guessing what it did

Use one model-controlled loop initially. Give it only the tools needed for the exercise. Capture the question, permitted tool names, arguments, returned evidence and final answer with sensitive values removed. Test stale readings, no matching shipment, no policy match, tool timeout and an instruction embedded in a retrieved document.

The trace should establish what was called. Do not treat a fluent explanation as evidence that a tool actually ran. Set bounded tool steps, timeouts and an API spending budget. Keep offline deterministic tests separate from model evaluations, whose outputs may vary. The existing upstream integration guide remains relevant; the new adapter is not a verified replacement for that full stack yet.

## D5: a real defect to practise on

Reproduced on the current lab on 15 October 2026:

```bash
python -m lab ask "What rules apply to my truck in Melbourne?"
python -m lab ask "What rules apply to my trucks in Melbourne?"
```

The singular form returns `POLICY_ONLY`; the plural form returns `OK` with shipment assessments. The policy-only routing exclusion in `lab/core.py` includes `trucks` but omits `truck`.

Our acceptance criterion is that these equivalent fleet questions both obtain shipment evidence, while a standalone policy question still uses policy lookup. Add a regression test before changing the router, demonstrate the failure, make the smallest fix, then rerun the suite. This foundation PR documents the defect; the fix belongs in the learner's separate D5 PR. The existing 12 tests passing does not cover this missing case.

## D6-D9: delivery decisions we will implement

Our initial target is **GitHub Actions + Docker + Azure Container Apps**, using Bicep for infrastructure. This builds on the existing GitHub repo and your Azure experience. An ADO translation can be a later exercise once the same lifecycle works here.

Create an HTTP service before attempting a long-running Container App deployment; the existing CLI demo alone is not a hosted web application. First deploy the deterministic service with synthetic data. Enable the full agent only after its data services, credentials, durable state and evaluations work. A container's writable filesystem or the current local JSONL trace is not durable shared production storage.

Use separate dev/prod applications, identities, configuration and data. An image registry holds the built artifact; an environment selects its configuration. Store runtime secrets through the chosen secret store/managed identity arrangement. Keep deployment identities separate from runtime identities. Add bounded log retention and observability for errors, latency, tool failures and model usage.

The [branching and release guide](BRANCHING_AND_RELEASES.md) defines promotion by the dev-tested image digest, the release checks and rollback. Azure supports deployment of an existing container image, so the release job can promote an artifact without building it again. Its deployment guide includes older secret-based login examples; our authentication design uses the separate [GitHub-to-Azure OIDC guidance](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure).

Local offline exercises incur no API/cloud fees. Model calls, container registry, logs, databases and hosted environments can incur charges. Before the first cloud exercise, choose the subscription, region, resource names, access boundary, cost estimate and cleanup plan. A budget alert is not a guaranteed spending cap. No paid resource is needed to start D1-D3's protocol-only practice; coding-agent subscription usage remains separate.

## Record the result

Use [the tracker](../progress/LEARNING_TRACKER.md). For a release, record:

- Requirement or defect, branch, PR and source commit.
- Test/evaluation evidence and container digest.
- Dev deployment and smoke checks; release approval and production smoke checks.
- Previous working digest, configuration version, rollback result and what you learned.

## Primary references checked for this extension

- [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture): protocol roles, transports and server capabilities.
- [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp): read-only documentation connection for the coding-agent exercise.
- [GitHub deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments): reviewers, branch restrictions and environment settings.
- [GitHub OIDC with Azure](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure): federation and scoped token permissions.
- [Azure Container Apps with GitHub Actions](https://learn.microsoft.com/en-us/azure/container-apps/github-actions): publishing revisions and deploying an existing image.
