# Search Memory - Mem0
Source: https://docs.mem0.ai/core-concepts/memory-operations/search
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​How Mem0 Searches Memory
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#how-mem0-searches-memory)- Retrieves the right facts without rebuilding prompts from scratch.
- Supports both managed Platform and OSS so you can test locally and deploy at scale.
- Keeps results relevant with filters, rerankers, and thresholds.

## ​Key terms
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#key-terms)- Query– Natural-language question or statement you pass tosearch.
`search`- Filters– JSON logic (AND/OR, comparison operators) that narrows results by user, categories, dates, etc.
- top_k / threshold– Controls how many memories return and the minimum similarity score.
- Rerank– Optional second pass that boosts precision when a reranker is configured.

## ​Architecture
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#architecture)
Architecture diagram illustrating the memory search process.

Query processing

Vector search

Filtering & reranking

Results delivery

## ​How does it work?
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#how-does-it-work%3F)
```
# Minimal example that shows the concept in action
# Platform API
client.search("What are Alice's hobbies?", filters={"user_id": "alice"})

# OSS
m.search("What are Alice's hobbies?", user_id="alice")

```
`user_id`
## ​When should you use it?
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#when-should-you-use-it%3F)- Context retrieval- When your agent needs past context to generate better responses
- Personalization- To recall user preferences, history, or past interactions
- Fact checking- To verify information against stored memories before responding
- Decision support- When agents need relevant background information to make decisions

## ​Platform vs OSS usage
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#platform-vs-oss-usage)`filters={"user_id": "alice"}``user_id="alice"``AND``OR``rerank=True``threshold``top_k`
## ​Search with Mem0 Platform
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#search-with-mem0-platform)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

query = "What do you know about me?"
filters = {
   "OR": [
      {"user_id": "alice"},
      {"agent_id": {"in": ["travel-assistant", "customer-support"]}}
   ]
}

results = client.search(query, filters=filters)

```

## ​Search with Mem0 Open Source
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#search-with-mem0-open-source)
```
from mem0 import Memory

m = Memory()

# Simple search
related_memories = m.search("Should I drink coffee or tea?", user_id="alice")

# Search with filters
memories = m.search(
    "food preferences",
    user_id="alice",
    filters={"categories": {"contains": "diet"}}
)

```

## ​Filter patterns
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#filter-patterns)
```
# Get memories from a specific agent session
client.search("query", filters={
    "AND": [
        {"user_id": "alice"},
        {"agent_id": "chatbot"},
        {"run_id": "session-123"}
    ]
})

```

```
# Get memories from a specific agent session
m.search("query", user_id="alice", agent_id="chatbot", run_id="session-123")

```

```
# Platform only - date filtering
client.search("recent memories", filters={
    "AND": [
        {"user_id": "alice"},
        {"created_at": {"gte": "2024-07-01"}}
    ]
})

```

```
# Platform only - category filtering
client.search("preferences", filters={
    "AND": [
        {"user_id": "alice"},
        {"categories": {"contains": "food"}}
    ]
})

```

## ​Tips for better search
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#tips-for-better-search)- Use natural language: Mem0 understands intent, so describe what you’re looking for naturally
- Scope with user ID: Always provideuser_idto scope search to relevant memoriesPlatform API: Usefilters={"user_id": "alice"}OSS: Useuser_id="alice"as parameter
`user_id`- Platform API: Usefilters={"user_id": "alice"}
`filters={"user_id": "alice"}`- OSS: Useuser_id="alice"as parameter
`user_id="alice"`- Combine filters: Use AND/OR logic to create precise queries (Platform)
- Consider wildcard filters: Use wildcard filters (e.g.,run_id: "*") for broader matches
`run_id: "*"`- Tune parameters: Adjusttop_kfor result count,thresholdfor relevance cutoff
`top_k``threshold`- Enable reranking: Usererank=True(default) when you have a reranker configured
`rerank=True`
### ​More Details
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#more-details)[Search Memory API Reference](https://docs.mem0.ai/api-reference/memory/search-memories)
## ​Put it into practice
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#put-it-into-practice)- Revisit theAdd Memoryguide to ensure you capture the context you expect to retrieve.
[Add Memory](https://docs.mem0.ai/core-concepts/memory-operations/add)- Configure rerankers and filters inAdvanced Retrievalfor higher precision.
[Advanced Retrieval](https://docs.mem0.ai/platform/features/advanced-retrieval)
## ​See it live
[​](https://docs.mem0.ai/core-concepts/memory-operations/search#see-it-live)- Support Inbox with Mem0demonstrates scoped search with rerankers.
[Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox)- Tavily Search with Mem0shows hybrid search in action.
[Tavily Search with Mem0](https://docs.mem0.ai/cookbooks/integrations/tavily-search)[Search Memory API](https://docs.mem0.ai/api-reference/memory/search-memories)
## Search Memory API
[Support Inbox Cookbook](https://docs.mem0.ai/cookbooks/operations/support-inbox)
## Support Inbox Cookbook
