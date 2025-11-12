# Azure AI Search - Mem0
Source: https://docs.mem0.ai/components/vectordbs/dbs/azure
Downloaded: 2025-11-12 21:20:20
================================================================================

[Azure AI Search](https://learn.microsoft.com/azure/search/search-what-is-azure-search/)
## ​Usage
[​](https://docs.mem0.ai/components/vectordbs/dbs/azure#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "sk-xx"   # This key is used for embedding purpose

config = {
    "vector_store": {
        "provider": "azure_ai_search",
        "config": {
            "service_name": "<your-azure-ai-search-service-name>",
            "api_key": "<your-api-key>",
            "collection_name": "mem0", 
            "embedding_model_dims": 1536
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

## ​Using binary compression for large vector collections
[​](https://docs.mem0.ai/components/vectordbs/dbs/azure#using-binary-compression-for-large-vector-collections)
```
config = {
    "vector_store": {
        "provider": "azure_ai_search",
        "config": {
            "service_name": "<your-azure-ai-search-service-name>",
            "api_key": "<your-api-key>",
            "collection_name": "mem0", 
            "embedding_model_dims": 1536,
            "compression_type": "binary",
            "use_float16": True  # Use half precision for storage efficiency
        }
    }
}

```

## ​Using hybrid search
[​](https://docs.mem0.ai/components/vectordbs/dbs/azure#using-hybrid-search)
```
config = {
    "vector_store": {
        "provider": "azure_ai_search",
        "config": {
            "service_name": "<your-azure-ai-search-service-name>",
            "api_key": "<your-api-key>",
            "collection_name": "mem0", 
            "embedding_model_dims": 1536,
            "hybrid_search": True,
            "vector_filter_mode": "postFilter"
        }
    }
}

```

## ​Using Azure Identity for Authentication
[​](https://docs.mem0.ai/components/vectordbs/dbs/azure#using-azure-identity-for-authentication)- Environment Credential:Azure client ID, secret, tenant ID, or certificate in environment variables for service principal authentication.
- Workload Identity Credential:Utilizes Azure Workload Identity (relevant for Kubernetes and Azure workloads).
- Managed Identity Credential:Authenticates as a Managed Identity (for apps/services hosted in Azure with Managed Identity enabled), this is the most secure production credential.
- Shared Token Cache Credential / Visual Studio Credential (Windows only):Uses cached credentials from Visual Studio sign-ins (and sometimes VS Code if SSO is enabled).
- Azure CLI Credential:Uses the currently logged-in user from the Azure CLI (az login), this is the most common development credential.
`az login`- Azure PowerShell Credential:Uses the identity from Azure PowerShell (Connect-AzAccount).
`Connect-AzAccount`- Azure Developer CLI Credential:Uses the session from Azure Developer CLI (azd auth login).
`azd auth login`- In the Azure Portal, navigate to yourAzure AI Searchservice.
- In the left menu, selectSettings>Keys.
- Change the authentication setting toRole-based access control, orBothif you need API key compatibility. The default is “Key-based authentication”—you must switch it to use Azure roles.
- Go to Access Control (IAM):In the Azure Portal, select your Search service.ClickAccess Control (IAM)on the left.
- In the Azure Portal, select your Search service.
- ClickAccess Control (IAM)on the left.
- Add a Role Assignment:ClickAdd>Add role assignment.
- ClickAdd>Add role assignment.
- Choose Role:Mem0 requires theSearch Index Data ContributorandSearch Service Contributorrole.
- Mem0 requires theSearch Index Data ContributorandSearch Service Contributorrole.
- Choose MemberTo assign to a User, Group, Service Principal or Managed Identity:For production it is recommended to use a service principal or managed identity.For a service principal: selectUser, group, or service principaland search for the service principal.For a managed identity: selectManaged identityand choose the managed identity.For development, you can assign the role to a user account.For development: selectUser, group, or service principaland pick an Azure Entra ID account (the same used withaz login).
- To assign to a User, Group, Service Principal or Managed Identity:For production it is recommended to use a service principal or managed identity.For a service principal: selectUser, group, or service principaland search for the service principal.For a managed identity: selectManaged identityand choose the managed identity.For development, you can assign the role to a user account.For development: selectUser, group, or service principaland pick an Azure Entra ID account (the same used withaz login).
- For production it is recommended to use a service principal or managed identity.For a service principal: selectUser, group, or service principaland search for the service principal.For a managed identity: selectManaged identityand choose the managed identity.
- For a service principal: selectUser, group, or service principaland search for the service principal.
- For a managed identity: selectManaged identityand choose the managed identity.
- For development, you can assign the role to a user account.For development: selectUser, group, or service principaland pick an Azure Entra ID account (the same used withaz login).
- For development: selectUser, group, or service principaland pick an Azure Entra ID account (the same used withaz login).
`az login`- Complete the Assignment:ClickReview + Assign.
- ClickReview + Assign.
`api_key`
```
config = {
    "vector_store": {
        "provider": "azure_ai_search",
        "config": {
            "service_name": "<your-azure-ai-search-service-name>",
            "collection_name": "mem0", 
            "embedding_model_dims": 1536,
            "compression_type": "binary",
            "use_float16": True  # Use half precision for storage efficiency
        }
    }
}

```

### ​Environment Variables to Use Azure Identity Credential
[​](https://docs.mem0.ai/components/vectordbs/dbs/azure#environment-variables-to-use-azure-identity-credential)- For an Environment Credential, you will need to setup a Service Principal and set the following environment variables:AZURE_TENANT_ID: Your Azure Active Directory tenant ID.AZURE_CLIENT_ID: The client ID of your service principal or managed identity.AZURE_CLIENT_SECRET: The client secret of your service principal.
- AZURE_TENANT_ID: Your Azure Active Directory tenant ID.
`AZURE_TENANT_ID`- AZURE_CLIENT_ID: The client ID of your service principal or managed identity.
`AZURE_CLIENT_ID`- AZURE_CLIENT_SECRET: The client secret of your service principal.
`AZURE_CLIENT_SECRET`- For a User-Assigned Managed Identity, you will need to set the following environment variable:AZURE_CLIENT_ID: The client ID of the user-assigned managed identity.
- AZURE_CLIENT_ID: The client ID of the user-assigned managed identity.
`AZURE_CLIENT_ID`- For a System-Assigned Managed Identity, no additional environment variables are needed.

### ​Developer Logins for Azure Identity Credential
[​](https://docs.mem0.ai/components/vectordbs/dbs/azure#developer-logins-for-azure-identity-credential)- For an Azure CLI Credential, you need to have the Azure CLI installed and logged in withaz login.
`az login`- For an Azure PowerShell Credential, you need to have the Azure PowerShell module installed and logged in withConnect-AzAccount.
`Connect-AzAccount`- For an Azure Developer CLI Credential, you need to have the Azure Developer CLI installed and logged in withazd auth login.
`azd auth login`[Azure Identity](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/identity/azure-identity/TROUBLESHOOTING.md#troubleshoot-environmentcredential-authentication-issues)
## ​Configuration Parameters
[​](https://docs.mem0.ai/components/vectordbs/dbs/azure#configuration-parameters)`service_name``api_key`[Azure Identity](https://docs.mem0.ai/components/vectordbs/dbs/azure#using-azure-identity-for-authentication)`collection_name``mem0``embedding_model_dims``1536``compression_type``none``none``scalar``binary``use_float16``False``True``False``vector_filter_mode``preFilter``postFilter``preFilter``hybrid_search``False``True``False`
## ​Notes on Configuration Options
[​](https://docs.mem0.ai/components/vectordbs/dbs/azure#notes-on-configuration-options)- compression_type:none: No compression, uses full vector precisionscalar: Scalar quantization with reasonable balance of speed and accuracybinary: Binary quantization for maximum compression with some accuracy trade-off
- none: No compression, uses full vector precision
`none`- scalar: Scalar quantization with reasonable balance of speed and accuracy
`scalar`- binary: Binary quantization for maximum compression with some accuracy trade-off
`binary`- vector_filter_mode:preFilter: Applies filters before vector search (faster)postFilter: Applies filters after vector search (may provide better relevance)
- preFilter: Applies filters before vector search (faster)
`preFilter`- postFilter: Applies filters after vector search (may provide better relevance)
`postFilter`- use_float16: Using half precision (float16) reduces storage requirements but may slightly impact accuracy. Useful for very large vector collections.
- Filterable Fields: The implementation automatically extractsuser_id,run_id, andagent_idfields from payloads for filtering.
`user_id``run_id``agent_id`