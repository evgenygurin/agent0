# LangChain - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/langchain
Downloaded: 2025-11-12 21:20:20
================================================================================


## ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/langchain#usage)
```
import os
from mem0 import Memory
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Initialize a LangChain vector store
embeddings = OpenAIEmbeddings()
vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings,
    collection_name="mem0"  # Required collection name
)

# Pass the initialized vector store to the config
config = {
    "vector_store": {
        "provider": "langchain",
        "config": {
            "client": vector_store
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

## ​Supported LangChain Vector Stores
[​](https://docs.mem0.ai/components/vectordbs/dbs/langchain#supported-langchain-vector-stores)- Chroma
- FAISS
- Pinecone
- Weaviate
- Milvus
- Qdrant
- And many more
[LangChain Vector Stores documentation](https://python.langchain.com/docs/integrations/vectorstores)
## ​Limitations
[​](https://docs.mem0.ai/components/vectordbs/dbs/langchain#limitations)- Bulk Operations: Theget_allanddelete_alloperations are not supported when using LangChain as the vector store provider. This is because LangChain’s vector store interface doesn’t provide standardized methods for these bulk operations across all providers.
`get_all``delete_all`- Provider-Specific Features: Some advanced features may not be available depending on the specific vector store implementation you’re using through LangChain.

## ​Provider-Specific Configuration
[​](https://docs.mem0.ai/components/vectordbs/dbs/langchain#provider-specific-configuration)- Set the appropriate environment variables for your chosen vector store provider
- Import and initialize the specific vector store class you want to use
- Pass the initialized vector store instance to the config

## ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/langchain#config)`langchain`[Master List of All Params in Config](https://docs.mem0.ai/components/vectordbs/config)