# Together - Mem0
Source: https://docs.mem0.ai/components/llms/models/together
Downloaded: 2025-11-12 21:20:19
================================================================================

`TOGETHER_API_KEY`[Account settings page](https://api.together.xyz/settings/api-keys)
## ​Usage
[​](https://docs.mem0.ai/components/llms/models/together#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key" # used for embedding model
os.environ["TOGETHER_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "together",
        "config": {
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "temperature": 0.2,
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
[​](https://docs.mem0.ai/components/llms/models/together#config)`together`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)