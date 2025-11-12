# Mongodb - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/mongodb
Downloaded: 2025-11-12 21:20:20
================================================================================


# ​MongoDB
[​](https://docs.mem0.ai/components/vectordbs/dbs/mongodb#mongodb)[MongoDB](https://www.mongodb.com/)
## ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/mongodb#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "mongodb",
        "config": {
            "db_name": "mem0-db",
            "collection_name": "mem0-collection",
            "mongo_uri":"mongodb://username:password@localhost:27017"
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

## ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/mongodb#config)`"mem0_db"``"mem0_collection"``1536``mongodb://username:password@localhost:27017``mongo_uri``mongodb://username:password@localhost:27017`