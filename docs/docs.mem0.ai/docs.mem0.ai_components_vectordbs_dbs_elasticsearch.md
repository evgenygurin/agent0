# Elasticsearch - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/elasticsearch
Downloaded: 2025-11-12 21:20:20
================================================================================

[Elasticsearch](https://www.elastic.co/)
### ​Installation
[​](https://docs.mem0.ai/components/vectordbs/dbs/elasticsearch#installation)
```
pip install elasticsearch>=8.0.0

```

### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/elasticsearch#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "elasticsearch",
        "config": {
            "collection_name": "mem0",
            "host": "localhost",
            "port": 9200,
            "embedding_model_dims": 1536
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
[​](https://docs.mem0.ai/components/vectordbs/dbs/elasticsearch#config)`collection_name``mem0``embedding_model_dims``1536``host``localhost``port``9200``cloud_id``None``api_key``None``user``None``password``None``verify_certs``True``auto_create_index``True``custom_search_query``None``headers``None`
### ​Features
[​](https://docs.mem0.ai/components/vectordbs/dbs/elasticsearch#features)- Efficient vector search using Elasticsearch’s native k-NN search
- Support for both local and cloud deployments (Elastic Cloud)
- Multiple authentication methods (Basic Auth, API Key)
- Automatic index creation with optimized mappings for vector search
- Memory isolation through payload filtering
- Custom search query function to customize the search query

### ​Custom Search Query
[​](https://docs.mem0.ai/components/vectordbs/dbs/elasticsearch#custom-search-query)`custom_search_query``Memory.search`
```
import os
from typing import List, Optional, Dict
from mem0 import Memory

def custom_search_query(query: List[float], limit: int, filters: Optional[Dict]) -> Dict:
    return {
        "knn": {
            "field": "vector", 
            "query_vector": query, 
            "k": limit, 
            "num_candidates": limit * 2
        }
    }

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "elasticsearch",
        "config": {
            "collection_name": "mem0",
            "host": "localhost",
            "port": 9200,
            "embedding_model_dims": 1536,
            "custom_search_query": custom_search_query
        }
    }
}

```
- query: a query vector used inMemory.search
`query``Memory.search`- limit: a number of results used inMemory.search
`limit``Memory.search`- filters: a dictionary of key-value pairs used inMemory.search. You can add custom pairs for the custom search query.
`filters``Memory.search`