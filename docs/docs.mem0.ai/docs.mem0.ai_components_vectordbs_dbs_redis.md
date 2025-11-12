# Redis - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/redis
Downloaded: 2025-11-12 21:20:20
================================================================================

[Redis](https://redis.io/)
### ​Installation
[​](https://docs.mem0.ai/components/vectordbs/dbs/redis#installation)
```
pip install redis redisvl

```

```
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

```

### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/redis#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "redis",
        "config": {
            "collection_name": "mem0",
            "embedding_model_dims": 1536,
            "redis_url": "redis://localhost:6379"
        }
    },
    "version": "v1.1"
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
[​](https://docs.mem0.ai/components/vectordbs/dbs/redis#config)`redis`- Python
- TypeScript
`collection_name``mem0``embedding_model_dims``1536``redis_url``None`