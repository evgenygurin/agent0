# LangChain - Mem0
Source: https://docs.mem0.ai/components/embedders/models/langchain
Downloaded: 2025-11-12 21:20:20
================================================================================

[LangChain Text Embedding documentation](https://python.langchain.com/docs/integrations/text_embedding/)
## ​Usage
[​](https://docs.mem0.ai/components/embedders/models/langchain#usage)
```
import os
from mem0 import Memory
from langchain_openai import OpenAIEmbeddings

# Set necessary environment variables for your chosen LangChain provider
os.environ["OPENAI_API_KEY"] = "your-api-key"

# Initialize a LangChain embeddings model directly
openai_embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=1536
)

# Pass the initialized model to the config
config = {
    "embedder": {
        "provider": "langchain",
        "config": {
            "model": openai_embeddings
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

## ​Supported LangChain Embedding Providers
[​](https://docs.mem0.ai/components/embedders/models/langchain#supported-langchain-embedding-providers)- OpenAI (OpenAIEmbeddings)
`OpenAIEmbeddings`- Cohere (CohereEmbeddings)
`CohereEmbeddings`- Google (VertexAIEmbeddings)
`VertexAIEmbeddings`- Hugging Face (HuggingFaceEmbeddings)
`HuggingFaceEmbeddings`- Sentence Transformers (HuggingFaceEmbeddings)
`HuggingFaceEmbeddings`- Azure OpenAI (AzureOpenAIEmbeddings)
`AzureOpenAIEmbeddings`- Ollama (OllamaEmbeddings)
`OllamaEmbeddings`- Together (TogetherEmbeddings)
`TogetherEmbeddings`- And many more
[LangChain Text Embedding documentation](https://python.langchain.com/docs/integrations/text_embedding/)
## ​Provider-Specific Configuration
[​](https://docs.mem0.ai/components/embedders/models/langchain#provider-specific-configuration)- Set the appropriate environment variables for your chosen embedding provider
- Import and initialize the specific model class you want to use
- Pass the initialized model instance to the config

### ​Examples with Different Providers
[​](https://docs.mem0.ai/components/embedders/models/langchain#examples-with-different-providers)
```
HuggingFace Embeddings
```

```
Ollama Embeddings
```

## ​Config
[​](https://docs.mem0.ai/components/embedders/models/langchain#config)`langchain`[Master List of All Params in Config](https://docs.mem0.ai/components/embedders/config)