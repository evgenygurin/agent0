# Weaviate - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/weaviate
Downloaded: 2025-11-12 21:20:19
================================================================================

[Weaviate](https://weaviate.io/)
### ​Installation
[​](https://docs.mem0.ai/components/vectordbs/dbs/weaviate#installation)
```
pip install weaviate weaviate-client

```

### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/weaviate#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "weaviate",
        "config": {
            "collection_name": "test",
            "cluster_url": "http://localhost:8080",
            "auth_client_secret": None,
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about a thriller movie? They can be quite engaging."},
    {"role": "user", "content": "I’m not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```

### ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/weaviate#config)`collection_name``mem0``embedding_model_dims``1536``cluster_url``None``auth_client_secret``None`