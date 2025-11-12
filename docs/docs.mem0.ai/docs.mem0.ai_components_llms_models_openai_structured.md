# OpenAI - Mem0
Source: https://docs.mem0.ai/components/llms/models/openai_structured
Downloaded: 2025-11-12 21:20:20
================================================================================

`OPENAI_API_KEY`[OpenAI Platform](https://platform.openai.com/account/api-keys)`Parallel tool calling``temperature``top_p``presence_penalty``frequency_penalty``logprobs``top_logprobs``logit_bias``max_tokens`
## ​Usage
[​](https://docs.mem0.ai/components/llms/models/openai_structured#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4.1-nano-2025-04-14",
            "temperature": 0.2,
            "max_tokens": 2000,
        }
    }
}

# Use Openrouter by passing it's api key
# os.environ["OPENROUTER_API_KEY"] = "your-api-key"
# config = {
#    "llm": {
#        "provider": "openai",
#        "config": {
#            "model": "meta-llama/llama-3.1-70b-instruct",
#        }
#    }
# }

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I’m not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```
[OpenAI structured-outputs](https://platform.openai.com/docs/guides/structured-outputs/introduction)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "openai_structured",
        "config": {
            "model": "gpt-4.1-nano-2025-04-14",
            "temperature": 0.0,
        }
    }
}

m = Memory.from_config(config)

```

## ​Config
[​](https://docs.mem0.ai/components/llms/models/openai_structured#config)`openai`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)