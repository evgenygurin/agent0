# Azure OpenAI - Mem0
Source: https://docs.mem0.ai/components/embedders/models/azure_openai
Downloaded: 2025-11-12 21:20:20
================================================================================

`EMBEDDING_AZURE_OPENAI_API_KEY``EMBEDDING_AZURE_DEPLOYMENT``EMBEDDING_AZURE_ENDPOINT``EMBEDDING_AZURE_API_VERSION`
### ​Usage
[​](https://docs.mem0.ai/components/embedders/models/azure_openai#usage)
```
import os
from mem0 import Memory

os.environ["EMBEDDING_AZURE_OPENAI_API_KEY"] = "your-api-key"
os.environ["EMBEDDING_AZURE_DEPLOYMENT"] = "your-deployment-name"
os.environ["EMBEDDING_AZURE_ENDPOINT"] = "your-api-base-url"
os.environ["EMBEDDING_AZURE_API_VERSION"] = "version-to-use"

os.environ["OPENAI_API_KEY"] = "your_api_key" # For LLM


config = {
    "embedder": {
        "provider": "azure_openai",
        "config": {
            "model": "text-embedding-3-large",
            "azure_kwargs": {
                  "api_version": "",
                  "azure_deployment": "",
                  "azure_endpoint": "",
                  "api_key": "",
                  "default_headers": {
                    "CustomHeader": "your-custom-header",
                  }
              }
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
[Azure OpenAI role-based security](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/role-based-access-control)
```
import os
from mem0 import Memory
# You can set the values directly in the config dictionary or use environment variables

os.environ["LLM_AZURE_DEPLOYMENT"] = "your-deployment-name"
os.environ["LLM_AZURE_ENDPOINT"] = "your-api-base-url"
os.environ["LLM_AZURE_API_VERSION"] = "version-to-use"

config = {
    "llm": {
        "provider": "azure_openai_structured",
        "config": {
            "model": "your-deployment-name",
            "temperature": 0.1,
            "max_tokens": 2000,
            "azure_kwargs": {
                  "azure_deployment": "<your-deployment-name>",
                  "api_version": "<version-to-use>",
                  "azure_endpoint": "<your-api-base-url>",
                  "default_headers": {
                    "CustomHeader": "your-custom-header",
                  }
              }
        }
    }
}

```
[Azure Identity troubleshooting tips](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/identity/azure-identity/TROUBLESHOOTING.md#troubleshoot-environmentcredential-authentication-issues)
### ​Config
[​](https://docs.mem0.ai/components/embedders/models/azure_openai#config)- Python
- TypeScript
`model``text-embedding-3-small``embedding_dims``1536``azure_kwargs``config_keys`