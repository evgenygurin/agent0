# Product Updates - Mem0
Source: https://docs.mem0.ai/changelog
Downloaded: 2025-11-12 21:20:22
================================================================================

- Python
- TypeScript
- Platform
- Vercel AI SDK
[​](https://docs.mem0.ai/changelog#2025-10-16)- Vector Stores:Added Azure MySQL supportAdded Azure AI Search Vector Store support
- Added Azure MySQL support
- Added Azure AI Search Vector Store support
- LLMs:Added Tool Call support for LangchainLLMEnabled custom model and parameters for Hugging Face with huggingface_base_urlUpdated default LLM configuration
- Added Tool Call support for LangchainLLM
- Enabled custom model and parameters for Hugging Face with huggingface_base_url
- Updated default LLM configuration
- Rerankers:Added reranker support: Cohere, ZeroEntropy, Hugging Face, Sentence Transformers, and LLMs
- Added reranker support: Cohere, ZeroEntropy, Hugging Face, Sentence Transformers, and LLMs
- Core:Added metadata filtering for OSSAdded Assistant memory retrievalEnabled async mode as default
- Added metadata filtering for OSS
- Added Assistant memory retrieval
- Enabled async mode as default
- Prompts:Improved prompt for better memory retrieval
- Improved prompt for better memory retrieval
- Dependencies:Updated dependency compatibility with OpenAI 2.x
- Updated dependency compatibility with OpenAI 2.x
- Validation:Validated embedding_dims for Kuzu integration
- Validated embedding_dims for Kuzu integration
- Vector Stores:Fixed Databricks Vector Store integrationFixed Milvus DB bug and added test coverageFixed Weaviate search method
- Fixed Databricks Vector Store integration
- Fixed Milvus DB bug and added test coverage
- Fixed Weaviate search method
- LLMs:Fixed bug with thinking LLM in vLLM
- Fixed bug with thinking LLM in vLLM
[​](https://docs.mem0.ai/changelog#2025-09-25)- Vector Stores:Added Valkey vector store supportAdded support for ChromaDB CloudAdded Mem0 vector store backend integration for Neptune Analytics
- Added Valkey vector store support
- Added support for ChromaDB Cloud
- Added Mem0 vector store backend integration for Neptune Analytics
- Graph Store:Added Neptune-DB graph store with vector store
- Added Neptune-DB graph store with vector store
- Core:Implemented structured exception classes with error codes and suggested actions
- Implemented structured exception classes with error codes and suggested actions
- Dependencies:Updated OpenAI dependency and improved Ollama compatibility
- Updated OpenAI dependency and improved Ollama compatibility
- Testing:Added Weaviate DB testAdded comprehensive test suite for SQLiteManager
- Added Weaviate DB test
- Added comprehensive test suite for SQLiteManager
- Documentation:Updated category docsUpdated Search V2 / Get All V2 filters documentationRefactored AWS example titleFixed Quickstart cURL example
- Updated category docs
- Updated Search V2 / Get All V2 filters documentation
- Refactored AWS example title
- Fixed Quickstart cURL example
- Vector Stores:Databricks bug fixesFixed S3 Vectors memory initialization issue from configuration
- Databricks bug fixes
- Fixed S3 Vectors memory initialization issue from configuration
- Core:Fixed JSON parsing with new memoriesReplaced hardcoded LLM provider with provider from configuration
- Fixed JSON parsing with new memories
- Replaced hardcoded LLM provider with provider from configuration
- LLMs:Fixed Bedrock Anthropic models to use system field
- Fixed Bedrock Anthropic models to use system field
[​](https://docs.mem0.ai/changelog#2025-09-03)- OpenMemory:Added memory export / import featureAdded vector store integrations: Weaviate, FAISS, PGVector, Chroma, Redis, Elasticsearch, MilvusAddedexport_openmemory.shmigration script
- Added memory export / import feature
- Added vector store integrations: Weaviate, FAISS, PGVector, Chroma, Redis, Elasticsearch, Milvus
- Addedexport_openmemory.shmigration script
`export_openmemory.sh`- Vector Stores:Added Amazon S3 Vectors supportAdded Databricks Mosaic AI vector store supportAdded support for OpenAI Store
- Added Amazon S3 Vectors support
- Added Databricks Mosaic AI vector store support
- Added support for OpenAI Store
- Graph Memory:Added support for graph memory using Kuzu
- Azure:Added Azure Identity for Azure OpenAI and Azure AI Search authentication
- Elasticsearch:Added headers configuration support
- Added custom connection client to enable connecting to local containers for Weaviate
- Updated configuration AWS Bedrock
- Fixed dependency issues and tests; updated docstrings
- Documentation:Fixed Graph Docs page missing in sidebarUpdated integration documentationAdded version param in Search V2 API documentationUpdated Databricks documentation and refactored docsUpdated favicon logoFixed typos and Typescript docs
- Fixed Graph Docs page missing in sidebar
- Updated integration documentation
- Added version param in Search V2 API documentation
- Updated Databricks documentation and refactored docs
- Updated favicon logo
- Fixed typos and Typescript docs
- Baidu: Added missing provider for Baidu vector DB
- MongoDB: Replacedquery_vectorargs in search method
`query_vector`- Fixed new memory mistaken for current
- AsyncMemory._add_to_vector_store: handled edge case when no facts found
- Fixed missing commas in Kuzu graph INSERT queries
- Fixed inconsistent created and updated properties for Graph
- Fixed missingapp_idon client for Neptune Analytics
`app_id`- Correctly pick AWS region from environment variable
- Fixed Ollama model existence check
- PGVector:Use internal connection pools and context managers
[​](https://docs.mem0.ai/changelog#2025-08-14)- Pinecone:Added namespace support and improved type safety
- Milvus:Added db_name field to MilvusDBConfig
- Vector Stores:Added multi-id filters support
- Vercel AI SDK:Migration to AI SDK V5.0
- Python Support:Added Python 3.12 support
- Graph Memory:Added sanitizer methods for nodes and relationships
- LLM Monitoring:Added monitoring callback support
- Performance:Improved async handling in AsyncMemory class
- Improved async handling in AsyncMemory class
- Documentation:Added async add announcementAdded personalized search docsAdded Neptune examplesAdded V5 migration docs
- Added async add announcement
- Added personalized search docs
- Added Neptune examples
- Added V5 migration docs
- Configuration:Refactored base class config for LLMsAdded sslmode for pgvector
- Refactored base class config for LLMs
- Added sslmode for pgvector
- Dependencies:Updated psycopg to version 3Updated Docker compose
- Updated psycopg to version 3
- Updated Docker compose
- Tests:Fixed failing testsRestricted package versions
- Fixed failing tests
- Restricted package versions
- Memgraph:Fixed async attribute errorsFixed n_embeddings usageFixed indexing issues
- Fixed async attribute errors
- Fixed n_embeddings usage
- Fixed indexing issues
- Vector Stores:Fixed Qdrant cloud indexingFixed Neo4j Cypher syntaxFixed LLM parameters
- Fixed Qdrant cloud indexing
- Fixed Neo4j Cypher syntax
- Fixed LLM parameters
- Graph Store:Fixed LM config prioritization
- Fixed LM config prioritization
- Dependencies:Fixed JSON import for psycopg
- Fixed JSON import for psycopg
- Google AI:Refactored from Gemini to Google AI
- Base Classes:Refactored LLM base class configuration
[​](https://docs.mem0.ai/changelog#2025-07-24)- Enhanced project management viaclient.projectandAsyncMemoryClient.projectinterfaces
`client.project``AsyncMemoryClient.project`- Full support for project CRUD operations (create, read, update, delete)
- Project member management: add, update, remove, and list members
- Manage project settings including custom instructions, categories, retrieval criteria, and graph enablement
- Both sync and async support for all project management operations
- Documentation:Added detailed API reference and usage examples for new project management methods.Updated all docs to useclient.project.get()andclient.project.update()instead of deprecated methods.
- Added detailed API reference and usage examples for new project management methods.
- Updated all docs to useclient.project.get()andclient.project.update()instead of deprecated methods.
`client.project.get()``client.project.update()`- Deprecation:Markedget_project()andupdate_project()as deprecated (these methods were already present); added warnings to guide users to the new API.
- Markedget_project()andupdate_project()as deprecated (these methods were already present); added warnings to guide users to the new API.
`get_project()``update_project()`- Tests:Fixed Gemini embedder and LLM test mocks for correct error handling and argument structure.
- Fixed Gemini embedder and LLM test mocks for correct error handling and argument structure.
- vLLM:Fixed duplicate import in vLLM module.
- Fixed duplicate import in vLLM module.
[​](https://docs.mem0.ai/changelog#2025-07-05)- OpenAI Agents:Added OpenAI agents SDK support
- Amazon Neptune:Added Amazon Neptune Analytics graph_store configuration and integration
- vLLM:Added vLLM support
- Documentation:Added SOC2 and HIPAA compliance documentationEnhanced group chat feature documentation for platformAdded Google AI ADK Integration documentationFixed documentation images and links
- Added SOC2 and HIPAA compliance documentation
- Enhanced group chat feature documentation for platform
- Added Google AI ADK Integration documentation
- Fixed documentation images and links
- Setup:Fixed Mem0 setup, logging, and documentation issues
- MongoDB:Fixed MongoDB Vector Store misaligned strings and classes
- vLLM:Fixed missing OpenAI import in vLLM module and call errors
- Dependencies:Fixed CI issues related to missing dependencies
- Installation:Reverted pip install changes
[​](https://docs.mem0.ai/changelog#2025-06-30)- Gemini:Fixed Gemini embedder configuration
[​](https://docs.mem0.ai/changelog#2025-06-27)- Memory:Added immutable parameter to add method
- OpenMemory:Added async_mode parameter support
- Documentation:Enhanced platform feature documentationFixed documentation linksAdded async_mode documentation
- Enhanced platform feature documentation
- Fixed documentation links
- Added async_mode documentation
- MongoDB:Fixed MongoDB configuration name
- Bedrock:Fixed Bedrock LLM, embeddings, tools, and temporary credentials
- Memory:Fixed memory categorization by updating dependencies and correcting API usage
- Gemini:Fixed Gemini Embeddings and LLM issues
[​](https://docs.mem0.ai/changelog#2025-06-23)- OpenMemory:Added OpenMemory augment supportAdded OpenMemory Local Support using new library
- Added OpenMemory augment support
- Added OpenMemory Local Support using new library
- vLLM:Added vLLM support integration
- Documentation:Added MCP Client Integration Guide and updated installation commandsImproved Agent Id documentation for Mem0 OSS Graph Memory
- Added MCP Client Integration Guide and updated installation commands
- Improved Agent Id documentation for Mem0 OSS Graph Memory
- Core:Added JSON parsing to solve hallucination errors
- Gemini:Fixed Gemini Embeddings migration
[​](https://docs.mem0.ai/changelog#2025-06-20)- Baidu:Added Baidu vector database integration
- Documentation:Updated changelogFixed example in quickstart pageUpdated client.update() method documentation in OpenAPI specification
- Updated changelog
- Fixed example in quickstart page
- Updated client.update() method documentation in OpenAPI specification
- OpenSearch:Updated logger warning
- CI:Fixed failing CI pipeline
[​](https://docs.mem0.ai/changelog#2025-06-19)- AgentOps:Added AgentOps integration
- LM Studio:Added response_format parameter for LM Studio configuration
- Examples:Added Memory agent powered by voice (Cartesia + Agno)
- AI SDK:Added output_format parameter
- Client:Enhanced update method to support metadata
- Google:Added Google Genai library support
- Build:Fixed Build CI failure
- Pinecone:Fixed pinecone for async memory
[​](https://docs.mem0.ai/changelog#2025-06-14)- MongoDB:Added MongoDB Vector Store support
- Client:Added client support for summary functionality
- Pinecone:Fixed pinecone version issues
- OpenSearch:Added logger support
- Testing:Added python version test environments
[​](https://docs.mem0.ai/changelog#2025-06-11)- Documentation:Updated Livekit documentation migrationUpdated OpenMemory hosted version documentation
- Updated Livekit documentation migration
- Updated OpenMemory hosted version documentation
- Core:Updated categorization flow
- Storage:Fixed migration issues
[​](https://docs.mem0.ai/changelog#2025-06-09)- Cloudflare:Added Cloudflare vector store support
- Search:Added threshold parameter to search functionality
- API:Added wildcard character support for v2 Memory APIs
- Documentation:Updated README docs for OpenMemory environment setup
- Core:Added support for unique user IDs
- Core:Fixed error handling exceptions
[​](https://docs.mem0.ai/changelog#2025-06-03)- Vector Stores:Fixed GET_ALL functionality for FAISS and OpenSearch
[​](https://docs.mem0.ai/changelog#2025-06-02)- LLM:Added support for OpenAI compatible LLM providers with baseUrl configuration
- Documentation:Fixed broken linksImproved Graph Memory features documentation clarityUpdated enable_graph documentation
- Fixed broken links
- Improved Graph Memory features documentation clarity
- Updated enable_graph documentation
- TypeScript SDK:Updated Google SDK peer dependency version
- Client:Added async mode parameter
[​](https://docs.mem0.ai/changelog#2025-05-26)- Examples:Added Neo4j example
- AI SDK:Added Google provider support
- OpenMemory:Added LLM and Embedding Providers support
- Documentation:Updated memory export documentationEnhanced role-based memory attribution rules documentationUpdated API reference and messages documentationAdded Mastra and Raycast documentationAdded NOT filter documentation for Search and GetAll V2Announced Claude 4 support
- Updated memory export documentation
- Enhanced role-based memory attribution rules documentation
- Updated API reference and messages documentation
- Added Mastra and Raycast documentation
- Added NOT filter documentation for Search and GetAll V2
- Announced Claude 4 support
- Core:Removed support for passing string as input in client.add()Added support for sarvam-m model
- Removed support for passing string as input in client.add()
- Added support for sarvam-m model
- TypeScript SDK:Fixed types from message interface
- Memory:Prevented saving prompt artifacts as memory when no new facts are present
- OpenMemory:Fixed typos in MCP tool description
[​](https://docs.mem0.ai/changelog#2025-05-15)- Neo4j:Added base label configuration support
- Documentation:Updated Healthcare example indexEnhanced collaborative task agent documentation clarityAdded criteria-based filtering documentation
- Updated Healthcare example index
- Enhanced collaborative task agent documentation clarity
- Added criteria-based filtering documentation
- OpenMemory:Added cURL command for easy installation
- Build:Migrated to Hatch build system
[​](https://docs.mem0.ai/changelog#2025-05-10)- Memory:Added Group Chat Memory Feature support
- Examples:Added Healthcare assistant using Mem0 and Google ADK
- SSE:Fixed SSE connection issues
- MCP:Fixed memories not appearing in MCP clients added from Dashboard
[​](https://docs.mem0.ai/changelog#2025-05-07)- OpenMemory:Added OpenMemory support
- Neo4j:Added weights to Neo4j model
- AWS:Added support for Opsearch Serverless
- Examples:Added ElizaOS Example
- Documentation:Updated Azure AI documentation
- AI SDK:Added missing parameters and updated demo application
- OSS:Fixed AOSS and AWS BedRock LLM
[​](https://docs.mem0.ai/changelog#2025-04-30)- Neo4j:Added support for Neo4j database
- AWS:Added support for AWS Bedrock Embeddings
- Client:Updated delete_users() to use V2 API endpoints
- Documentation:Updated timestamp and dual-identity memory management docs
- Neo4j:Improved Neo4j queries and removed warnings
- AI SDK:Added support for graceful failure when services are down
- Fixed AI SDK filters
- Fixed new memories wrong type
- Fixed duplicated metadata issue while adding/updating memories
[​](https://docs.mem0.ai/changelog#2025-04-23)- HuggingFace:Added support for HF Inference
- Fixed proxy for Mem0
[​](https://docs.mem0.ai/changelog#2025-04-16)- Vercel AI SDK:Added Graph Memory support
- Documentation:Fixed timestamp and README links
- Client:Updated TS client to use proper types for deleteUsers
- Dependencies:Removed unnecessary dependencies from base package
[​](https://docs.mem0.ai/changelog#2025-04-09)- Client:Fixed Ping Method for using default org_id and project_id
- Documentation:Updated documentation
- Fixed mem0-migrations issue
[​](https://docs.mem0.ai/changelog#2025-04-26)- Integrations:Added Memgraph integration
- Memory:Added timestamp support
- Vector Stores:Added reset function for VectorDBs
- Documentation:Updated timestamp and expiration_date documentationFixed v2 search documentationAdded “memory” in EC “Custom config” sectionFixed typos in the json config sample
- Updated timestamp and expiration_date documentation
- Fixed v2 search documentation
- Added “memory” in EC “Custom config” section
- Fixed typos in the json config sample
[​](https://docs.mem0.ai/changelog#2025-04-21)- Vector Stores:Initialized embedding_model_dims in all vectordbs
- Documentation:Fixed agno link
[​](https://docs.mem0.ai/changelog#2025-04-18)- Memory:Added Memory Reset functionality
- Client:Added support for Custom Instructions
- Examples:Added Fitness Checker powered by memory
- Core:Updated capture_event
- Documentation:Fixed curl for v2 get_all
- Vector Store:Fixed user_id functionality
- Client:Various client improvements
[​](https://docs.mem0.ai/changelog#2025-04-16-2)- LLM Integrations:Added Azure OpenAI Embedding Model
- Examples:Added movie recommendation using grok3Added Voice Assistant using Elevenlabs
- Added movie recommendation using grok3
- Added Voice Assistant using Elevenlabs
- Documentation:Added keywords AIReformatted navbar page URLsUpdated changelogUpdated openai.mdx
- Added keywords AI
- Reformatted navbar page URLs
- Updated changelog
- Updated openai.mdx
- FAISS:Silenced FAISS info logs
[​](https://docs.mem0.ai/changelog#2025-04-11)- LLM Integrations:Added Mistral AI as LLM provider
- Documentation:Updated changelogFixed memory exclusion exampleUpdated xAI documentationUpdated YouTube Chrome extension example documentation
- Updated changelog
- Fixed memory exclusion example
- Updated xAI documentation
- Updated YouTube Chrome extension example documentation
- Core:Fixed EmbedderFactory.create() in GraphMemory
- Azure OpenAI:Added patch to fix Azure OpenAI
- Telemetry:Fixed telemetry issue
[​](https://docs.mem0.ai/changelog#2025-04-11-2)- Langchain Integration:Added support for Langchain VectorStores
- Examples:Added personal assistant exampleAdded personal study buddy exampleAdded YouTube assistant Chrome extension exampleAdded agno exampleUpdated OpenAI Responses API examples
- Added personal assistant example
- Added personal study buddy example
- Added YouTube assistant Chrome extension example
- Added agno example
- Updated OpenAI Responses API examples
- Vector Store:Added capability to store user_id in vector database
- Async Memory:Added async support for OSS
- Documentation:Updated formatting and examples
[​](https://docs.mem0.ai/changelog#2025-04-09-2)- Upstash Vector:Added support for Upstash Vector store
- Code Quality:Removed redundant code lines
- Build:Updated MAKEFILE
- Documentation:Updated memory export documentation
[​](https://docs.mem0.ai/changelog#2025-04-07)- FAISS:Added embedding_dims parameter to FAISS vector store
[​](https://docs.mem0.ai/changelog#2025-04-07-2)- Langchain Embedder:Added Langchain embedder integration
- Langchain LLM:Updated Langchain LLM integration to directly pass the Langchain object LLM
[​](https://docs.mem0.ai/changelog#2025-04-07-3)- Langchain LLM:Fixed issues with Langchain LLM integration
[​](https://docs.mem0.ai/changelog#2025-04-07-4)- LLM Integrations:Added support for Langchain LLMs, Google as new LLM and embedder
- Development:Added development docker compose
- Output Format:Set output_format=‘v1.1’ and updated documentation
- Integrations:Added LMStudio and Together.ai documentation
- API Reference:Updated output_format documentation
- Integrations:Added PipeCat integration documentation
- Integrations:Added Flowise integration documentation for Mem0 memory setup
- Tests:Fixed failing unit tests
[​](https://docs.mem0.ai/changelog#2025-04-02)- FAISS Support:Added FAISS vector store support
[​](https://docs.mem0.ai/changelog#2025-04-02-2)- Livekit Integration:Added Mem0 livekit example
- Evaluation:Added evaluation framework and tools
- Multimodal:Updated multimodal documentation
- Examples:Added examples for email processing
- API Reference:Updated API reference section
- Elevenlabs:Added Elevenlabs integration example
- OpenAI Environment Variables:Fixed issues with OpenAI environment variables
- Deployment Errors:Addedpackage.jsonfile to fix deployment errors
`package.json`- Tools:Fixed tools issues and improved formatting
- Docs:Updated API reference section forexpiration date
`expiration date`[​](https://docs.mem0.ai/changelog#2025-03-26)- OpenAI Environment Variables:Fixed issues with OpenAI environment variables
- Deployment Errors:Addedpackage.jsonfile to fix deployment errors
`package.json`- Tools:Fixed tools issues and improved formatting
- Docs:Updated API reference section forexpiration date
`expiration date`[​](https://docs.mem0.ai/changelog#2025-03-19)- Supabase Vector Store:Added support for Supabase Vector Store
- Supabase History DB:Added Supabase History DB to run Mem0 OSS on Serverless
- Feedback Method:Added feedback method to client
- Azure OpenAI:Fixed issues with Azure OpenAI
- Azure AI Search:Fixed test cases for Azure AI Search
