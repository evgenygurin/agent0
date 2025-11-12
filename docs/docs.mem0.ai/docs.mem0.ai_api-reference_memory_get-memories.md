# Get Memories - Mem0
Source: https://docs.mem0.ai/api-reference/memory/get-memories
Downloaded: 2025-11-12 21:20:22
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
memories = client.get_all(
    filters={
        "AND": [
            {
                "user_id": "alex"
            },
            {
                "created_at": {"gte": "2024-07-01", "lte": "2024-07-31"}
            }
        ]
    }
)

```

## ​Graph Memory
[​](https://docs.mem0.ai/api-reference/memory/get-memories#graph-memory)`output_format="v1.1"`
```
memories = client.get_all(
    filters={
        "user_id": "alex"
    },
    output_format="v1.1"
)

```

#### Authorizations
[​](https://docs.mem0.ai/api-reference/memory/get-memories#authorization-authorization)
API key authentication. Prefix your Mem0 API key with 'Token '. Example: 'Token your_api_key'

#### Body
[​](https://docs.mem0.ai/api-reference/memory/get-memories#body-filters)
A dictionary of filters to apply to retrieve memories. Available fields are: user_id, agent_id, app_id, run_id, created_at, updated_at, categories, keywords. Supports logical operators (AND, OR) and comparison operators (in, gte, lte, gt, lt, ne, contains, icontains, *). For categories field, use 'contains' for partial matching (e.g., {"categories": {"contains": "finance"}}) or 'in' for exact matching (e.g., {"categories": {"in": ["personal_information"]}}).

Showchild attributes
[​](https://docs.mem0.ai/api-reference/memory/get-memories#body-fields)
A list of field names to include in the response. If not provided, all fields will be returned.
[​](https://docs.mem0.ai/api-reference/memory/get-memories#body-page)
Page number for pagination. Default: 1
[​](https://docs.mem0.ai/api-reference/memory/get-memories#body-page-size)
Number of items per page. Default: 100
[​](https://docs.mem0.ai/api-reference/memory/get-memories#body-org-id)
The unique identifier of the organization associated with the memory.
[​](https://docs.mem0.ai/api-reference/memory/get-memories#body-project-id)
The unique identifier of the project associated with the memory.

#### Response

Successfully retrieved memories.
[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-id)[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-memory)[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-created-at)[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-updated-at)[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-owner)[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-organization)[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-immutable)
Whether the memory is immutable.
[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-expiration-date)
The date and time when the memory will expire. Format: YYYY-MM-DD.
[​](https://docs.mem0.ai/api-reference/memory/get-memories#response-metadata)