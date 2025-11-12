# Node SDK Quickstart - Mem0
Source: https://docs.mem0.ai/open-source/node-quickstart
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Prerequisites
[​](https://docs.mem0.ai/open-source/node-quickstart#prerequisites)- Node.js 18 or higher
- (Optional) OpenAI API key stored in your environment when you want to customize providers

## ​Install and run your first memory
[​](https://docs.mem0.ai/open-source/node-quickstart#install-and-run-your-first-memory)
Install the SDK

```
npm install mem0ai

```

Initialize the client

```
import { Memory } from "mem0ai/oss";

const memory = new Memory();

```

Add a memory

```
const messages = [
  { role: "user", content: "I'm planning to watch a movie tonight. Any recommendations?" },
  { role: "assistant", content: "How about thriller movies? They can be quite engaging." },
  { role: "user", content: "I'm not a big fan of thriller movies but I love sci-fi movies." },
  { role: "assistant", content: "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future." }
];

await memory.add(messages, { userId: "alice", metadata: { category: "movie_recommendations" } });

```

Search memories

```
const results = await memory.search("What do you know about me?", { userId: "alice" });
console.log(results);

```

```
{
  "results": [
    {
      "id": "892db2ae-06d9-49e5-8b3e-585ef9b85b8e",
      "memory": "User is planning to watch a movie tonight.",
      "score": 0.38920719231944799,
      "metadata": {
        "category": "movie_recommendations"
      },
      "userId": "alice"
    }
  ]
}

```
`gpt-4.1-nano-2025-04-14``text-embedding-3-small`
## ​Configure for production
[​](https://docs.mem0.ai/open-source/node-quickstart#configure-for-production)
```
import { Memory } from "mem0ai/oss";

const memory = new Memory({
  version: "v1.1",
  embedder: {
    provider: "openai",
    config: {
      apiKey: process.env.OPENAI_API_KEY || "",
      model: "text-embedding-3-small"
    }
  },
  vectorStore: {
    provider: "memory",
    config: {
      collectionName: "memories",
      dimension: 1536
    }
  },
  llm: {
    provider: "openai",
    config: {
      apiKey: process.env.OPENAI_API_KEY || "",
      model: "gpt-4-turbo-preview"
    }
  },
  historyDbPath: "memory.db"
});

```

## ​Manage memories (optional)
[​](https://docs.mem0.ai/open-source/node-quickstart#manage-memories-optional)
```
const allMemories = await memory.getAll({ userId: "alice" });
console.log(allMemories);

```

```
// Audit history
const history = await memory.history("892db2ae-06d9-49e5-8b3e-585ef9b85b8e");
console.log(history);

// Delete specific or scoped memories
await memory.delete("892db2ae-06d9-49e5-8b3e-585ef9b85b8e");
await memory.deleteAll({ userId: "alice" });

// Reset everything
await memory.reset();

```

## ​Use a custom history store
[​](https://docs.mem0.ai/open-source/node-quickstart#use-a-custom-history-store)
```
import { Memory } from "mem0ai/oss";

const memory = new Memory({
  historyStore: {
    provider: "supabase",
    config: {
      supabaseUrl: process.env.SUPABASE_URL || "",
      supabaseKey: process.env.SUPABASE_KEY || "",
      tableName: "memory_history"
    }
  }
});

```

```
create table memory_history (
  id text primary key,
  memory_id text not null,
  previous_value text,
  new_value text,
  action text not null,
  created_at timestamp with time zone default timezone('utc', now()),
  updated_at timestamp with time zone,
  is_deleted integer default 0
);

```

## ​Configuration parameters
[​](https://docs.mem0.ai/open-source/node-quickstart#configuration-parameters)
Vector store
`provider``"memory"``"memory"``host``"localhost"``port``undefined`
LLM
`provider``"openai"``"anthropic"``model``temperature``apiKey``maxTokens``topP``topK``openaiBaseUrl`
Graph store
`provider``"neo4j"``"neo4j"``url``process.env.NEO4J_URL``username``process.env.NEO4J_USERNAME``password``process.env.NEO4J_PASSWORD`
Embedder
`provider``"openai"``model``"text-embedding-3-small"``apiKey``undefined`
General
`historyDbPath``"{mem0_dir}/history.db"``version``"v1.0"``customPrompt``undefined`
History store
`provider``"sqlite"``config``undefined``disableHistory``false`
Complete config example

```
const config = {
  version: "v1.1",
  embedder: {
    provider: "openai",
    config: {
      apiKey: process.env.OPENAI_API_KEY || "",
      model: "text-embedding-3-small"
    }
  },
  vectorStore: {
    provider: "memory",
    config: {
      collectionName: "memories",
      dimension: 1536
    }
  },
  llm: {
    provider: "openai",
    config: {
      apiKey: process.env.OPENAI_API_KEY || "",
      model: "gpt-4-turbo-preview"
    }
  },
  historyStore: {
    provider: "supabase",
    config: {
      supabaseUrl: process.env.SUPABASE_URL || "",
      supabaseKey: process.env.SUPABASE_KEY || "",
      tableName: "memories"
    }
  },
  disableHistory: false,
  customPrompt: "I'm a virtual assistant. I'm here to help you with your queries."
};

```

## ​What’s next?
[​](https://docs.mem0.ai/open-source/node-quickstart#what%E2%80%99s-next%3F)[Explore Memory OperationsReview CRUD patterns, filters, and advanced retrieval across the OSS stack.](https://docs.mem0.ai/open-source/overview)
## Explore Memory Operations
[Customize ConfigurationSwap in your preferred LLM, vector store, and history provider for production use.](https://docs.mem0.ai/open-source/configuration)
## Customize Configuration
[Automate Node WorkflowsSee a full Node-based workflow that layers Mem0 memories onto tool-calling agents.](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls)
## Automate Node Workflows
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
