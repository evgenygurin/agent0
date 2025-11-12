# Add Memory - Mem0
Source: https://docs.mem0.ai/core-concepts/memory-operations/add
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​How Mem0 Adds Memory
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#how-mem0-adds-memory)- Preserves user preferences, goals, and feedback across sessions.
- Powers personalization and decision-making in downstream conversations.
- Keeps context consistent between managed Platform and OSS deployments.

## ​Key terms
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#key-terms)- Messages– The ordered list of user/assistant turns you send toadd.
`add`- Infer– Controls whether Mem0 extracts structured memories (infer=True, default) or stores raw messages.
`infer=True`- Metadata– Optional filters (e.g.,{"category": "movie_recommendations"}) that improve retrieval later.
`{"category": "movie_recommendations"}`- User / Session identifiers–user_id,session_id, orrun_idthat scope the memory for future searches.
`user_id``session_id``run_id`
## ​How does it work?
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#how-does-it-work%3F)- Mem0 Platform– Fully managed API with dashboard, scaling, and graph features.
- Mem0 Open Source– Local SDK that you run in your own environment.

Architecture diagram illustrating the process of adding memories.

Information extraction

Conflict resolution

Storage
`infer=True``infer=False``add`
## ​Add with Mem0 Platform
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#add-with-mem0-platform)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

messages = [
    {"role": "user", "content": "I'm planning a trip to Tokyo next month."},
    {"role": "assistant", "content": "Great! I’ll remember that for future suggestions."}
]

client.add(
    messages=messages,
    user_id="alice",
    
)

```
`memory_id`
## ​Add with Mem0 Open Source
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#add-with-mem0-open-source)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key"

m = Memory()

messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]

# Store inferred memories (default behavior)
result = m.add(messages, user_id="alice", metadata={"category": "movie_recommendations"})

# Optionally store raw messages without inference
result = m.add(messages, user_id="alice", metadata={"category": "movie_recommendations"}, infer=False)

```
`infer=False``infer=False``infer=True`
## ​When Should You Add Memory?
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#when-should-you-add-memory%3F)- A new user preference is shared
- A decision or suggestion is made
- A goal or task is completed
- A new entity is introduced
- A user gives feedback or clarification

### ​More Details
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#more-details)[Add Memory API Reference](https://docs.mem0.ai/api-reference/memory/add-memories)
## ​Managed vs OSS differences
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#managed-vs-oss-differences)`enable_graph=True`
## ​Put it into practice
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#put-it-into-practice)- Review theAdvanced Memory Operationsguide to layer metadata, rerankers, and graph toggles.
[Advanced Memory Operations](https://docs.mem0.ai/platform/advanced-memory-operations)- Explore theAdd Memories API referencefor every request/response field.
[Add Memories API reference](https://docs.mem0.ai/api-reference/memory/add-memories)
## ​See it live
[​](https://docs.mem0.ai/core-concepts/memory-operations/add#see-it-live)- Support Inbox with Mem0shows add + search powering a support flow.
[Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox)- AI Tutor with Mem0uses add to personalize lesson plans.
[AI Tutor with Mem0](https://docs.mem0.ai/cookbooks/companions/ai-tutor)[Explore Search Concepts](https://docs.mem0.ai/core-concepts/memory-operations/search)
## Explore Search Concepts
[Build a Support Agent](https://docs.mem0.ai/cookbooks/operations/support-inbox)
## Build a Support Agent
