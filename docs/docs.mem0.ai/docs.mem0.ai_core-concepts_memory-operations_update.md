# Update Memory - Mem0
Source: https://docs.mem0.ai/core-concepts/memory-operations/update
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​Keep Memories Accurate with Update
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#keep-memories-accurate-with-update)- Corrects outdated or incorrect memories immediately.
- Adds new metadata so filters and rerankers stay sharp.
- Works for both one-off edits and large batches (up to 1000 memories).

## ​Key terms
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#key-terms)- memory_id– Unique identifier returned byaddorsearchresults.
`add``search`- text/data– New content that replaces the stored memory value.
- metadata– Optional key-value pairs you update alongside the text.
- batch_update– Platform API that edits multiple memories in a single request.
- immutable– Flagged memories that must be deleted and re-added instead of updated.

## ​How the update flow works
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#how-the-update-flow-works)
Locate the memory
`search``memory_id`
Submit the update
`update``batch_update`
Verify
`search`
## ​Single memory update (Platform)
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#single-memory-update-platform)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

memory_id = "your_memory_id"
client.update(
    memory_id=memory_id,
    text="Updated memory content about the user",
    metadata={"category": "profile-update"}
)

```

## ​Batch update (Platform)
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#batch-update-platform)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

update_memories = [
    {"memory_id": "id1", "text": "Watches football"},
    {"memory_id": "id2", "text": "Likes to travel"}
]

response = client.batch_update(update_memories)
print(response)

```

## ​Update with Mem0 OSS
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#update-with-mem0-oss)
```
from mem0 import Memory

memory = Memory()

memory.update(
    memory_id="mem_123",
    data="Alex now prefers decaf coffee",
)

```
`update`
## ​Tips
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#tips)- Update bothtextandmetadatatogether to keep filters accurate.
`text``metadata`- Batch updates are ideal after large imports or when syncing CRM corrections.
- Immutable memories must be deleted and re-added instead of updated.
- Pair updates with feedback signals (thumbs up/down) to self-heal memories automatically.

## ​Managed vs OSS differences
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#managed-vs-oss-differences)`client.update(memory_id, {...})``memory.update(memory_id, data=...)``client.batch_update`
## ​Put it into practice
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#put-it-into-practice)- Review theUpdate Memory API referencefor request/response details.
[Update Memory API reference](https://docs.mem0.ai/api-reference/memory/update-memory)- Combine updates withFeedback Mechanismto automate corrections.
[Feedback Mechanism](https://docs.mem0.ai/platform/features/feedback-mechanism)
## ​See it live
[​](https://docs.mem0.ai/core-concepts/memory-operations/update#see-it-live)- Support Inbox with Mem0uses updates to refine customer profiles.
[Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox)- AI Tutor with Mem0demonstrates user preference corrections mid-course.
[AI Tutor with Mem0](https://docs.mem0.ai/cookbooks/companions/ai-tutor)[Learn Delete Concepts](https://docs.mem0.ai/core-concepts/memory-operations/delete)
## Learn Delete Concepts
[Automate Corrections](https://docs.mem0.ai/platform/features/feedback-mechanism)
## Automate Corrections
