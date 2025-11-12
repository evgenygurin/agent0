# Memory as OpenAI Tool - Mem0
Source: https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Getting Started
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#getting-started)
### ​Installation
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#installation)
```
npm install mem0ai openai zod

```

## ​Environment Setup
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#environment-setup)`.env`
```
MEM0_API_KEY=your_mem0_api_key
OPENAI_API_KEY=your_openai_api_key

```
[Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys)
### ​Configuration
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#configuration)
```
const mem0Config = {
    apiKey: process.env.MEM0_API_KEY,
    user_id: "sample-user",
};

const openAIClient = new OpenAI();
const mem0Client = new MemoryClient(mem0Config);

```

## ​Adding Memories
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#adding-memories)
```
async function addUserPreferences() {
    const mem0Client = new MemoryClient(mem0Config);
    
    const userPreferences = "I Love BMW, Audi and Porsche. I Hate Mercedes. I love Red cars and Maroon cars. I have a budget of 120K to 150K USD. I like Audi the most.";
    
    await mem0Client.add([{
        role: "user",
        content: userPreferences,
    }], mem0Config);
}

await addUserPreferences();

```

## ​Retrieving Memories
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#retrieving-memories)
```
const relevantMemories = await mem0Client.search(userInput, mem0Config);

```

## ​Structured Responses with Zod
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#structured-responses-with-zod)
```
// Define the schema for a car recommendation
const CarSchema = z.object({
  car_name: z.string(),
  car_price: z.string(),
  car_url: z.string(),
  car_image: z.string(),
  car_description: z.string(),
});

// Schema for a list of car recommendations
const Cars = z.object({
  cars: z.array(CarSchema),
});

// Create a function tool based on the schema
const carRecommendationTool = zodResponsesFunction({ 
    name: "carRecommendations", 
    parameters: Cars 
});

// Use the tool in your OpenAI request
const response = await openAIClient.responses.create({
    model: "gpt-4.1-nano-2025-04-14",
    tools: [{ type: "web_search_preview" }, carRecommendationTool],
    input: `${getMemoryString(relevantMemories)}\n${userInput}`,
});

```

## ​Using Web Search
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#using-web-search)
```
const response = await openAIClient.responses.create({
    model: "gpt-4.1-nano-2025-04-14",
    tools: [{ type: "web_search_preview" }, carRecommendationTool],
    input: `${getMemoryString(relevantMemories)}\n${userInput}`,
});

```

## ​Examples
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#examples)
## ​Complete Car Recommendation System
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#complete-car-recommendation-system)
```
import MemoryClient from "mem0ai";
import { OpenAI } from "openai";
import { zodResponsesFunction } from "openai/helpers/zod";
import { z } from "zod";
import dotenv from 'dotenv';

dotenv.config();

const mem0Config = {
    apiKey: process.env.MEM0_API_KEY,
    user_id: "sample-user",
};

async function run() {
    // Responses without memories
    console.log("\n\nRESPONSES WITHOUT MEMORIES\n\n");
    await main();

    // Adding sample memories
    await addSampleMemories();

    // Responses with memories
    console.log("\n\nRESPONSES WITH MEMORIES\n\n");
    await main(true);
}

// OpenAI Response Schema
const CarSchema = z.object({
  car_name: z.string(),
  car_price: z.string(),
  car_url: z.string(),
  car_image: z.string(),
  car_description: z.string(),
});

const Cars = z.object({
  cars: z.array(CarSchema),
});

async function main(memory = false) {
  const openAIClient = new OpenAI();
  const mem0Client = new MemoryClient(mem0Config);

  const input = "Suggest me some cars that I can buy today.";

  const tool = zodResponsesFunction({ name: "carRecommendations", parameters: Cars });

  // Store the user input as a memory
  await mem0Client.add([{
    role: "user",
    content: input,
  }], mem0Config);

  // Search for relevant memories
  let relevantMemories = []
  if (memory) {
    relevantMemories = await mem0Client.search(input, mem0Config);
  }

  const response = await openAIClient.responses.create({
    model: "gpt-4.1-nano-2025-04-14",
    tools: [{ type: "web_search_preview" }, tool],
    input: `${getMemoryString(relevantMemories)}\n${input}`,
  });

  console.log(response.output);
}

async function addSampleMemories() {
  const mem0Client = new MemoryClient(mem0Config);

  const myInterests = "I Love BMW, Audi and Porsche. I Hate Mercedes. I love Red cars and Maroon cars. I have a budget of 120K to 150K USD. I like Audi the most.";
  
  await mem0Client.add([{
    role: "user",
    content: myInterests,
  }], mem0Config);
}

const getMemoryString = (memories) => {
    const MEMORY_STRING_PREFIX = "These are the memories I have stored. Give more weightage to the question by users and try to answer that first. You have to modify your answer based on the memories I have provided. If the memories are irrelevant you can ignore them. Also don't reply to this section of the prompt, or the memories, they are only for your reference. The MEMORIES of the USER are: \n\n";
    const memoryString = (memories?.results || memories).map((mem) => `${mem.memory}`).join("\n") ?? "";
    return memoryString.length > 0 ? `${MEMORY_STRING_PREFIX}${memoryString}` : "";
};

run().catch(console.error);

```

## ​Responses
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#responses)
```
{
  "cars": [
    {
      "car_name": "Toyota Camry",
      "car_price": "$25,000",
      "car_url": "https://www.toyota.com/camry/",
      "car_image": "https://link-to-toyota-camry-image.com",
      "car_description": "Reliable mid-size sedan with great fuel efficiency."
    },
    {
      "car_name": "Honda Accord",
      "car_price": "$26,000",
      "car_url": "https://www.honda.com/accord/",
      "car_image": "https://link-to-honda-accord-image.com",
      "car_description": "Comfortable and spacious with advanced safety features."
    },
    {
      "car_name": "Ford Mustang",
      "car_price": "$28,000",
      "car_url": "https://www.ford.com/mustang/",
      "car_image": "https://link-to-ford-mustang-image.com",
      "car_description": "Iconic sports car with powerful engine options."
    },
    {
      "car_name": "Tesla Model 3",
      "car_price": "$38,000",
      "car_url": "https://www.tesla.com/model3",
      "car_image": "https://link-to-tesla-model3-image.com",
      "car_description": "Electric vehicle with advanced technology and long range."
    },
    {
      "car_name": "Chevrolet Equinox",
      "car_price": "$24,000",
      "car_url": "https://www.chevrolet.com/equinox/",
      "car_image": "https://link-to-chevron-equinox-image.com",
      "car_description": "Compact SUV with a spacious interior and user-friendly technology."
    }
  ]
}

```

## ​Resources
[​](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls#resources)- Mem0 Documentation
[Mem0 Documentation](https://docs.mem0.ai)- Mem0 Dashboard
[Mem0 Dashboard](https://app.mem0.ai/dashboard)- API Reference
[API Reference](https://docs.mem0.ai/api-reference)- OpenAI Documentation
[OpenAI Documentation](https://platform.openai.com/docs)[Agents SDK Tool with Mem0Extend the OpenAI Agents SDK with Mem0 integration capabilities.](https://docs.mem0.ai/cookbooks/integrations/agents-sdk-tool)
## Agents SDK Tool with Mem0
[Control Memory IngestionFine-tune what memories get stored during tool calls.](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion)
## Control Memory Ingestion
