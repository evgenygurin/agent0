# Reranker-Enhanced Search - Mem0
Source: https://docs.mem0.ai/open-source/features/reranker-search
Downloaded: 2025-11-12 21:20:19
================================================================================

- Queries are nuanced and require semantic understanding beyond vector distance.
- Large memory collections produce too many near matches to review manually.
- You want consistent scoring across providers by delegating ranking to a dedicated model.
`provider``config``rerank`
## ​Feature anatomy
[​](https://docs.mem0.ai/open-source/features/reranker-search#feature-anatomy)- Initial vector search:Retrieve candidate memories by similarity.
- Reranker pass:A specialized model scores each candidate against the original query.
- Reordered results:Mem0 sorts responses using the reranker’s scores before returning them.
- Optional fallbacks:Toggle reranking per request or disable it entirely if performance or cost becomes a concern.

Supported providers
- Cohere– Multilingual hosted reranker with API-based scoring.
[Cohere](https://docs.mem0.ai/components/rerankers/models/cohere)- Sentence Transformer– Local Hugging Face cross-encoders for GPU or CPU.
[Sentence Transformer](https://docs.mem0.ai/components/rerankers/models/sentence_transformer)- Hugging Face– Bring any hosted or on-prem reranker model ID.
[Hugging Face](https://docs.mem0.ai/components/rerankers/models/huggingface)- LLM Reranker– Use your preferred LLM (OpenAI, etc.) for prompt-driven scoring.
[LLM Reranker](https://docs.mem0.ai/components/rerankers/models/llm_reranker)- Zero Entropy– High-quality neural reranking tuned for retrieval tasks.
[Zero Entropy](https://docs.mem0.ai/components/rerankers/models/zero_entropy)
Provider comparison

## ​Configure it
[​](https://docs.mem0.ai/open-source/features/reranker-search#configure-it)
### ​Basic setup
[​](https://docs.mem0.ai/open-source/features/reranker-search#basic-setup)
```
from mem0 import Memory

config = {
    "reranker": {
        "provider": "cohere",
        "config": {
            "model": "rerank-english-v3.0",
            "api_key": "your-cohere-api-key"
        }
    }
}

m = Memory.from_config(config)

```
`results["results"][0]["score"]``top_k`
### ​Provider-specific options
[​](https://docs.mem0.ai/open-source/features/reranker-search#provider-specific-options)
```
# Cohere reranker
config = {
    "reranker": {
        "provider": "cohere",
        "config": {
            "model": "rerank-english-v3.0",
            "api_key": "your-cohere-api-key",
            "top_k": 10,
            "return_documents": True
        }
    }
}

# Sentence Transformer reranker
config = {
    "reranker": {
        "provider": "sentence_transformer",
        "config": {
            "model": "cross-encoder/ms-marco-MiniLM-L-6-v2",
            "device": "cuda",
            "max_length": 512
        }
    }
}

# Hugging Face reranker
config = {
    "reranker": {
        "provider": "huggingface",
        "config": {
            "model": "BAAI/bge-reranker-base",
            "device": "cuda",
            "batch_size": 32
        }
    }
}

# LLM-based reranker
config = {
    "reranker": {
        "provider": "llm_reranker",
        "config": {
            "llm": {
                "provider": "openai",
                "config": {
                    "model": "gpt-4",
                    "api_key": "your-openai-api-key"
                }
            },
            "top_k": 5
        }
    }
}

```

### ​Full stack example
[​](https://docs.mem0.ai/open-source/features/reranker-search#full-stack-example)
```
config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4",
            "api_key": "your-openai-api-key"
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small",
            "api_key": "your-openai-api-key"
        }
    },
    "reranker": {
        "provider": "cohere",
        "config": {
            "model": "rerank-english-v3.0",
            "api_key": "your-cohere-api-key",
            "top_k": 15,
            "return_documents": True
        }
    }
}

m = Memory.from_config(config)

```

### ​Async support
[​](https://docs.mem0.ai/open-source/features/reranker-search#async-support)
```
from mem0 import AsyncMemory

async_memory = AsyncMemory.from_config(config)

async def search_with_rerank():
    return await async_memory.search(
        "What are my preferences?",
        user_id="alice",
        rerank=True
    )

import asyncio
results = asyncio.run(search_with_rerank())

```

### ​Tune performance and cost
[​](https://docs.mem0.ai/open-source/features/reranker-search#tune-performance-and-cost)
```
# GPU-friendly local reranker configuration
config = {
    "reranker": {
        "provider": "sentence_transformer",
        "config": {
            "model": "cross-encoder/ms-marco-MiniLM-L-6-v2",
            "device": "cuda",
            "batch_size": 32,
            "top_k": 10,
            "max_length": 256
        }
    }
}

# Smart toggle for hosted rerankers
def smart_search(query, user_id, use_rerank=None):
    if use_rerank is None:
        use_rerank = len(query.split()) > 3
    return m.search(query, user_id=user_id, rerank=use_rerank)

```

### ​Handle failures gracefully
[​](https://docs.mem0.ai/open-source/features/reranker-search#handle-failures-gracefully)
```
try:
    results = m.search("test query", user_id="alice", rerank=True)
except Exception as exc:
    print(f"Reranking failed: {exc}")
    results = m.search("test query", user_id="alice", rerank=False)

```

### ​Migrate from v0.x
[​](https://docs.mem0.ai/open-source/features/reranker-search#migrate-from-v0-x)
```
# Before: basic vector search
results = m.search("query", user_id="alice")

# After: same API with reranking enabled via config
config = {
    "reranker": {
        "provider": "sentence_transformer",
        "config": {
            "model": "cross-encoder/ms-marco-MiniLM-L-6-v2"
        }
    }
}

m = Memory.from_config(config)
results = m.search("query", user_id="alice")

```

## ​See it in action
[​](https://docs.mem0.ai/open-source/features/reranker-search#see-it-in-action)
### ​Basic reranked search
[​](https://docs.mem0.ai/open-source/features/reranker-search#basic-reranked-search)
```
results = m.search(
    "What are my food preferences?",
    user_id="alice"
)

for result in results["results"]:
    print(f"Memory: {result['memory']}")
    print(f"Score: {result['score']}")

```

### ​Toggle reranking per request
[​](https://docs.mem0.ai/open-source/features/reranker-search#toggle-reranking-per-request)
```
results_with_rerank = m.search(
    "What movies do I like?",
    user_id="alice",
    rerank=True
)

results_without_rerank = m.search(
    "What movies do I like?",
    user_id="alice",
    rerank=False
)

```

### ​Combine with metadata filters
[​](https://docs.mem0.ai/open-source/features/reranker-search#combine-with-metadata-filters)
```
results = m.search(
    "important work tasks",
    user_id="alice",
    filters={
        "AND": [
            {"category": "work"},
            {"priority": {"gte": 7}}
        ]
    },
    rerank=True,
    limit=20
)

```

### ​Real-world playbooks
[​](https://docs.mem0.ai/open-source/features/reranker-search#real-world-playbooks)
#### ​Customer support
[​](https://docs.mem0.ai/open-source/features/reranker-search#customer-support)
```
config = {
    "reranker": {
        "provider": "cohere",
        "config": {
            "model": "rerank-english-v3.0",
            "api_key": "your-cohere-api-key"
        }
    }
}

m = Memory.from_config(config)

results = m.search(
    "customer having login issues with mobile app",
    agent_id="support_bot",
    filters={"category": "technical_support"},
    rerank=True
)

```

#### ​Content recommendation
[​](https://docs.mem0.ai/open-source/features/reranker-search#content-recommendation)
```
results = m.search(
    "science fiction books with space exploration themes",
    user_id="reader123",
    filters={"content_type": "book_recommendation"},
    rerank=True,
    limit=10
)

for result in results["results"]:
    print(f"Recommendation: {result['memory']}")
    print(f"Relevance: {result['score']:.3f}")

```

#### ​Personal assistant
[​](https://docs.mem0.ai/open-source/features/reranker-search#personal-assistant)
```
results = m.search(
    "What restaurants did I enjoy last month that had good vegetarian options?",
    user_id="foodie_user",
    filters={
        "AND": [
            {"category": "dining"},
            {"rating": {"gte": 4}},
            {"date": {"gte": "2024-01-01"}}
        ]
    },
    rerank=True
)

```
`m.search(...)`
## ​Verify the feature is working
[​](https://docs.mem0.ai/open-source/features/reranker-search#verify-the-feature-is-working)- Inspect result payloads for bothscore(vector) and reranker scores; mismatched fields indicate the reranker didn’t execute.
`score`- Track latency before and after enabling reranking to ensure SLAs hold.
- Review provider logs or dashboards for throttling or quota warnings.
- Run A/B comparisons (rerank on/off) to validate improved relevance before defaulting to reranked responses.

## ​Best practices
[​](https://docs.mem0.ai/open-source/features/reranker-search#best-practices)- Start local:Try Sentence Transformer models to prove value before paying for hosted APIs.
- Monitor latency:Add metrics around reranker duration so you notice regressions quickly.
- Control spend:Usetop_kand selective toggles to cap hosted reranker costs.
`top_k`- Keep a fallback:Always catch reranker failures and continue with vector-only ordering.
- Experiment often:Swap providers or models to find the best fit for your domain and language mix.
[Configure RerankersReview provider fields, defaults, and environment variables before going live.](https://docs.mem0.ai/components/rerankers/config)
## Configure Rerankers
[Build a Custom LLM RerankerExtend scoring with prompt-tuned LLM rerankers for niche workflows.](https://docs.mem0.ai/components/rerankers/models/llm_reranker)
## Build a Custom LLM Reranker
