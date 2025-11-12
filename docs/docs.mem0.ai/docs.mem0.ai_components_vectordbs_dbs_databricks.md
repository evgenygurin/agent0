# Databricks - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/databricks
Downloaded: 2025-11-12 21:20:20
================================================================================

[Databricks Vector Search](https://docs.databricks.com/en/generative-ai/vector-search.html)
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#usage)
```
import os
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "databricks",
        "config": {
            "workspace_url": "https://your-workspace.databricks.com",
            "access_token": "your-access-token",
            "endpoint_name": "your-vector-search-endpoint",
            "index_name": "catalog.schema.index_name",
            "source_table_name": "catalog.schema.source_table",
            "embedding_dimension": 1536
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
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#config)`workspace_url``access_token``None``service_principal_client_id``None``service_principal_client_secret``None``endpoint_name``index_name``source_table_name``embedding_dimension``1536``embedding_source_column``None``embedding_model_endpoint_name``None``embedding_vector_column``embedding``endpoint_type``STANDARD``STORAGE_OPTIMIZED``STANDARD``sync_computed_embeddings``True`
### ​Authentication
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#authentication)
#### ​Service Principal (Recommended for Production)
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#service-principal-recommended-for-production)
```
config = {
    "vector_store": {
        "provider": "databricks",
        "config": {
            "workspace_url": "https://your-workspace.databricks.com",
            "service_principal_client_id": "your-service-principal-id",
            "service_principal_client_secret": "your-service-principal-secret",
            "endpoint_name": "your-endpoint",
            "index_name": "catalog.schema.index_name",
            "source_table_name": "catalog.schema.source_table"
        }
    }
}

```

#### ​Personal Access Token (for Development)
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#personal-access-token-for-development)
```
config = {
    "vector_store": {
        "provider": "databricks",
        "config": {
            "workspace_url": "https://your-workspace.databricks.com",
            "access_token": "your-personal-access-token",
            "endpoint_name": "your-endpoint",
            "index_name": "catalog.schema.index_name",
            "source_table_name": "catalog.schema.source_table"
        }
    }
}

```

### ​Embedding Options
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#embedding-options)
#### ​Self-Managed Embeddings (Default)
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#self-managed-embeddings-default)
```
config = {
    "vector_store": {
        "provider": "databricks",
        "config": {
            # ... authentication config ...
            "embedding_dimension": 768,  # Match your embedding model
            "embedding_vector_column": "embedding"
        }
    }
}

```

#### ​Databricks-Computed Embeddings
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#databricks-computed-embeddings)
```
config = {
    "vector_store": {
        "provider": "databricks",
        "config": {
            # ... authentication config ...
            "embedding_source_column": "text",
            "embedding_model_endpoint_name": "e5-small-v2"
        }
    }
}

```

### ​Important Notes
[​](https://docs.mem0.ai/components/vectordbs/dbs/databricks#important-notes)- Delta Sync Index: This implementation uses Delta Sync Index, which automatically syncs with your source Delta table. Direct vector insertion/deletion/update operations will log warnings as they’re not supported with Delta Sync.
- Unity Catalog: Both the source table and index must be in Unity Catalog format (catalog.schema.table_name).
`catalog.schema.table_name`- Endpoint Auto-Creation: If the specified endpoint doesn’t exist, it will be created automatically.
- Index Auto-Creation: If the specified index doesn’t exist, it will be created automatically with the provided configuration.
- Filter Support: Supports filtering by metadata fields, with different syntax for STANDARD vs STORAGE_OPTIMIZED endpoints.
