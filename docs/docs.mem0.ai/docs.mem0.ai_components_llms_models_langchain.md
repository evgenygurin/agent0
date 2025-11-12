# LangChain - Mem0
Source: https://docs.mem0.ai/components/llms/models/langchain
Downloaded: 2025-11-12 21:20:19
================================================================================

[LangChain Chat Models documentation](https://python.langchain.com/docs/integrations/chat)
## ​Usage
[​](https://docs.mem0.ai/components/llms/models/langchain#usage)
```
import os
from mem0 import Memory
from langchain_openai import ChatOpenAI

# Set necessary environment variables for your chosen LangChain provider
os.environ["OPENAI_API_KEY"] = "your-api-key"

# Initialize a LangChain model directly
openai_model = ChatOpenAI(
    model="gpt-4.1-nano-2025-04-14",
    temperature=0.2,
    max_tokens=2000
)

# Pass the initialized model to the config
config = {
    "llm": {
        "provider": "langchain",
        "config": {
            "model": openai_model
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

## ​Supported LangChain Providers
[​](https://docs.mem0.ai/components/llms/models/langchain#supported-langchain-providers)- OpenAI (ChatOpenAI)
`ChatOpenAI`- Anthropic (ChatAnthropic)
`ChatAnthropic`- Google (ChatGoogleGenerativeAI,ChatGooglePalm)
`ChatGoogleGenerativeAI``ChatGooglePalm`- Mistral (ChatMistralAI)
`ChatMistralAI`- Ollama (ChatOllama)
`ChatOllama`- Azure OpenAI (AzureChatOpenAI)
`AzureChatOpenAI`- HuggingFace (HuggingFaceChatEndpoint)
`HuggingFaceChatEndpoint`- And many more
[LangChain Chat Models documentation](https://python.langchain.com/docs/integrations/chat)
## ​Provider-Specific Configuration
[​](https://docs.mem0.ai/components/llms/models/langchain#provider-specific-configuration)- Set the appropriate environment variables for your chosen LLM provider
- Import and initialize the specific model class you want to use
- Pass the initialized model instance to the config

## ​Config
[​](https://docs.mem0.ai/components/llms/models/langchain#config)`langchain`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)