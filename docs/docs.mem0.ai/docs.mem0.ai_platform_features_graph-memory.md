# Graph Memory - Mem0
Source: https://docs.mem0.ai/platform/features/graph-memory
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Overview
[​](https://docs.mem0.ai/platform/features/graph-memory#overview)
## ​How Graph Memory Works
[​](https://docs.mem0.ai/platform/features/graph-memory#how-graph-memory-works)- Mem0 automatically builds a graph representation of entities
- Vector search returns the top semantic matches (with any reranker you configure)
- Graph relations are returned alongside those results to provide additional context—they do not reorder the vector hits

## ​Using Graph Memory
[​](https://docs.mem0.ai/platform/features/graph-memory#using-graph-memory)`enable_graph=True`
### ​Adding Memories with Graph Memory
[​](https://docs.mem0.ai/platform/features/graph-memory#adding-memories-with-graph-memory)
```
from mem0 import MemoryClient

client = MemoryClient(
    api_key="your-api-key",
    org_id="your-org-id",
    project_id="your-project-id"
)

messages = [
    {"role": "user", "content": "My name is Joseph"},
    {"role": "assistant", "content": "Hello Joseph, it's nice to meet you!"},
    {"role": "user", "content": "I'm from Seattle and I work as a software engineer"}
]

# Enable graph memory when adding
client.add(
    messages,
    user_id="joseph",
    enable_graph=True
)

```
`add``get_all()`
### ​Searching with Graph Memory
[​](https://docs.mem0.ai/platform/features/graph-memory#searching-with-graph-memory)
```
# Search with graph memory enabled
results = client.search(
    "what is my name?",
    user_id="joseph",
    enable_graph=True
)

print(results)

```
`results``relations`
### ​Retrieving All Memories with Graph Memory
[​](https://docs.mem0.ai/platform/features/graph-memory#retrieving-all-memories-with-graph-memory)
```
# Get all memories with graph context
memories = client.get_all(
    user_id="joseph",
    enable_graph=True
)

print(memories)

```

### ​Setting Graph Memory at Project Level
[​](https://docs.mem0.ai/platform/features/graph-memory#setting-graph-memory-at-project-level)`enable_graph=True`
```
from mem0 import MemoryClient

client = MemoryClient(
    api_key="your-api-key",
    org_id="your-org-id",
    project_id="your-project-id"
)

# Enable graph memory for all operations in this project
client.project.update(enable_graph=True)

# Now all add operations will use graph memory by default
messages = [
    {"role": "user", "content": "My name is Joseph"},
    {"role": "assistant", "content": "Hello Joseph, it's nice to meet you!"},
    {"role": "user", "content": "I'm from Seattle and I work as a software engineer"}
]

client.add(
    messages,
    user_id="joseph"
)

```

## ​Best Practices
[​](https://docs.mem0.ai/platform/features/graph-memory#best-practices)- Enable Graph Memory for applications where understanding context and relationships between memories is important.
- Graph Memory works best with a rich history of related conversations.
- Consider Graph Memory for long-running assistants that need to track evolving information.

## ​Performance Considerations
[​](https://docs.mem0.ai/platform/features/graph-memory#performance-considerations)[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
