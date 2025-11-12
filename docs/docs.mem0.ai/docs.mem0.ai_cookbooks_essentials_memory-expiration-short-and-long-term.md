# Set Memory Expiration - Mem0
Source: https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#overview)- Understand default (permanent) memory behavior
- Add expiration dates for temporary memories
- Decide what should be temporary vs permanent

## ​Setup
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#setup)
```
from mem0 import MemoryClient
from datetime import datetime, timedelta

client = MemoryClient(api_key="your-api-key")

```
`datetime``timedelta`
## ​Default Behavior: Everything Persists
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#default-behavior%3A-everything-persists)
```
# Store user preference
client.add("User prefers dark mode", user_id="sarah")

# Store session context
client.add("Currently browsing electronics category", user_id="sarah")

# 6 months later - both still exist
results = client.get_all(filters={"user_id": "sarah"})
print(f"Total memories: {len(results['results'])}")


```

```
Total memories: 2


```

## ​The Problem: Memory Bloat
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#the-problem%3A-memory-bloat)
## ​Short-Term Memories: Adding Expiration
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#short-term-memories%3A-adding-expiration)`expiration_date`
```
from datetime import datetime, timedelta

# Session context - expires in 7 days
expires_at = (datetime.now() + timedelta(days=7)).isoformat()

client.add(
    "Currently browsing electronics category",
    user_id="sarah",
    expiration_date=expires_at
)

# User preference - no expiration, persists forever
client.add(
    "User prefers dark mode",
    user_id="sarah"
)


```
`expiration_date`
## ​When to Use Each
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#when-to-use-each)
### ​Permanent Memories (no expiration_date):
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#permanent-memories-no-expiration-date-%3A)- User preferences and settings
- Account information
- Important facts and milestones
- Historical data that matters long-term

```
client.add("User prefers email notifications", user_id="sarah")
client.add("User's birthday is March 15th", user_id="sarah")
client.add("User completed onboarding on Jan 5th", user_id="sarah")


```

### ​Temporary Memories (with expiration_date):
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#temporary-memories-with-expiration-date-%3A)- Session context (current page, browsing history)
- Temporary reminders
- Recent chat history
- Cached data

```
expires_7d = (datetime.now() + timedelta(days=7)).isoformat()

client.add(
    "Currently viewing product ABC123",
    user_id="sarah",
    expiration_date=expires_7d
)

client.add(
    "Asked about return policy",
    user_id="sarah",
    expiration_date=expires_7d
)


```

## ​Setting Different Expiration Periods
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#setting-different-expiration-periods)
```
# Session context - 7 days
expires_7d = (datetime.now() + timedelta(days=7)).isoformat()
client.add("Browsing electronics", user_id="sarah", expiration_date=expires_7d)

# Recent chat - 30 days
expires_30d = (datetime.now() + timedelta(days=30)).isoformat()
client.add("User asked about warranty", user_id="sarah", expiration_date=expires_30d)

# Important preference - no expiration
client.add("User prefers dark mode", user_id="sarah")


```

## ​Using Metadata to Track Memory Types
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#using-metadata-to-track-memory-types)
```
expires_7d = (datetime.now() + timedelta(days=7)).isoformat()

# Tag session context
client.add(
    "Browsing electronics",
    user_id="sarah",
    expiration_date=expires_7d,
    metadata={"type": "session"}
)

# Tag preference
client.add(
    "User prefers dark mode",
    user_id="sarah",
    metadata={"type": "preference"}
)

# Query only preferences
preferences = client.get_all(
    filters={
        "AND": [
            {"user_id": "sarah"},
            {"metadata": {"type": "preference"}}
        ]
    }
)


```

## ​Checking Expiration Status
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#checking-expiration-status)
```
results = client.get_all(filters={"user_id": "sarah"})

for memory in results['results']:
    exp_date = memory.get('expiration_date')

    if exp_date:
        print(f"Temporary: {memory['memory']}")
        print(f"  Expires: {exp_date}\\n")
    else:
        print(f"Permanent: {memory['memory']}\\n")


```

```
Temporary: Browsing electronics
  Expires: 2025-11-01T10:30:00Z

Temporary: Viewed MacBook Pro and Dell XPS
  Expires: 2025-11-01T10:30:00Z

Permanent: User prefers dark mode

Permanent: User prefers email notifications


```

## ​What You Built
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#what-you-built)- Automatic expiration- Memories self-destruct after defined periods, no cron jobs needed
- Tiered retention- 7-day session context, 30-day chat history, permanent preferences
- Metadata tagging- Classify memories by type (session, preference, chat) for filtered retrieval
- Expiration tracking- Check which memories will expire and when usingget_all()
`get_all()`
## ​Summary
[​](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term#summary)`expiration_date`[Control Memory IngestionPair expirations with ingestion rules so only trusted context persists.](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion)
## Control Memory Ingestion
[Export Memories SafelyBuild compliant archives once your retention windows are dialed in.](https://docs.mem0.ai/cookbooks/essentials/exporting-memories)
## Export Memories Safely
