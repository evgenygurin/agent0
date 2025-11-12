# Memory-Powered Support Agent - Mem0
Source: https://docs.mem0.ai/cookbooks/operations/support-inbox
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/operations/support-inbox#overview)
## ​Setup
[​](https://docs.mem0.ai/cookbooks/operations/support-inbox#setup)
```
pip install openai mem0ai

```

## ​Full Code Example
[​](https://docs.mem0.ai/cookbooks/operations/support-inbox#full-code-example)
```
import os
from openai import OpenAI
from mem0 import Memory

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = 'sk-xxx'

class CustomerSupportAIAgent:
    def __init__(self):
        """
        Initialize the CustomerSupportAIAgent with memory configuration and OpenAI client.
        """
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": "localhost",
                    "port": 6333,
                }
            },
        }
        self.memory = Memory.from_config(config)
        self.client = OpenAI()
        self.app_id = "customer-support"

    def handle_query(self, query, user_id=None):
        """
        Handle a customer query and store the relevant information in memory.

        :param query: The customer query to handle.
        :param user_id: Optional user ID to associate with the memory.
        """
        # Start a streaming chat completion request to the AI
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": "You are a customer support AI agent."},
                {"role": "user", "content": query}
            ]
        )
        # Store the query in memory
        self.memory.add(query, user_id=user_id, metadata={"app_id": self.app_id})

        # Print the response from the AI in real-time
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        Retrieve all memories associated with the given customer ID.

        :param user_id: Optional user ID to filter memories.
        :return: List of memories.
        """
        return self.memory.get_all(user_id=user_id)

# Instantiate the CustomerSupportAIAgent
support_agent = CustomerSupportAIAgent()

# Define a customer ID
customer_id = "jane_doe"

# Handle a customer query
support_agent.handle_query("I need help with my recent order. It hasn't arrived yet.", user_id=customer_id)

```

### ​Fetching Memories
[​](https://docs.mem0.ai/cookbooks/operations/support-inbox#fetching-memories)
```
memories = support_agent.get_memories(user_id=customer_id)
for m in memories['results']:
    print(m['memory'])

```

### ​Key Points
[​](https://docs.mem0.ai/cookbooks/operations/support-inbox#key-points)- Initialization: The CustomerSupportAIAgent class is initialized with the necessary memory configuration and OpenAI client setup.
- Handling Queries: The handle_query method sends a query to the AI and stores the relevant information in memory.
- Retrieving Memories: The get_memories method fetches all stored memories associated with a customer.

### ​Conclusion
[​](https://docs.mem0.ai/cookbooks/operations/support-inbox#conclusion)[Build a Mem0 CompanionMaster the foundational patterns for building memory-powered assistants.](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion)
## Build a Mem0 Companion
[Email Automation with Mem0Extend support capabilities with intelligent email processing and routing.](https://docs.mem0.ai/cookbooks/operations/email-automation)
## Email Automation with Mem0
