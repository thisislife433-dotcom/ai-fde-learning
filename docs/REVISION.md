# Revision notes

## The two-minute recall

The business needs a defensible decision. **SQL gives recorded facts. Policy retrieval gives written rules. Weather adds dated environmental context. The model combines available evidence; tools execute code under configured permissions.** LangGraph manages the loop and state. Streamlit presents it. Logs record observable activity. Evaluations judge whether the behaviour was acceptable.

Do not confuse a historical row with live telemetry, a similar passage with the correct rule, a plausible answer with verified evidence, or a prompt with an access control.

Before using a recommendation, ask: Which record? Which timestamp? Which policy version? Which missing facts? Which human decides? Those questions matter more than memorising library names.

## Five commands worth remembering

```bash
python -m lab demo
python -m lab ask "What are the temperature rules?"
python -m unittest discover -s tests -v
python scripts/review.py --limit 5
python scripts/cost_estimator.py
```

The review program keeps private due dates locally and increases successful review intervals to 1, 3, 7, 14 and 30 days. A missed card returns to one day. This is a simple revision aid, not a validated mastery score. Run `python scripts/review.py --list` to see all 28 question prompts without changing progress.

## Glossary

| Term | Plain explanation |
|---|---|
| FDE | An engineer who works closely with a customer to turn a real operational need into a working solution |
| LLM | A model that generates language and can propose structured tool requests |
| Token | A unit of model input/output; not necessarily a whole word |
| Embedding | Numbers representing text for similarity comparison |
| Vector database | A store/index supporting vector similarity retrieval |
| RAG | Retrieving source information and supplying it as generation context |
| Chunk | A section of a document indexed for retrieval |
| Metadata | Information about a record or source, such as filename, version or timestamp |
| Tool | An application function the agent is allowed to request |
| Tool schema | The expected arguments and their types |
| Agent state | Information carried between workflow steps, often messages |
| Checkpoint | Saved workflow state used to continue a thread |
| Thread ID | A key distinguishing one conversation/workflow context from another |
| ReAct | An approach that alternates model decisions and tool actions/results |
| SOP | A written standard operating procedure |
| Semantic view | A database view exposing a clearer, constrained data shape |
| Least privilege | Giving an identity only the operations/data it needs |
| Idempotency | Repeating an operation does not create unintended additional effects |
| Reconciliation | Comparing intended/recorded progress with actual system state and repairing discrepancies |
| Guardrail | A specific control limiting behaviour; its actual coverage must be tested |
| Evaluation | A test of output/behaviour against defined acceptance criteria |
| Observability | Evidence such as logs, metrics and traces that helps explain system operation |
| CI/CD | Automated checks and controlled delivery of software changes |
| IaC | Infrastructure defined and managed through code |
| Managed identity | A platform-managed workload identity, reducing the need to distribute passwords |
| Human approval | An explicit recorded decision by an authorised person before an operation proceeds |

## Recall without opening the code

Answer these first; use the matching cards in `study/cards.json` or the command-line reviewer to reveal explanations.

1. When would fixed rules solve this problem better than an agent?
2. What does the original SQL view expose, and what does its name misleadingly suggest?
3. Why can changing an embedding model invalidate an otherwise unchanged index?
4. Where is the true permission boundary for a database tool?
5. What happens after the model returns a tool call?
6. Why did the UI miss the CLI's system prompt?
7. What survives a process restart?
8. What is actually measured by the weather tool, and what is synthetic?
9. Can the source identify an actual truck and its cargo category?
10. What costs persist after shutting down compute?

## Worked answer: an old high reading

`MEL-103` has a 7.0 C reading from the previous day. The fixture clock is 24 September at 10:00 UTC. That establishes a historical measurement; it does not establish the cargo's temperature now. The fictional `DATA-01` rule makes current status unknown and asks for a fresh validated observation. A response that simply announces a current breach has overclaimed its evidence.

## Worked answer: a policy-only question

"What are the temperature rules?" needs policy evidence. It does not inherently need a shipment query or a current-weather call. The offline lab demonstrates explicit routing. In an AI system, evaluate the model's routing and enforce any mandatory evidence/access restrictions in code.

## Monthly rebuild exercise

Without the source open, draw the architecture and write three function contracts. Then recreate the small offline example in a fresh folder using your own names and synthetic data. Compare your result with this companion only after it runs. Record the parts you could explain and the parts you had to look up.

If you can reproduce only the commands, repeat the relevant concept lesson. If you can explain the boundaries and failure cases, move on to the independent Azure challenge in [the study guide](STUDY_GUIDE.md).
