# Advanced Memory Operations - Mem0
Source: https://docs.mem0.ai/platform/advanced-memory-operations
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​Make Platform Memory Operations Smarter
[​](https://docs.mem0.ai/platform/advanced-memory-operations#make-platform-memory-operations-smarter)- Platform workspace with API key
- Python 3.10+ and Node.js 18+
- Async memories enabled in your dashboard (Settings → Memory Options)
[Add Memory](https://docs.mem0.ai/core-concepts/memory-operations/add)
## ​Install and authenticate
[​](https://docs.mem0.ai/platform/advanced-memory-operations#install-and-authenticate)- Python
- TypeScript

Install the SDK with async extras

```
pip install "mem0ai[async]"

```

Export your API key

```
export MEM0_API_KEY="sk-platform-..."

```

Create an async client

```
import os
from mem0 import AsyncMemoryClient

memory = AsyncMemoryClient(api_key=os.environ["MEM0_API_KEY"])

```

## ​Add memories with metadata and graph context
[​](https://docs.mem0.ai/platform/advanced-memory-operations#add-memories-with-metadata-and-graph-context)- Python
- TypeScript

Record conversations with metadata

```
conversation = [
    {"role": "user", "content": "I'm Morgan, planning a 3-week trip to Japan in May."},
    {"role": "assistant", "content": "Great! I'll track dietary notes and cities you mention."},
    {"role": "user", "content": "Please remember I avoid shellfish and prefer boutique hotels in Tokyo."},
]

result = await memory.add(
    conversation,
    user_id="traveler-42",
    metadata={"trip": "japan-2025", "preferences": ["boutique", "no-shellfish"]},
    enable_graph=True,
    run_id="planning-call-1",
)

```
`trip=japan-2025`
## ​Retrieve and refine
[​](https://docs.mem0.ai/platform/advanced-memory-operations#retrieve-and-refine)- Python
- TypeScript

Filter by metadata + reranker

```
matches = await memory.search(
    "Any food alerts?",
    user_id="traveler-42",
    filters={"metadata.trip": "japan-2025"},
    rerank=True,
    include_vectors=False,
)

```

Update a memory inline

```
await memory.update(
    memory_id=matches["results"][0]["id"],
    content="Morgan avoids shellfish and prefers boutique hotels in central Tokyo.",
)

```
`enableGraph: false``enable_graph=False`
## ​Clean up
[​](https://docs.mem0.ai/platform/advanced-memory-operations#clean-up)- Python
- TypeScript

Delete scoped memories

```
await memory.delete_all(user_id="traveler-42", run_id="planning-call-1")

```

## ​Quick recovery
[​](https://docs.mem0.ai/platform/advanced-memory-operations#quick-recovery)- Missing required key enableGraph: update the SDK tomem0ai>=0.4.0.
`Missing required key enableGraph``mem0ai>=0.4.0`- Graph backend unavailable: retry withenableGraph=Falseand inspect your graph provider status.
`Graph backend unavailable``enableGraph=False`- Empty results with filters: logfiltersvalues and confirm metadata keys match (case-sensitive).
`filters``trip_id``preferences`[Tune Metadata Filtering](https://docs.mem0.ai/open-source/features/metadata-filtering)
## Tune Metadata Filtering
[Explore Reranker Search](https://docs.mem0.ai/open-source/features/reranker-search)
## Explore Reranker Search
