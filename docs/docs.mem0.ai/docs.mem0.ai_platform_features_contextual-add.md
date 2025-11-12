# Contextual Memory Creation - Mem0
Source: https://docs.mem0.ai/platform/features/contextual-add
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​What is Contextual Memory Creation?
[​](https://docs.mem0.ai/platform/features/contextual-add#what-is-contextual-memory-creation%3F)
```
# Just send new messages - Mem0 handles the context
messages = [
    {"role": "user", "content": "I love Italian food, especially pasta"},
    {"role": "assistant", "content": "Great! I'll remember your preference for Italian cuisine."}
]

client.add(messages, user_id="user123", version="v2")

```

## ​Why Use Contextual Memory Creation?
[​](https://docs.mem0.ai/platform/features/contextual-add#why-use-contextual-memory-creation%3F)- Simple: Send only new messages, no manual history tracking
- Efficient: Smaller payloads and faster processing
- Automatic: Context management handled by Mem0
- Reliable: No risk of missing interaction history
- Scalable: Works seamlessly as your application grows

## ​How It Works
[​](https://docs.mem0.ai/platform/features/contextual-add#how-it-works)
### ​Basic Usage
[​](https://docs.mem0.ai/platform/features/contextual-add#basic-usage)
```
# First interaction
messages1 = [
    {"role": "user", "content": "Hi, I'm Sarah from New York"},
    {"role": "assistant", "content": "Hello Sarah! Nice to meet you."}
]
client.add(messages1, user_id="sarah", version="v2")

# Later interaction - just send new messages
messages2 = [
    {"role": "user", "content": "I'm planning a trip to Italy next month"},
    {"role": "assistant", "content": "How exciting! Italy is beautiful this time of year."}
]
client.add(messages2, user_id="sarah", version="v2")
# Mem0 automatically knows Sarah is from New York and can use this context

```

## ​Organization Strategies
[​](https://docs.mem0.ai/platform/features/contextual-add#organization-strategies)
### ​User-Level Memories (user_idonly)
[​](https://docs.mem0.ai/platform/features/contextual-add#user-level-memories-user-id-only)`user_id`
```
# Persistent user memories across all interactions
messages = [
    {"role": "user", "content": "I'm allergic to nuts and dairy"},
    {"role": "assistant", "content": "I've noted your allergies for future reference."}
]

client.add(messages, user_id="user123", version="v2")
# This allergy info will be available in ALL future interactions

```

### ​Session-Specific Memories (user_id+run_id)
[​](https://docs.mem0.ai/platform/features/contextual-add#session-specific-memories-user-id-%2B-run-id)`user_id``run_id`
```
# Trip planning session
messages1 = [
    {"role": "user", "content": "I want to plan a 5-day trip to Tokyo"},
    {"role": "assistant", "content": "Perfect! Let's plan your Tokyo adventure."}
]
client.add(messages1, user_id="user123", run_id="tokyo-trip-2024", version="v2")

# Later in the same trip planning session
messages2 = [
    {"role": "user", "content": "I prefer staying near Shibuya"},
    {"role": "assistant", "content": "Great choice! Shibuya is very convenient."}
]
client.add(messages2, user_id="user123", run_id="tokyo-trip-2024", version="v2")

# Different session for work project (separate context)
work_messages = [
    {"role": "user", "content": "Let's discuss the Q4 marketing strategy"},
    {"role": "assistant", "content": "Sure! What are your main goals for Q4?"}
]
client.add(work_messages, user_id="user123", run_id="q4-marketing", version="v2")

```

## ​Real-World Use Cases
[​](https://docs.mem0.ai/platform/features/contextual-add#real-world-use-cases)- Customer Support
- Personal AI Assistant
- Educational Platform

```
# Support ticket context - keeps interaction focused
messages = [
    {"role": "user", "content": "My subscription isn't working"},
    {"role": "assistant", "content": "I can help with that. What specific issue are you experiencing?"},
    {"role": "user", "content": "I can't access premium features even though I paid"}
]

# Each support ticket gets its own run_id
client.add(messages, 
    user_id="customer123", 
    run_id="ticket-2024-001", 
    version="v2"
)

```

## ​Best Practices
[​](https://docs.mem0.ai/platform/features/contextual-add#best-practices)
### ​✅ Do
[​](https://docs.mem0.ai/platform/features/contextual-add#%E2%9C%85-do)- Organize by context scope: Useuser_idonly for persistent data, addrun_idfor session-specific context
`user_id``run_id`- Keep messages focusedon the current interaction
- Test with real interaction flowsto ensure context works as expected

### ​❌ Don’t
[​](https://docs.mem0.ai/platform/features/contextual-add#%E2%9D%8C-don%E2%80%99t)- Send duplicate messages or interaction history
- Forget to includeversion="v2"parameter
`version="v2"`- Mix contextual and non-contextual approaches in the same application

## ​Troubleshooting
[​](https://docs.mem0.ai/platform/features/contextual-add#troubleshooting)`version="v2"``user_id``run_id``user_id``run_id``run_id`[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
