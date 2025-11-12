# Expiration Date - Mem0
Source: https://docs.mem0.ai/platform/features/expiration-date
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Benefits of Memory Expiration
[​](https://docs.mem0.ai/platform/features/expiration-date#benefits-of-memory-expiration)- Time-Sensitive Information Management: Handle information that is only relevant for a specific time period.
- Event-Based Memory: Manage information related to upcoming events that becomes irrelevant after the event passes.

## ​Setting Memory Expiration Date
[​](https://docs.mem0.ai/platform/features/expiration-date#setting-memory-expiration-date)
```
import datetime
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

messages = [
    {
        "role": "user", 
        "content": "I'll be in San Francisco until the end of this month."
    }
]

# Set an expiration date for this memory
client.add(messages=messages, user_id="alex", expiration_date=str(datetime.datetime.now().date() + datetime.timedelta(days=30)))

# You can also use an explicit date string
client.add(messages=messages, user_id="alex", expiration_date="2023-08-31")

```
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
