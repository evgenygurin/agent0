# Async Client - Mem0
Source: https://docs.mem0.ai/platform/features/async-client
Downloaded: 2025-11-12 21:20:18
================================================================================

`AsyncMemoryClient``MemoryClient`
## ​Initialization
[​](https://docs.mem0.ai/platform/features/async-client#initialization)
```
import os
from mem0 import AsyncMemoryClient

os.environ["MEM0_API_KEY"] = "your-api-key"

client = AsyncMemoryClient()

```

## ​Methods
[​](https://docs.mem0.ai/platform/features/async-client#methods)`AsyncMemoryClient`
### ​Add
[​](https://docs.mem0.ai/platform/features/async-client#add)
```
messages = [
    {"role": "user", "content": "Alice loves playing badminton"},
    {"role": "assistant", "content": "That's great! Alice is a fitness freak"},
]
await client.add(messages, user_id="alice")

```

### ​Search
[​](https://docs.mem0.ai/platform/features/async-client#search)
```
await client.search("What is Alice's favorite sport?", user_id="alice")

```

### ​Get All
[​](https://docs.mem0.ai/platform/features/async-client#get-all)
```
await client.get_all(user_id="alice")

```

### ​Delete
[​](https://docs.mem0.ai/platform/features/async-client#delete)
```
await client.delete(memory_id="memory-id-here")

```

### ​Delete All
[​](https://docs.mem0.ai/platform/features/async-client#delete-all)
```
await client.delete_all(user_id="alice")

```

### ​History
[​](https://docs.mem0.ai/platform/features/async-client#history)
```
await client.history(memory_id="memory-id-here")

```

### ​Users
[​](https://docs.mem0.ai/platform/features/async-client#users)
```
await client.users()

```

### ​Reset
[​](https://docs.mem0.ai/platform/features/async-client#reset)
```
await client.reset()

```

## ​Conclusion
[​](https://docs.mem0.ai/platform/features/async-client#conclusion)`AsyncMemoryClient`[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
