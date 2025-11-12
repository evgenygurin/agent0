# Azure OpenAI - Mem0
Source: https://docs.mem0.ai/components/llms/models/azure_openai_structured
Downloaded: 2025-11-12 21:20:20
================================================================================

`LLM_AZURE_OPENAI_API_KEY``LLM_AZURE_ENDPOINT``LLM_AZURE_DEPLOYMENT``LLM_AZURE_API_VERSION`[Azure](https://azure.microsoft.com/)`LLM_AZURE_OPENAI_API_KEY``Parallel tool calling``temperature``top_p``presence_penalty``frequency_penalty``logprobs``top_logprobs``logit_bias``max_tokens`
## ​Usage
[​](https://docs.mem0.ai/components/llms/models/azure_openai_structured#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key" # used for embedding model

os.environ["LLM_AZURE_OPENAI_API_KEY"] = "your-api-key"
os.environ["LLM_AZURE_DEPLOYMENT"] = "your-deployment-name"
os.environ["LLM_AZURE_ENDPOINT"] = "your-api-base-url"
os.environ["LLM_AZURE_API_VERSION"] = "version-to-use"

config = {
    "llm": {
        "provider": "azure_openai",
        "config": {
            "model": "your-deployment-name",
            "temperature": 0.1,
            "max_tokens": 2000,
            "azure_kwargs": {
                  "azure_deployment": "",
                  "api_version": "",
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
m.add(messages, user_id="alice", metadata={"category": "movies"})

```
[OpenAI structured-outputs](https://platform.openai.com/docs/guides/structured-outputs/introduction)`azure_openai_structured`
```
import os
from mem0 import Memory

os.environ["LLM_AZURE_OPENAI_API_KEY"] = "your-api-key"
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
                  "azure_deployment": "",
                  "api_version": "",
                  "azure_endpoint": "",
                  "api_key": "",
                  "default_headers": {
                    "CustomHeader": "your-custom-header",
                  }
              }
        }
    }
}

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
## ​Config
[​](https://docs.mem0.ai/components/llms/models/azure_openai_structured#config)`azure_openai`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)