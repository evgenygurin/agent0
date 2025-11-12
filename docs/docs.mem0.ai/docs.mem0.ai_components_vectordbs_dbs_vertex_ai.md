# Vertex AI Vector Search - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/vertex_ai
Downloaded: 2025-11-12 21:20:20
================================================================================


### ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/vertex_ai#usage)`mem0``vector_store``mem0`
```
import os
from mem0 import Memory

os.environ["GOOGLE_API_KEY"] = "sk-xx"

config = {
    "vector_store": {
        "provider": "vertex_ai_vector_search",
        "config": {
            "endpoint_id": "YOUR_ENDPOINT_ID",            # Required: Vector Search endpoint ID
            "index_id": "YOUR_INDEX_ID",                  # Required: Vector Search index ID 
            "deployment_index_id": "YOUR_DEPLOYMENT_INDEX_ID",  # Required: Deployment-specific ID
            "project_id": "YOUR_PROJECT_ID",              # Required: Google Cloud project ID
            "project_number": "YOUR_PROJECT_NUMBER",      # Required: Google Cloud project number
            "region": "YOUR_REGION",                      # Optional: Defaults to GOOGLE_CLOUD_REGION
            "credentials_path": "path/to/credentials.json", # Optional: Defaults to GOOGLE_APPLICATION_CREDENTIALS
            "vector_search_api_endpoint": "YOUR_API_ENDPOINT" # Required for get operations
        }
    }
}
m = Memory.from_config(config)
m.add("Your text here", user_id="user", metadata={"category": "example"})

```

### ​Required Parameters
[​](https://docs.mem0.ai/components/vectordbs/dbs/vertex_ai#required-parameters)`endpoint_id``index_id``deployment_index_id``project_id``project_number``vector_search_api_endpoint``region``credentials_path`