# Anthropic - Mem0
Source: https://docs.mem0.ai/components/llms/models/anthropic
Downloaded: 2025-11-12 21:20:19
================================================================================

`ANTHROPIC_API_KEY`[Account Settings Page](https://console.anthropic.com/account/keys)
## ​Usage
[​](https://docs.mem0.ai/components/llms/models/anthropic#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key" # used for embedding model
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "anthropic",
        "config": {
            "model": "claude-sonnet-4-20250514",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I’m not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```

## ​Config
[​](https://docs.mem0.ai/components/llms/models/anthropic#config)`anthropic`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)