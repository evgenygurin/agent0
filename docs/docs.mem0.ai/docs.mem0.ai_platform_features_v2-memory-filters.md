# Memory Filters v2 - Mem0
Source: https://docs.mem0.ai/platform/features/v2-memory-filters
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Quick Start
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#quick-start)
### ​Memories for a specific user
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#memories-for-a-specific-user)
```
{
  "AND": [
    { "user_id": "u1" }
  ]
}

```

### ​User memories across all runs
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#user-memories-across-all-runs)
```
{
  "AND": [
    { "user_id": "u1" },
    { "run_id": "*" }
  ]
}

```

## ​Filter Structure
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#filter-structure)- Root must beANDorOR(orNOT) containing anarrayof conditions.
`AND``OR``NOT`- Aconditionis either a simple equality{ "user_id": "u1" }or an operator clause{ "created_at": { "gte": "..." } }.
`{ "user_id": "u1" }``{ "created_at": { "gte": "..." } }`
```
{
  "AND": [
    { "user_id": "u1" },
    { "run_id": "*" },
    { "created_at": { "lt": "2025-06-01T00:00:00Z" } },
    { "categories": { "in": ["finance", "health"] } }
  ]
}

```

```
{ "AND": [ /* conditions... */ ] }
{ "OR":  [ /* conditions... */ ] }
{ "NOT": [ /* conditions... */ ] }

```

## ​Available Fields
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#available-fields)`user_id``agent_id``app_id``run_id`
## ​Wildcards
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#wildcards)`"*"``*`
```
{ "AND": [ { "user_id": "*" } ] }       // any record with a user_id
{ "AND": [ { "user_id": "*" }, { "run_id": "*" } ] } // require both non-null
{ "OR":  [ { "user_id": "*" }, { "run_id": "*" } ] } // either non-null

```

## ​Operators and Fields
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#operators-and-fields)- Entities:user_id,agent_id,app_id,run_id
`user_id``agent_id``app_id``run_id`- Time:created_at,updated_at,timestamp
`created_at``updated_at``timestamp`- Content:categories,metadata,keywords
`categories``metadata``keywords`- Special:memory_ids(array of IDs)
`memory_ids`- in: Matches any of the values specified
`in`- gte: Greater than or equal to
`gte`- lte: Less than or equal to
`lte`- gt: Greater than
`gt`- lt: Less than
`lt`- ne: Not equal to
`ne`- contains: Case-sensitive containment check
`contains`- icontains: Case-insensitive containment check
`icontains`- *: Wildcard character that matches everything
`*`
```
// Entity fields
{ "user_id": "u1" }
{ "agent_id": "a1" }
{ "app_id": "app1" }
{ "run_id": "run1" }

// Time fields
{ "created_at": { "gte": "2025-01-01T00:00:00Z" } }
{ "updated_at": { "lt": "2025-02-01T00:00:00Z" } }

// Categories (exact matching)
{ "categories": { "in": ["personal_information", "finance"] } }
// Categories (partial matching)
{ "categories": { "contains": "finance" } }

// Metadata (exact key-value match)
{ "metadata": { "key": "value" } }

// Keywords (text search)
{ "keywords": { "icontains": "budget" } }

// Memory IDs
{ "memory_ids": ["m1", "m2", "m3"] }

```
- eqis implied:{ "user_id": "u1" }≡{ "user_id": { "eq": "u1" } }
`eq``{ "user_id": "u1" }``{ "user_id": { "eq": "u1" } }`- neincludesNULLs: results where the field is eithernot equalormissing
`ne`- Forcategories, usecontainsfor partial matching orinfor exact matching
`categories``contains``in`
## ​Examples
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#examples)
### ​User and Agent Filters
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#user-and-agent-filters)
```
{ "AND": [ { "user_id": "u1" } ] }

```

```
{ "AND": [ { "user_id": "*" } ] }

```

```
{ "AND": [ { "user_id": "u1" }, { "run_id": "*" } ] }

```

```
{ "AND": [ { "agent_id": "a1" } ] }

```

```
{ "AND": [ { "agent_id": "a1" }, { "run_id": "*" } ] }

```

### ​Content and Text Filters
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#content-and-text-filters)
```
{ "AND": [
  { "user_id": "u1" },
  { "keywords": { "icontains": "pizza" } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "keywords": { "contains": "BudgetQ1" } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "categories": { "in": ["finance", "health"] } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "metadata": { "foo": "bar" } }
] }

```

### ​Time-based Filters
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#time-based-filters)
```
{ "AND": [
  { "user_id": "u1" },
  { "created_at": { "gt": "2025-01-01T00:00:00Z" } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "created_at": { "gte": "2025-01-01T00:00:00Z" } },
  { "created_at": { "lt":  "2025-02-01T00:00:00Z" } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "updated_at": { "gte": "2025-05-01T00:00:00Z" } },
  { "updated_at": { "lte": "2025-05-31T23:59:59Z" } }
] }

```

### ​Advanced Filters
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#advanced-filters)
```
{ "AND": [ { "user_id": { "in": ["u1", "u2", "u3"] } } ] }

```

```
{ "OR": [ { "user_id": "u1" }, { "run_id": "run1" } ] }

```

```
{ "AND": [ { "user_id": "*" }, { "run_id": "*" } ] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "NOT": { "categories": { "in": ["spam", "test"] } } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "memory_ids": ["m1", "m2", "m3"] }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "keywords": { "icontains": "invoice" } },
  { "categories": { "in": ["finance"] } },
  { "created_at": { "gte": "2025-03-01T00:00:00Z" } }
] }

```

### ​Comprehensive Filters
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#comprehensive-filters)
```
{ "AND": [ 
  { "user_id": "*" }, 
  { "agent_id": "*" }, 
  { "run_id": "*" }, 
  { "app_id": "*" } 
] }

```

```
{ "OR": [ 
  { "user_id": "*" }, 
  { "agent_id": "*" }, 
  { "run_id": "*" }, 
  { "app_id": "*" } 
] }

```

## ​Common Patterns
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#common-patterns)
```
{ "AND": [ { "user_id": "u1" } ] }

```

```
{ "AND": [ { "user_id": "u1" }, { "run_id": "*" } ] }

```

```
{ "AND": [ { "user_id": "*" } ] }

```

```
{ "AND": [ { "agent_id": "a1" }, { "user_id": { "in": ["u1", "u2"] } } ] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "keywords": { "icontains": "budget" } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "created_at": { "gte": "<from>" } },
  { "created_at": { "lt": "<to>" } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "NOT": { "categories": { "in": ["spam", "test"] } } }
] }

```

```
{ "AND": [
  { "user_id": "u1" },
  { "memory_ids": ["id1", "id2"] }
] }

```

## ​Troubleshooting
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#troubleshooting)
### ​”I filtered byuser_id, but I don’t see items that have anagent_id.”
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#%E2%80%9Di-filtered-by-user-id%2C-but-i-don%E2%80%99t-see-items-that-have-an-agent-id-%E2%80%9D)`user_id``agent_id``{ "user_id": "u1" }``agent_id = NULL``run_id = NULL``app_id = NULL``{ "agent_id": "*" }`
```
{ "AND": [ { "user_id": "u1" }, { "agent_id": "*" } ] }

```

### ​”Myneseems to return more than I expect.”
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#%E2%80%9Dmy-ne-seems-to-return-more-than-i-expect-%E2%80%9D)`ne``ne`
```
{ "AND": [ { "agent_id": "*" }, { "agent_id": { "ne": "a1" } } ] }

```

### ​”Case-insensitive search?”
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#%E2%80%9Dcase-insensitive-search%3F%E2%80%9D)`icontains`
```
{ "AND": [ { "keywords": { "icontains": "receipt" } } ] }

```

### ​”Between two dates?”
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#%E2%80%9Dbetween-two-dates%3F%E2%80%9D)`gte``lt``lte`
```
{ "AND": [
  { "user_id": "u1" },
  { "created_at": { "gte": "2025-01-01T00:00:00Z" } },
  { "created_at": { "lt":  "2025-02-01T00:00:00Z" } }
] }

```

### ​”Complex logic with NOT”
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#%E2%80%9Dcomplex-logic-with-not%E2%80%9D)`NOT``u1``spam``test`
```
{ "AND": [
  { "user_id": "u1" },
  { "NOT": { "categories": { "in": ["spam", "test"] } } }
] }

```

### ​”Metadata matching isn’t working.”
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#%E2%80%9Dmetadata-matching-isn%E2%80%99t-working-%E2%80%9D)
```
{ "AND": [ { "metadata": { "foo": "bar" } } ] }

```

### ​”I want all users, all agents, all runs.”
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#%E2%80%9Di-want-all-users%2C-all-agents%2C-all-runs-%E2%80%9D)
```
{ "AND": [ { "user_id": "*" }, { "agent_id": "*" }, { "run_id": "*" } ] }

```

## ​FAQ
[​](https://docs.mem0.ai/platform/features/v2-memory-filters#faq)`AND``OR``AND``OR``NOT``"*"``NULL``eq``{ "user_id": "u1" }``ne``{ "field": "*" }``ne``keywords``contains``icontains``{ "metadata": { "foo": "bar" } }`