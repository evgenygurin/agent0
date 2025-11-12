# Pgvector - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/pgvector
Downloaded: 2025-11-12 21:20:20
================================================================================

[pgvector](https://github.com/pgvector/pgvector)`CREATE EXTENSION IF NOT EXISTS vector;`
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/pgvector#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "pgvector",
        "config": {
            "user": "test",
            "password": "123",
            "host": "127.0.0.1",
            "port": "5432",
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

### ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/pgvector#config)`dbname``postgres``collection_name``mem0``embedding_model_dims``1536``user``None``password``None``host``None``port``None``diskann``True``hnsw``False``sslmode``None``connection_string``None``connection_pool``None`- connection_pool(highest priority)
`connection_pool`- connection_string
`connection_string`- Individual connection parameters (user,password,host,port,sslmode)
`user``password``host``port``sslmode`