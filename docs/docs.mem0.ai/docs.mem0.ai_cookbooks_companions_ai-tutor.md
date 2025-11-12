# Personalized AI Tutor - Mem0
Source: https://docs.mem0.ai/cookbooks/companions/ai-tutor
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/companions/ai-tutor#overview)
## ​Setup
[​](https://docs.mem0.ai/cookbooks/companions/ai-tutor#setup)
```
pip install openai mem0ai

```

## ​Full Code Example
[​](https://docs.mem0.ai/cookbooks/companions/ai-tutor#full-code-example)
```
import os 
from openai import OpenAI
from mem0 import Memory

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = 'sk-xxx'

# Initialize the OpenAI client
client = OpenAI()

class PersonalAITutor:
    def __init__(self):
        """
        Initialize the PersonalAITutor with memory configuration and OpenAI client.
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
        self.client = client
        self.app_id = "app-1"

    def ask(self, question, user_id=None):
        """
        Ask a question to the AI and store the relevant facts in memory

        :param question: The question to ask the AI.
        :param user_id: Optional user ID to associate with the memory.
        """
        # Start a streaming response request to the AI
        response = self.client.responses.create(
            model="gpt-4.1-nano-2025-04-14",
            instructions="You are a personal AI Tutor.",
            input=question,
            stream=True
        )

        # Store the question in memory
        self.memory.add(question, user_id=user_id, metadata={"app_id": self.app_id})

        # Print the response from the AI in real-time
        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="")

    def get_memories(self, user_id=None):
        """
        Retrieve all memories associated with the given user ID.

        :param user_id: Optional user ID to filter memories.
        :return: List of memories.
        """
        return self.memory.get_all(user_id=user_id)

# Instantiate the PersonalAITutor
ai_tutor = PersonalAITutor()

# Define a user ID
user_id = "john_doe"

# Ask a question
ai_tutor.ask("I am learning introduction to CS. What is queue? Briefly explain.", user_id=user_id)

```

### ​Fetching Memories
[​](https://docs.mem0.ai/cookbooks/companions/ai-tutor#fetching-memories)
```
memories = ai_tutor.get_memories(user_id=user_id)
for m in memories['results']:
    print(m['memory'])

```

## ​Key Points
[​](https://docs.mem0.ai/cookbooks/companions/ai-tutor#key-points)- Initialization: The PersonalAITutor class is initialized with the necessary memory configuration and OpenAI client setup
- Asking Questions: The ask method sends a question to the AI and stores the relevant information in memory
- Retrieving Memories: The get_memories method fetches all stored memories associated with a user

## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/companions/ai-tutor#conclusion)[Build a Mem0 CompanionLearn the foundations of memory-powered companions with production-ready patterns.](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion)
## Build a Mem0 Companion
[Travel Assistant with Mem0Build a travel companion that remembers preferences and past conversations.](https://docs.mem0.ai/cookbooks/companions/travel-assistant)
## Travel Assistant with Mem0
