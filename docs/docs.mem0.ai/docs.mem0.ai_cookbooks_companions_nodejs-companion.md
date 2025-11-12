# Build a Node.js Companion - Mem0
Source: https://docs.mem0.ai/cookbooks/companions/nodejs-companion
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/companions/nodejs-companion#overview)
## ​Setup
[​](https://docs.mem0.ai/cookbooks/companions/nodejs-companion#setup)
```
npm install openai mem0ai

```

## ​Full Code Example
[​](https://docs.mem0.ai/cookbooks/companions/nodejs-companion#full-code-example)
```
import { OpenAI } from 'openai';
import { Memory } from 'mem0ai/oss';
import * as readline from 'readline';

const openaiClient = new OpenAI();
const memory = new Memory();

async function chatWithMemories(message, userId = "default_user") {
  const relevantMemories = await memory.search(message, { userId: userId });
  
  const memoriesStr = relevantMemories.results
    .map(entry => `- ${entry.memory}`)
    .join('\n');
  
  const systemPrompt = `You are a helpful AI. Answer the question based on query and memories.
User Memories:
${memoriesStr}`;
  
  const messages = [
    { role: "system", content: systemPrompt },
    { role: "user", content: message }
  ];
  
  const response = await openaiClient.chat.completions.create({
    model: "gpt-4.1-nano-2025-04-14",
    messages: messages
  });
  
  const assistantResponse = response.choices[0].message.content || "";
  
  messages.push({ role: "assistant", content: assistantResponse });
  await memory.add(messages, { userId: userId });
  
  return assistantResponse;
}

async function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  console.log("Chat with AI (type 'exit' to quit)");
  
  const askQuestion = () => {
    return new Promise((resolve) => {
      rl.question("You: ", (input) => {
        resolve(input.trim());
      });
    });
  };
  
  try {
    while (true) {
      const userInput = await askQuestion();
      
      if (userInput.toLowerCase() === 'exit') {
        console.log("Goodbye!");
        rl.close();
        break;
      }
      
      const response = await chatWithMemories(userInput, "sample_user");
      console.log(`AI: ${response}`);
    }
  } catch (error) {
    console.error("An error occurred:", error);
    rl.close();
  }
}

main().catch(console.error);

```

### ​Key Components
[​](https://docs.mem0.ai/cookbooks/companions/nodejs-companion#key-components)- InitializationThe code initializes both OpenAI and Mem0 Memory clientsUses Node.js’s built-in readline module for command-line interaction
- The code initializes both OpenAI and Mem0 Memory clients
- Uses Node.js’s built-in readline module for command-line interaction
- Memory Management (chatWithMemories function)Retrieves relevant memories using Mem0’s search functionalityConstructs a system prompt that includes past memoriesMakes API calls to OpenAI for generating responsesStores new interactions in memory
- Retrieves relevant memories using Mem0’s search functionality
- Constructs a system prompt that includes past memories
- Makes API calls to OpenAI for generating responses
- Stores new interactions in memory
- Interactive Chat Interface (main function)Creates a command-line interface for user interactionHandles user input and displays AI responsesIncludes graceful exit functionality
- Creates a command-line interface for user interaction
- Handles user input and displays AI responses
- Includes graceful exit functionality

### ​Environment Setup
[​](https://docs.mem0.ai/cookbooks/companions/nodejs-companion#environment-setup)
```
export OPENAI_API_KEY=your_api_key

```

### ​Conclusion
[​](https://docs.mem0.ai/cookbooks/companions/nodejs-companion#conclusion)[Build AI with PersonalitySeparate user and agent memories to keep your companion’s personality consistent.](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality)
## Build AI with Personality
[Quickstart Demo with Mem0Run the full showcase app to see memory-powered companions in action.](https://docs.mem0.ai/cookbooks/companions/quickstart-demo)
## Quickstart Demo with Mem0
