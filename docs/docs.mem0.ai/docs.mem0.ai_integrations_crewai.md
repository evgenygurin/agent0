# CrewAI - Mem0
Source: https://docs.mem0.ai/integrations/crewai
Downloaded: 2025-11-12 21:20:20
================================================================================


## ​Overview
[​](https://docs.mem0.ai/integrations/crewai#overview)- Uses CrewAI to manage AI agents and tasks
- Leverages Mem0 to store and retrieve conversation history
- Creates personalized experiences based on stored user preferences

## ​Setup and Configuration
[​](https://docs.mem0.ai/integrations/crewai#setup-and-configuration)
```
pip install crewai crewai-tools mem0ai

```
[Mem0 Platform](https://app.mem0.ai)[OpenAI](https://platform.openai.com)[Serper Dev](https://serper.dev)
```
import os
from mem0 import MemoryClient
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Configuration
os.environ["MEM0_API_KEY"] = "your-mem0-api-key"
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["SERPER_API_KEY"] = "your-serper-api-key"

# Initialize Mem0 client
client = MemoryClient()

```

## ​Store User Preferences
[​](https://docs.mem0.ai/integrations/crewai#store-user-preferences)
```
def store_user_preferences(user_id: str, conversation: list):
    """Store user preferences from conversation history"""
    client.add(conversation, user_id=user_id)

# Example conversation storage
messages = [
    {
        "role": "user",
        "content": "Hi there! I'm planning a vacation and could use some advice.",
    },
    {
        "role": "assistant",
        "content": "Hello! I'd be happy to help with your vacation planning. What kind of destination do you prefer?",
    },
    {"role": "user", "content": "I am more of a beach person than a mountain person."},
    {
        "role": "assistant",
        "content": "That's interesting. Do you like hotels or Airbnb?",
    },
    {"role": "user", "content": "I like Airbnb more."},
]

store_user_preferences("crew_user_1", messages)

```

## ​Create CrewAI Agent
[​](https://docs.mem0.ai/integrations/crewai#create-crewai-agent)
```
def create_travel_agent():
    """Create a travel planning agent with search capabilities"""
    search_tool = SerperDevTool()

    return Agent(
        role="Personalized Travel Planner Agent",
        goal="Plan personalized travel itineraries",
        backstory="""You are a seasoned travel planner, known for your meticulous attention to detail.""",
        allow_delegation=False,
        memory=True,
        tools=[search_tool],
    )

```

## ​Define Tasks
[​](https://docs.mem0.ai/integrations/crewai#define-tasks)
```
def create_planning_task(agent, destination: str):
    """Create a travel planning task"""
    return Task(
        description=f"""Find places to live, eat, and visit in {destination}.""",
        expected_output=f"A detailed list of places to live, eat, and visit in {destination}.",
        agent=agent,
    )

```

## ​Set Up Crew
[​](https://docs.mem0.ai/integrations/crewai#set-up-crew)
```
def setup_crew(agents: list, tasks: list):
    """Set up a crew with Mem0 memory integration"""
    return Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        memory=True,
        memory_config={
            "provider": "mem0",
            "config": {"user_id": "crew_user_1"},
        }
    )

```

## ​Main Execution Function
[​](https://docs.mem0.ai/integrations/crewai#main-execution-function)
```
def plan_trip(destination: str, user_id: str):
    # Create agent
    travel_agent = create_travel_agent()

    # Create task
    planning_task = create_planning_task(travel_agent, destination)

    # Setup crew
    crew = setup_crew([travel_agent], [planning_task])

    # Execute and return results
    return crew.kickoff()

# Example usage
if __name__ == "__main__":
    result = plan_trip("San Francisco", "crew_user_1")
    print(result)

```

## ​Key Features
[​](https://docs.mem0.ai/integrations/crewai#key-features)- Persistent Memory: Uses Mem0 to maintain user preferences and conversation history
- Agent-Based Architecture: Leverages CrewAI’s agent system for task execution
- Search Integration: Includes SerperDev tool for real-world information retrieval
- Personalization: Utilizes stored preferences for tailored recommendations

## ​Benefits
[​](https://docs.mem0.ai/integrations/crewai#benefits)- Persistent Context & Memory: Maintains user preferences and interaction history across sessions
- Flexible & Scalable Design: Easily extendable with new agents, tasks, and capabilities

## ​Conclusion
[​](https://docs.mem0.ai/integrations/crewai#conclusion)[AutoGen IntegrationBuild multi-agent systems with AutoGen and Mem0](https://docs.mem0.ai/integrations/autogen)
## AutoGen Integration
[LangGraph IntegrationCreate stateful agent workflows with memory](https://docs.mem0.ai/integrations/langgraph)
## LangGraph Integration
