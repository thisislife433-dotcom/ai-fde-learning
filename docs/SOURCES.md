# Sources and review scope

Prepared 24 September 2026 for an independent learning companion.

## Primary project material

- Video: [Complete End To End AI Forward Deployed Engineer (FDE) Project Implementation](https://www.youtube.com/watch?v=FSZhPDzESPU), Krish Naik's channel, about 4:51:00.
- Code: [nimowhyca/cold-chain-logistics-FDE-Project](https://github.com/nimowhyca/cold-chain-logistics-FDE-Project).
- Reviewed commit: [ef6633928950ef9c13115fb77439ccab40397790](https://github.com/nimowhyca/cold-chain-logistics-FDE-Project/commit/ef6633928950ef9c13115fb77439ccab40397790).
- Original data source link from the repo: [Kaggle logistics and supply-chain dataset](https://www.kaggle.com/datasets/datasetengineer/logistics-and-supply-chain-dataset). The checked-in CSV schema and row count were inspected; the original dataset's asserted collection history was not independently verified.

All Python application and preparation files, SQL setup, workflow, requirements, configuration and SOP in that commit were reviewed. The five handwritten note pages were rendered and visually inspected. The TDD and business deck were read through their extracted text; diagrams in those two PDFs were not independently reconstructed or fully verified visually.

The published video chapter outline was located. An auto-generated transcript export was available but ended at approximately **3:27:24** with an explicit truncation marker. Selected passages were examined across the available chapters. Later sections are documented from checked-in code, setup notes, chapter titles and the accompanying design material. **This is not a claim that every spoken minute was watched or transcribed.** No full transcript is redistributed in the companion.

## Provenance

The original project is included as a pinned Git submodule, preserving its repository and authorship. At the reviewed commit no top-level licence file was present. The companion does not assign the upstream work a new licence or claim it as original work. Review applicable permissions before independently redistributing or commercially incorporating original materials.

The offline sample data, fictional policy, teaching implementation, lessons, recall cards and setup helper are new companion material. They are explicitly separated from the original project. The helper makes a local working copy and records its changes; the source submodule is not rewritten.

## Technical and pricing references

| Source | Used for |
|---|---|
| [GPT-4o model page](https://developers.openai.com/api/docs/models/gpt-4o) | Original model pricing |
| [GPT-4.1 mini model page](https://developers.openai.com/api/docs/models/gpt-4.1-mini) | Optional learning-copy model pricing and tool capability |
| [Embedding model page](https://developers.openai.com/api/docs/models/text-embedding-3-small) | Explicit embedding choice reference |
| [Pinecone pricing](https://www.pinecone.io/pricing/) | Free tier and paid plan minimums |
| [GitHub pricing](https://github.com/pricing) | Free repositories and included CI allowance |
| [Open-Meteo pricing](https://open-meteo.com/en/pricing) | Personal non-commercial weather API use |
| [Microsoft SQL container quickstart](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver17) | Supported container host architecture and development setup |
| [Microsoft ODBC driver](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17) | Native driver requirement |
| [AWS public IPv4 pricing](https://aws.amazon.com/vpc/pricing/) | Per-address hourly cost |
| [EC2 stop/start](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html) | Retained disk charges |

Pricing examples use stated usage and FX assumptions. They are not account-specific quotes. Azure service mapping is a proposed architecture extension, not a deployed or verified migration.
