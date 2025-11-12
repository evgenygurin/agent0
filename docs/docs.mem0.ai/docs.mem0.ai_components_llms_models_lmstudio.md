# LM Studio - Mem0
Source: https://docs.mem0.ai/components/llms/models/lmstudio
Downloaded: 2025-11-12 21:20:19
================================================================================


## ​Usage
[​](https://docs.mem0.ai/components/llms/models/lmstudio#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key" # used for embedding model

config = {
    "llm": {
        "provider": "lmstudio",
        "config": {
            "model": "lmstudio-community/Meta-Llama-3.1-70B-Instruct-GGUF/Meta-Llama-3.1-70B-Instruct-IQ2_M.gguf",
            "temperature": 0.2,
            "max_tokens": 2000,
            "lmstudio_base_url": "http://localhost:1234/v1", # default LM Studio API URL
            "lmstudio_response_format": {"type": "json_schema", "json_schema": {"type": "object", "schema": {}}},
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

### ​Running Completely Locally
[​](https://docs.mem0.ai/components/llms/models/lmstudio#running-completely-locally)
```
from mem0 import Memory

# No external API keys needed!
config = {
    "llm": {
        "provider": "lmstudio"
    },
    "embedder": {
        "provider": "lmstudio"
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice123", metadata={"category": "movies"})

```
- An LLM model loaded for generating responses
- An embedding model loaded for vector embeddings
- The server enabled with the correct endpoints accessible
- Download and installLM Studio
[LM Studio](https://lmstudio.ai/)- Start a local server from the “Server” tab
- Set the appropriatelmstudio_base_urlin your configuration (default is usuallyhttp://localhost:1234/v1)
`lmstudio_base_url`[http://localhost:1234/v1](http://localhost:1234/v1)
## ​Config
[​](https://docs.mem0.ai/components/llms/models/lmstudio#config)`lmstudio`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)