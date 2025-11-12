# ReAct Agents with Memory - Mem0
Source: https://docs.mem0.ai/cookbooks/frameworks/llamaindex-react
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-react#overview)
## ​Setup
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-react#setup)
```
pip install llama-index-core llama-index-memory-mem0

```

```
import os
from llama_index.llms.openai import OpenAI

os.environ["OPENAI_API_KEY"] = "<your-openai-api-key>"
llm = OpenAI(model="gpt-4.1-nano-2025-04-14")

```
[here](https://app.mem0.ai/dashboard/api-keys)[Open Source](https://docs.mem0.ai/open-source/overview)
```
os.environ["MEM0_API_KEY"] = "<your-mem0-api-key>"

from llama_index.memory.mem0 import Mem0Memory

context = {"user_id": "david"}
memory_from_client = Mem0Memory.from_client(
    context=context,
    api_key=os.environ["MEM0_API_KEY"],
    search_msg_limit=4,  # optional, default is 5
)

```

```
from llama_index.core.tools import FunctionTool

def call_fn(name: str):
    """Call the provided name.
    Args:
        name: str (Name of the person)
    """
    return f"Calling... {name}"

def email_fn(name: str):
    """Email the provided name.
    Args:
        name: str (Name of the person)
    """
    return f"Emailing... {name}"

def order_food(name: str, dish: str):
    """Order food for the provided name.
    Args:
        name: str (Name of the person)
        dish: str (Name of the dish)
    """
    return f"Ordering {dish} for {name}"

call_tool = FunctionTool.from_defaults(fn=call_fn)
email_tool = FunctionTool.from_defaults(fn=email_fn)
order_food_tool = FunctionTool.from_defaults(fn=order_food)

```

```
from llama_index.core.agent import FunctionCallingAgent

agent = FunctionCallingAgent.from_tools(
    [call_tool, email_tool, order_food_tool],
    llm=llm,
    memory=memory_from_client,  # or memory_from_config
    verbose=True,
)

```

```
response = agent.chat("Hi, My name is David")
print(response)

```

```
> Running step bf44a75a-a920-4cf3-944e-b6e6b5695043. Step input: Hi, My name is David
Added user message to memory: Hi, My name is David
=== LLM Response ===
Hello, David! How can I assist you today?

```

```
response = agent.chat("I love to eat pizza on weekends")
print(response)

```

```
> Running step 845783b0-b85b-487c-baee-8460ebe8b38d. Step input: I love to eat pizza on weekends
Added user message to memory: I love to eat pizza on weekends
=== LLM Response ===
Pizza is a great choice for the weekend! If you'd like, I can help you order some. Just let me know what kind of pizza you prefer!

```

```
response = agent.chat("My preferred way of communication is email")
print(response)

```

```
> Running step 345842f0-f8a0-42ea-a1b7-612265d72a92. Step input: My preferred way of communication is email
Added user message to memory: My preferred way of communication is email
=== LLM Response ===
Got it! If you need any assistance or have any requests, feel free to let me know, and I can communicate with you via email.

```

## ​Using the Agent Without Memory
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-react#using-the-agent-without-memory)
```
agent = FunctionCallingAgent.from_tools(
    [call_tool, email_tool, order_food_tool],
    # memory is not provided
    llm=llm,
    verbose=True,
)
response = agent.chat("I am feeling hungry, order me something and send me the bill")
print(response)

```

```
> Running step e89eb75d-75e1-4dea-a8c8-5c3d4b77882d. Step input: I am feeling hungry, order me something and send me the bill
Added user message to memory: I am feeling hungry, order me something and send me the bill
=== LLM Response ===
Please let me know your name and the dish you'd like to order, and I'll take care of it for you!

```

## ​Using the Agent With Memory
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-react#using-the-agent-with-memory)
```
agent = FunctionCallingAgent.from_tools(
    [call_tool, email_tool, order_food_tool],
    llm=llm,
    # memory is provided
    memory=memory_from_client,  # or memory_from_config
    verbose=True,
)
response = agent.chat("I am feeling hungry, order me something and send me the bill")
print(response)

```

```
> Running step 5e473db9-3973-4cb1-a5fd-860be0ab0006. Step input: I am feeling hungry, order me something and send me the bill
Added user message to memory: I am feeling hungry, order me something and send me the bill
=== Calling Function ===
Calling function: order_food with args: {"name": "David", "dish": "pizza"}
=== Function Output ===
Ordering pizza for David
=== Calling Function ===
Calling function: email_fn with args: {"name": "David"}
=== Function Output ===
Emailing... David
> Running step 38080544-6b37-4bb2-aab2-7670100d926e. Step input: None
=== LLM Response ===
I've ordered a pizza for you, and the bill has been sent to your email. Enjoy your meal! If there's anything else you need, feel free to let me know.

```
[LlamaIndex Multiagent with Mem0Scale to multi-agent workflows with shared memory coordination.](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent)
## LlamaIndex Multiagent with Mem0
[Build a Mem0 CompanionMaster the core patterns for memory-powered agents across frameworks.](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion)
## Build a Mem0 Companion
