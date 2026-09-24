# Running costs

Prepared **24 September 2026**. Provider rates below are in **USD**. AUD examples use an explicit planning assumption of **US$1 = AU$1.55**, not a checked live exchange rate. Tax, card conversion fees and existing equipment/internet costs are excluded. Recheck source pages before paying.

## Recommended progression

| Stage | Cost expectation | What it includes |
|---|---|---|
| Read, revise and run the offline lab | **$0 cloud/API fees** | Python standard library, synthetic data and local revision cards |
| Store the repository on GitHub Free | **$0 within included usage** | Unlimited public/private repositories; Actions has plan allowances |
| Full stack locally, small model, light use | Plan **AU$10-20** for an initial month of practice | A budget allowance, not a provider subscription or guarantee; actual token charges may be lower |
| Cloud lab started only for practice | Compute hours plus retained resources | Region, VM size, number of VMs, disk, IPv4 and APIs determine cost |
| Always-on cloud demo | Illustrative **AU$60-150/month** planning range | A small lab, not a quote or a production budget; validate the chosen topology |

Nothing in this repository creates paid cloud infrastructure automatically. The checked offline lab and preparation helper make no provider API calls. Running the original ingestion, agent or UI can create usage charges after you add credentials.

## Model example you can recalculate

Assume **300 questions/month**, **3 model calls per question**, and on average **2,500 input + 500 output tokens per call**. This means 2.25 million input and 0.45 million output tokens. These are assumed workload figures, not a measurement of the original project. Growing conversation history and retries can raise usage.

| Model | Input per 1M tokens | Output per 1M tokens | Example USD | Example AUD |
|---|---:|---:|---:|---:|
| `gpt-4.1-mini` (learning-copy default) | $0.40 | $1.60 | $1.62 | $2.51 |
| `gpt-4o` (original OpenAI branch) | $2.50 | $10.00 | $10.13 | $15.69 |

Formula: `questions × calls × (input_tokens × input_rate + output_tokens × output_rate) / 1,000,000`.

Sources: [GPT-4.1 mini](https://developers.openai.com/api/docs/models/gpt-4.1-mini), [GPT-4o](https://developers.openai.com/api/docs/models/gpt-4o). Standard, uncached text rates; no batch discount assumed.

```bash
python scripts/cost_estimator.py
python scripts/cost_estimator.py --model gpt-4o
python scripts/cost_estimator.py --questions 1000 --calls 4 --input-tokens 4000
```

The calculator is for scenarios. It does not read your provider bill or enforce a spending limit.

## Other services

| Service | Pricing fact checked | Learning choice |
|---|---|---|
| Pinecone | Starter is free within its limits; Builder is US$20/month; Standard has a US$50 monthly minimum | Use Starter for this tiny personal lab if available; do not upgrade accidentally |
| Embeddings | Charged separately when using a paid embedding API | Explicit model in the learning copy; re-index only when required and monitor usage |
| Open-Meteo | Free endpoint is for non-commercial use with published limits | Personal practice within terms; commercial use needs an appropriate licence/plan |
| Local SQL Server Developer | Intended for development/testing, not production | Local teaching database; read Microsoft's licensing terms |
| GitHub Actions | Included/free usage depends on plan and repository/runners | Short offline tests only; no cloud deployment workflow in this companion |
| AWS public IPv4 | US$0.005/hour per in-use or idle public IPv4 address | About US$3.65 for one address held 730 hours, independent of API cost |

Sources: [Pinecone](https://www.pinecone.io/pricing/), [embedding model](https://developers.openai.com/api/docs/models/text-embedding-3-small), [Open-Meteo](https://open-meteo.com/en/pricing), [GitHub](https://github.com/pricing), [Microsoft SQL container guidance](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver17), [AWS IPv4](https://aws.amazon.com/vpc/pricing/).

## Cloud example, not a vendor quote

To illustrate the arithmetic only, assume one suitably sized app/database lab host costs **US$0.06/hour**, retained disk costs **US$5/month**, and one public IPv4 address is held while running. These are planning inputs; the US$0.06 VM rate and US$5 disk allowance are **not verified prices for a specific SKU or region**. Choose a real supported size/region and replace them. The original design can use separate app/database VMs and cost more.

| Assumed usage | Compute | Disk | IPv4 | Model from example | Approx. total AUD |
|---|---:|---:|---:|---:|---:|
| 40 hours, IP held for 40 hours | $2.40 | $5.00 | $0.20 | $1.62 | $14.29 |
| 730 hours, IP held all month | $43.80 | $5.00 | $3.65 | $1.62 | $83.81 |

Embeddings, egress, logs, taxes, extra networking and paid vector tiers are not included. A retained idle IP still incurs its hourly charge. Stopping a VM does not remove disk charges; [AWS explains retained EBS charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html). Use [AWS Pricing Calculator](https://calculator.aws/) or [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) for the selected cloud design.

## Keep the experiment within budget

Start locally. Use short evaluation conversations, a small model and an explicit maximum graph step count. Check actual provider token usage after ten representative questions and extrapolate. Set provider usage alerts; alerts are not necessarily hard spending caps. Shut down lab compute after practice and check retained disks/IPs separately.

For **this preparation work in ChatGPT**, I cannot inspect your exact plan charges, credit usage or per-task billing. I cannot give an exact cost for this conversation. The running costs above refer to the learning software and external services, not your ChatGPT bill.
