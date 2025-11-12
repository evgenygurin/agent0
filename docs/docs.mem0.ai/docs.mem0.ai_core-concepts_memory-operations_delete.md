# Delete Memory - Mem0
Source: https://docs.mem0.ai/core-concepts/memory-operations/delete
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​Remove Memories Safely
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#remove-memories-safely)- Satisfies user erasure (GDPR/CCPA) without touching the rest of your data.
- Keeps knowledge bases accurate by removing stale or incorrect facts.
- Works for both the managed Platform API and the OSS SDK.

## ​Key terms
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#key-terms)- memory_id– Unique ID returned byadd/searchidentifying the record to delete.
`add``search`- batch_delete– API call that removes up to 1000 memories in one request.
- delete_all– Filter-based deletion by user, agent, run, or metadata.
- immutable– Flagged memories that cannot be updated; delete + re-add instead.

## ​How the delete flow works
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#how-the-delete-flow-works)
Choose the scope

Submit the delete call
`delete``batch_delete``delete_all`
Verify
`search`
## ​Delete a single memory (Platform)
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#delete-a-single-memory-platform)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

memory_id = "your_memory_id"
client.delete(memory_id=memory_id)

```

## ​Batch delete multiple memories (Platform)
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#batch-delete-multiple-memories-platform)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

delete_memories = [
    {"memory_id": "id1"},
    {"memory_id": "id2"}
]

response = client.batch_delete(delete_memories)
print(response)

```

## ​Delete memories by filter (Platform)
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#delete-memories-by-filter-platform)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

# Delete all memories for a specific user
client.delete_all(user_id="alice")

```
- agent_id
`agent_id`- run_id
`run_id`- metadata(as JSON string)
`metadata``delete_all`
## ​Delete with Mem0 OSS
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#delete-with-mem0-oss)
```
from mem0 import Memory

memory = Memory()

memory.delete(memory_id="mem_123")
memory.delete_all(user_id="alice")

```

## ​Use cases recap
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#use-cases-recap)- Forget a user’s preferences at their request.
- Remove outdated or incorrect facts before they spread.
- Clean up memories after session expiration or retention deadlines.
- Comply with privacy legislation (GDPR, CCPA) and internal policies.

## ​Method comparison
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#method-comparison)`delete(memory_id)``batch_delete([...])``delete_all(...)`
## ​Put it into practice
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#put-it-into-practice)- Review theDelete Memory API reference, plusBatch DeleteandFiltered Delete.
[Delete Memory API reference](https://docs.mem0.ai/api-reference/memory/delete-memory)[Batch Delete](https://docs.mem0.ai/api-reference/memory/batch-delete)[Filtered Delete](https://docs.mem0.ai/api-reference/memory/delete-memories)- Pair deletes withExpiration Policiesto automate retention.
[Expiration Policies](https://docs.mem0.ai/platform/features/expiration-date)
## ​See it live
[​](https://docs.mem0.ai/core-concepts/memory-operations/delete#see-it-live)- Support Inbox with Mem0demonstrates compliance-driven deletes.
[Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox)- Data Management toolingshows how deletes fit into broader lifecycle flows.
[Data Management tooling](https://docs.mem0.ai/platform/features/direct-import)[Review Add Concepts](https://docs.mem0.ai/core-concepts/memory-operations/add)
## Review Add Concepts
[Enable Expiration Policies](https://docs.mem0.ai/platform/features/expiration-date)
## Enable Expiration Policies
