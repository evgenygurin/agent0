# Memory Types - Mem0
Source: https://docs.mem0.ai/core-concepts/memory-types
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​How Mem0 Organizes Memory
[​](https://docs.mem0.ai/core-concepts/memory-types#how-mem0-organizes-memory)- Keeps conversations coherent without repeating instructions.
- Lets agents personalize responses based on long-term preferences.
- Avoids over-fetching data by scoping memory to the correct layer.

## ​Key terms
[​](https://docs.mem0.ai/core-concepts/memory-types#key-terms)- Conversation memory– In-flight messages inside a single turn (what was just said).
- Session memory– Short-lived facts that apply for the current task or channel.
- User memory– Long-lived knowledge tied to a person, account, or workspace.
- Organizational memory– Shared context available to multiple agents or teams.

## ​Short-term vs long-term memory
[​](https://docs.mem0.ai/core-concepts/memory-types#short-term-vs-long-term-memory)- Conversation history– recent turns in order so the agent remembers what was just said.
- Working memory– temporary state such as tool outputs or intermediate calculations.
- Attention context– the immediate focus of the assistant, similar to what a person holds in mind mid-sentence.
- Factual memory– user preferences, account details, and domain facts.
- Episodic memory– summaries of past interactions or completed tasks.
- Semantic memory– relationships between concepts so agents can reason about them later.

## ​How does it work?
[​](https://docs.mem0.ai/core-concepts/memory-types#how-does-it-work%3F)- Capture– Messages enter the conversation layer while the turn is active.
- Promote– Relevant details persist to session or user memory based on youruser_id,session_id, and metadata.
`user_id``session_id`- Retrieve– The search pipeline pulls from all layers, ranking user memories first, then session notes, then raw history.

```
import os

from mem0 import Memory

memory = Memory(api_key=os.environ["MEM0_API_KEY"])

# Sticky note: conversation memory
memory.add(
    ["I'm Alex and I prefer boutique hotels."],
    user_id="alex",
    session_id="trip-planning-2025",
)

# Later in the session, pull long-term + session context
results = memory.search(
    "Any hotel preferences?",
    user_id="alex",
    session_id="trip-planning-2025",
)

```
`session_id``user_id`
## ​When should you use each layer?
[​](https://docs.mem0.ai/core-concepts/memory-types#when-should-you-use-each-layer%3F)- Conversation memory– Tool calls or chain-of-thought that only matter within the current turn.
- Session memory– Multi-step tasks (onboarding flows, debugging sessions) that should reset once complete.
- User memory– Personal preferences, account state, or compliance details that must persist across interactions.
- Organizational memory– Shared FAQs, product catalogs, or policies that every agent should recall.

## ​How it compares
[​](https://docs.mem0.ai/core-concepts/memory-types#how-it-compares)
## ​Put it into practice
[​](https://docs.mem0.ai/core-concepts/memory-types#put-it-into-practice)- Use theAdd Memoryguide to persist user preferences.
[Add Memory](https://docs.mem0.ai/core-concepts/memory-operations/add)- FollowAdvanced Memory Operationsto tune metadata and graph writes.
[Advanced Memory Operations](https://docs.mem0.ai/platform/advanced-memory-operations)
## ​See it live
[​](https://docs.mem0.ai/core-concepts/memory-types#see-it-live)- AI Tutor with Mem0shows session vs user memories in action.
[AI Tutor with Mem0](https://docs.mem0.ai/cookbooks/companions/ai-tutor)- Support Inbox with Mem0demonstrates shared org memory.
[Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox)[Explore Memory Operations](https://docs.mem0.ai/core-concepts/memory-operations/add)
## Explore Memory Operations
[See a Cookbook](https://docs.mem0.ai/cookbooks/operations/support-inbox)
## See a Cookbook
