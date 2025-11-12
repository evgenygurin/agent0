# Memory Export - Mem0
Source: https://docs.mem0.ai/platform/features/memory-export
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Overview
[​](https://docs.mem0.ai/platform/features/memory-export#overview)
## ​Creating a Memory Export
[​](https://docs.mem0.ai/platform/features/memory-export#creating-a-memory-export)- Define your schema structure
- Submit an export job
- Retrieve the exported data

### ​Define Schema
[​](https://docs.mem0.ai/platform/features/memory-export#define-schema)
```
{
    "$defs": {
        "EducationLevel": {
            "enum": ["high_school", "bachelors", "masters"],
            "title": "EducationLevel",
            "type": "string"
        },
        "EmploymentStatus": {
            "enum": ["full_time", "part_time", "student"],
            "title": "EmploymentStatus", 
            "type": "string"
        }
    },
    "properties": {
        "full_name": {
            "anyOf": [
                {
                    "maxLength": 100,
                    "minLength": 2,
                    "type": "string"
                },
                {
                    "type": "null"
                }
            ],
            "default": null,
            "description": "The professional's full name",
            "title": "Full Name"
        },
        "current_role": {
            "anyOf": [
                {
                    "type": "string"
                },
                {
                    "type": "null"
                }
            ],
            "default": null,
            "description": "Current job title or role",
            "title": "Current Role"
        }
    },
    "title": "ProfessionalProfile",
    "type": "object"
}

```

### ​Submit Export Job
[​](https://docs.mem0.ai/platform/features/memory-export#submit-export-job)`export_instructions`
```
# Basic export request
filters = {"user_id": "alice"}
response = client.create_memory_export(
    schema=json_schema,
    filters=filters
)

# Export with custom instructions and additional filters
export_instructions = """
1. Create a comprehensive profile with detailed information in each category
2. Only mark fields as "None" when absolutely no relevant information exists
3. Base all information directly on the user's memories
4. When contradictions exist, prioritize the most recent information
5. Clearly distinguish between factual statements and inferences
"""

filters = {
    "AND": [
        {"user_id": "alex"},
        {"created_at": {"gte": "2024-01-01"}}
    ]
}

response = client.create_memory_export(
    schema=json_schema,
    filters=filters,
    export_instructions=export_instructions  # Optional
)

print(response)

```

### ​Retrieve Export
[​](https://docs.mem0.ai/platform/features/memory-export#retrieve-export)
#### ​Using Export ID
[​](https://docs.mem0.ai/platform/features/memory-export#using-export-id)
```
# Retrieve using export ID
response = client.get_memory_export(memory_export_id="550e8400-e29b-41d4-a716-446655440000")
print(response)

```

#### ​Using Filters
[​](https://docs.mem0.ai/platform/features/memory-export#using-filters)
```
# Retrieve using filters
filters = {
    "AND": [
        {"created_at": {"gte": "2024-07-10", "lte": "2024-07-20"}},
        {"user_id": "alex"}
    ]
}

response = client.get_memory_export(filters=filters)
print(response)

```

## ​Available Filters
[​](https://docs.mem0.ai/platform/features/memory-export#available-filters)- user_id: Filter memories by specific user
`user_id`- agent_id: Filter memories by specific agent
`agent_id`- run_id: Filter memories by specific run
`run_id`- session_id: Filter memories by specific session
`session_id`- created_at: Filter memories by date
`created_at`[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
