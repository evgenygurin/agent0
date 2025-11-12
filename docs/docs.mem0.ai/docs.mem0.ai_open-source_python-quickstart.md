# Python SDK Quickstart - Mem0
Source: https://docs.mem0.ai/open-source/python-quickstart
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Prerequisites
[​](https://docs.mem0.ai/open-source/python-quickstart#prerequisites)- Python 3.10 or higher
- OpenAI API key (Get one here)
[Get one here](https://platform.openai.com/api-keys)
## ​Installation
[​](https://docs.mem0.ai/open-source/python-quickstart#installation)
Install via pip

```
pip install mem0ai

```

Initialize Memory

```
from mem0 import Memory

m = Memory(api_key="your-openai-api-key")

```

Add a memory

```
messages = [
    {"role": "user", "content": "Hi, I'm Alex. I love basketball and gaming."},
    {"role": "assistant", "content": "Hey Alex! I'll remember your interests."}
]
m.add(messages, user_id="alex")

```

Search memories

```
results = m.search("What do you know about me?", filters={"user_id": "alex"})
print(results)

```

```
{
  "results": [
    {
      "id": "mem_123abc",
      "memory": "Name is Alex. Enjoys basketball and gaming.",
      "user_id": "alex",
      "categories": ["personal_info"],
      "created_at": "2025-10-22T04:40:22.864647-07:00",
      "score": 0.89
    }
  ]
}

```
`Memory()`- OpenAIgpt-4.1-nano-2025-04-14for fact extraction and updates
`gpt-4.1-nano-2025-04-14`- OpenAItext-embedding-3-smallembeddings (1536 dimensions)
`text-embedding-3-small`- Qdrant vector store with on-disk data at/tmp/qdrant
`/tmp/qdrant`- SQLite history at~/.mem0/history.db
`~/.mem0/history.db`- No reranker (add one in the config when you need it)

## ​What’s Next?
[​](https://docs.mem0.ai/open-source/python-quickstart#what%E2%80%99s-next%3F)[Memory OperationsLearn how to search, update, and manage memories with full CRUD operations](https://docs.mem0.ai/open-source/overview)
## Memory Operations
[ConfigurationCustomize Mem0 with different LLMs, vector stores, and embedders for production use](https://docs.mem0.ai/open-source/configuration)
## Configuration
[Advanced FeaturesExplore async support, graph memory, and multi-agent memory organization](https://docs.mem0.ai/open-source/features/async-memory)
## Advanced Features

## ​Additional Resources
[​](https://docs.mem0.ai/open-source/python-quickstart#additional-resources)- OpenAI Compatibility- Use Mem0 with OpenAI-compatible chat completions
[OpenAI Compatibility](https://docs.mem0.ai/open-source/features/openai_compatibility)- Contributing Guide- Learn how to contribute to Mem0
[Contributing Guide](https://docs.mem0.ai/contributing/development)- Examples- See Mem0 in action with Ollama and other integrations
[Examples](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama)