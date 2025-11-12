# Vertexai - Mem0
Source: https://docs.mem0.ai/components/embedders/models/vertexai
Downloaded: 2025-11-12 21:20:20
================================================================================


### ​Vertex AI
[​](https://docs.mem0.ai/components/embedders/models/vertexai#vertex-ai)`GOOGLE_APPLICATION_CREDENTIALS`[Google Cloud Console](https://console.cloud.google.com/)
### ​Usage
[​](https://docs.mem0.ai/components/embedders/models/vertexai#usage)
```
import os
from mem0 import Memory

# Set the path to your Google Cloud credentials JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/credentials.json"
os.environ["OPENAI_API_KEY"] = "your_api_key" # For LLM

config = {
    "embedder": {
        "provider": "vertexai",
        "config": {
            "model": "text-embedding-004",
            "memory_add_embedding_type": "RETRIEVAL_DOCUMENT",
            "memory_update_embedding_type": "RETRIEVAL_DOCUMENT",
            "memory_search_embedding_type": "RETRIEVAL_QUERY"
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
m.add(messages, user_id="john")

```
- SEMANTIC_SIMILARITY
- CLASSIFICATION
- CLUSTERING
- RETRIEVAL_DOCUMENT, RETRIEVAL_QUERY, QUESTION_ANSWERING, FACT_VERIFICATION
- CODE_RETRIEVAL_QUERYCheck out theVertex AI documentationfor more information.
[Vertex AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/task-types#supported_task_types)
### ​Config
[​](https://docs.mem0.ai/components/embedders/models/vertexai#config)`model``text-embedding-004``vertex_credentials_json``None``embedding_dims``256``memory_add_embedding_type``RETRIEVAL_DOCUMENT``memory_update_embedding_type``RETRIEVAL_DOCUMENT``memory_search_embedding_type``RETRIEVAL_QUERY`