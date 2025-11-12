# Choose Vector vs Graph Memory - Mem0
Source: https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Vector and Graph Stores
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#vector-and-graph-stores)
## ​Starting Simple
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#starting-simple)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")
# Add employee info
client.add("Emma is a software engineer in Seattle", user_id="company_kb")
client.add("David is a product manager in Austin", user_id="company_kb")


```

```
results = client.search("What does Emma do?", filters={"user_id": "company_kb"})
print(results['results'][0]['memory'])


```

```
Emma is a software engineer in Seattle


```

## ​Adding Team Structure
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#adding-team-structure)
```
client.add("Emma works with David on the mobile app redesign", user_id="company_kb")
client.add("David reports to Rachel, who manages the design team", user_id="company_kb")


```
- Emma works with David
- David reports to Rachel

```
results = client.search(
    "Who is Emma's teammate's manager?",
    filters={"user_id": "company_kb"}
)

for r in results['results']:
    print(r['memory'])


```

```
Emma works with David on the mobile app redesign
David reports to Rachel, who manages the design team


```
- Emma’s teammate is David (from memory 1)
- David’s manager is Rachel (from memory 2)
- So the answer is Rachel

## ​Enter Graph Memory
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#enter-graph-memory)
```
client.add(
    "Emma works with David on the mobile app redesign",
    user_id="company_kb",
    enable_graph=True
)

client.add(
    "David reports to Rachel, who manages the design team",
    user_id="company_kb",
    enable_graph=True
)


```
`enable_graph=True`- emma --[works_with]--> david
`emma --[works_with]--> david`- david --[reports_to]--> rachel
`david --[reports_to]--> rachel`- rachel --[manages]--> design_team
`rachel --[manages]--> design_team`
```
results = client.search(
    "Who is Emma's teammate's manager?",
    filters={"user_id": "company_kb"},
    enable_graph=True
)

print(results['results'][0]['memory'])
print("\\nRelationships found:")
for rel in results.get('relations', []):
    print(f"  {rel['source']}, {rel['target']} ({rel['relationship']})")


```

```
David reports to Rachel, who manages the design team

Relationships found:
  emma, david (works_with)
  david, rachel (reports_to)


```

## ​How It Connects
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#how-it-connects)
## ​When to Use Each
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#when-to-use-each)- Searching documents by semantic similarity
- Looking up facts that don’t need relationships
- Building FAQs or knowledge bases where each item stands alone
- Tracking organizational hierarchies (who reports to whom)
- Understanding project teams (who collaborates with whom)
- Building CRMs (which contacts connect to which companies)
- Product recommendations (what items are bought together)
- Vector for individual facts: “Emma specializes in React”
- Graph for relationships: “Emma works with David”

## ​Putting It Together
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#putting-it-together)
```
# Facts about individuals - vector store is fine
client.add("Emma specializes in React and TypeScript", user_id="company_kb")
client.add("David has 5 years of product management experience", user_id="company_kb")

# Relationships - use graph memory
client.add(
    "Emma and David work together on the mobile app",
    user_id="company_kb",
    enable_graph=True
)

client.add(
    "David reports to Rachel",
    user_id="company_kb",
    enable_graph=True
)

client.add(
    "Rachel runs weekly team syncs every Tuesday",
    user_id="company_kb",
    enable_graph=True
)


```

```
# Direct fact - vector search
results = client.search("What are Emma's skills?", filters={"user_id": "company_kb"})
print(results['results'][0]['memory'])


```

```
Emma specializes in React and TypeScript


```

```
# Multi-hop relationship - graph search
results = client.search(
    "What meetings does Emma's project manager's boss run?",
    filters={"user_id": "company_kb"},
    enable_graph=True
)
print(results['results'][0]['memory'])


```

```
Rachel runs weekly team syncs every Tuesday


```

## ​The Tradeoff
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#the-tradeoff)`client.add()``enable_graph=True``add()`
```
# Long-term organizational structure - worth using graph
client.add(
    "Emma mentors two junior engineers on the frontend team",
    user_id="company_kb",
    enable_graph=True
)

# Temporary notes - skip graph, not worth the cost
client.add(
    "Emma is out sick today",
    user_id="company_kb",
    run_id="daily_notes"
)


```

## ​Enabling Graph Memory
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#enabling-graph-memory)
```
client.add("Emma works with David", user_id="company_kb", enable_graph=True)
client.search("team structure", filters={"user_id": "company_kb"}, enable_graph=True)


```

```
client.project.update(enable_graph=True)

# Now every add uses graph automatically
client.add("Emma mentors Jordan", user_id="company_kb")


```

## ​What You Built
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#what-you-built)- Vector search- Fast semantic lookups for individual facts (Emma’s skills, David’s experience)
- Graph memory- Multi-hop relationship traversal (Emma’s teammate’s manager, project hierarchies)
- Selective enablement- Graph only for long-term organizational structure, vector for everything else
- Cost optimization- Skip graph extraction for temporary notes and simple facts

## ​Summary
[​](https://docs.mem0.ai/cookbooks/essentials/choosing-memory-architecture-vector-vs-graph#summary)[Build AI with PersonalityScope memories across user and agent IDs to balance personalization and reuse.](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality)
## Build AI with Personality
[Export Everything SafelyLearn how to migrate or audit stored memories with structured exports.](https://docs.mem0.ai/cookbooks/essentials/exporting-memories)
## Export Everything Safely
