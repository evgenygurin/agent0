# OpenAI - Mem0
Source: https://docs.mem0.ai/components/embedders/models/openai
Downloaded: 2025-11-12 21:20:20
================================================================================

`OPENAI_API_KEY`[OpenAI Platform](https://platform.openai.com/account/api-keys)
### ​Usage
[​](https://docs.mem0.ai/components/embedders/models/openai#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your_api_key"

config = {
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-large"
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
m.add(messages, user_id="john")

```

### ​Config
[​](https://docs.mem0.ai/components/embedders/models/openai#config)- Python
- TypeScript
`model``text-embedding-3-small``embedding_dims``1536``api_key``None`