# Self-Hosted AI Companion - Mem0
Source: https://docs.mem0.ai/cookbooks/companions/local-companion-ollama
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama#overview)
## ​Setup
[​](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama#setup)
## ​Full Code Example
[​](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama#full-code-example)
```
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "test",
            "host": "localhost",
            "port": 6333,
            "embedding_model_dims": 768,  # Change this according to your local model's dimensions
        },
    },
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "llama3.1:latest",
            "temperature": 0,
            "max_tokens": 2000,
            "ollama_base_url": "http://localhost:11434",  # Ensure this URL is correct
        },
    },
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text:latest",
            # Alternatively, you can use "snowflake-arctic-embed:latest"
            "ollama_base_url": "http://localhost:11434",
        },
    },
}

# Initialize Memory with the configuration
m = Memory.from_config(config)

# Add a memory
m.add("I'm visiting Paris", user_id="john")

# Retrieve memories
memories = m.get_all(user_id="john")

```

## ​Key Points
[​](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama#key-points)- Configuration: The setup involves configuring the vector store, language model, and embedding model to use local resources
- Vector Store: Qdrant is used as the vector store, running on localhost
- Language Model: Ollama is used as the LLM provider, with thellama3.1:latestmodel
`llama3.1:latest`- Embedding Model: Ollama is also used for embeddings, with thenomic-embed-text:latestmodel
`nomic-embed-text:latest`
## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama#conclusion)[Configure Open SourceExplore advanced configuration options for vector stores, LLMs, and embedders.](https://docs.mem0.ai/open-source/configuration)
## Configure Open Source
[Build a Mem0 CompanionLearn core companion patterns that work with any LLM provider.](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion)
## Build a Mem0 Companion
