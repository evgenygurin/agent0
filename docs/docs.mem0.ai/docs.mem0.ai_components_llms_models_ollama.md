# Ollama - Mem0
Source: https://docs.mem0.ai/components/llms/models/ollama
Downloaded: 2025-11-12 21:20:19
================================================================================

[models](https://ollama.com/search?c=tools)
## ​Usage
[​](https://docs.mem0.ai/components/llms/models/ollama#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key" # for embedder

config = {
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "mixtral:8x7b",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```

## ​Config
[​](https://docs.mem0.ai/components/llms/models/ollama#config)`ollama`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)