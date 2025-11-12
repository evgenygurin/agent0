# Together - Mem0
Source: https://docs.mem0.ai/components/embedders/models/together
Downloaded: 2025-11-12 21:20:20
================================================================================

`TOGETHER_API_KEY`[Together Platform](https://api.together.xyz/settings/api-keys)
### ​Usage
[​](https://docs.mem0.ai/components/embedders/models/together#usage)`embedding_model_dims``vector_store``768`
```
import os
from mem0 import Memory

os.environ["TOGETHER_API_KEY"] = "your_api_key"
os.environ["OPENAI_API_KEY"] = "your_api_key" # For LLM

config = {
    "embedder": {
        "provider": "together",
        "config": {
            "model": "togethercomputer/m2-bert-80M-8k-retrieval"
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
[​](https://docs.mem0.ai/components/embedders/models/together#config)`model``togethercomputer/m2-bert-80M-8k-retrieval``embedding_dims``768``api_key``None`