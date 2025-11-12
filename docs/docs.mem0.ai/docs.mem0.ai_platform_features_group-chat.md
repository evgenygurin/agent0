# Group Chat - Mem0
Source: https://docs.mem0.ai/platform/features/group-chat
Downloaded: 2025-11-12 21:20:19
================================================================================

[Read our research paper](https://mem0.ai/research)
## ​Overview
[​](https://docs.mem0.ai/platform/features/group-chat#overview)- Extracts memories from each participant’s messages separately
- Attributes each memory to the correct speaker using their name as theuser_idoragent_id
`user_id``agent_id`- Maintains individual memory profiles for each participant

## ​How Group Chat Works
[​](https://docs.mem0.ai/platform/features/group-chat#how-group-chat-works)`name`
```
{
  "role": "user",
  "name": "Alice",
  "content": "Hey team, I think we should use React for the frontend"
}

```
- Formats messages as"Alice (user): content"for processing
`"Alice (user): content"`- Extracts memories with proper attribution to each speaker
- Stores memories with the speaker’s name as theuser_id(for users) oragent_id(for assistants/agents)
`user_id``agent_id`
### ​Memory Attribution Rules
[​](https://docs.mem0.ai/platform/features/group-chat#memory-attribution-rules)- User Messages: Thenamefield becomes theuser_idin stored memories
`name``user_id`- Assistant/Agent Messages: Thenamefield becomes theagent_idin stored memories
`name``agent_id`- Messages without names: Fall back to standard processing using role as identifier

## ​Using Group Chat
[​](https://docs.mem0.ai/platform/features/group-chat#using-group-chat)
### ​Basic Group Chat
[​](https://docs.mem0.ai/platform/features/group-chat#basic-group-chat)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

# Group chat with multiple users
messages = [
    {"role": "user", "name": "Alice", "content": "Hey team, I think we should use React for the frontend"},
    {"role": "user", "name": "Bob", "content": "I disagree, Vue.js would be better for our use case"},
    {"role": "user", "name": "Charlie", "content": "What about considering Angular? It has great enterprise support"},
    {"role": "assistant", "content": "All three frameworks have their merits. Let me summarize the pros and cons of each."}
]

response = client.add(
    messages,
    run_id="group_chat_1",
    infer=True
)
print(response)

```

## ​Retrieving Group Chat Memories
[​](https://docs.mem0.ai/platform/features/group-chat#retrieving-group-chat-memories)
### ​Get All Memories for a Session
[​](https://docs.mem0.ai/platform/features/group-chat#get-all-memories-for-a-session)
```
# Get all memories for a specific run_id
# Use wildcard "*" for user_id to match all participants
filters = {
    "AND": [
        {"user_id": "*"},
        {"run_id": "group_chat_1"}
    ]
}

all_memories = client.get_all(filters=filters, page=1)
print(all_memories)

```

### ​Get Memories for a Specific Participant
[​](https://docs.mem0.ai/platform/features/group-chat#get-memories-for-a-specific-participant)
```
# Get memories for a specific participant
filters = {
    "AND": [
        {"user_id": "charlie"},
        {"run_id": "group_chat_1"}
    ]
}

charlie_memories = client.get_all(filters=filters, page=1)
print(charlie_memories)

```

### ​Search Within Group Chat Context
[​](https://docs.mem0.ai/platform/features/group-chat#search-within-group-chat-context)
```
# Search within group chat context
filters = {
    "AND": [
        {"user_id": "charlie"},
        {"run_id": "group_chat_1"}
    ]
}

search_response = client.search(
    query="What are the tasks?",
    filters=filters
)
print(search_response)

```

## ​Async Mode Support
[​](https://docs.mem0.ai/platform/features/group-chat#async-mode-support)
```
# Group chat with async mode
response = client.add(
    messages,
    run_id="groupchat_async",
    infer=True,
    async_mode=True
)
print(response)

```

## ​Message Format Requirements
[​](https://docs.mem0.ai/platform/features/group-chat#message-format-requirements)
### ​Required Fields
[​](https://docs.mem0.ai/platform/features/group-chat#required-fields)- role: The participant’s role ("user","assistant","agent")
`role``"user"``"assistant"``"agent"`- content: The message content
`content`- name: The participant’s name (required for group chat detection)
`name`
### ​Example Message Structure
[​](https://docs.mem0.ai/platform/features/group-chat#example-message-structure)
```
{
  "role": "user",
  "name": "Alice",
  "content": "I think we should use React for the frontend"
}

```

### ​Supported Roles
[​](https://docs.mem0.ai/platform/features/group-chat#supported-roles)- user: Human participants (memories stored withuser_id)
`user``user_id`- assistant: AI assistants (memories stored withagent_id)
`assistant``agent_id`
## ​Best Practices
[​](https://docs.mem0.ai/platform/features/group-chat#best-practices)- Consistent Naming: Use consistent names for participants across sessions to maintain proper memory attribution.
- Clear Role Assignment: Ensure each participant has the correct role (user,assistant, oragent) for proper memory categorization.
`user``assistant``agent`- Session Management: Use meaningfulrun_idvalues to organize group chat sessions and enable easy retrieval.
`run_id`- Memory Filtering: Use filters to retrieve memories from specific participants or sessions when needed.
- Async Processing: Useasync_mode=Truefor large group conversations to improve performance.
`async_mode=True`- Search Context: Leverage the search functionality to find specific information within group chat contexts.

## ​Use Cases
[​](https://docs.mem0.ai/platform/features/group-chat#use-cases)- Team Meetings: Track individual team member preferences and contributions
- Customer Support: Maintain separate memory profiles for different customers
- Multi-Agent Systems: Manage conversations with multiple AI assistants
- Collaborative Projects: Track individual preferences and expertise areas
- Group Discussions: Maintain context for each participant’s viewpoints
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
