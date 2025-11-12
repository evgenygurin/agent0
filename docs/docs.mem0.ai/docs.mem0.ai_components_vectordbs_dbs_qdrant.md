# Qdrant - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/qdrant
Downloaded: 2025-11-12 21:20:19
================================================================================

[Qdrant](https://qdrant.tech/)
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/qdrant#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "test",
            "host": "localhost",
            "port": 6333,
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
[​](https://docs.mem0.ai/components/vectordbs/dbs/qdrant#config)`qdrant`- Python
- TypeScript
`collection_name``mem0``embedding_model_dims``1536``client``None``host``None``port``None``path``/tmp/qdrant``url``None``api_key``None``on_disk``False`