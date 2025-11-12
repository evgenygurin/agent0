# Opensearch - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/opensearch
Downloaded: 2025-11-12 21:20:20
================================================================================

[OpenSearch](https://opensearch.org/)
### ​Installation
[​](https://docs.mem0.ai/components/vectordbs/dbs/opensearch#installation)
```
pip install opensearch-py

```

### ​Prerequisites
[​](https://docs.mem0.ai/components/vectordbs/dbs/opensearch#prerequisites)
#### ​AWS OpenSearch Service
[​](https://docs.mem0.ai/components/vectordbs/dbs/opensearch#aws-opensearch-service)- Navigate toOpenSearch Service Console
[OpenSearch Service Console](https://console.aws.amazon.com/aos/home)- Click “Create collection”
- Select “Serverless collection” and then enable “Vector search” capabilities
- Once created, note the endpoint URL (host) for your configuration

### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/opensearch#usage)
```
import os
from mem0 import Memory
import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

# For AWS OpenSearch Service with IAM authentication
region = 'us-west-2'
service = 'aoss'
credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region, service)

config = {
    "vector_store": {
        "provider": "opensearch",
        "config": {
            "collection_name": "mem0",
            "host": "your-domain.us-west-2.aoss.amazonaws.com",
            "port": 443,
            "http_auth": auth,
            "embedding_model_dims": 1024,
            "connection_class": RequestsHttpConnection,
            "pool_maxsize": 20,
            "use_ssl": True,
            "verify_certs": True
        }
    }
}

```

### ​Add Memories
[​](https://docs.mem0.ai/components/vectordbs/dbs/opensearch#add-memories)
```
m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```

### ​Search Memories
[​](https://docs.mem0.ai/components/vectordbs/dbs/opensearch#search-memories)
```
results = m.search("What kind of movies does Alice like?", user_id="alice")

```

### ​Features
[​](https://docs.mem0.ai/components/vectordbs/dbs/opensearch#features)- Fast and Efficient Vector Search
- Can be deployed on-premises, in containers, or on cloud platforms like AWS OpenSearch Service
- Multiple authentication and security methods (Basic Authentication, API Keys, LDAP, SAML, and OpenID Connect)
- Automatic index creation with optimized mappings for vector search
- Memory optimization through disk-based vector search and quantization
- Real-time analytics and observability
