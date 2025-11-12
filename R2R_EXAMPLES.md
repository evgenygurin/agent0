# R2R: Usage Examples & Configuration Samples

## Table of Contents
1. [Installation & Setup](#installation--setup)
2. [Docker Compose Examples](#docker-compose-examples)
3. [Environment Configuration](#environment-configuration)
4. [Python SDK Examples](#python-sdk-examples)
5. [JavaScript SDK Examples](#javascript-sdk-examples)
6. [API Endpoint Examples](#api-endpoint-examples)
7. [Advanced Search Patterns](#advanced-search-patterns)

---

## Installation & Setup

### Prerequisites
```bash
# Install Docker & Docker Compose
brew install docker docker-compose  # macOS
sudo apt-get install docker.io docker-compose  # Ubuntu

# Or use Docker Desktop (recommended)
# https://www.docker.com/products/docker-desktop

# Verify installation
docker --version
docker compose --version
```

### Clone R2R Repository
```bash
git clone https://github.com/SciPhi-AI/R2R.git
cd R2R
ls -la
# Output should show:
# - compose.full.yaml
# - compose.light.yaml
# - .env.example
# - docker/
# - deployment/
```

---

## Docker Compose Examples

### Full Production Setup (compose.full.yaml)

```yaml
version: '3.8'

services:
  # R2R API Server
  r2r:
    image: ragtoriches/prod:3.6.5
    container_name: r2r-api
    ports:
      - "7272:7272"
    environment:
      # Core Configuration
      R2R_CONFIG_NAME: "full"
      R2R_LOG_LEVEL: "INFO"
      
      # Database
      DATABASE_URL: "postgresql://r2r_user:${POSTGRES_PASSWORD}@postgres:5432/r2r_db"
      POSTGRES_HOST: "postgres"
      POSTGRES_PORT: "5432"
      POSTGRES_DB: "r2r_db"
      POSTGRES_USER: "r2r_user"
      POSTGRES_PASSWORD: "${POSTGRES_PASSWORD}"
      
      # LLM Configuration
      OPENAI_API_KEY: "${OPENAI_API_KEY}"
      ANTHROPIC_API_KEY: "${ANTHROPIC_API_KEY}"
      
      # External APIs (Optional)
      SERPER_API_KEY: "${SERPER_API_KEY}"
      FIRECRAWL_API_KEY: "${FIRECRAWL_API_KEY}"
      
      # Redis
      REDIS_HOST: "redis"
      REDIS_PORT: "6379"
      
      # Security
      JWT_SECRET_KEY: "${JWT_SECRET_KEY}"
    
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
    
    volumes:
      - ./config:/app/config:ro
    
    networks:
      - r2r-network
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:7272/v3/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # PostgreSQL Database
  postgres:
    image: postgres:15-alpine
    container_name: r2r-postgres
    environment:
      POSTGRES_USER: "r2r_user"
      POSTGRES_PASSWORD: "${POSTGRES_PASSWORD}"
      POSTGRES_DB: "r2r_db"
      PGDATA: "/var/lib/postgresql/data/pgdata"
    
    ports:
      - "5432:5432"
    
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-db.sql:/docker-entrypoint-initdb.d/init.sql
    
    networks:
      - r2r-network
    
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U r2r_user -d r2r_db"]
      interval: 10s
      timeout: 5s
      retries: 5
    
    command: 
      - "postgres"
      - "-c"
      - "shared_preload_libraries=vector"

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: r2r-redis
    ports:
      - "6379:6379"
    
    volumes:
      - redis_data:/data
    
    networks:
      - r2r-network
    
    command: redis-server --appendonly yes
    
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Optional: PgAdmin for Database Management
  pgadmin:
    image: dpage/pgadmin4:latest
    container_name: r2r-pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: "admin@example.com"
      PGADMIN_DEFAULT_PASSWORD: "${PGADMIN_PASSWORD:-admin}"
    
    ports:
      - "5050:80"
    
    depends_on:
      - postgres
    
    networks:
      - r2r-network
    
    profiles:
      - dev

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local

networks:
  r2r-network:
    driver: bridge
```

### Light Development Setup (compose.light.yaml)

```yaml
version: '3.8'

services:
  r2r:
    image: ragtoriches/prod:3.6.5
    ports:
      - "7272:7272"
    environment:
      R2R_CONFIG_NAME: "light"
      OPENAI_API_KEY: "${OPENAI_API_KEY}"
    networks:
      - r2r-network

networks:
  r2r-network:
    driver: bridge
```

### Startup Commands

```bash
# Full production setup
export R2R_CONFIG_NAME=full
export OPENAI_API_KEY=sk-your-api-key
export POSTGRES_PASSWORD=secure_postgres_password
export JWT_SECRET_KEY=your-jwt-secret-key

docker compose -f compose.full.yaml --profile postgres up -d

# Light development setup
export OPENAI_API_KEY=sk-your-api-key
docker compose -f compose.light.yaml up -d

# View logs
docker compose logs -f r2r

# Stop services
docker compose down

# Stop and remove all data
docker compose down -v
```

---

## Environment Configuration

### .env File Template

```bash
# .env file - Keep this secure!
# Never commit to version control

# ============================================
# Core Configuration
# ============================================
R2R_CONFIG_NAME=full              # "light" or "full"
R2R_LOG_LEVEL=INFO                # DEBUG, INFO, WARNING, ERROR
R2R_PORT=7272
R2R_HOST=0.0.0.0

# ============================================
# PostgreSQL Database
# ============================================
POSTGRES_USER=r2r_user
POSTGRES_PASSWORD=your_secure_password_here_change_this
POSTGRES_DB=r2r_db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
DATABASE_URL=postgresql://r2r_user:your_secure_password@postgres:5432/r2r_db

# ============================================
# LLM Providers
# ============================================
# OpenAI
OPENAI_API_KEY=sk-your-openai-api-key-here

# Anthropic/Claude
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key

# Azure OpenAI
AZURE_OPENAI_API_KEY=your-azure-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# ============================================
# External Services (Optional)
# ============================================
# Web Search
SERPER_API_KEY=your-serper-api-key

# Web Scraping
FIRECRAWL_API_KEY=your-firecrawl-api-key

# ============================================
# Redis Cache (Optional)
# ============================================
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=

# ============================================
# Security
# ============================================
JWT_SECRET_KEY=your-jwt-secret-key-change-this
JWT_ALGORITHM=HS256

# ============================================
# Optional: Development Tools
# ============================================
PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin
```

### Load Environment Variables

```bash
# Method 1: Source from file
source .env

# Method 2: Export individually
export OPENAI_API_KEY=sk-...
export POSTGRES_PASSWORD=...

# Method 3: Docker compose loads automatically from .env
docker compose up -d
```

---

## Python SDK Examples

### Basic Setup & Authentication

```python
from r2r import R2RClient

# Initialize client
client = R2RClient(
    base_url="http://localhost:7272",
    api_key=None  # Auto-loads from R2R_API_KEY env var
)

# Or with explicit API key
client = R2RClient(
    base_url="http://localhost:7272",
    api_key="your-api-key"
)

# Or authenticate with email/password
client.users.login(email="user@example.com", password="password")
```

### Document Management

```python
# Create sample document
response = client.documents.create_sample(hi_res=True)
print(f"Document ID: {response.document_id}")

# Upload custom document
with open("my_document.pdf", "rb") as f:
    response = client.documents.create(
        file_path="my_document.pdf",
        metadata={
            "author": "John Doe",
            "year": 2024
        }
    )

# List documents
documents = client.documents.list()
for doc in documents:
    print(f"{doc.id}: {doc.metadata.get('title')} ({doc.ingestion_status})")

# Get document details
doc = client.documents.get(document_id="doc-id")
print(f"Size: {doc.size_in_bytes} bytes")
print(f"Summary: {doc.summary}")
print(f"Total tokens: {doc.total_tokens}")

# Delete document
client.documents.delete(document_id="doc-id")
```

### Basic Search

```python
# Simple semantic search
results = client.retrieval.search(
    query="What is artificial intelligence?",
    search_mode="basic"
)

print(f"Found {len(results.chunk_search_results)} results")
for result in results.chunk_search_results:
    print(f"Score: {result.score}")
    print(f"Text: {result.text[:200]}...")
```

### Hybrid Search

```python
# Hybrid search (semantic + full-text)
results = client.retrieval.search(
    query="machine learning algorithms",
    search_settings={
        "use_hybrid_search": True,
        "hybrid_settings": {
            "semantic_weight": 1.0,
            "full_text_weight": 1.0,
            "full_text_limit": 100,
            "rrf_k": 60  # Reciprocal Rank Fusion parameter
        },
        "limit": 10,
        "include_scores": True
    }
)

for chunk in results.chunk_search_results:
    print(f"Score: {chunk.score:.3f}")
    print(f"Source: {chunk.metadata.get('source')}")
```

### Advanced Filtering

```python
# Search with filters
results = client.retrieval.search(
    query="climate change",
    search_settings={
        "filters": {
            "$and": [
                {"document_type": {"$eq": "pdf"}},
                {"metadata.year": {"$gte": 2020}},
                {"metadata.topic": {"$in": ["climate", "environment"]}}
            ]
        },
        "limit": 5
    }
)
```

### RAG (Retrieval-Augmented Generation)

```python
# Basic RAG
response = client.retrieval.rag(
    query="What are the main causes of climate change?",
    search_settings={"limit": 5}
)

print(f"Answer: {response.results.generated_answer}")
print(f"Citations: {len(response.results.citations)}")

for citation in response.results.citations:
    print(f"- [{citation.id}] {citation.payload.text[:100]}...")
```

### Streaming RAG

```python
from r2r import (
    SearchResultsEvent,
    MessageEvent,
    CitationEvent,
    FinalAnswerEvent
)

# RAG with streaming
stream = client.retrieval.rag(
    query="Explain quantum computing",
    search_settings={"limit": 10},
    rag_generation_config={"stream": True}
)

print("Streaming RAG response:")
for event in stream:
    if isinstance(event, SearchResultsEvent):
        print(f"Found {len(event.data.data.chunk_search_results)} search results")
    
    elif isinstance(event, MessageEvent):
        # Print text as it streams
        if event.data.delta and event.data.delta.content:
            print(event.data.delta.content[0].payload.value, end="", flush=True)
    
    elif isinstance(event, CitationEvent):
        print(f"\n[Citation: {event.data.id}]")
    
    elif isinstance(event, FinalAnswerEvent):
        print(f"\n\nFinal Answer Generated")
        print(f"Total citations: {len(event.data.citations)}")
```

### Agentic RAG (Deep Research)

```python
from r2r import (
    ThinkingEvent,
    ToolCallEvent,
    ToolResultEvent,
    FinalAnswerEvent
)

# Deep research with Claude
response = client.retrieval.agent(
    message={
        "role": "user",
        "content": "What are the implications of AI for education in 2025?"
    },
    rag_generation_config={
        "model": "anthropic/claude-3-7-sonnet-20250219",
        "extended_thinking": True,
        "thinking_budget": 4096,
        "temperature": 1,
        "stream": True
    }
)

for event in response:
    if isinstance(event, ThinkingEvent):
        print(f"Thinking: {event.data.delta.content[0].payload.value}")
    
    elif isinstance(event, ToolCallEvent):
        print(f"Tool: {event.data.name}({event.data.arguments})")
    
    elif isinstance(event, ToolResultEvent):
        print(f"Result: {event.data.content[:200]}...")
    
    elif isinstance(event, FinalAnswerEvent):
        print(f"Answer: {event.data.generated_answer}")
```

### Collections & Access Control

```python
# Create collection
collection = client.collections.create(
    name="my-knowledge-base",
    description="Company documents and research papers"
)

# Add documents to collection
client.documents.update(
    document_id="doc-id",
    collection_ids=[collection.id]
)

# Share collection
client.collections.share(
    collection_id=collection.id,
    user_id="user-id",
    permission="read"
)
```

### Conversations & Memory

```python
# Create conversation
conversation = client.conversations.create(
    name="Knowledge Exploration"
)

# Multi-turn conversation
messages = [
    {"role": "user", "content": "What is machine learning?"},
    {"role": "assistant", "content": "Machine learning is a subset of AI..."},
    {"role": "user", "content": "How is it different from deep learning?"}
]

response = client.retrieval.rag(
    query=messages[-1]["content"],
    conversation_id=conversation.id,
    search_settings={"limit": 5}
)

# Retrieve conversation history
history = client.conversations.get(conversation_id=conversation.id)
```

---

## JavaScript SDK Examples

### Basic Setup

```javascript
const { r2rClient } = require('r2r-js');

// Initialize client
const client = new r2rClient('http://localhost:7272');

// Or with authentication
const client = new r2rClient({
  baseURL: 'http://localhost:7272',
  apiKey: process.env.R2R_API_KEY
});
```

### Document Operations

```javascript
// Create sample document
const docResponse = await client.documents.createSample({
  ingestionMode: 'hi-res'
});

// Upload document
const uploadResponse = await client.documents.create({
  filePath: '/path/to/document.pdf',
  metadata: {
    author: 'John Doe',
    year: 2024
  }
});

// List documents
const documents = await client.documents.list();
documents.forEach(doc => {
  console.log(`${doc.id}: ${doc.metadata.title} (${doc.ingestionStatus})`);
});

// Get document
const document = await client.documents.get({ 
  documentId: 'doc-id' 
});

// Delete document
await client.documents.delete({ documentId: 'doc-id' });
```

### Search Operations

```javascript
// Basic search
const results = await client.retrieval.search({
  query: 'What is machine learning?',
  searchMode: 'basic'
});

console.log(`Found ${results.chunkSearchResults.length} results`);

// Hybrid search
const hybridResults = await client.retrieval.search({
  query: 'AI and machine learning',
  searchSettings: {
    useHybridSearch: true,
    hybridSettings: {
      semanticWeight: 1.0,
      fullTextWeight: 1.0,
      rrfK: 60
    },
    limit: 10
  }
});

// Filtered search
const filteredResults = await client.retrieval.search({
  query: 'climate change',
  searchSettings: {
    filters: {
      $and: [
        { 'metadata.year': { $gte: 2020 } },
        { 'document_type': { $eq: 'pdf' } }
      ]
    },
    limit: 5
  }
});
```

### RAG Operations

```javascript
// Basic RAG
const ragResponse = await client.retrieval.rag({
  query: 'Explain quantum computing',
  searchSettings: { limit: 5 }
});

console.log(ragResponse.generatedAnswer);

// Streaming RAG
const streamResponse = await client.retrieval.rag({
  query: 'What is blockchain?',
  searchSettings: { limit: 5 },
  ragGenerationConfig: { stream: true }
});

if (Symbol.asyncIterator in streamResponse) {
  for await (const event of streamResponse) {
    switch(event.event) {
      case 'search_results':
        console.log(`Found ${event.data.chunkSearchResults.length} results`);
        break;
      case 'message':
        process.stdout.write(event.data.delta.content[0].text.value);
        break;
      case 'citation':
        console.log(`\n[Citation: ${event.data.id}]`);
        break;
      case 'final_answer':
        console.log(`\nFinal Answer: ${event.data.generatedAnswer}`);
        break;
    }
  }
}
```

---

## API Endpoint Examples

### Using cURL

```bash
# Health Check
curl -X GET "http://localhost:7272/v3/health" \
  -H "Content-Type: application/json"

# Create Sample Document
curl -X POST "http://localhost:7272/v3/documents" \
  -H "Content-Type: application/json" \
  -d '{
    "ingestion_mode": "hi_res"
  }'

# List Documents
curl -X GET "http://localhost:7272/v3/documents" \
  -H "Content-Type: application/json"

# Basic Search
curl -X POST "http://localhost:7272/v3/retrieval/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is AI?"
  }'

# Hybrid Search
curl -X POST "http://localhost:7272/v3/retrieval/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "machine learning",
    "search_settings": {
      "use_hybrid_search": true,
      "hybrid_settings": {
        "semantic_weight": 1.0,
        "full_text_weight": 1.0,
        "rrf_k": 60
      },
      "limit": 10
    }
  }'

# RAG Query
curl -X POST "http://localhost:7272/v3/retrieval/rag" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain neural networks"
  }'

# Agentic RAG (Streaming)
curl -X POST "http://localhost:7272/v3/retrieval/agent" \
  -H "Content-Type: application/json" \
  -d '{
    "message": {
      "role": "user",
      "content": "What are the implications of AI for society?"
    },
    "rag_generation_config": {
      "model": "anthropic/claude-3-7-sonnet-20250219",
      "stream": true
    }
  }'
```

---

## Advanced Search Patterns

### Distance Metrics for Vector Search

```python
# Cosine Distance (Default - Recommended)
results = client.retrieval.search(
    query="quantum computing",
    search_settings={
        "chunk_settings": {
            "index_measure": "cosine_distance"
        }
    }
)

# L2 Distance (Euclidean)
results = client.retrieval.search(
    query="deep learning",
    search_settings={
        "chunk_settings": {
            "index_measure": "l2_distance"
        }
    }
)

# Other supported: max_inner_product, l1_distance, hamming_distance, jaccard_distance
```

### RAG with Web Search

```python
# Include web search results
response = client.retrieval.rag(
    query="Latest developments in quantum computing 2024",
    include_web_search=True,
    search_settings={
        "limit": 5
    }
)

print("From documents:", len(response.results.search_results.chunk_search_results))
print("From web:", len(response.results.search_results.web_search_results))
print("Answer:", response.results.generated_answer)
```

### Knowledge Graph Search

```python
# Search with graph context
results = client.retrieval.search(
    query="relationships between AI concepts",
    search_settings={
        "use_graph_search": True,
        "graph_settings": {
            "include_entities": True,
            "include_relationships": True,
            "max_depth": 2
        }
    }
)

# Access graph results
for graph_result in results.graph_search_results:
    print(f"Type: {graph_result.result_type}")
    print(f"Content: {graph_result.content}")
```

---

## Monitoring & Debugging

### Health Check

```python
import requests

response = requests.get("http://localhost:7272/v3/health")
health_status = response.json()

print(f"API Status: {health_status['status']}")
print(f"Version: {health_status['version']}")
print(f"Database: {health_status['postgres']}")
print(f"Redis: {health_status['redis']}")
```

### View Logs

```bash
# Docker logs
docker compose logs -f r2r

# With grep filter
docker compose logs -f r2r | grep ERROR

# Last 100 lines
docker compose logs --tail=100 r2r
```

### Test Connectivity

```bash
# Test API connectivity
curl -v http://localhost:7272/v3/health

# Test PostgreSQL
docker exec r2r-postgres psql -U r2r_user -d r2r_db -c "SELECT version();"

# Test Redis
docker exec r2r-redis redis-cli ping
```

