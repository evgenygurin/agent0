# Milvus - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/milvus
Downloaded: 2025-11-12 21:20:20
================================================================================

[Milvus](https://milvus.io/)
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/milvus#usage)
```
import os
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "milvus",
        "config": {
            "collection_name": "test",
            "embedding_model_dims": 1536,
            "url": "127.0.0.1",
            "token": "8e4b8ca8cf2c67",
            "db_name": "my_database",
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
[​](https://docs.mem0.ai/components/vectordbs/dbs/milvus#config)`url``http://localhost:19530``token``None``collection_name``mem0``embedding_model_dims``1536``metric_type``L2``db_name``""`