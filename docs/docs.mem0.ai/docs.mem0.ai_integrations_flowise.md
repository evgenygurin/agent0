# Flowise - Mem0
Source: https://docs.mem0.ai/integrations/flowise
Downloaded: 2025-11-12 21:20:20
================================================================================

[Mem0 Memory](https://github.com/mem0ai/mem0)[Flowise](https://github.com/FlowiseAI/Flowise)[Flowise](https://flowiseai.com/)
## ​Overview
[​](https://docs.mem0.ai/integrations/flowise#overview)- Provides persistent memory storage for Flowise chatflows
- Seamless integration with existing Flowise templates
- Compatible with various LLM nodes in Flowise
- Supports custom memory configurations
- Easy to set up and manage

## ​Prerequisites
[​](https://docs.mem0.ai/integrations/flowise#prerequisites)- Flowise installed(NodeJS >= 18.15.0 required):
[Flowise installed](https://github.com/FlowiseAI/Flowise#%E2%9A%A1quick-start)
```
npm install -g flowise
npx flowise start

```
- Access to the Flowise UI athttp://localhost:3000
[http://localhost:3000](http://localhost:3000)- Basic familiarity withFlowise’s LLM orchestrationconcepts
[Flowise’s LLM orchestration](https://flowiseai.com/#features)
## ​Setup and Configuration
[​](https://docs.mem0.ai/integrations/flowise#setup-and-configuration)
### ​1. Set Up Flowise
[​](https://docs.mem0.ai/integrations/flowise#1-set-up-flowise)- Open the Flowise application and create a new canvas, or select a template from the Flowise marketplace.
- In this example, we use theConversation Chaintemplate.
- Replace the defaultBuffer MemorywithMem0 Memory.

### ​2. Obtain Your Mem0 API Key
[​](https://docs.mem0.ai/integrations/flowise#2-obtain-your-mem0-api-key)- Navigate to theMem0 API Key dashboard.
[Mem0 API Key dashboard](https://app.mem0.ai/dashboard/api-keys)- Generate or copy your existing Mem0 API Key.

### ​3. Configure Mem0 Credentials
[​](https://docs.mem0.ai/integrations/flowise#3-configure-mem0-credentials)- Enter theMem0 API Keyin the Mem0 Credentials section.
- Configure additional settings as needed:

```
{
  "apiKey": "m0-xxx",
  "userId": "user-123",  // Optional: Specify user ID
  "projectId": "proj-xxx",  // Optional: Specify project ID
  "orgId": "org-xxx"  // Optional: Specify organization ID
}

```

## ​Memory Features
[​](https://docs.mem0.ai/integrations/flowise#memory-features)
### ​1. Basic Memory Storage
[​](https://docs.mem0.ai/integrations/flowise#1-basic-memory-storage)- Save your Flowise configuration
- Run a test chat and store some information
- Verify the stored memories in theMem0 Dashboard
[Mem0 Dashboard](https://app.mem0.ai/dashboard/requests)
### ​2. Memory Retention
[​](https://docs.mem0.ai/integrations/flowise#2-memory-retention)- Clear the chat history in Flowise
- Ask a question about previously stored information
- Confirm that the AI remembers the context

## ​Advanced Configuration
[​](https://docs.mem0.ai/integrations/flowise#advanced-configuration)
### ​Memory Settings
[​](https://docs.mem0.ai/integrations/flowise#memory-settings)- Search Only Mode: Enable memory retrieval without creating new memories
- Mem0 Entities: Configure identifiers:user_id: Unique identifier for each userrun_id: Specific conversation session IDapp_id: Application identifieragent_id: AI agent identifier
- user_id: Unique identifier for each user
`user_id`- run_id: Specific conversation session ID
`run_id`- app_id: Application identifier
`app_id`- agent_id: AI agent identifier
`agent_id`- Project ID: Assign memories to specific projects
- Organization ID: Organize memories by organization

### ​Platform Configuration
[​](https://docs.mem0.ai/integrations/flowise#platform-configuration)[Mem0 Project Settings](https://app.mem0.ai/dashboard/project-settings)- Custom Instructions: Define memory extraction rules
- Expiration Date: Set automatic memory cleanup periods

## ​Best Practices
[​](https://docs.mem0.ai/integrations/flowise#best-practices)- User Identification: Use consistentuser_idvalues for reliable memory retrieval
`user_id`- Memory Organization: Utilize projects and organizations for better memory management
- Regular Maintenance: Monitor and clean up unused memories periodically
[LangChain IntegrationBuild LangChain-powered flows with memory](https://docs.mem0.ai/integrations/langchain)
## LangChain Integration
[Dify IntegrationCreate AI workflows with Dify platform](https://docs.mem0.ai/integrations/dify)
## Dify Integration
