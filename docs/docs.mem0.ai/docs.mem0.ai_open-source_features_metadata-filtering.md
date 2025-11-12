# Enhanced Metadata Filtering - Mem0
Source: https://docs.mem0.ai/open-source/features/metadata-filtering
Downloaded: 2025-11-12 21:20:19
================================================================================

- Retrieval must respect multiple metadata conditions before returning context.
- You need to mix numeric, boolean, and string filters in a single query.
- Agents rely on deterministic filtering instead of broad semantic search alone.

## ​Feature anatomy
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#feature-anatomy)
Operator quick reference
`eq``ne``gt``gte``lt``lte``in``nin``contains``icontains``*``AND``OR``NOT`
### ​Metadata selectors
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#metadata-selectors)
```
from mem0 import Memory

m = Memory()

# Search with simple metadata filters
results = m.search(
    "What are my preferences?",
    user_id="alice",
    filters={"category": "preferences"}
)

```
`category="preferences"``user_id`
### ​Comparison operators
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#comparison-operators)`eq``ne`
```
# Greater than / Less than
results = m.search(
    "recent activities",
    user_id="alice",
    filters={
        "score": {"gt": 0.8},
        "priority": {"gte": 5},
        "confidence": {"lt": 0.9},
        "rating": {"lte": 3}
    }
)

# Equality operators
results = m.search(
    "specific content",
    user_id="alice",
    filters={
        "status": {"eq": "active"},
        "archived": {"ne": True}
    }
)

```

### ​List-based operators
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#list-based-operators)`in``nin`
```
# In / Not in operators
results = m.search(
    "multi-category search",
    user_id="alice",
    filters={
        "category": {"in": ["food", "travel", "entertainment"]},
        "status": {"nin": ["deleted", "archived"]}
    }
)

```

### ​String operators
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#string-operators)`contains``icontains`
```
# Text matching operators
results = m.search(
    "content search",
    user_id="alice",
    filters={
        "title": {"contains": "meeting"},
        "description": {"icontains": "important"},
        "tags": {"contains": "urgent"}
    }
)

```

### ​Wildcard matching
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#wildcard-matching)
```
# Match any value for a field
results = m.search(
    "all with category",
    user_id="alice",
    filters={
        "category": "*"
    }
)

```

### ​Logical combinations
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#logical-combinations)`AND``OR``NOT`
```
# Logical AND
results = m.search(
    "complex query",
    user_id="alice",
    filters={
        "AND": [
            {"category": "work"},
            {"priority": {"gte": 7}},
            {"status": {"ne": "completed"}}
        ]
    }
)

# Logical OR
results = m.search(
    "flexible query",
    user_id="alice",
    filters={
        "OR": [
            {"category": "urgent"},
            {"priority": {"gte": 9}},
            {"deadline": {"contains": "today"}}
        ]
    }
)

# Logical NOT
results = m.search(
    "exclusion query",
    user_id="alice",
    filters={
        "NOT": [
            {"category": "archived"},
            {"status": "deleted"}
        ]
    }
)

# Complex nested logic
results = m.search(
    "advanced query",
    user_id="alice",
    filters={
        "AND": [
            {
                "OR": [
                    {"category": "work"},
                    {"category": "personal"}
                ]
            },
            {"priority": {"gte": 5}},
            {
                "NOT": [
                    {"status": "archived"}
                ]
            }
        ]
    }
)

```

## ​Configure it
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#configure-it)
```
# Ensure your vector store supports indexing on filtered fields
config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "indexed_fields": ["category", "priority", "status", "user_id"]
        }
    }
}

```

```
# More efficient: Filter on indexed fields first
good_filters = {
    "AND": [
        {"user_id": "alice"},
        {"category": "work"},
        {"content": {"contains": "meeting"}}
    ]
}

# Less efficient: Complex operations first
avoid_filters = {
    "AND": [
        {"description": {"icontains": "complex text search"}},
        {"user_id": "alice"}
    ]
}

```
`good_filters``avoid_filters`
Qdrant

Chroma

Pinecone
`in``nin`
Weaviate

### ​Migrate from earlier filters
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#migrate-from-earlier-filters)
```
# Before (v0.x) - simple key-value filtering only
results = m.search(
    "query",
    user_id="alice",
    filters={"category": "work", "status": "active"}
)

# After (v1.0.0) - enhanced filtering with operators
results = m.search(
    "query",
    user_id="alice",
    filters={
        "AND": [
            {"category": "work"},
            {"status": {"ne": "archived"}},
            {"priority": {"gte": 5}}
        ]
    }
)

```

## ​See it in action
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#see-it-in-action)
### ​Project management filtering
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#project-management-filtering)
```
# Find high-priority active tasks
results = m.search(
    "What tasks need attention?",
    user_id="project_manager",
    filters={
        "AND": [
            {"project": {"in": ["alpha", ""]}},
            {"priority": {"gte": 8}},
            {"status": {"ne": "completed"}},
            {
                "OR": [
                    {"assignee": "alice"},
                    {"assignee": "bob"}
                ]
            }
        ]
    }
)

```

### ​Customer support filtering
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#customer-support-filtering)
```
# Find recent unresolved tickets
results = m.search(
    "pending support issues",
    agent_id="support_bot",
    filters={
        "AND": [
            {"ticket_status": {"ne": "resolved"}},
            {"priority": {"in": ["high", "critical"]}},
            {"created_date": {"gte": "2024-01-01"}},
            {
                "NOT": [
                    {"category": "spam"}
                ]
            }
        ]
    }
)

```
`agent_id`
### ​Content recommendation filtering
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#content-recommendation-filtering)
```
# Personalized content filtering
results = m.search(
    "recommend content",
    user_id="reader123",
    filters={
        "AND": [
            {
                "OR": [
                    {"genre": {"in": ["sci-fi", "fantasy"]}},
                    {"author": {"contains": "favorite"}}
                ]
            },
            {"rating": {"gte": 4.0}},
            {"read_status": {"ne": "completed"}},
            {"language": "english"}
        ]
    }
)

```

### ​Handle invalid operators
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#handle-invalid-operators)
```
try:
    results = m.search(
        "test query",
        user_id="alice",
        filters={
            "invalid_operator": {"unknown": "value"}
        }
    )
except ValueError as e:
    print(f"Filter error: {e}")
    results = m.search(
        "test query",
        user_id="alice",
        filters={"category": "general"}
    )

```

## ​Verify the feature is working
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#verify-the-feature-is-working)- Log the filters sent to your vector store and confirm the response metadata matches every clause.
- Benchmark queries before and after indexing to ensure latency improvements materialize.
- Add analytics or debug logging to track how often fallbacks execute when operators fail validation.

## ​Best practices
[​](https://docs.mem0.ai/open-source/features/metadata-filtering#best-practices)- Use indexed fields first:Order filters so equality checks run before complex string operations.
- Combine operators intentionally:Keep logical trees readable—large nests are harder to debug.
- Test performance regularly:Benchmark critical queries with production-like payloads.
- Plan graceful degradation:Provide fallback filters when an operator isn’t available.
- Validate syntax early:Catch malformed filters during development to protect agents at runtime.
[Explore Vector Store OptionsCompare operator coverage and indexing strategies across supported stores.](https://docs.mem0.ai/components/vectordbs/overview)
## Explore Vector Store Options
[Tag and Organize MemoriesPractice building workflows that label and retrieve memories with clear metadata filters.](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories)
## Tag and Organize Memories
