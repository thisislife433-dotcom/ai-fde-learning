# What the source does, and where to be careful

Review date: **24 September 2026**. Scope: the pinned source commit, all application/preparation code, configuration, dataset schema, bundled TDD, business deck and handwritten notes. This is a practical code review, not a penetration test or production certification.

"Handled" below means the companion's generated **local teaching copy** addresses the named issue. The original submodule remains unchanged. Complete live integration is not verified here.

| Finding and evidence | Consequence | Companion treatment |
|---|---|---|
| **System prompt missing from UI path.** `orchestrator.py` loads it in `__main__`; `ui.py` imports the compiled graph. | Browser and CLI requests can have different instructions. | Helper supplies the prompt in the shared reasoner when missing. Source is unchanged. |
| **Historical data called active.** `VW_ACTIVE_FLEET` has no recency/active filter. | Responses can present historical conditions as current. | Documented. Offline lab explicitly checks age. Full copy still requires a proper data model and freshness design. |
| **Missing operational identifiers.** The CSV has no shipment ID or cargo type, and ingestion drops `eta_variation_hours`. | The system cannot identify an actual truck or reliably apply cargo-specific/ETA actions from those fields alone. | Documented; independent synthetic lab supplies explicit IDs and ETA for its own fictional cases. |
| **Current weather paired with historical observations.** Weather tool requests today's conditions. | A causal explanation of an old temperature event can be unsupported. | Documented. Weather is not connected in the offline lab. Add timestamp-aligned data before claiming real-time analysis. |
| **Synthetic congestion value.** Weather tool uses wind greater than ten to choose 8.5 or 2.5. | A made-up score looks like measured traffic evidence. | Learning copy labels it a synthetic weather heuristic. It is still not traffic telemetry. |
| **Unsafe SQL trust assumption.** A SELECT-prefix test accepts SQL strings; query results are truncated to ten fetched rows. | Prefix checking is not full query validation, and incomplete results can look exhaustive. | Documented. Offline lab uses fixed parameterised SQL. Live source needs approved query contracts, engine limits and tested permissions. |
| **Non-transactional vector replacement.** Old document vectors are deleted before all new chunks are uploaded. | Failed processing can remove usable policy context. | Documented as an exercise in versioned writes/reconciliation. Not fully repaired by the helper. |
| **Shared hash cache.** One cache covers different indexes/models and is committed upstream. | A clean learner account may skip ingestion into an empty index. | Helper excludes the inherited cache and uses an index/dimension-specific cache in a fresh working copy. Model/config changes and manual index recreation still require explicit reindexing. |
| **Destructive dimension repair.** Ingestion deletes an existing mismatched Pinecone index. | Data can be lost merely by changing settings. | Helper changes this to a clear failure, preserving the existing index. |
| **Auditing is not independently immutable.** Agent can INSERT, administrators retain SQL control; failures are swallowed. | Logging may be missing and privileged changes remain possible. | Documented. Offline JSONL makes the same limitation explicit. Separate identity, retention controls, failure policy and tamper evidence are future work. |
| **Raw user request not explicitly logged as its own UI event.** Traces cover generated tool parameters, results and model text. | A complete user-to-response audit record is not guaranteed. | Documented. Offline trace includes the question, but is still only local teaching data. |
| **Demo access and connection settings.** Chat lacks SSO; admin panel uses DB credentials; SQL connection disables encryption. | This is unsuitable for public exposure or real sensitive data as supplied. | Local SQL binds to 127.0.0.1. Full-copy UI should also bind locally. Enterprise identity/TLS design remains work. |
| **Hard-coded sample passwords.** SQL setup and instructions contain example credentials. | Reusing published examples is unsafe. | Helper generates unique local credentials in ignored files; never commits them. |
| **Volatile graph memory.** `MemorySaver` is process-local. | Sessions do not survive restarts or transparently scale across app instances. | Documented. Durable state and retention policy are later design choices. |
| **Prompt requests all three tools for every case.** Setup examples include a policy-only case. | Extra calls, latency/cost and unnecessary data retrieval. | Documented. Offline lab shows explicit policy-only routing. Live prompt/routing needs evaluation. |
| **Deployment workflow assumes an existing VM.** It pulls main and restarts a service. | No automated provisioning, dependency update, health gate or rollback is supplied. | Companion includes offline CI only. Cloud runbook and Azure mapping explain the missing work. |

## Design document versus code

The TDD mentions shipment identifiers and cargo type that the actual view does not expose. It also describes stateless tiers, immutable auditing and IaC more strongly than the checked-in implementation supports. The source's app imports and memory are process-local; the deployment file does not provision infrastructure. Treat the TDD as intended design and inspect the implementation before repeating its claims.

## What to fix first for a real pilot

1. Establish real keys, cargo categories, trusted timestamps and the operational rules with the business owner.
2. Restrict tools to approved data access and explicitly require adequate evidence before recommendations.
3. Add user authentication, separate service identities, network boundaries and encrypted connections.
4. Create evaluation cases with expected answers and failure behaviours; measure the actual model and retrieval pipeline.
5. Design logging, durable state, ingestion recovery and deployment rollback.

The helper's convenience fixes do not complete this list. Use synthetic data while learning.
