# Export Stored Memories - Mem0
Source: https://docs.mem0.ai/cookbooks/essentials/exporting-memories
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Setup
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#setup)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")


```
[dashboard](https://app.mem0.ai)
```
# Dev's work history
client.add(
    "Dev works at TechCorp as a senior engineer",
    user_id="dev",
    metadata={"type": "professional"}
)

# Arjun's preferences
client.add(
    "Arjun prefers morning meetings and async communication",
    user_id="arjun",
    metadata={"type": "preference"}
)

# Carl's project notes
client.add(
    "Carl is leading the API redesign project, targeting Q2 launch",
    user_id="carl",
    metadata={"type": "project"}
)


```

## ​Getting All Memories
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#getting-all-memories)`get_all()`
```
dev_memories = client.get_all(
    filters={"user_id": "dev"},
    page_size=50
)

print(f"Total memories: {dev_memories['count']}")
print(f"First memory: {dev_memories['results'][0]['memory']}")


```

```
Total memories: 1
First memory: Dev works at TechCorp as a senior engineer


```
`get_all()`
```
carl_projects = client.get_all(
    filters={
        "AND": [
            {"user_id": "carl"},
            {"metadata": {"type": "project"}}
        ]
    }
)

for memory in carl_projects['results']:
    print(memory['memory'])


```

```
Carl is leading the API redesign project, targeting Q2 launch


```

## ​Searching Memories
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#searching-memories)`search()`
```
results = client.search(
    query="What does Dev do for work?",
    filters={"user_id": "dev"},
    top_k=5
)

for result in results['results']:
    print(f"{result['memory']} (score: {result['score']:.2f})")


```

```
Dev works at TechCorp as a senior engineer (score: 0.89)


```
`get_all()`
## ​Exporting to Structured Format
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#exporting-to-structured-format)
### ​Step 1: Define the schema
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#step-1%3A-define-the-schema)
```
professional_profile_schema = {
    "properties": {
        "full_name": {
            "type": "string",
            "description": "The person's full name"
        },
        "current_role": {
            "type": "string",
            "description": "Current job title or role"
        },
        "company": {
            "type": "string",
            "description": "Current employer"
        }
    },
    "title": "ProfessionalProfile",
    "type": "object"
}


```

### ​Step 2: Create export job
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#step-2%3A-create-export-job)
```
export_job = client.create_memory_export(
    schema=professional_profile_schema,
    filters={"user_id": "dev"}
)

print(f"Export ID: {export_job['id']}")
print(f"Status: {export_job['status']}")


```

```
Export ID: exp_abc123
Status: processing


```
`get_memory_export()`
### ​Step 3: Download the export
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#step-3%3A-download-the-export)
```
# Get by ID
export_data = client.get_memory_export(
    memory_export_id=export_job['id']
)

print(export_data['data'])


```

```
{
  "full_name": "Dev",
  "current_role": "senior engineer",
  "company": "TechCorp"
}


```

```
# Get latest export matching filters
export_by_filters = client.get_memory_export(
    filters={"user_id": "dev"}
)

print(export_by_filters['data'])


```

## ​Adding Export Instructions
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#adding-export-instructions)
```
export_with_instructions = client.create_memory_export(
    schema=professional_profile_schema,
    filters={"user_id": "arjun"},
    export_instructions="""
1. Use the most recent information if there are conflicts
2. Only include confirmed facts, not speculation
3. Return null for missing fields rather than guessing
"""
)


```
`get_memory_export()``status == "completed"`
## ​Platform Export
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#platform-export)- Navigate toMemory Exportsin your project dashboard
- ClickCreate Export
- Select your filters and schema
- Download the completed export as JSON

## ​What You Built
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#what-you-built)- Bulk retrieval (get_all)- Fetch all memories matching filters for comprehensive audits
- Semantic search- Query-based lookups with relevance scoring
- Structured exports- Pydantic-schema exports for migrations and compliance
- Export instructions- Guide conflict resolution and data formatting
- Platform UI exports- One-off manual downloads via dashboard

## ​Summary
[​](https://docs.mem0.ai/cookbooks/essentials/exporting-memories#summary)`get_all()``search()``create_memory_export()`[Expire Short-Term DataKeep exports lean by clearing session context before you archive it.](https://docs.mem0.ai/cookbooks/essentials/memory-expiration-short-and-long-term)
## Expire Short-Term Data
[Control Memory IngestionEnsure only verified insights make it into your export pipeline.](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion)
## Control Memory Ingestion
