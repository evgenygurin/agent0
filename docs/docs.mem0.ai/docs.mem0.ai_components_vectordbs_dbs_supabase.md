# Supabase - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/supabase
Downloaded: 2025-11-12 21:20:20
================================================================================

[Supabase](https://supabase.com/)[Supabase](https://supabase.com/dashboard/projects)[docs](https://supabase.github.io/vecs/hosting/)
### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/supabase#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "supabase",
        "config": {
            "connection_string": "postgresql://user:password@host:port/database",
            "collection_name": "memories",
            "index_method": "hnsw",  # Optional: defaults to "auto"
            "index_measure": "cosine_distance"  # Optional: defaults to "cosine_distance"
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```

### ​SQL Migrations for TypeScript Implementation
[​](https://docs.mem0.ai/components/vectordbs/dbs/supabase#sql-migrations-for-typescript-implementation)
```
-- Enable the vector extension
create extension if not exists vector;

-- Create the memories table
create table if not exists memories (
  id text primary key,
  embedding vector(1536),
  metadata jsonb,
  created_at timestamp with time zone default timezone('utc', now()),
  updated_at timestamp with time zone default timezone('utc', now())
);

-- Create the vector similarity search function
create or replace function match_vectors(
  query_embedding vector(1536),
  match_count int,
  filter jsonb default '{}'::jsonb
)
returns table (
  id text,
  similarity float,
  metadata jsonb
)
language plpgsql
as $$
begin
  return query
  select
    t.id::text,
    1 - (t.embedding <=> query_embedding) as similarity,
    t.metadata
  from memories t
  where case
    when filter::text = '{}'::text then true
    else t.metadata @> filter
  end
  order by t.embedding <=> query_embedding
  limit match_count;
end;
$$;

```
[Supabase](https://supabase.com/dashboard/projects)
### ​Config
[​](https://docs.mem0.ai/components/vectordbs/dbs/supabase#config)- Python
- TypeScript
`connection_string``collection_name``mem0``embedding_model_dims``1536``index_method``auto``index_measure``cosine_distance`
### ​Index Methods
[​](https://docs.mem0.ai/components/vectordbs/dbs/supabase#index-methods)- auto: Automatically selects the best available index method
`auto`- hnsw: Hierarchical Navigable Small World graph index (faster search, more memory usage)
`hnsw`- ivfflat: Inverted File Flat index (good balance of speed and memory)
`ivfflat`
### ​Distance Measures
[​](https://docs.mem0.ai/components/vectordbs/dbs/supabase#distance-measures)- cosine_distance: Cosine similarity (recommended for most embedding models)
`cosine_distance`- l2_distance: Euclidean distance
`l2_distance`- l1_distance: Manhattan distance
`l1_distance`- max_inner_product: Maximum inner product similarity
`max_inner_product`
### ​Best Practices
[​](https://docs.mem0.ai/components/vectordbs/dbs/supabase#best-practices)- Index Method Selection:Usehnswfor fastest search performance when memory is not a constraintUseivfflatfor a good balance of search speed and memory usageUseautoif unsure, it will select the best method based on your data
- Usehnswfor fastest search performance when memory is not a constraint
`hnsw`- Useivfflatfor a good balance of search speed and memory usage
`ivfflat`- Useautoif unsure, it will select the best method based on your data
`auto`- Distance Measure Selection:Usecosine_distancefor most embedding models (OpenAI, Hugging Face, etc.)Usemax_inner_productif your vectors are normalizedUsel2_distanceorl1_distanceif working with raw feature vectors
- Usecosine_distancefor most embedding models (OpenAI, Hugging Face, etc.)
`cosine_distance`- Usemax_inner_productif your vectors are normalized
`max_inner_product`- Usel2_distanceorl1_distanceif working with raw feature vectors
`l2_distance``l1_distance`- Connection String:Always use environment variables for sensitive information in the connection stringFormat:postgresql://user:password@host:port/database
- Always use environment variables for sensitive information in the connection string
- Format:postgresql://user:password@host:port/database
`postgresql://user:password@host:port/database`