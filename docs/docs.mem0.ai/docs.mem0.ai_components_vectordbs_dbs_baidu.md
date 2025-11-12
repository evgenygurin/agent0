# Baidu VectorDB (Mochow) - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/baidu
Downloaded: 2025-11-12 21:20:20
================================================================================

[Baidu VectorDB](https://cloud.baidu.com/doc/VDB/index.html)
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/baidu#usage)
```
import os
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "baidu",
        "config": {
            "endpoint": "http://your-mochow-endpoint:8287",
            "account": "root",
            "api_key": "your-api-key",
            "database_name": "mem0",
            "table_name": "mem0_table",
            "embedding_model_dims": 1536,
            "metric_type": "COSINE"
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about a thriller movie? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```

### ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/baidu#config)`endpoint``account``root``api_key``database_name``mem0``table_name``mem0_table``embedding_model_dims``1536``metric_type``L2`
### ​Distance Metrics
[​](https://docs.mem0.ai/components/vectordbs/dbs/baidu#distance-metrics)- L2: Euclidean distance (default)
`L2`- IP: Inner product
`IP`- COSINE: Cosine similarity
`COSINE`
### ​Index Configuration
[​](https://docs.mem0.ai/components/vectordbs/dbs/baidu#index-configuration)- m: 16 (number of connections per element)
`m`- efconstruction: 200 (size of the dynamic candidate list)
`efconstruction`- auto_build: true (automatically build index)
`auto_build`- auto_build_index_policy: Incremental build with 10000 rows increment
`auto_build_index_policy`