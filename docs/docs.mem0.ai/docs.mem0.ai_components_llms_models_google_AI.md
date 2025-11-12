# Google AI - Mem0
Source: https://docs.mem0.ai/components/llms/models/google_AI
Downloaded: 2025-11-12 21:20:19
================================================================================

`GOOGLE_API_KEY`[Google AI Studio](https://aistudio.google.com/app/apikey)`google.genai``google.generativeai``types``google.genai``"gemini-2.0-flash-001"``"gemini-2.0-flash-lite-001"`
## ​Usage
[​](https://docs.mem0.ai/components/llms/models/google_AI#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-openai-api-key"  # Used for embedding model
os.environ["GOOGLE_API_KEY"] = "your-gemini-api-key"

config = {
    "llm": {
        "provider": "gemini",
        "config": {
            "model": "gemini-2.0-flash-001",
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
    {"role": "user", "content": "I’m not a big fan of thrillers, but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thrillers and suggest sci-fi movies instead."}
]

m.add(messages, user_id="alice", metadata={"category": "movies"})


```

## ​Config
[​](https://docs.mem0.ai/components/llms/models/google_AI#config)`Gemini`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)