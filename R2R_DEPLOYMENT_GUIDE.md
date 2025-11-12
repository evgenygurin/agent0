# R2R: Comprehensive Deployment & Architecture Report

## 1. WHAT IS R2R?

**R2R** (RAG to Riches) is an **advanced, production-ready AI retrieval system** built by SciPhi-AI that provides:

### Core Purpose
- **Retrieval-Augmented Generation (RAG)** framework for document understanding
- **Agentic RAG** with deep research capabilities (multi-step reasoning)
- **RESTful API** for enterprise-grade document management and search
- **Multimodal content ingestion** (PDF, TXT, JSON, PNG, MP3, etc.)

### Key Capabilities
1. **Semantic & Hybrid Search** - Vector search combined with full-text search
2. **Knowledge Graphs** - Automatic entity & relationship extraction
3. **Agentic RAG** - AI agent that can reason, search documents, query web, execute code
4. **Document Management** - Complete file lifecycle management with collections
5. **User & Access Control** - Authentication and collection-based access control
6. **Web Integration** - Web search and scraping capabilities

---

## 2. R2R COMPONENTS & ARCHITECTURE

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      R2R REST API (Port 7272)                   │
│                    (Python FastAPI Application)                  │
└────────────────────────────────────────────────────────────────┬┘
                                          │
         ┌────────────────────────────────┼────────────────────────────────┐
         │                                │                                │
         ▼                                ▼                                ▼
    ┌─────────────┐           ┌──────────────────┐         ┌──────────────────┐
    │ PostgreSQL  │           │  Vector Database │         │ LLM Providers    │
    │  Database   │           │  (pgvector/HNSW)│         │  (OpenAI, etc.)  │
    │ (Metadata)  │           │  (Embeddings)    │         │                  │
    └─────────────┘           └──────────────────┘         └──────────────────┘
         │                                │                        │
         └────────────────────────────────┼────────────────────────┘
                                          │
         ┌────────────────────────────────┼──────────────────────────┐
         │                                │                          │
         ▼                                ▼                          ▼
    ┌─────────────┐           ┌──────────────────┐     ┌──────────────────┐
    │   Redis     │           │  Search Engine   │     │ External APIs    │
    │   (Cache)   │           │  (Full-text)     │     │ (Serper, Crawl)  │
    └─────────────┘           └──────────────────┘     └──────────────────┘
```

### Component Breakdown

#### 1. **R2R Application Server**
- **Language**: Python 3.12+
- **Framework**: FastAPI
- **Port**: 7272 (default, configurable)
- **Mode**: RESTful API
- **SDKs**: Python (`r2r`) and JavaScript (`r2r-js`)

#### 2. **PostgreSQL Database**
- **Purpose**: Metadata storage (documents, chunks, users, collections, conversations)
- **Version**: Recommended 14+ 
- **Port**: 5432
- **Extensions Required**: `pgvector` (for vector operations)
- **Data Stored**:
  - Document metadata
  - Chunk information
  - User accounts & permissions
  - Collection definitions
  - Conversation history
  - Graph data (entities, relationships)

#### 3. **Vector Database (Embeddings)**
- **Technologies**: pgvector (PostgreSQL extension) or dedicated vector DB
- **Purpose**: Store and retrieve vector embeddings for semantic search
- **Data**: Document chunk embeddings (768-1536 dimensions typical)
- **Index Types**: HNSW (Hierarchical Navigable Small World) for fast retrieval

#### 4. **Redis Cache (Optional)**
- **Purpose**: Session caching, rate limiting, temporary data
- **Port**: 6379
- **Use Cases**: Performance optimization, distributed deployment

#### 5. **Search Engine (Full-text)**
- **Technology**: PostgreSQL Full-text search or external search engine
- **Purpose**: Keyword-based search alongside semantic search
- **Hybrid Search**: Combines semantic + full-text with RRF (Reciprocal Rank Fusion)

#### 6. **LLM Integration**
- **Supported Models**:
  - OpenAI (GPT-4, GPT-4o, etc.)
  - Anthropic (Claude 3 series)
  - Azure OpenAI
  - Custom models via LiteLLM
- **Purpose**: RAG generation and reasoning
- **Configuration**: Environment variables for API keys

#### 7. **External APIs (Optional)**
- **Serper** (web search) - requires `SERPER_API_KEY`
- **Firecrawl** (web scraping) - requires `FIRECRAWL_API_KEY`
- **Purpose**: Real-time web search in agentic RAG

---

## 3. DEPLOYMENT OPTIONS

### Option A: Light Mode (Local Development)
```bash
# Single command - minimal dependencies
export OPENAI_API_KEY=sk-...
r2r
```
**Includes**: In-memory SQLite, basic RAG
**Use Case**: Development, prototyping
**Requirements**: Python 3.12+, pip, OpenAI API key

### Option B: Full Mode with Docker Compose (Recommended for Production)

**Repository Structure**:
```
R2R/
├── docker/
│   ├── Dockerfile
│   └── docker-entrypoint.sh
├── compose.full.yaml      # Full production setup
├── compose.light.yaml     # Development setup
├── .env.example
└── deployment/
    └── k8s/              # Kubernetes files
```

**Deployment Command**:
```bash
git clone https://github.com/SciPhi-AI/R2R.git && cd R2R

# Export configuration
export R2R_CONFIG_NAME=full
export OPENAI_API_KEY=sk-...

# Run with docker compose
docker compose -f compose.full.yaml --profile postgres up -d
```

### Option C: Kubernetes (Enterprise Scale)
```
deployment/k8s/ contains Kubernetes manifests for:
- R2R API deployment
- PostgreSQL StatefulSet
- Service definitions
- ConfigMaps for configuration
```

---

## 4. PORTS & SERVICES

| Component | Port | Protocol | Purpose | Environment |
|-----------|------|----------|---------|-------------|
| R2R API | 7272 | HTTP/WebSocket | REST API & Streaming | All |
| PostgreSQL | 5432 | TCP | Database | Full mode |
| Redis | 6379 | TCP | Caching | Full mode (optional) |
| PgAdmin | 5050 | HTTP | DB Management | Development |

---

## 5. EXTERNAL DEPENDENCIES

### Required
1. **Python 3.12+**
2. **Docker & Docker Compose** (for containerized deployment)
3. **PostgreSQL 14+** (for full mode)
4. **LLM API Keys**:
   - OpenAI: `OPENAI_API_KEY`
   - Anthropic: `ANTHROPIC_API_KEY`
   - Azure: `AZURE_OPENAI_API_KEY`

### Optional
1. **Redis** (for caching/distributed deployment)
2. **Serper API Key** (`SERPER_API_KEY`) - for web search
3. **Firecrawl API Key** (`FIRECRAWL_API_KEY`) - for web scraping
4. **Postgres Extensions**:
   - `pgvector` - Vector storage
   - Full-text search (built-in)

---

## 6. ENVIRONMENT VARIABLES

### Core Configuration
```bash
# API Configuration
R2R_CONFIG_NAME=full              # "light" or "full"
R2R_LOG_LEVEL=DEBUG               # Log verbosity

# Server Configuration
R2R_PORT=7272                      # API port
R2R_HOST=0.0.0.0                  # Bind address

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/r2r
POSTGRES_PASSWORD=secure_password
POSTGRES_USER=r2r_user
POSTGRES_DB=r2r_db

# Redis (optional)
REDIS_URL=redis://localhost:6379

# LLM Providers
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=claude-...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=https://...

# External Services
SERPER_API_KEY=...                # Web search
FIRECRAWL_API_KEY=...             # Web scraping

# Security
JWT_SECRET_KEY=your-secret-key
```

---

## 7. DOCKER COMPOSE CONFIGURATION (FULL MODE)

### Service Definition
```yaml
services:
  r2r-api:
    image: ragtoriches/prod:latest
    ports:
      - "7272:7272"
    environment:
      - R2R_CONFIG_NAME=full
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATABASE_URL=postgresql://r2r_user:${POSTGRES_PASSWORD}@postgres:5432/r2r_db
    depends_on:
      - postgres
    networks:
      - r2r-network

  postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=r2r_user
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=r2r_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - r2r-network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    networks:
      - r2r-network

volumes:
  postgres_data:

networks:
  r2r-network:
    driver: bridge
```

---

## 8. QUICK START: LOCAL DEPLOYMENT

### Step 1: Clone Repository
```bash
git clone https://github.com/SciPhi-AI/R2R.git
cd R2R
```

### Step 2: Setup Environment
```bash
cp .env.example .env

# Edit .env with your API keys
nano .env
```

### Step 3: Run with Docker Compose
```bash
# Full mode with all services
export R2R_CONFIG_NAME=full
export OPENAI_API_KEY=sk-...
export POSTGRES_PASSWORD=your_secure_password

docker compose -f compose.full.yaml --profile postgres up -d
```

### Step 4: Verify Installation
```bash
# Check API is running
curl http://localhost:7272/v3/health

# Expected response: 200 OK with health status
```

### Step 5: Install Python SDK
```bash
pip install r2r

# Or JavaScript
npm install r2r-js
```

### Step 6: Test Basic Operations
```python
from r2r import R2RClient

client = R2RClient(base_url="http://localhost:7272")

# Ingest a sample document
response = client.documents.create_sample(hi_res=True)

# Perform search
results = client.retrieval.search(query="What is AI?")

# RAG query
answer = client.retrieval.rag(query="What is AI?")
print(answer.results.generated_answer)
```

---

## 9. PRODUCTION DEPLOYMENT CHECKLIST

- [ ] PostgreSQL database initialized with pgvector extension
- [ ] Redis configured (if using distributed mode)
- [ ] All API keys set in environment variables
- [ ] Docker images pulled and verified
- [ ] Networks configured for inter-container communication
- [ ] Volumes for persistent data (PostgreSQL) defined
- [ ] Health checks configured
- [ ] Logging aggregation setup
- [ ] Security: Firewall rules, API authentication
- [ ] Backup strategy for PostgreSQL
- [ ] Monitoring and alerting configured
- [ ] Load balancer configured (if multi-instance)

---

## 10. KEY FEATURES & CAPABILITIES

### Document Ingestion
- **Supported Formats**: PDF, TXT, JSON, PNG, MP3, DOCX, PPTX
- **Processing**: Automatic chunking, embedding generation, summarization
- **Metadata**: Document tracking, version control, collection assignment

### Search Modes
1. **Basic**: Simple semantic search (vector similarity)
2. **Advanced**: Hybrid search (semantic + full-text)
3. **Custom**: Fine-grained control over search parameters

### RAG Capabilities
- **Semantic Search**: Vector-based document retrieval
- **Hybrid Search**: Combines keyword and semantic matching
- **Knowledge Graphs**: Entity/relationship extraction and graph search
- **Citations**: Automatic source attribution in generated responses
- **Streaming**: Real-time response generation
- **Web Search**: Integration with external search APIs

### Agentic RAG (Deep Research)
- **Multi-step Reasoning**: Complex query analysis
- **Tool Usage**: Search, scrape, execute code, reason
- **Web Integration**: Real-time information gathering
- **Extended Thinking**: Claude 3.7 integration with reasoning budget
- **Conversation Memory**: Multi-turn dialogue support

### User Management
- **Authentication**: Email/password, API keys
- **Collections**: Organize documents by user/project
- **Permissions**: Fine-grained access control
- **Audit Logs**: Track API usage and modifications

---

## 11. MONITORING & HEALTH CHECKS

### Health Endpoint
```bash
curl http://localhost:7272/v3/health
```

### Available Metrics
- API response times
- Document ingestion status
- Search latency
- Vector database health
- LLM provider connectivity
- Database connection pool stats

---

## 12. TROUBLESHOOTING

### Common Issues

**Issue**: Port 7272 already in use
```bash
# Check what's using the port
lsof -i :7272

# Change port in docker-compose.yaml
ports:
  - "8000:7272"
```

**Issue**: PostgreSQL connection failed
```bash
# Verify PostgreSQL is running
docker ps | grep postgres

# Check credentials
echo $POSTGRES_PASSWORD
```

**Issue**: OpenAI API key not recognized
```bash
# Verify env var is set
echo $OPENAI_API_KEY

# Restart container to pick up new env var
docker compose restart r2r-api
```

---

## 13. USEFUL RESOURCES

- **Official Docs**: https://r2r-docs.sciphi.ai/
- **GitHub**: https://github.com/SciPhi-AI/R2R
- **Discord Community**: https://discord.gg/p6KqD2kjtB
- **Python SDK**: https://pypi.org/project/r2r/
- **JavaScript SDK**: https://www.npmjs.com/package/r2r-js

---

## SUMMARY TABLE

| Aspect | Details |
|--------|---------|
| **Type** | Production-ready RAG system |
| **API** | RESTful (Port 7272) |
| **Database** | PostgreSQL 14+ with pgvector |
| **Caching** | Redis (optional) |
| **Language** | Python 3.12+ (Core), JavaScript (SDK) |
| **Deployment** | Docker Compose, Kubernetes, Local |
| **Search** | Semantic, Full-text, Hybrid |
| **LLM Support** | OpenAI, Anthropic, Azure, Custom |
| **Special Feature** | Agentic RAG with web search & code execution |
| **License** | MIT (Open Source) |
