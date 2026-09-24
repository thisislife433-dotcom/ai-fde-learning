# Guided study and build plan

Use one lesson at a time. Each lesson has a concept, a concrete task and evidence that you understood it. Reading alone does not complete a lesson. The video is about 4 hours 51 minutes; allow **roughly 20-35 hours** for this route if you have basic Python, more if Python is new. This is a planning estimate, not a promise.

Suggested rhythm: 30-45 minutes on weekdays, with a longer practical session when convenient. Review the previous lesson for five minutes, do one new task, then record a checkpoint.

## Video map

These are the published chapter boundaries; the lessons below regroup them for learning.

| Chapter | Starts | Focus |
|---|---|---|
| Main introduction | [00:00](https://www.youtube.com/watch?v=FSZhPDzESPU&t=0s) | Overall project |
| Introduction | [05:18](https://www.youtube.com/watch?v=FSZhPDzESPU&t=318s) | Learning context |
| Prerequisites | [06:32](https://www.youtube.com/watch?v=FSZhPDzESPU&t=392s) | Python, SQL and AI concepts assumed |
| Problem | [10:13](https://www.youtube.com/watch?v=FSZhPDzESPU&t=613s) | Discover the customer need |
| Data | [19:26](https://www.youtube.com/watch?v=FSZhPDzESPU&t=1166s) | Inspect and stage the legacy data |
| Solution | [1:11:12](https://www.youtube.com/watch?v=FSZhPDzESPU&t=4272s) | Choose capabilities |
| Architecture | [1:45:32](https://www.youtube.com/watch?v=FSZhPDzESPU&t=6332s) | Describe the technical design |
| Business pitch | [2:06:50](https://www.youtube.com/watch?v=FSZhPDzESPU&t=7610s) | Explain business value |
| SOP ingestion | [2:15:14](https://www.youtube.com/watch?v=FSZhPDzESPU&t=8114s) | Parse, chunk, embed and index |
| Permissions | [2:59:41](https://www.youtube.com/watch?v=FSZhPDzESPU&t=10781s) | Limit database access |
| Tools | [3:08:46](https://www.youtube.com/watch?v=FSZhPDzESPU&t=11326s) | SQL, weather and policy tools |
| Agent | [3:24:10](https://www.youtube.com/watch?v=FSZhPDzESPU&t=12250s) | Model and tool loop |
| UI and audit | [3:47:49](https://www.youtube.com/watch?v=FSZhPDzESPU&t=13669s) | Stream results and record traces |
| Deployment | [4:17:28](https://www.youtube.com/watch?v=FSZhPDzESPU&t=15448s) | GitHub Actions and EC2 |

## Lesson 0 - Bridge the prerequisites

Watch 06:32-10:13. The instructor explicitly treats this as an applied project, not a first introduction to Python, LLMs or vector databases. Use this companion to fill those gaps before combining everything.

Learn these Python ideas first: dictionaries hold named fields; lists hold records; functions take inputs and return values; exceptions represent failures; imports reuse code; environment variables provide configuration. A virtual environment isolates installed libraries for one project. An API call is a program request to another service.

Open `lab/core.py`. Trace how `query_shipments` returns a list of dictionaries, then how `assess` converts one dictionary into a result. Do not try to memorise every import.

**Task:** Run the offline demo. Open `lab/data/shipments.json`, identify the stale record, and explain why the output is unknown. Change a synthetic record's temperature, run `python -m lab seed`, then run the question again. Restore the file when finished.

**Done when:** You can change a value, run the program, predict the effect and explain a function's input and output. If not, spend two or three sessions on these Python basics before Lesson 3.

## Lesson 1 - Define the business problem

Watch 10:13-19:26. A request such as "chat with our data" is underspecified. You need the operational decision, the information required for it and a way to measure success.

Example discovery: a dispatcher spends time finding the latest cargo reading and the applicable response procedure. Ask which shipment identifiers exist, how fresh readings are, who can see them, who approves actions, which systems supply facts and how the current process performs.

**Task:** Write a five-line brief: user, decision, inputs, output and success measure. Add five discovery questions. Use a hypothetical measure such as time to produce an evidence-backed recommendation; label any target as a proposed target until measured.

**Done when:** You can explain why a threshold alert alone might solve a narrow problem, while an assistant may help users combine evidence or ask varied questions. Do not choose an agent merely because the video uses one.

## Lesson 2 - Understand the data before designing the answer

Watch 19:26-1:11:12. Read the first two sections of [the code walkthrough](CODE_WALKTHROUGH.md).

There are two datasets in your checkout: the original large CSV and five synthetic companion records. They serve different purposes. The original ingester keeps only selected fields and gives them legacy column names. The SQL view maps those to readable names again.

**Task:** List which original fields can support location, temperature and risk questions. Then identify the missing evidence needed for "Which truck should go to which cold store?" The source does not supply a truck ID, cargo type or cold-store inventory, and its selected view omits ETA duration.

Run `python -m lab sql` and compare with the original view definition. Explain why the companion adds explicit record IDs and observation timestamps for its exercises.

**Done when:** You can distinguish missing data from an LLM limitation. Explain why historical data plus today's weather is not a validated live incident assessment.

## Lesson 3 - Design the simplest useful system

Watch 1:11:12-2:15:14. Read [Architecture](ARCHITECTURE.md) and the original design and business PDFs in the submodule.

A high-level design explains components and boundaries. A low-level design explains schemas, contracts, state and failure handling. A business pitch explains outcomes and evidence. These are different views of the same solution.

**Task:** Draw the dispatcher, interface, model, SQL tool, weather tool, policy tool and audit store. Mark which connections cross a network and which are ordinary in-process Python calls. Then give a 60-second business explanation without naming libraries.

**Done when:** You can trace one request through the drawing and name the source of each fact. Identify one claim in the TDD that is not implemented in code; the review findings provide examples after you try.

## Lesson 4 - Give tools narrow, testable contracts

Watch 3:08:46-3:24:10 after inspecting `src/agent_tools.py`. Learn tools before the agent that chooses them.

A tool's description helps the model choose it. Its schema tells the model how to call it. Its implementation and permissions decide what happens. For a weather tool, coordinates are inputs and dated conditions are evidence. For a shipment tool, a shipment ID or approved filter is often easier to constrain than arbitrary SQL.

**Task:** Compare `query_shipments(location)` in the companion with the original `query_telemetry_db(sql_query)`. Write the benefits and costs of each. Run the test that treats SQL-looking text as a parameter value:

```bash
python -m unittest discover -s tests -p test_lab.py -v
```

**Done when:** You can explain why a prompt saying "only read" cannot replace a database permission. Also explain why the offline router's refusal words are only a teaching convenience, not a robust security design.

## Lesson 5 - Understand RAG and ingestion

Watch 2:15:14-2:59:41. Read `scripts/ingest_sop_pinecone.py` from the submodule.

The pipeline extracts text, splits it into chunks, embeds those chunks, stores vectors with source metadata, and retrieves relevant passages for a question. Retrieval is a search step. The model still needs to interpret the returned evidence correctly.

**Task:** Open the upstream SOP. Mark where you would split sections, then identify the metadata required for a defensible citation: document ID, version, effective date, section/page and source. Compare your chunk choices with the source's 600-character splitting.

Run `python -m lab ask "What are the temperature rules?"`. This uses keyword search, not embeddings. Explain a question that synonyms would make difficult for this search and how semantic retrieval might help. Also describe a case in which semantic similarity returns the wrong policy.

**Done when:** You can explain why changing documents does not require retraining the model, and why changing the embedding model may require a new index or re-embedding.

## Lesson 6 - Learn reliable ingestion

Revisit the latter part of the SOP chapter. The hash cache resembles a processed-record log, but local files and a remote vector store do not share one atomic transaction.

**Task:** Draw what happens if old vectors are deleted and uploading replacements fails. Then propose versioned writes: upload a new version, verify its chunk count, make that version active, and only later clean up the old one. Record enough state to retry safely and reconcile local progress with the remote store.

Inspect the shared cache problem in [Review findings](REVIEW_FINDINGS.md). Explain why a hash of document bytes alone does not identify the embedding model, chunking version or target index.

**Done when:** You can explain idempotency, reconciliation and the limits of transaction boundaries in this example. A retry should not silently duplicate data or label an incomplete index as complete.

## Lesson 7 - Connect the model and the agent loop

Watch 3:24:10-3:47:49. Read `src/orchestrator.py` and the source prompt.

The graph accumulates messages. The model can return tool calls; the framework executes tools and gives their results back. The model can then answer or request more information. The loop needs a stopping condition and bounded work.

**Task:** Trace an invented turn on paper: user question, first tool request, tool result, second request, second result and final answer. Mark what is model output versus code execution. Count model calls and explain how each contributes to latency and cost.

Find the system-prompt initialisation problem: the CLI's main block runs only when that module is directly executed. The Streamlit app imports it. Review how `prepare_full_project.py` moves prompt supply to the shared reasoning boundary.

**Done when:** You can explain state, messages, thread IDs, tools and memory without treating the LLM as a program with unlimited authority. You know that zero temperature does not prove correctness.

## Lesson 8 - Build the full local integration

Follow [Full-project setup](FULL_PROJECT_SETUP.md) in order. Use an isolated local teaching database and your own provider accounts. Start with the configured small paid model if you choose to use the API; the offline lessons remain available without it.

**Task:** Prepare the local copy, configure secrets privately, start SQL, ingest data, create permissions, index the SOP, test the three tools individually, then launch Streamlit. Record each working checkpoint. If a tool fails alone, resolve that first before testing the agent.

Test one question about policy and one about recorded telemetry. Compare source timestamps with the output. Ask the assistant to distinguish facts, assumptions and missing evidence.

**Done when:** You can explain an actual tool trace and reproduce it. A green UI is not sufficient: you must know which data and policy were retrieved. Record provider/model versions and a dependency lock once the integration passes on your machine.

## Lesson 9 - Permissions, logging and evaluation

Watch 2:59:41-3:08:46 and 3:47:49-4:17:28. Read [Review findings](REVIEW_FINDINGS.md).

Logs explain what happened; evaluations judge whether it was acceptable. Database identity, UI authentication and audit retention solve different problems. A local append-only program or SQL INSERT grant is not proof that nobody can alter history.

**Task:** Build ten evaluation cases before changing prompts. Include exact threshold, below-zero reading, old timestamp, unknown shipment, missing policy, weather timeout, requested data mutation, malformed SQL, conflicting rules and ordinary policy-only query. Write the acceptable behaviour for each, including refusal or uncertainty where appropriate.

**Done when:** You can separate an answer that sounds useful from an answer supported by the correct record and rule. Do not mark live AI cases passed based on the deterministic offline tests.

## Lesson 10 - Deploy with an operational plan

Watch 4:17:28 onward and inspect the deployment workflow. The upstream action expects an existing EC2 setup. It does not provision infrastructure or validate the release.

**Task:** Write a release checklist: tested commit, dependency lock, secrets, SQL network boundary, authenticated HTTPS access, health check, known-good rollback, logs and budget alert. Describe what happens if the service restarts or two app instances serve different requests. Map the components to Azure using [Architecture](ARCHITECTURE.md).

For now, run only the companion checks. Deploy after you can operate the local stack and have selected a budget and cloud design. No cloud resources are required to complete the architecture exercise.

**Done when:** You can distinguish application deployment from infrastructure provisioning, explain the limits of process memory, and name the resources that continue charging after compute stops.

## Lesson 11 - Rebuild and revise

Close the walkthrough. Recreate the component diagram, name the three tools, explain retrieval, and describe one ingestion failure and its recovery. Run `python scripts/review.py --limit 10`. Use [Revision](REVISION.md) only after answering.

**Task:** Make a small independent change to the companion: add a new fictional policy and one sample record, then write a test of the new expected behaviour. Do not merely copy an existing test with a renamed variable.

**Done when:** You can predict the effect of the change, explain its limits and show a passing test. Update your tracker with what you can now do without help.

## Final challenge

Adapt the architecture to an Azure operational-support assistant: ask about failed jobs, read a status table, retrieve the approved runbook, suggest a diagnostic step and keep an audit trail. Begin with read-only diagnostics. A remediation action should be a separate authorised operation with an explicit approval record.

Deliver your own one-page problem statement, component diagram, three tool contracts, five failure cases, estimated cost and explanation of identity boundaries. Reuse the ideas, not the logistics vocabulary.

Pass when you can defend the choices and demonstrate at least one test for missing or stale evidence. This is a project learning milestone, not a claim of job readiness or certification.
