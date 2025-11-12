# Search Memories - Mem0
Source: https://docs.mem0.ai/api-reference/memory/search-memories
Downloaded: 2025-11-12 21:20:21
================================================================================

- in: Matches any of the values specified
`in`- gte: Greater than or equal to
`gte`- lte: Less than or equal to
`lte`- gt: Greater than
`gt`- lt: Less than
`lt`- ne: Not equal to
`ne`- icontains: Case-insensitive containment check
`icontains`- *: Wildcard character that matches everything
`*`
```
related_memories = client.search(
    query="What are Alice's hobbies?",
    filters={
        "OR": [
            {
              "user_id": "alice"
            },
            {
              "agent_id": {"in": ["travel-agent", "sports-agent"]}
            }
        ]
    },
)

```

```
# Using wildcard to match all run_ids for a specific user
all_memories = client.search(
    query="What are Alice's hobbies?",
    filters={
        "AND": [
            {
                "user_id": "alice"
            },
            {
                "run_id": "*"
            }
        ]
    },
)

```

```
# Example 1: Using 'contains' for partial matching
finance_memories = client.search(
    query="What are my financial goals?",
    filters={
        "AND": [
            { "user_id": "alice" },
            {
                "categories": {
                    "contains": "finance"
                }
            }
        ]
    },
)

# Example 2: Using 'in' for exact matching
personal_memories = client.search(
    query="What personal information do you have?",
    filters={
        "AND": [
            { "user_id": "alice" },
            {
                "categories": {
                    "in": ["personal_information"]
                }
            }
        ]
    },
)

```

#### Authorizations
[​](https://docs.mem0.ai/api-reference/memory/search-memories#authorization-authorization)
API key authentication. Prefix your Mem0 API key with 'Token '. Example: 'Token your_api_key'

#### Body
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-query)
The query to search for in the memory.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-filters)
A dictionary of filters to apply to the search. Available fields are: user_id, agent_id, app_id, run_id, created_at, updated_at, categories, keywords. Supports logical operators (AND, OR) and comparison operators (in, gte, lte, gt, lt, ne, contains, icontains). For categories field, use 'contains' for partial matching (e.g., {"categories": {"contains": "finance"}}) or 'in' for exact matching (e.g., {"categories": {"in": ["personal_information"]}}).

Showchild attributes
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-version)
The version of the memory to use. This should always be v2.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-top-k)
The number of top results to return.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-fields)
A list of field names to include in the response. If not provided, all fields will be returned.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-rerank)
Whether to rerank the memories.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-keyword-search)
Whether to search for memories based on keywords.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-filter-memories)
Whether to filter the memories.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-threshold)
The minimum similarity threshold for returned results.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-org-id)
The unique identifier of the organization associated with the memory.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#body-project-id)
The unique identifier of the project associated with the memory.

#### Response

Successfully retrieved search results.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-id)
Unique identifier for the memory.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-memory)
The content of the memory
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-user-id)
The identifier of the user associated with this memory
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-created-at)
The timestamp when the memory was created.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-updated-at)
The timestamp when the memory was last updated.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-metadata)
Additional metadata associated with the memory
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-categories)
Categories associated with the memory
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-immutable)
Whether the memory is immutable.
[​](https://docs.mem0.ai/api-reference/memory/search-memories#response-expiration-date)
The date and time when the memory will expire. Format: YYYY-MM-DD.
