# AutoGen - Mem0
Source: https://docs.mem0.ai/integrations/autogen
Downloaded: 2025-11-12 21:20:20
================================================================================


## ​Overview
[​](https://docs.mem0.ai/integrations/autogen#overview)
## ​Setup and Configuration
[​](https://docs.mem0.ai/integrations/autogen#setup-and-configuration)
```
pip install autogen mem0ai openai python-dotenv

```
[Mem0 Platform](https://app.mem0.ai)
```
import os
from autogen import ConversableAgent
from mem0 import MemoryClient
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuration
# OPENAI_API_KEY = 'sk-xxx'  # Replace with your actual OpenAI API key
# MEM0_API_KEY = 'your-mem0-key'  # Replace with your actual Mem0 API key from https://app.mem0.ai
USER_ID = "alice"

# Set up OpenAI API key
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
# os.environ['MEM0_API_KEY'] = MEM0_API_KEY

# Initialize Mem0 and AutoGen agents
memory_client = MemoryClient()
agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": OPENAI_API_KEY}]},
    code_execution_config=False,
    human_input_mode="NEVER",
)

```

## ​Storing Conversations in Memory
[​](https://docs.mem0.ai/integrations/autogen#storing-conversations-in-memory)
```
conversation = [
    {"role": "assistant", "content": "Hi, I'm Best Buy's chatbot! How can I help you?"},
    {"role": "user", "content": "I'm seeing horizontal lines on my TV."},
    {"role": "assistant", "content": "I'm sorry to hear that. Can you provide your TV model?"},
    {"role": "user", "content": "It's a Sony - 77\" Class BRAVIA XR A80K OLED 4K UHD Smart Google TV"},
    {"role": "assistant", "content": "Thank you for the information. Let's troubleshoot this issue..."}
]

memory_client.add(messages=conversation, user_id=USER_ID)
print("Conversation added to memory.")

```

## ​Retrieving and Using Memory
[​](https://docs.mem0.ai/integrations/autogen#retrieving-and-using-memory)
```
def get_context_aware_response(question):
    relevant_memories = memory_client.search(question, user_id=USER_ID)
    context = "\n".join([m["memory"] for m in relevant_memories.get('results', [])])

    prompt = f"""Answer the user question considering the previous interactions:
    Previous interactions:
    {context}

    Question: {question}
    """

    reply = agent.generate_reply(messages=[{"content": prompt, "role": "user"}])
    return reply

# Example usage
question = "What was the issue with my TV?"
answer = get_context_aware_response(question)
print("Context-aware answer:", answer)

```

## ​Multi-Agent Conversation
[​](https://docs.mem0.ai/integrations/autogen#multi-agent-conversation)
```
manager = ConversableAgent(
    "manager",
    system_message="You are a manager who helps in resolving complex customer issues.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": OPENAI_API_KEY}]},
    human_input_mode="NEVER"
)

def escalate_to_manager(question):
    relevant_memories = memory_client.search(question, user_id=USER_ID)
    context = "\n".join([m["memory"] for m in relevant_memories.get('results', [])])

    prompt = f"""
    Context from previous interactions:
    {context}

    Customer question: {question}

    As a manager, how would you address this issue?
    """

    manager_response = manager.generate_reply(messages=[{"content": prompt, "role": "user"}])
    return manager_response

# Example usage
complex_question = "I'm not satisfied with the troubleshooting steps. What else can be done?"
manager_answer = escalate_to_manager(complex_question)
print("Manager's response:", manager_answer)

```

## ​Conclusion
[​](https://docs.mem0.ai/integrations/autogen#conclusion)[CrewAI IntegrationBuild multi-agent systems with CrewAI and Mem0](https://docs.mem0.ai/integrations/crewai)
## CrewAI Integration
[LangGraph IntegrationCreate stateful workflows with LangGraph](https://docs.mem0.ai/integrations/langgraph)
## LangGraph Integration
