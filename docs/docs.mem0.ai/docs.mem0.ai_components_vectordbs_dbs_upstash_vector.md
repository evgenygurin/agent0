# Upstash vector - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/upstash_vector
Downloaded: 2025-11-12 21:20:20
================================================================================

[Upstash Vector](https://upstash.com/docs/vector)
### ​Usage with Upstash embeddings
[​](https://docs.mem0.ai/components/vectordbs/dbs/upstash_vector#usage-with-upstash-embeddings)`enable_embeddings``True`
```
import os
from mem0 import Memory

os.environ["UPSTASH_VECTOR_REST_URL"] = "..."
os.environ["UPSTASH_VECTOR_REST_TOKEN"] = "..."

config = {
    "vector_store": {
        "provider": "upstash_vector",
        "enable_embeddings": True,
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})

```
`enable_embeddings``True`
### ​Usage with external embedding providers
[​](https://docs.mem0.ai/components/vectordbs/dbs/upstash_vector#usage-with-external-embedding-providers)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "..."
os.environ["UPSTASH_VECTOR_REST_URL"] = "..."
os.environ["UPSTASH_VECTOR_REST_TOKEN"] = "..."

config = {
    "vector_store": {
        "provider": "upstash_vector",
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-large"
        },
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})

```

### ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/upstash_vector#config)`url``None``token``None``client``upstash_vector.Index``None``collection_name``""``enable_embeddings``False``url``token``UPSTASH_VECTOR_REST_URL``UPSTASH_VECTOR_REST_TOKEN`