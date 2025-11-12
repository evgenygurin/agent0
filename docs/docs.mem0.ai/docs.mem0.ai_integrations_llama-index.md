# LlamaIndex - Mem0
Source: https://docs.mem0.ai/integrations/llama-index
Downloaded: 2025-11-12 21:20:20
================================================================================

[memory store](https://llamahub.ai/l/memory/llama-index-memory-mem0)[Mem0Memory](https://docs.llamaindex.ai/en/stable/examples/memory/Mem0Memory/)
### ​Installation
[​](https://docs.mem0.ai/integrations/llama-index#installation)
```
pip install llama-index-core llama-index-memory-mem0 python-dotenv

```

### ​Setup with Mem0 Platform
[​](https://docs.mem0.ai/integrations/llama-index#setup-with-mem0-platform)`<your-mem0-api-key>`[Mem0 Platform](https://app.mem0.ai/login)
```
from dotenv import load_dotenv
import os

load_dotenv()

# os.environ["MEM0_API_KEY"] = "<your-mem0-api-key>"

```

```
from llama_index.memory.mem0 import Mem0Memory

context = {"user_id": "alice"}
memory_from_client = Mem0Memory.from_client(
    context=context,
    search_msg_limit=4,  # optional, default is 5
)

```
`Mem0Memory`
```
context = {
    "user_id": "alice", 
    "agent_id": "llama_agent_1",
    "run_id": "run_1",
}

```
`search_msg_limit``search_msg_limit``limit``limit`
### ​Setup with Mem0 OSS
[​](https://docs.mem0.ai/integrations/llama-index#setup-with-mem0-oss)[Mem0 OSS Quickstart](https://docs.mem0.ai/open-source/overview)
```
config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "test_9",
            "host": "localhost",
            "port": 6333,
            "embedding_model_dims": 1536,  # Change this according to your local model's dimensions
        },
    },
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4.1-nano-2025-04-14",
            "temperature": 0.2,
            "max_tokens": 2000,
        },
    },
    "embedder": {
        "provider": "openai",
        "config": {"model": "text-embedding-3-small"},
    },
    "version": "v1.1",
}

```

```
memory_from_config = Mem0Memory.from_config(
    context=context,
    config=config,
    search_msg_limit=4,  # optional, default is 5
    # Remove deprecation warnings
)

```

```
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_KEY"] = "<your-openai-api-key>"
llm = OpenAI(model="gpt-4.1-nano-2025-04-14")

```

### ​SimpleChatEngine
[​](https://docs.mem0.ai/integrations/llama-index#simplechatengine)`SimpleChatEngine`
```
from llama_index.core.chat_engine import SimpleChatEngine

agent = SimpleChatEngine.from_defaults(
    llm=llm, memory=memory_from_client  # or memory_from_config
)

# Start the chat
response = agent.chat("Hi, My name is Alice")
print(response)

```

```
from llama_index.core.tools import FunctionTool


def call_fn(name: str):
    """Call the provided name.
    Args:
        name: str (Name of the person)
    """
    print(f"Calling... {name}")


def email_fn(name: str):
    """Email the provided name.
    Args:
        name: str (Name of the person)
    """
    print(f"Emailing... {name}")


call_tool = FunctionTool.from_defaults(fn=call_fn)
email_tool = FunctionTool.from_defaults(fn=email_fn)

```

### ​FunctionCallingAgent
[​](https://docs.mem0.ai/integrations/llama-index#functioncallingagent)
```
from llama_index.core.agent import FunctionCallingAgent

agent = FunctionCallingAgent.from_tools(
    [call_tool, email_tool],
    llm=llm,
    memory=memory_from_client,  # or memory_from_config
    verbose=True,
)

# Start the chat
response = agent.chat("Hi, My name is Alice")
print(response)

```

### ​ReActAgent
[​](https://docs.mem0.ai/integrations/llama-index#reactagent)
```
from llama_index.core.agent import ReActAgent

agent = ReActAgent.from_tools(
    [call_tool, email_tool],
    llm=llm,
    memory=memory_from_client,  # or memory_from_config
    verbose=True,
)

# Start the chat
response = agent.chat("Hi, My name is Alice")
print(response)

```

## ​Key Features
[​](https://docs.mem0.ai/integrations/llama-index#key-features)- Memory Integration: Uses Mem0 to store and retrieve relevant information from past interactions.
- Personalization: Provides context-aware agent responses based on user history and preferences.
- Flexible Architecture: LlamaIndex allows for easy integration of the memory with the agent.
- Continuous Learning: Each interaction is stored, improving future responses.

## ​Conclusion
[​](https://docs.mem0.ai/integrations/llama-index#conclusion)[LlamaIndex Multiagent CookbookBuild multi-agent systems with LlamaIndex and Mem0](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent)
## LlamaIndex Multiagent Cookbook
[LlamaIndex ReAct CookbookCreate ReAct agents with LlamaIndex](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-react)
## LlamaIndex ReAct Cookbook
