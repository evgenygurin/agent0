# Pinecone - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/pinecone
Downloaded: 2025-11-12 21:20:19
================================================================================

[Pinecone](https://www.pinecone.io/)`namespace``embedding_model_dims`
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/pinecone#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"
os.environ["PINECONE_API_KEY"] = "your-api-key"

# Example using serverless configuration
config = {
    "vector_store": {
        "provider": "pinecone",
        "config": {
            "collection_name": "testing",
            "embedding_model_dims": 1536,  # Matches OpenAI's text-embedding-3-small
            "namespace": "my-namespace", # Optional: specify a namespace for multi-tenancy
            "serverless_config": {
                "cloud": "aws",  # Choose between 'aws' or 'gcp' or 'azure'
                "region": "us-east-1"
            },
            "metric": "cosine"
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
[​](https://docs.mem0.ai/components/vectordbs/dbs/pinecone#config)`collection_name``embedding_model_dims``client``None``api_key``PINECONE_API_KEY``environment``None``serverless_config``None``pod_config``None``hybrid_search``False``metric``"cosine"``batch_size``100``namespace``None``serverless_config``pod_config`
#### ​Serverless Config Example
[​](https://docs.mem0.ai/components/vectordbs/dbs/pinecone#serverless-config-example)
```
config = {
    "vector_store": {
        "provider": "pinecone",
        "config": {
            "collection_name": "memory_index",
            "embedding_model_dims": 1536,  # For OpenAI's text-embedding-3-small
            "namespace": "my-namespace",  # Optional: custom namespace
            "serverless_config": {
                "cloud": "aws",  # or "gcp" or "azure"
                "region": "us-east-1"  # Choose appropriate region
            }
        }
    }
}

```

#### ​Pod Config Example
[​](https://docs.mem0.ai/components/vectordbs/dbs/pinecone#pod-config-example)
```
config = {
    "vector_store": {
        "provider": "pinecone",
        "config": {
            "collection_name": "memory_index",
            "embedding_model_dims": 1536,  # For OpenAI's text-embedding-ada-002
            "namespace": "my-namespace",  # Optional: custom namespace
            "pod_config": {
                "environment": "gcp-starter",
                "replicas": 1,
                "pod_type": "starter"
            }
        }
    }
}

```
