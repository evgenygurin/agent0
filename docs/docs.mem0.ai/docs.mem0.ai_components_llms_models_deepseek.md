# DeepSeek - Mem0
Source: https://docs.mem0.ai/components/llms/models/deepseek
Downloaded: 2025-11-12 21:20:19
================================================================================

`DEEPSEEK_API_KEY``DEEPSEEK_API_BASE`[https://api.deepseek.com](https://api.deepseek.com)
## ​Usage
[​](https://docs.mem0.ai/components/llms/models/deepseek#usage)
```
import os
from mem0 import Memory

os.environ["DEEPSEEK_API_KEY"] = "your-api-key"
os.environ["OPENAI_API_KEY"] = "your-api-key" # for embedder model

config = {
    "llm": {
        "provider": "deepseek",
        "config": {
            "model": "deepseek-chat",  # default model
            "temperature": 0.2,
            "max_tokens": 2000,
            "top_p": 1.0
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

```
config = {
    "llm": {
        "provider": "deepseek",
        "config": {
            "model": "deepseek-chat",
            "deepseek_base_url": "https://your-custom-endpoint.com",
            "api_key": "your-api-key"  # alternatively to using environment variable
        }
    }
}

```

## ​Config
[​](https://docs.mem0.ai/components/llms/models/deepseek#config)`deepseek`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)