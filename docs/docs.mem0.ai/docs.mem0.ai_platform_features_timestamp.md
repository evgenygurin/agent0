# Memory Timestamps - Mem0
Source: https://docs.mem0.ai/platform/features/timestamp
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Overview
[​](https://docs.mem0.ai/platform/features/timestamp#overview)- Maintain accurate chronological ordering of memories
- Import historical data with proper timestamps
- Create memories that reflect when events actually occurred
- Build timelines with precise temporal information

## ​Benefits of Custom Timestamps
[​](https://docs.mem0.ai/platform/features/timestamp#benefits-of-custom-timestamps)- Historical Accuracy: Preserve the exact timing of past events and information.
- Data Migration: Seamlessly migrate existing data while maintaining original timestamps.
- Time-Sensitive Analysis: Enable time-based analysis and pattern recognition across memories.
- Consistent Chronology: Maintain proper ordering of memories for coherent storytelling.

## ​Using Custom Timestamps
[​](https://docs.mem0.ai/platform/features/timestamp#using-custom-timestamps)
### ​Adding Memories with Custom Timestamps
[​](https://docs.mem0.ai/platform/features/timestamp#adding-memories-with-custom-timestamps)
```
import os
import time
from datetime import datetime, timedelta

from mem0 import MemoryClient

os.environ["MEM0_API_KEY"] = "your-api-key"

client = MemoryClient()

# Get the current time
current_time = datetime.now()

# Calculate 5 days ago
five_days_ago = current_time - timedelta(days=5)

# Convert to Unix timestamp (seconds since epoch)
unix_timestamp = int(five_days_ago.timestamp())

# Add memory with custom timestamp
messages = [
    {"role": "user", "content": "I'm travelling to SF"}
]
client.add(messages, user_id="user1", timestamp=unix_timestamp)

```

### ​Timestamp Format
[​](https://docs.mem0.ai/platform/features/timestamp#timestamp-format)
```
# January 1, 2023 timestamp
january_2023_timestamp = 1672531200  # Unix timestamp for 2023-01-01 00:00:00 UTC

messages = [
    {"role": "user", "content": "I'm travelling to SF"}
]
client.add(messages, user_id="user1", timestamp=january_2023_timestamp)

```
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
