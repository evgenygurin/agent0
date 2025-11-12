# Vercel AI SDK - Mem0
Source: https://docs.mem0.ai/integrations/vercel-ai-sdk
Downloaded: 2025-11-12 21:20:20
================================================================================

[Mem0 AI SDK Provider](https://www.npmjs.com/package/@mem0/vercel-ai-provider)
## ​Overview
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#overview)- Offers persistent memory storage for conversational AI
- Enables smooth integration with the Vercel AI SDK
- Ensures compatibility with multiple LLM providers
- Supports structured message formats for clarity
- Facilitates streaming response capabilities

## ​Setup and Configuration
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#setup-and-configuration)
```
npm install @mem0/vercel-ai-provider

```

## ​Getting Started
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#getting-started)
### ​Setting Up Mem0
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#setting-up-mem0)- Get yourMem0 API Keyfrom theMem0 Dashboard.
[Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys)- Initialize the Mem0 Client in your application:CopyAsk AIimport{createMem0}from"@mem0/vercel-ai-provider";constmem0=createMem0({provider:"openai",mem0ApiKey:"m0-xxx",apiKey:"provider-api-key",config:{// Options for LLM Provider},// Optional Mem0 Global Configmem0Config:{user_id:"mem0-user-id",},});Note: Theopenaiprovider is set as default. Consider usingMEM0_API_KEYandOPENAI_API_KEYas environment variables for security.Note: Themem0Configis optional. It is used to set the global config for the Mem0 Client (eg.user_id,agent_id,app_id,run_id,org_id,project_idetc).

```
import { createMem0 } from "@mem0/vercel-ai-provider";

const mem0 = createMem0({
  provider: "openai",
  mem0ApiKey: "m0-xxx",
  apiKey: "provider-api-key",
  config: {
    // Options for LLM Provider
  },
  // Optional Mem0 Global Config
  mem0Config: {
    user_id: "mem0-user-id",
  },
});

```
`openai``MEM0_API_KEY``OPENAI_API_KEY``mem0Config``user_id``agent_id``app_id``run_id``org_id``project_id`- Add Memories to Enhance Context:CopyAsk AIimport{LanguageModelV2Prompt}from"@ai-sdk/provider";import{addMemories}from"@mem0/vercel-ai-provider";constmessages:LanguageModelV2Prompt=[{role:"user",content:[{type:"text",text:"I love red cars."}] },];awaitaddMemories(messages, {user_id:"borat"});

```
import { LanguageModelV2Prompt } from "@ai-sdk/provider";
import { addMemories } from "@mem0/vercel-ai-provider";

const messages: LanguageModelV2Prompt = [
  { role: "user", content: [{ type: "text", text: "I love red cars." }] },
];

await addMemories(messages, { user_id: "borat" });

```

### ​Standalone Features:
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#standalone-features%3A)
```
await addMemories(messages, { user_id: "borat", mem0ApiKey: "m0-xxx" });
await retrieveMemories(prompt, { user_id: "borat", mem0ApiKey: "m0-xxx" });
await getMemories(prompt, { user_id: "borat", mem0ApiKey: "m0-xxx" });

```
`addMemories``retrieveMemories``getMemories``MEM0_API_KEY``getMemories``retrieveMemories``getMemories``results``relations``enable_graph`
### ​1. Basic Text Generation with Memory Context
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#1-basic-text-generation-with-memory-context)
```
import { generateText } from "ai";
import { createMem0 } from "@mem0/vercel-ai-provider";

const mem0 = createMem0();

const { text } = await generateText({
  model: mem0("gpt-4-turbo", { user_id: "borat" }),
  prompt: "Suggest me a good car to buy!",
});

```

### ​2. Combining OpenAI Provider with Memory Utils
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#2-combining-openai-provider-with-memory-utils)
```
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
import { retrieveMemories } from "@mem0/vercel-ai-provider";

const prompt = "Suggest me a good car to buy.";
const memories = await retrieveMemories(prompt, { user_id: "borat" });

const { text } = await generateText({
  model: openai("gpt-4-turbo"),
  prompt: prompt,
  system: memories,
});

```

### ​3. Structured Message Format with Memory
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#3-structured-message-format-with-memory)
```
import { generateText } from "ai";
import { createMem0 } from "@mem0/vercel-ai-provider";

const mem0 = createMem0();

const { text } = await generateText({
  model: mem0("gpt-4-turbo", { user_id: "borat" }),
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Suggest me a good car to buy." },
        { type: "text", text: "Why is it better than the other cars for me?" },
      ],
    },
  ],
});

```

### ​3. Streaming Responses with Memory Context
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#3-streaming-responses-with-memory-context)
```
import { streamText } from "ai";
import { createMem0 } from "@mem0/vercel-ai-provider";

const mem0 = createMem0();

const { textStream } = streamText({
    model: mem0("gpt-4-turbo", {
        user_id: "borat",
    }),
    prompt: "Suggest me a good car to buy! Why is it better than the other cars for me? Give options for every price range.",
});

for await (const textPart of textStream) {
    process.stdout.write(textPart);
}

```

### ​4. Generate Responses with Tools Call
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#4-generate-responses-with-tools-call)
```
import { generateText } from "ai";
import { createMem0 } from "@mem0/vercel-ai-provider";
import { z } from "zod";

const mem0 = createMem0({
  provider: "anthropic",
  apiKey: "anthropic-api-key",
  mem0Config: {
    // Global User ID
    user_id: "borat"
  }
});

const prompt = "What the temperature in the city that I live in?"

const result = await generateText({
  model: mem0('claude-3-5-sonnet-20240620'),
  tools: {
    weather: tool({
      description: 'Get the weather in a location',
      parameters: z.object({
        location: z.string().describe('The location to get the weather for'),
      }),
      execute: async ({ location }) => ({
        location,
        temperature: 72 + Math.floor(Math.random() * 21) - 10,
      }),
    }),
  },
  prompt: prompt,
});

console.log(result);

```

### ​5. Get sources from memory
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#5-get-sources-from-memory)
```
const { text, sources } = await generateText({
    model: mem0("gpt-4-turbo"),
    prompt: "Suggest me a good car to buy!",
});

console.log(sources);

```
`streamText`
### ​6. File Support with Memory Context
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#6-file-support-with-memory-context)
```
import { streamText } from "ai";
import { createMem0 } from "@mem0/vercel-ai-provider";
import { readFileSync } from 'fs';
import { join } from 'path';

const mem0 = createMem0({
  provider: "google",
  mem0ApiKey: "m0-xxx",
  config: {
    apiKey: "google-api-key"
  },
  mem0Config: {
    user_id: "alice",
  },
});

async function main() {
  // Read the PDF file
  const filePath = join(process.cwd(), 'my_pdf.pdf');
  const fileBuffer = readFileSync(filePath);

  // Convert the file's arrayBuffer to a Base64 data URL
  const arrayBuffer = fileBuffer.buffer.slice(fileBuffer.byteOffset, fileBuffer.byteOffset + fileBuffer.byteLength);
  const uint8Array = new Uint8Array(arrayBuffer);

  // Convert Uint8Array to an array of characters
  const charArray = Array.from(uint8Array, byte => String.fromCharCode(byte));
  const binaryString = charArray.join('');
  const base64Data = Buffer.from(binaryString, 'binary').toString('base64');
  const fileDataUrl = `data:application/pdf;base64,${base64Data}`;

  const { textStream } = streamText({
    model: mem0("gemini-2.5-flash"),
    messages: [
      {
        role: 'user',
        content: [
          {
            type: 'text',
            text: 'Analyze the following PDF and generate a summary.',
          },
          {
            type: 'file',
            data: fileDataUrl,
            mediaType: 'application/pdf',
          },
        ],
      },
    ],
  });

  for await (const textPart of textStream) {
    process.stdout.write(textPart);
  }
}

main();

```

## ​Graph Memory
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#graph-memory)`enable_graph``true``mem0Config`
```
const mem0 = createMem0({
  mem0Config: { enable_graph: true },
});

```
`enable_graph``getMemories``retrieveMemories``addMemories`
```
const memories = await getMemories(prompt, { user_id: "borat", mem0ApiKey: "m0-xxx", enable_graph: true });

```
`getMemories``results``relations``enable_graph``true`
## ​Supported LLM Providers
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#supported-llm-providers)`google``@ai-sdk/google`
## ​Key Features
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#key-features)- createMem0(): Initializes a new Mem0 provider instance.
`createMem0()`- retrieveMemories(): Retrieves memory context for prompts.
`retrieveMemories()`- getMemories(): Get memories from your profile in array format.
`getMemories()`- addMemories(): Adds user memories to enhance contextual responses.
`addMemories()`
## ​Best Practices
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#best-practices)- User Identification: Use a uniqueuser_idfor consistent memory retrieval.
`user_id`- Memory Cleanup: Regularly clean up unused memory data.Note: We also have support foragent_id,app_id, andrun_id. ReferDocs.
`agent_id``app_id``run_id`[Docs](https://docs.mem0.ai/api-reference/memory/add-memories)
## ​Conclusion
[​](https://docs.mem0.ai/integrations/vercel-ai-sdk#conclusion)[OpenAI Agents SDKBuild agents with OpenAI SDK and Mem0](https://docs.mem0.ai/integrations/openai-agents-sdk)
## OpenAI Agents SDK
[Mastra IntegrationCreate intelligent agents with Mastra framework](https://docs.mem0.ai/integrations/mastra)
## Mastra Integration
