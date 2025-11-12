# Ollama - Mem0
Source: https://docs.mem0.ai/components/embedders/models/ollama
Downloaded: 2025-11-12 21:20:20
================================================================================


### ​Usage
[​](https://docs.mem0.ai/components/embedders/models/ollama#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your_api_key" # For LLM

config = {
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large"
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
m.add(messages, user_id="john")

```

### ​Config
[​](https://docs.mem0.ai/components/embedders/models/ollama#config)- Python
- TypeScript
`model``nomic-embed-text``embedding_dims``512``ollama_base_url``None`