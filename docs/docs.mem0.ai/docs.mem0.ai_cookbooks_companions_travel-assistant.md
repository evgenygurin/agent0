# Smart Travel Assistant - Mem0
Source: https://docs.mem0.ai/cookbooks/companions/travel-assistant
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/companions/travel-assistant#overview)
## ​Setup
[​](https://docs.mem0.ai/cookbooks/companions/travel-assistant#setup)
```
pip install openai mem0ai

```

## ​Full Code Example
[​](https://docs.mem0.ai/cookbooks/companions/travel-assistant#full-code-example)
```
import os
from openai import OpenAI
from mem0 import Memory

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = "sk-xxx"

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4.1-nano-2025-04-14",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-large"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "test",
            "embedding_model_dims": 3072,
        }
    },
    "version": "v1.1",
}

class PersonalTravelAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.memory = Memory.from_config(config)
        self.messages = [{"role": "system", "content": "You are a personal AI Assistant."}]

    def ask_question(self, question, user_id):
        # Fetch previous related memories
        previous_memories = self.search_memories(question, user_id=user_id)

        # Build the prompt
        system_message = "You are a personal AI Assistant."

        if previous_memories:
            prompt = f"{system_message}\n\nUser input: {question}\nPrevious memories: {', '.join(previous_memories)}"
        else:
            prompt = f"{system_message}\n\nUser input: {question}"

        # Generate response using Responses API
        response = self.client.responses.create(
            model="gpt-4.1-nano-2025-04-14",
            input=prompt
        )

        # Extract answer from the response
        answer = response.output[0].content[0].text

        # Store the question in memory
        self.memory.add(question, user_id=user_id)
        return answer

    def get_memories(self, user_id):
        memories = self.memory.get_all(user_id=user_id)
        return [m['memory'] for m in memories['results']]

    def search_memories(self, query, user_id):
        memories = self.memory.search(query, user_id=user_id)
        return [m['memory'] for m in memories['results']]

# Usage example
user_id = "traveler_123"
ai_assistant = PersonalTravelAssistant()

def main():
    while True:
        question = input("Question: ")
        if question.lower() in ['q', 'exit']:
            print("Exiting...")
            break

        answer = ai_assistant.ask_question(question, user_id=user_id)
        print(f"Answer: {answer}")
        memories = ai_assistant.get_memories(user_id=user_id)
        print("Memories:")
        for memory in memories:
            print(f"- {memory}")
        print("-----")

if __name__ == "__main__":
    main()

```

## ​Key Components
[​](https://docs.mem0.ai/cookbooks/companions/travel-assistant#key-components)- Initialization: ThePersonalTravelAssistantclass is initialized with the OpenAI client and Mem0 memory setup.
`PersonalTravelAssistant`- Asking Questions: Theask_questionmethod sends a question to the AI, incorporates previous memories, and stores new information.
`ask_question`- Memory Management: Theget_memoriesand search_memories methods handle retrieval and searching of stored memories.
`get_memories`
## ​Usage
[​](https://docs.mem0.ai/cookbooks/companions/travel-assistant#usage)- Set your OpenAI API key in the environment variable.
- Instantiate thePersonalTravelAssistant.
`PersonalTravelAssistant`- Use themain()function to interact with the assistant in a loop.
`main()`
## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/companions/travel-assistant#conclusion)[Tag and Organize MemoriesUse categories to organize travel preferences, destinations, and user context.](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories)
## Tag and Organize Memories
[AI Tutor with Mem0Build an educational companion that remembers learning progress and preferences.](https://docs.mem0.ai/cookbooks/companions/ai-tutor)
## AI Tutor with Mem0
