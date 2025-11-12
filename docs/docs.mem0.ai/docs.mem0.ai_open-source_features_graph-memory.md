# Graph Memory - Mem0
Source: https://docs.mem0.ai/open-source/features/graph-memory
Downloaded: 2025-11-12 21:20:19
================================================================================

- Conversation history mixes multiple actors and objects that vectors alone blur together
- Compliance or auditing demands a graph of who said what and when
- Agent teams need shared context without duplicating every memory in each run

## ​How Graph Memory Maps Context
[​](https://docs.mem0.ai/open-source/features/graph-memory#how-graph-memory-maps-context)
## ​How It Works
[​](https://docs.mem0.ai/open-source/features/graph-memory#how-it-works)
Extract people, places, and facts
`memory.add`
Store vectors and edges together

Expose graph context at search time
`memory.search``relations`
## ​Quickstart (Neo4j Aura)
[​](https://docs.mem0.ai/open-source/features/graph-memory#quickstart-neo4j-aura)[Neo4j Aura](https://neo4j.com/product/auradb/)- Python
- TypeScript

Install Mem0 with graph extras

```
pip install "mem0ai[graph]"

```

Export Neo4j credentials

```
export NEO4J_URL="neo4j+s://<your-instance>.databases.neo4j.io"
export NEO4J_USERNAME="neo4j"
export NEO4J_PASSWORD="your-password"

```

Add and recall a relationship

```
import os
from mem0 import Memory

config = {
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": os.environ["NEO4J_URL"],
            "username": os.environ["NEO4J_USERNAME"],
            "password": os.environ["NEO4J_PASSWORD"],
            "database": "neo4j",
        }
    }
}

memory = Memory.from_config(config)

conversation = [
    {"role": "user", "content": "Alice met Bob at GraphConf 2025 in San Francisco."},
    {"role": "assistant", "content": "Great! Logging that connection."},
]

memory.add(conversation, user_id="demo-user")

results = memory.search(
    "Who did Alice meet at GraphConf?",
    user_id="demo-user",
    limit=3,
    rerank=True,
)

for hit in results["results"]:
    print(hit["memory"])

```
`MATCH (p:Person)-[r]->(q:Person) RETURN p,r,q LIMIT 5;``relations``results`
## ​Operate Graph Memory Day-to-Day
[​](https://docs.mem0.ai/open-source/features/graph-memory#operate-graph-memory-day-to-day)
Refine extraction prompts

```
import os
from mem0 import Memory

config = {
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": os.environ["NEO4J_URL"],
            "username": os.environ["NEO4J_USERNAME"],
            "password": os.environ["NEO4J_PASSWORD"],
        },
        "custom_prompt": "Please only capture people, organisations, and project links.",
    }
}

memory = Memory.from_config(config_dict=config)

```

Raise the confidence threshold

```
config["graph_store"]["config"]["threshold"] = 0.75

```

Toggle graph writes per request

```
memory.add(messages, user_id="demo-user", enable_graph=False)
results = memory.search("marketing partners", user_id="demo-user", enable_graph=False)

```

Organize multi-agent graphs
`user_id``agent_id``run_id`
```
memory.add("I prefer Italian cuisine", { userId: "bob", agentId: "food-assistant" });
memory.add("I'm allergic to peanuts", { userId: "bob", agentId: "health-assistant" });
memory.add("I live in Seattle", { userId: "bob" });

const food = await memory.search("What food do I like?", { userId: "bob", agentId: "food-assistant" });
const allergies = await memory.search("What are my allergies?", { userId: "bob", agentId: "health-assistant" });
const location = await memory.search("Where do I live?", { userId: "bob" });

```
`MATCH (n) WHERE n.lastSeen < date() - duration('P90D') DETACH DELETE n`
## ​Troubleshooting
[​](https://docs.mem0.ai/open-source/features/graph-memory#troubleshooting)
Neo4j connection refused
`neo4j+s://...`
Neptune Analytics rejects requests
`neptune-graph:*DataViaQuery`
Graph store outage fallback
`enable_graph=False`
## ​Decision Points
[​](https://docs.mem0.ai/open-source/features/graph-memory#decision-points)- Select the graph store that fits your deployment (managed Aura vs. self-hosted Neo4j vs. AWS Neptune vs. local Kuzu).
- Decide when to enable graph writes per request; routine conversations may stay vector-only to save latency.
- Set a policy for pruning stale relationships so your graph stays fast and affordable.

## ​Provider setup
[​](https://docs.mem0.ai/open-source/features/graph-memory#provider-setup)
Neo4j Aura or self-hosted

```
import { Memory } from "mem0ai/oss";

const config = {
    enableGraph: true,
    graphStore: {
        provider: "neo4j",
        config: {
            url: "neo4j+s://<HOST>",
            username: "neo4j",
            password: "<PASSWORD>",
        }
    }
};

const memory = new Memory(config);

```
[Neo4j Aura Quickstart](https://neo4j.com/docs/aura/)[APOC installation](https://neo4j.com/docs/apoc/current/installation/)
Memgraph (Docker)

```
docker run -p 7687:7687 memgraph/memgraph-mage:latest --schema-info-enabled=True

```

```
from mem0 import Memory

config = {
    "graph_store": {
        "provider": "memgraph",
        "config": {
            "url": "bolt://localhost:7687",
            "username": "memgraph",
            "password": "your-password",
        },
    },
}

m = Memory.from_config(config_dict=config)

```
[Memgraph Docs](https://memgraph.com/docs)
Amazon Neptune Analytics

```
from mem0 import Memory

config = {
    "graph_store": {
        "provider": "neptune",
        "config": {
            "endpoint": "neptune-graph://<GRAPH_ID>",
        },
    },
}

m = Memory.from_config(config_dict=config)

```
[Neptune Analytics Guide](https://docs.aws.amazon.com/neptune/latest/analytics/)
Amazon Neptune DB (with external vectors)

```
from mem0 import Memory

config = {
    "graph_store": {
        "provider": "neptunedb",
        "config": {
            "collection_name": "<VECTOR_COLLECTION_NAME>",
            "endpoint": "neptune-graph://<HOST_ENDPOINT>",
        },
    },
}

m = Memory.from_config(config_dict=config)

```
[Accessing Data in Neptune DB](https://docs.aws.amazon.com/neptune/latest/userguide/)
Kuzu (embedded)
`:memory:`
```
config = {
    "graph_store": {
        "provider": "kuzu",
        "config": {
            "db": "/tmp/mem0-example.kuzu"
        }
    }
}

```
`:memory:`[Kuzu documentation](https://kuzudb.com/docs/)[Enhanced Metadata Filtering](https://docs.mem0.ai/open-source/features/metadata-filtering)
## Enhanced Metadata Filtering
[Reranker-Enhanced Search](https://docs.mem0.ai/open-source/features/reranker-search)
## Reranker-Enhanced Search
