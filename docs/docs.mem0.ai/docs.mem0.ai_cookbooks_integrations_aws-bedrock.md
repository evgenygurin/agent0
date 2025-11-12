# Bedrock with Persistent Memory - Mem0
Source: https://docs.mem0.ai/cookbooks/integrations/aws-bedrock
Downloaded: 2025-11-12 21:20:21
================================================================================

`mem0ai`
## ​Installation
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#installation)
```
pip install "mem0ai[graph,extras]"

```

## ​Environment Setup
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#environment-setup)
```
import os

# Set these in your environment or notebook
os.environ['AWS_REGION'] = 'us-west-2'
os.environ['AWS_ACCESS_KEY_ID'] = 'AK00000000000000000'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'AS00000000000000000'

# Confirm they are set
print(os.environ['AWS_REGION'])
print(os.environ['AWS_ACCESS_KEY_ID'])
print(os.environ['AWS_SECRET_ACCESS_KEY'])

```

## ​Configuration and Usage
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#configuration-and-usage)- AWS Bedrock for LLM
[AWS Bedrock for LLM](https://docs.mem0.ai/components/llms/models/aws_bedrock)- AWS Bedrock for embeddings
[AWS Bedrock for embeddings](https://docs.mem0.ai/components/embedders/models/aws_bedrock#aws-bedrock)- OpenSearch as the vector store
[OpenSearch as the vector store](https://docs.mem0.ai/components/vectordbs/dbs/opensearch)- Graph Memory guide
[Graph Memory guide](https://docs.mem0.ai/open-source/features/graph-memory)
```
import boto3
from opensearchpy import RequestsHttpConnection, AWSV4SignerAuth
from mem0.memory.main import Memory

region = 'us-west-2'
service = 'aoss'
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region, service)

config = {
    "embedder": {
        "provider": "aws_bedrock",
        "config": {
            "model": "amazon.titan-embed-text-v2:0"
        }
    },
    "llm": {
        "provider": "aws_bedrock",
        "config": {
            "model": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
            "temperature": 0.1,
            "max_tokens": 2000
        }
    },
    "vector_store": {
        "provider": "opensearch",
        "config": {
            "collection_name": "mem0",
            "host": "your-opensearch-domain.us-west-2.es.amazonaws.com",
            "port": 443,
            "http_auth": auth,
            "connection_class": RequestsHttpConnection,
            "pool_maxsize": 20,
            "use_ssl": True,
            "verify_certs": True,
            "embedding_model_dims": 1024,
        }
    },
    "graph_store": {
        "provider": "neptune",
        "config": {
            "endpoint": f"neptune-graph://my-graph-identifier",
        },
    },
}

# Initialize the memory system
m = Memory.from_config(config)

```

## ​Usage
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#usage)[Notebook example](https://github.com/mem0ai/mem0/blob/main/examples/graph-db-demo/neptune-example.ipynb)
### ​Add a memory
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#add-a-memory)
```
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]

# Store inferred memories (default behavior)
result = m.add(messages, user_id="alice", metadata={"category": "movie_recommendations"})

```

### ​Search a memory
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#search-a-memory)
```
relevant_memories = m.search(query, user_id="alice")

```

### ​Get all memories
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#get-all-memories)
```
all_memories = m.get_all(user_id="alice")

```

### ​Get a specific memory
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#get-a-specific-memory)
```
memory = m.get(memory_id)

```

## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/integrations/aws-bedrock#conclusion)[Neptune Analytics with Mem0Explore graph-based memory storage with AWS Neptune Analytics.](https://docs.mem0.ai/cookbooks/integrations/neptune-analytics)
## Neptune Analytics with Mem0
[Graph Memory FeaturesLearn how to leverage knowledge graphs for entity relationships.](https://docs.mem0.ai/platform/features/graph-memory)
## Graph Memory Features
