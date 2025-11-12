# LangGraph - Mem0
Source: https://docs.mem0.ai/integrations/langgraph
Downloaded: 2025-11-12 21:20:20
================================================================================


## ​Overview
[​](https://docs.mem0.ai/integrations/langgraph#overview)- Uses LangGraph to manage conversation flow
- Leverages Mem0 to store and retrieve relevant information from past interactions
- Provides personalized responses based on user history

## ​Setup and Configuration
[​](https://docs.mem0.ai/integrations/langgraph#setup-and-configuration)
```
pip install langgraph langchain-openai mem0ai python-dotenv

```
[Mem0 Platform](https://app.mem0.ai)
```
from typing import Annotated, TypedDict, List
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from mem0 import MemoryClient
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Configuration
# OPENAI_API_KEY = 'sk-xxx'  # Replace with your actual OpenAI API key
# MEM0_API_KEY = 'your-mem0-key'  # Replace with your actual Mem0 API key

# Initialize LangChain and Mem0
llm = ChatOpenAI(model="gpt-4")
mem0 = MemoryClient()

```

## ​Define State and Graph
[​](https://docs.mem0.ai/integrations/langgraph#define-state-and-graph)
```
class State(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], add_messages]
    mem0_user_id: str

graph = StateGraph(State)

```

## ​Create Chatbot Function
[​](https://docs.mem0.ai/integrations/langgraph#create-chatbot-function)
```
def chatbot(state: State):
    messages = state["messages"]
    user_id = state["mem0_user_id"]

    try:
        # Retrieve relevant memories
        memories = mem0.search(messages[-1].content, user_id=user_id)
        
        # Handle dict response format
        memory_list = memories['results']

        context = "Relevant information from previous conversations:\n"
        for memory in memory_list:
            context += f"- {memory['memory']}\n"

        system_message = SystemMessage(content=f"""You are a helpful customer support assistant. Use the provided context to personalize your responses and remember user preferences and past interactions.
{context}""")

        full_messages = [system_message] + messages
        response = llm.invoke(full_messages)

        # Store the interaction in Mem0
        try:
            interaction = [
                {
                    "role": "user",
                    "content": messages[-1].content
                },
                {
                    "role": "assistant", 
                    "content": response.content
                }
            ]
            result = mem0.add(interaction, user_id=user_id)
            print(f"Memory saved: {len(result.get('results', []))} memories added")
        except Exception as e:
            print(f"Error saving memory: {e}")
            
        return {"messages": [response]}
        
    except Exception as e:
        print(f"Error in chatbot: {e}")
        # Fallback response without memory context
        response = llm.invoke(messages)
        return {"messages": [response]}

```

## ​Set Up Graph Structure
[​](https://docs.mem0.ai/integrations/langgraph#set-up-graph-structure)
```
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", "chatbot")

compiled_graph = graph.compile()

```

## ​Create Conversation Runner
[​](https://docs.mem0.ai/integrations/langgraph#create-conversation-runner)
```
def run_conversation(user_input: str, mem0_user_id: str):
    config = {"configurable": {"thread_id": mem0_user_id}}
    state = {"messages": [HumanMessage(content=user_input)], "mem0_user_id": mem0_user_id}

    for event in compiled_graph.stream(state, config):
        for value in event.values():
            if value.get("messages"):
                print("Customer Support:", value["messages"][-1].content)
                return

```

## ​Main Interaction Loop
[​](https://docs.mem0.ai/integrations/langgraph#main-interaction-loop)
```
if __name__ == "__main__":
    print("Welcome to Customer Support! How can I assist you today?")
    mem0_user_id = "alice"  # You can generate or retrieve this based on your user management system
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Customer Support: Thank you for contacting us. Have a great day!")
            break
        run_conversation(user_input, mem0_user_id)

```

## ​Key Features
[​](https://docs.mem0.ai/integrations/langgraph#key-features)- Memory Integration: Uses Mem0 to store and retrieve relevant information from past interactions.
- Personalization: Provides context-aware responses based on user history.
- Flexible Architecture: LangGraph structure allows for easy expansion of the conversation flow.
- Continuous Learning: Each interaction is stored, improving future responses.

## ​Conclusion
[​](https://docs.mem0.ai/integrations/langgraph#conclusion)[LangChain IntegrationBuild conversational agents with LangChain and Mem0](https://docs.mem0.ai/integrations/langchain)
## LangChain Integration
[CrewAI IntegrationCreate multi-agent systems with CrewAI](https://docs.mem0.ai/integrations/crewai)
## CrewAI Integration
