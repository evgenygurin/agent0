# Overview - Mem0
Source: https://docs.mem0.ai/open-source/overview
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​Mem0 Open Source Overview
[​](https://docs.mem0.ai/open-source/overview#mem0-open-source-overview)[release notes](https://docs.mem0.ai/changelog)
## ​What Mem0 OSS provides
[​](https://docs.mem0.ai/open-source/overview#what-mem0-oss-provides)- Full control: Tune every component, from LLMs to vector stores, inside your environment.
- Offline ready: Keep memory on your own network when compliance or privacy demands it.
- Extendable codebase: Fork the repo, add providers, and ship custom automations.
[Python quickstart](https://docs.mem0.ai/open-source/python-quickstart)
## ​Choose your path
[​](https://docs.mem0.ai/open-source/overview#choose-your-path)[Python QuickstartBootstrap CLI and verify add/search loop.](https://docs.mem0.ai/open-source/python-quickstart)
## Python Quickstart
[Node.js QuickstartInstall TypeScript SDK and run starter script.](https://docs.mem0.ai/open-source/node-quickstart)
## Node.js Quickstart
[Configure ComponentsLLM, embedder, vector store, reranker setup.](https://docs.mem0.ai/open-source/configuration)
## Configure Components
[Graph Memory CapabilityRelationship-aware recall with Neo4j, Memgraph.](https://docs.mem0.ai/open-source/features/graph-memory)
## Graph Memory Capability
[Tune Retrieval & RerankersHybrid retrieval and reranker controls.](https://docs.mem0.ai/open-source/features/reranker-search)
## Tune Retrieval & Rerankers
[Deploy with Docker ComposeReference deployment with REST endpoints.](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama)
## Deploy with Docker Compose
[Use the REST APIAsync add/search flows and automation.](https://docs.mem0.ai/open-source/features/rest-api)
## Use the REST API
[Platform vs OSS guide](https://docs.mem0.ai/platform/platform-vs-oss)
What you get with Mem0 OSS

## ​Default components
[​](https://docs.mem0.ai/open-source/overview#default-components)- LLM: OpenAIgpt-4.1-nano-2025-04-14(viaOPENAI_API_KEY)
`gpt-4.1-nano-2025-04-14``OPENAI_API_KEY`- Embeddings: OpenAItext-embedding-3-small
`text-embedding-3-small`- Vector store: Local Qdrant instance storing data at/tmp/qdrant
`/tmp/qdrant`- History store: SQLite database at~/.mem0/history.db
`~/.mem0/history.db`- Reranker: Disabled until you configure a provider
[Memory.from_config](https://docs.mem0.ai/open-source/configuration)`Memory.from_config`
## ​Keep going
[​](https://docs.mem0.ai/open-source/overview#keep-going)[Review Platform vs OSS](https://docs.mem0.ai/platform/platform-vs-oss)
## Review Platform vs OSS
[Run the Python Quickstart](https://docs.mem0.ai/open-source/python-quickstart)
## Run the Python Quickstart
[Platform vs OSS guide](https://docs.mem0.ai/platform/platform-vs-oss)