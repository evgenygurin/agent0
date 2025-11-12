# Langchain - Mem0
Source: https://docs.mem0.ai/integrations/langchain
Downloaded: 2025-11-12 21:20:20
================================================================================


## ​Overview
[​](https://docs.mem0.ai/integrations/langchain#overview)- Uses LangChain to manage conversation flow
- Leverages Mem0 to store and retrieve relevant information from past interactions
- Provides personalized travel recommendations based on user history

## ​Setup and Configuration
[​](https://docs.mem0.ai/integrations/langchain#setup-and-configuration)
```
pip install langchain langchain_openai mem0ai python-dotenv

```
[Mem0 Platform](https://app.mem0.ai)
```
import os
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from mem0 import MemoryClient
from dotenv import load_dotenv

load_dotenv()

# Configuration
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
# os.environ["MEM0_API_KEY"] = "your-mem0-api-key"

# Initialize LangChain and Mem0
llm = ChatOpenAI(model="gpt-4.1-nano-2025-04-14")
mem0 = MemoryClient()

```

## ​Create Prompt Template
[​](https://docs.mem0.ai/integrations/langchain#create-prompt-template)
```
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="""You are a helpful travel agent AI. Use the provided context to personalize your responses and remember user preferences and past interactions. 
    Provide travel recommendations, itinerary suggestions, and answer questions about destinations. 
    If you don't have specific information, you can make general suggestions based on common travel knowledge."""),
    MessagesPlaceholder(variable_name="context"),
    HumanMessage(content="{input}")
])

```

## ​Define Helper Functions
[​](https://docs.mem0.ai/integrations/langchain#define-helper-functions)
```
def retrieve_context(query: str, user_id: str) -> List[Dict]:
    """Retrieve relevant context from Mem0"""
    try:
        memories = mem0.search(query, user_id=user_id)
        memory_list = memories['results']
        
        serialized_memories = ' '.join([mem["memory"] for mem in memory_list])
        context = [
            {
                "role": "system", 
                "content": f"Relevant information: {serialized_memories}"
            },
            {
                "role": "user",
                "content": query
            }
        ]
        return context
    except Exception as e:
        print(f"Error retrieving memories: {e}")
        # Return empty context if there's an error
        return [{"role": "user", "content": query}]

def generate_response(input: str, context: List[Dict]) -> str:
    """Generate a response using the language model"""
    chain = prompt | llm
    response = chain.invoke({
        "context": context,
        "input": input
    })
    return response.content

def save_interaction(user_id: str, user_input: str, assistant_response: str):
    """Save the interaction to Mem0"""
    try:
        interaction = [
            {
              "role": "user",
              "content": user_input
            },
            {
                "role": "assistant",
                "content": assistant_response
            }
        ]
        result = mem0.add(interaction, user_id=user_id)
        print(f"Memory saved successfully: {len(result.get('results', []))} memories added")
    except Exception as e:
        print(f"Error saving interaction: {e}")

```

## ​Create Chat Turn Function
[​](https://docs.mem0.ai/integrations/langchain#create-chat-turn-function)
```
def chat_turn(user_input: str, user_id: str) -> str:
    # Retrieve context
    context = retrieve_context(user_input, user_id)
    
    # Generate response
    response = generate_response(user_input, context)
    
    # Save interaction
    save_interaction(user_id, user_input, response)
    
    return response

```

## ​Main Interaction Loop
[​](https://docs.mem0.ai/integrations/langchain#main-interaction-loop)
```
if __name__ == "__main__":
    print("Welcome to your personal Travel Agent Planner! How can I assist you with your travel plans today?")
    user_id = "alice"
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Travel Agent: Thank you for using our travel planning service. Have a great trip!")
            break
        
        response = chat_turn(user_input, user_id)
        print(f"Travel Agent: {response}")

```

## ​Key Features
[​](https://docs.mem0.ai/integrations/langchain#key-features)- Memory Integration: Uses Mem0 to store and retrieve relevant information from past interactions.
- Personalization: Provides context-aware responses based on user history and preferences.
- Flexible Architecture: LangChain structure allows for easy expansion of the conversation flow.
- Continuous Learning: Each interaction is stored, improving future responses.

## ​Conclusion
[​](https://docs.mem0.ai/integrations/langchain#conclusion)[LangGraph IntegrationBuild stateful agents with LangGraph and Mem0](https://docs.mem0.ai/integrations/langgraph)
## LangGraph Integration
[LangChain ToolsUse Mem0 as LangChain tools for agent workflows](https://docs.mem0.ai/integrations/langchain-tools)
## LangChain Tools
