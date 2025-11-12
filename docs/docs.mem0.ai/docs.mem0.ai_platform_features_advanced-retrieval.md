# Advanced Retrieval - Mem0
Source: https://docs.mem0.ai/platform/features/advanced-retrieval
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​What is Advanced Retrieval?
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#what-is-advanced-retrieval%3F)
## ​Search Enhancement Options
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#search-enhancement-options)
### ​Keyword Search
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#keyword-search)- When to Use
- How it Works
- Performance
- Searching for specific entities, names, or technical terms
- Need comprehensive coverage of a topic
- Want broader recall even if some results are less relevant
- Working with domain-specific terminology

### ​Reranking
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#reranking)- When to Use
- How it Works
- Performance
- Need the most relevant result at the top
- Result order is critical for your application
- Want consistent quality across different queries
- Building user-facing features where accuracy matters

### ​Memory Filtering
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#memory-filtering)- When to Use
- How it Works
- Performance
- Need highly specific, focused results
- Working with large datasets where noise is problematic
- Quality over quantity is essential
- Building production or safety-critical applications

## ​Real-World Use Cases
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#real-world-use-cases)- Personal AI Assistant
- Customer Support
- Healthcare AI
- Learning Platform

```
# Smart home assistant finding device preferences
results = client.search(
    query="How do I like my bedroom temperature?",
    keyword_search=True,    # Find specific temperature mentions
    rerank=True,           # Get most recent preferences first
    user_id="user123"
)

# Finds: "Keep bedroom at 68°F", "Too cold last night at 65°F", etc.

```

## ​Choosing the Right Combination
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#choosing-the-right-combination)
### ​Recommended Configurations
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#recommended-configurations)
```
# Fast and broad - good for exploration
def quick_search(query, user_id):
    return client.search(
        query=query,
        keyword_search=True,
        user_id=user_id
    )

# Balanced - good for most applications  
def standard_search(query, user_id):
    return client.search(
        query=query,
        keyword_search=True,
        rerank=True,
        user_id=user_id
    )

# High precision - good for critical applications
def precise_search(query, user_id):
    return client.search(
        query=query,
        rerank=True,
        filter_memories=True,
        user_id=user_id
    )

```

## ​Best Practices
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#best-practices)
### ​Do
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#do)- Start simple with just one enhancement and measure impact
- Use keyword search for entity-heavy queries (names, places, technical terms)
- Use reranking when the top result quality matters most
- Use filtering for production systems where precision is critical
- Handle empty results gracefully when filtering is too aggressive
- Monitor latency and adjust based on your application’s needs

### ​Don’t
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#don%E2%80%99t)- Enable all options by default without measuring necessity
- Use filtering for broad exploratory queries
- Ignore latency impact in real-time applications
- Forget to handle cases where filtering returns no results
- Use advanced retrieval for simple, fast lookup scenarios

## ​Performance Guidelines
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#performance-guidelines)
### ​Latency Expectations
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#latency-expectations)
```
# Performance monitoring example
import time

start_time = time.time()
results = client.search(
    query="user preferences",
    keyword_search=True,  # +10ms
    rerank=True,         # +150ms
    filter_memories=True, # +250ms
    user_id="user123"
)
latency = time.time() - start_time
print(f"Search completed in {latency:.2f}s")  # ~0.41s expected

```

### ​Optimization Tips
[​](https://docs.mem0.ai/platform/features/advanced-retrieval#optimization-tips)- Cache frequent queriesto avoid repeated advanced processing
- Use session-specific searchwithrun_idto reduce search space
`run_id`- Implement fallback logicwhen filtering returns empty results
- Monitor and alerton search latency patterns
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
