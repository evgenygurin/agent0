# Faiss - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/faiss
Downloaded: 2025-11-12 21:20:20
================================================================================

[FAISS](https://github.com/facebookresearch/faiss)
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/faiss#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "faiss",
        "config": {
            "collection_name": "test",
            "path": "/tmp/faiss_memories",
            "distance_strategy": "euclidean"
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

### ​Installation
[​](https://docs.mem0.ai/components/vectordbs/dbs/faiss#installation)
```
# For CPU version
pip install faiss-cpu

# For GPU version (requires CUDA)
pip install faiss-gpu

```

### ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/faiss#config)`collection_name``mem0``path``/tmp/faiss/<collection_name>``distance_strategy``euclidean``normalize_L2``False`
### ​Performance Considerations
[​](https://docs.mem0.ai/components/vectordbs/dbs/faiss#performance-considerations)- Efficiency: FAISS is optimized for memory usage and speed, making it suitable for large-scale applications.
- Offline Support: FAISS works entirely locally, with no need for external servers or API calls.
- Storage Options: Vectors can be stored in-memory for maximum speed or persisted to disk.
- Multiple Index Types: FAISS supports different index types optimized for various use cases (though mem0 currently uses the basic flat index).

### ​Distance Strategies
[​](https://docs.mem0.ai/components/vectordbs/dbs/faiss#distance-strategies)- euclidean: L2 distance, suitable for most embedding models
- inner_product: Dot product similarity, useful for some specialized embeddings
- cosine: Cosine similarity, best for comparing semantic similarity regardless of vector magnitude
`cosine``inner_product``normalize_L2=True`