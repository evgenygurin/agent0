# Chroma - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/chroma
Downloaded: 2025-11-12 21:20:19
================================================================================

[Chroma](https://www.trychroma.com/)
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/chroma#usage)
#### ​Local Installation
[​](https://docs.mem0.ai/components/vectordbs/dbs/chroma#local-installation)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "test",
            "path": "db",
            # Optional: ChromaDB Cloud configuration
            # "api_key": "your-chroma-cloud-api-key",
            # "tenant": "your-chroma-cloud-tenant-id",
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

### ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/chroma#config)`collection_name``mem0``client``None``path``db``host``None``port``None``api_key``None``tenant``None`