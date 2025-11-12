# Amazon S3 Vectors - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/s3_vectors
Downloaded: 2025-11-12 21:20:20
================================================================================

[Amazon S3 Vectors](https://aws.amazon.com/s3/features/vectors/)
### ​Installation
[​](https://docs.mem0.ai/components/vectordbs/dbs/s3_vectors#installation)
```
pip install boto3

```

### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/s3_vectors#usage)`s3vectors:*``~/.aws/credentials`
```
import os
from mem0 import Memory

# Ensure your AWS credentials are configured in your environment
# e.g., by setting AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_DEFAULT_REGION

config = {
    "vector_store": {
        "provider": "s3_vectors",
        "config": {
            "vector_bucket_name": "my-mem0-vector-bucket",
            "collection_name": "my-memories-index",
            "embedding_model_dims": 1536,
            "distance_metric": "cosine",
            "region_name": "us-east-1"
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
[​](https://docs.mem0.ai/components/vectordbs/dbs/s3_vectors#config)`vector_bucket_name``collection_name``mem0``embedding_model_dims``1536``distance_metric``cosine``euclidean``cosine``region_name``None`
### ​IAM Permissions
[​](https://docs.mem0.ai/components/vectordbs/dbs/s3_vectors#iam-permissions)
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3vectors:*",
      "Resource": "*"
    }
  ]
}

```
