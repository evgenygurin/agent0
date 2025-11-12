# Quickstart - Mem0
Source: https://docs.mem0.ai/platform/quickstart
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Prerequisites
[​](https://docs.mem0.ai/platform/quickstart#prerequisites)- Mem0 Platform account (Sign up here)
[Sign up here](https://app.mem0.ai)- API key (Get one from dashboard)
[Get one from dashboard](https://app.mem0.ai/settings/api-keys)- Python 3.10+, Node.js 14+, or cURL

## ​Installation
[​](https://docs.mem0.ai/platform/quickstart#installation)
Install SDK

```
pip install mem0ai

```

Set your API key

```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

```

Add a memory

```
messages = [
    {"role": "user", "content": "I'm a vegetarian and allergic to nuts."},
    {"role": "assistant", "content": "Got it! I'll remember your dietary preferences."}
]
client.add(messages, user_id="user123")

```

Search memories

```
results = client.search("What are my dietary restrictions?", filters={"user_id": "user123"})
print(results)

```

```
{
  "results": [
    {
      "id": "14e1b28a-2014-40ad-ac42-69c9ef42193d",
      "memory": "Allergic to nuts",
      "user_id": "user123",
      "categories": ["health"],
      "created_at": "2025-10-22T04:40:22.864647-07:00",
      "score": 0.30
    }
  ]
}

```

## ​What’s Next?
[​](https://docs.mem0.ai/platform/quickstart#what%E2%80%99s-next%3F)[Memory OperationsLearn how to search, update, and delete memories with complete CRUD operations](https://docs.mem0.ai/core-concepts/memory-operations/add)
## Memory Operations
[Platform FeaturesExplore advanced features like metadata filtering, graph memory, and webhooks](https://docs.mem0.ai/platform/features/platform-overview)
## Platform Features
[API ReferenceSee complete API documentation and integration examples](https://docs.mem0.ai/api-reference/memory/add-memories)
## API Reference

## ​Additional Resources
[​](https://docs.mem0.ai/platform/quickstart#additional-resources)- Platform vs OSS- Understand the differences between Platform and Open Source
[Platform vs OSS](https://docs.mem0.ai/platform/platform-vs-oss)- Troubleshooting- Common issues and solutions
[Troubleshooting](https://docs.mem0.ai/platform/faqs)- Integration Examples- See Mem0 in action
[Integration Examples](https://docs.mem0.ai/cookbooks/companions/quickstart-demo)