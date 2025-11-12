# Configure the OSS Stack - Mem0
Source: https://docs.mem0.ai/open-source/configuration
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​Configure Mem0 OSS Components
[​](https://docs.mem0.ai/open-source/configuration#configure-mem0-oss-components)- Python 3.10+ withpipavailable
`pip`- Running vector database (e.g., Qdrant, Postgres + pgvector) or access credentials for a managed store
- API keys for your chosen LLM, embedder, and reranker providers
[Python quickstart](https://docs.mem0.ai/open-source/python-quickstart)
## ​Install dependencies
[​](https://docs.mem0.ai/open-source/configuration#install-dependencies)- Python
- Docker Compose

Install Mem0 OSS

```
pip install mem0ai

```

Add provider SDKs (example: Qdrant + OpenAI)

```
pip install qdrant-client openai

```

## ​Define your configuration
[​](https://docs.mem0.ai/open-source/configuration#define-your-configuration)- Python
- config.yaml

Create a configuration dictionary

```
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": 6333},
    },
    "llm": {
        "provider": "openai",
        "config": {"model": "gpt-4.1-mini", "temperature": 0.1},
    },
    "embedder": {
        "provider": "vertexai",
        "config": {"model": "textembedding-gecko@003"},
    },
    "reranker": {
        "provider": "cohere",
        "config": {"model": "rerank-english-v3.0"},
    },
}

memory = Memory.from_config(config)

```

Store secrets as environment variables

```
export QDRANT_API_KEY="..."
export OPENAI_API_KEY="..."
export COHERE_API_KEY="..."

```
`memory.add(["Remember my favorite cafe in Tokyo."], user_id="alex")``memory.search("favorite cafe", user_id="alex")`
## ​Tune component settings
[​](https://docs.mem0.ai/open-source/configuration#tune-component-settings)
Vector store collections
`collection_name`
LLM extraction temperature

Reranker depth
`top_k`
## ​Quick recovery
[​](https://docs.mem0.ai/open-source/configuration#quick-recovery)- Qdrant connection errors → confirm port6333is exposed and API key (if set) matches.
`6333`- Empty search results → verify the embedder model name; a mismatch causes dimension errors.
- Unknown reranker→ update the SDK (pip install --upgrade mem0ai) to load the latest provider registry.
`Unknown reranker``pip install --upgrade mem0ai`[Pick Providers](https://docs.mem0.ai/components/llms/overview)
## Pick Providers
[Deploy with Docker Compose](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama)
## Deploy with Docker Compose
