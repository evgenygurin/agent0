# Persistent Mastra Agents - Mem0
Source: https://docs.mem0.ai/cookbooks/integrations/mastra-agent
Downloaded: 2025-11-12 21:20:21
================================================================================

[Mastra’s agent](https://mastra.ai/)[agent memory features](https://mastra.ai/docs/agents/01-agent-memory)[Mastra repository](https://github.com/mastra-ai/mastra/tree/main/examples/memory-with-mem0)
## ​Overview
[​](https://docs.mem0.ai/cookbooks/integrations/mastra-agent#overview)
## ​Installation
[​](https://docs.mem0.ai/cookbooks/integrations/mastra-agent#installation)
```
npm install @mastra/mem0

```

```
import { Mem0Integration } from "@mastra/mem0";

export const mem0 = new Mem0Integration({
  config: {
    apiKey: process.env.MEM0_API_KEY!,
    userId: "alice",
  },
});

```

```
import { createTool } from "@mastra/core";
import { z } from "zod";
import { mem0 } from "../integrations";

export const mem0RememberTool = createTool({
  id: "Mem0-remember",
  description:
    "Remember your agent memories that you've previously saved using the Mem0-memorize tool.",
  inputSchema: z.object({
    question: z
      .string()
      .describe("Question used to look up the answer in saved memories."),
  }),
  outputSchema: z.object({
    answer: z.string().describe("Remembered answer"),
  }),
  execute: async ({ context }) => {
    console.log(`Searching memory "${context.question}"`);
    const memory = await mem0.searchMemory(context.question);
    console.log(`\nFound memory "${memory}"\n`);

    return {
      answer: memory,
    };
  },
});

export const mem0MemorizeTool = createTool({
  id: "Mem0-memorize",
  description:
    "Save information to mem0 so you can remember it later using the Mem0-remember tool.",
  inputSchema: z.object({
    statement: z.string().describe("A statement to save into memory"),
  }),
  execute: async ({ context }) => {
    console.log(`\nCreating memory "${context.statement}"\n`);
    // to reduce latency memories can be saved async without blocking tool execution
    void mem0.createMemory(context.statement).then(() => {
      console.log(`\nMemory "${context.statement}" saved.\n`);
    });
    return { success: true };
  },
});

```

```
import { openai } from '@ai-sdk/openai';
import { Agent } from '@mastra/core/agent';
import { mem0MemorizeTool, mem0RememberTool } from '../tools';

export const mem0Agent = new Agent({
  name: 'Mem0 Agent',
  instructions: `
    You are a helpful assistant that has the ability to memorize and remember facts using Mem0.
  `,
  model: openai('gpt-4.1-nano'),
  tools: { mem0RememberTool, mem0MemorizeTool },
});

```

```
import { Mastra } from '@mastra/core/mastra';
import { createLogger } from '@mastra/core/logger';

import { mem0Agent } from './agents';

export const mastra = new Mastra({
  agents: { mem0Agent },
  logger: createLogger({
    name: 'Mastra',
    level: 'error',
  }),
});

```
- We import the@mastra/mem0integration
`@mastra/mem0`- We define two tools that use the Mem0 API client to create new memories and recall previously saved memories
- The tool acceptsquestionas an input and returns the memory as a string
`question`[Build AI with PersonalitySeparate agent and user memories to maintain consistent personalities.](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality)
## Build AI with Personality
[Agents SDK Tool with Mem0Explore tool-calling patterns with the OpenAI Agents SDK.](https://docs.mem0.ai/cookbooks/integrations/agents-sdk-tool)
## Agents SDK Tool with Mem0
