# Search with Personal Context - Mem0
Source: https://docs.mem0.ai/cookbooks/integrations/tavily-search
Downloaded: 2025-11-12 21:20:21
================================================================================

[Tavily](https://tavily.com)
## ​Why Personalized Search
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#why-personalized-search)- With Mem0, your assistant builds a memory of the user’s world.
- With Tavily, it fetches fresh and accurate results in real time.

## ​Prerequisites
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#prerequisites)- Installed the dependencies:

```
pip install langchain mem0ai langchain-tavily langchain-openai

```
- Set up your API keys in a .env file:

```
OPENAI_API_KEY=your-openai-key
TAVILY_API_KEY=your-tavily-key
MEM0_API_KEY=your-mem0-key

```

## ​Code Walkthrough
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#code-walkthrough)
### ​1: Initialize Mem0 with Custom Instructions
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#1%3A-initialize-mem0-with-custom-instructions)
```
from mem0 import MemoryClient

mem0_client = MemoryClient()

mem0_client.project.update(
    custom_instructions='''
INFER THE MEMORIES FROM USER QUERIES EVEN IF IT'S A QUESTION.

We are building personalized search for which we need to understand about user's preferences and life
and extract facts and memories accordingly.
'''
)

```

### ​2. Simulating User History
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#2-simulating-user-history)
```
def setup_user_history(user_id):
    conversations = [
        [{"role": "user", "content": "What will be the weather today at Los Angeles? I need to pick up my daughter from office."},
         {"role": "assistant", "content": "I'll check the weather in LA for you."}],
        [{"role": "user", "content": "I'm looking for vegan restaurants in Santa Monica"},
         {"role": "assistant", "content": "I'll find great vegan options in Santa Monica."}],
        [{"role": "user", "content": "My 7-year-old daughter is allergic to peanuts"},
         {"role": "assistant", "content": "I'll remember to check for peanut-free options."}],
        [{"role": "user", "content": "I work remotely and need coffee shops with good wifi"},
         {"role": "assistant", "content": "I'll find remote-work-friendly coffee shops."}],
        [{"role": "user", "content": "We love hiking and outdoor activities on weekends"},
         {"role": "assistant", "content": "Great! I'll keep your outdoor activity preferences in mind."}],
    ]

    for conversation in conversations:
        mem0_client.add(conversation, user_id=user_id)

```

### ​3. Retrieving User Context from Memory
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#3-retrieving-user-context-from-memory)
```
def get_user_context(user_id, query):
    # For Platform API, user_id goes in filters
    filters = {"user_id": user_id}
    user_memories = mem0_client.search(query=query, filters=filters)

    if user_memories:
        context = "\n".join([f"- {memory['memory']}" for memory in user_memories])
        return context
    else:
        return "No previous user context available."

```

### ​4. Creating the Personalized Search Agent
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#4-creating-the-personalized-search-agent)
```
def create_personalized_search_agent(user_context):
    tavily_search = TavilySearch(
        max_results=10,
        search_depth="advanced",
        include_answer=True,
        topic="general"
    )

    tools = [tavily_search]

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a personalized search assistant.

USER CONTEXT AND PREFERENCES:
{user_context}

YOUR ROLE:
1. Analyze the user's query and context.
2. Enhance the query with relevant personal memories.
3. Always use tavily_search for results.
4. Explain which memories influenced personalization.
"""),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_openai_tools_agent(llm=llm, tools=tools, prompt=prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, return_intermediate_steps=True)

```

### ​5. Run a Personalized Search
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#5-run-a-personalized-search)
```
def conduct_personalized_search(user_id, query):
    user_context = get_user_context(user_id, query)
    agent_executor = create_personalized_search_agent(user_context)

    response = agent_executor.invoke({"messages": [HumanMessage(content=query)]})
    return {"agent_response": response['output']}

```

### ​6. Store New Interactions
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#6-store-new-interactions)
```
def store_search_interaction(user_id, original_query, agent_response):
    interaction = [
        {"role": "user", "content": f"Searched for: {original_query}"},
        {"role": "assistant", "content": f"Results based on preferences: {agent_response}"}
    ]
    mem0_client.add(messages=interaction, user_id=user_id)

```

### ​Full Example Run
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#full-example-run)
```
if __name__ == "__main__":
    user_id = "john"
    setup_user_history(user_id)

    queries = [
        "good coffee shops nearby for working",
        "what can I make for my kid in lunch?"
    ]

    for q in queries:
        results = conduct_personalized_search(user_id, q)
        print(f"\nQuery: {q}")
        print(f"Personalized Response: {results['agent_response']}")

```

## ​How It Works in Practice
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#how-it-works-in-practice)- Context Gathering: User previously mentioned living in Los Angeles, being vegan, and having a 7-year-old daughter allergic to peanuts.
- Enhanced Search Query:Query: “good coffee shops nearby for working”Enhanced Query: “good coffee shops in Los Angeles with strong WiFi, remote-work-friendly”
- Query: “good coffee shops nearby for working”
- Enhanced Query: “good coffee shops in Los Angeles with strong WiFi, remote-work-friendly”
- Personalized Results: The assistant only returns WiFi-friendly, work-friendly cafes near Los Angeles.
- Memory Update: Interaction is saved for better future recommendations.

## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/integrations/tavily-search#conclusion)[Personalized Search GitHub](https://github.com/mem0ai/mem0/blob/main/examples/misc/personalized_search.py)[Deep Research with Mem0Build comprehensive research agents that remember findings across sessions.](https://docs.mem0.ai/cookbooks/operations/deep-research)
## Deep Research with Mem0
[Tag and Organize MemoriesCategorize search results and user preferences for better personalization.](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories)
## Tag and Organize Memories
