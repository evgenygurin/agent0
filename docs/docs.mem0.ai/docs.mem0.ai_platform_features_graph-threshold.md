# Configurable Graph Threshold - Mem0
Source: https://docs.mem0.ai/platform/features/graph-threshold
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​Overview
[​](https://docs.mem0.ai/platform/features/graph-threshold#overview)
## ​Configuration
[​](https://docs.mem0.ai/platform/features/graph-threshold#configuration)`threshold`
```
from mem0 import Memory

config = {
    "graph_store": {
        "provider": "neo4j",  # or memgraph, neptune, kuzu
        "config": {
            "url": "bolt://localhost:7687",
            "username": "neo4j",
            "password": "password"
        },
        "threshold": 0.7  # Default value, range: 0.0 to 1.0
    }
}

memory = Memory.from_config(config)

```

## ​Parameters
[​](https://docs.mem0.ai/platform/features/graph-threshold#parameters)`threshold`
## ​Use Cases
[​](https://docs.mem0.ai/platform/features/graph-threshold#use-cases)
### ​Strict Matching (UUIDs, IDs)
[​](https://docs.mem0.ai/platform/features/graph-threshold#strict-matching-uuids%2C-ids)
```
config = {
    "graph_store": {
        "provider": "neo4j",
        "config": {...},
        "threshold": 0.95  # Strict matching
    }
}

```
`MXxBUE18QVBQTElDQVRJT058MjM3MTM4NjI5``MXxBUE18QVBQTElDQVRJT058MjA2OTYxMzM`
### ​Permissive Matching (Natural Language)
[​](https://docs.mem0.ai/platform/features/graph-threshold#permissive-matching-natural-language)
```
config = {
    "graph_store": {
        "threshold": 0.6  # Permissive matching
    }
}

```

## ​Threshold Guidelines
[​](https://docs.mem0.ai/platform/features/graph-threshold#threshold-guidelines)
## ​Examples
[​](https://docs.mem0.ai/platform/features/graph-threshold#examples)
### ​Example 1: Preventing Data Loss with UUIDs
[​](https://docs.mem0.ai/platform/features/graph-threshold#example-1%3A-preventing-data-loss-with-uuids)
```
from mem0 import Memory

config = {
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "bolt://localhost:7687",
            "username": "neo4j",
            "password": "password"
        },
        "threshold": 0.98  # Very strict for UUIDs
    }
}

memory = Memory.from_config(config)

# These UUIDs create separate nodes instead of being incorrectly merged
memory.add(
    [{"role": "user", "content": "MXxBUE18QVBQTElDQVRJT058MjM3MTM4NjI5 relates to Project A"}],
    user_id="user1"
)

memory.add(
    [{"role": "user", "content": "MXxBUE18QVBQTElDQVRJT058MjA2OTYxMzM relates to Project B"}],
    user_id="user1"
)

```

### ​Example 2: Merging Entity Variations
[​](https://docs.mem0.ai/platform/features/graph-threshold#example-2%3A-merging-entity-variations)
```
config = {
    "graph_store": {
        "provider": "neo4j",
        "config": {...},
        "threshold": 0.6  # More permissive
    }
}

memory = Memory.from_config(config)

# These will be merged as the same entity
memory.add([{"role": "user", "content": "Bob works at Google"}], user_id="user1")
memory.add([{"role": "user", "content": "Robert works at Google"}], user_id="user1")

```

### ​Example 3: Different Thresholds for Different Clients
[​](https://docs.mem0.ai/platform/features/graph-threshold#example-3%3A-different-thresholds-for-different-clients)
```
# Client 1: Strict matching for transactional data
memory_strict = Memory.from_config({
    "graph_store": {"threshold": 0.95}
})

# Client 2: Permissive matching for conversational data
memory_permissive = Memory.from_config({
    "graph_store": {"threshold": 0.6}
})

```

## ​Supported Graph Providers
[​](https://docs.mem0.ai/platform/features/graph-threshold#supported-graph-providers)- ✅ Neo4j
- ✅ Memgraph
- ✅ Kuzu
- ✅ Neptune (both Analytics and DB)

## ​How It Works
[​](https://docs.mem0.ai/platform/features/graph-threshold#how-it-works)- Embedding Generation: The system generates embeddings for source and destination entities
- Node Search: Searches for existing nodes with similar embeddings
- Threshold Comparison: Compares similarity scores against the configured threshold
- Decision:If similarity ≥ threshold: Uses the existing nodeIf similarity < threshold: Creates a new node
- If similarity ≥ threshold: Uses the existing node
- If similarity < threshold: Creates a new node

```
# Pseudocode
if node_similarity >= threshold:
    use_existing_node()
else:
    create_new_node()

```

## ​Troubleshooting
[​](https://docs.mem0.ai/platform/features/graph-threshold#troubleshooting)
### ​Issue: Duplicate nodes being created
[​](https://docs.mem0.ai/platform/features/graph-threshold#issue%3A-duplicate-nodes-being-created)
```
config = {"graph_store": {"threshold": 0.6}}

```

### ​Issue: Unrelated entities being merged
[​](https://docs.mem0.ai/platform/features/graph-threshold#issue%3A-unrelated-entities-being-merged)
```
config = {"graph_store": {"threshold": 0.95}}

```

### ​Issue: Validation error
[​](https://docs.mem0.ai/platform/features/graph-threshold#issue%3A-validation-error)`ValidationError: threshold must be between 0.0 and 1.0`
```
config = {"graph_store": {"threshold": 0.7}}  # Valid: 0.0 ≤ x ≤ 1.0

```

## ​Backward Compatibility
[​](https://docs.mem0.ai/platform/features/graph-threshold#backward-compatibility)- Default Value: 0.7 (maintains existing behavior)
- Optional Parameter: Existing code works without any changes
- No Breaking Changes: Graceful fallback if not specified

## ​Related
[​](https://docs.mem0.ai/platform/features/graph-threshold#related)- Graph Memory
[Graph Memory](https://docs.mem0.ai/platform/features/graph-memory)- Issue #3590
[Issue #3590](https://github.com/mem0ai/mem0/issues/3590)