# R2R Documentation & Analysis

This directory contains comprehensive documentation about R2R (RAG to Riches) - an advanced, production-ready AI retrieval system built by SciPhi-AI.

## Files in This Directory

### 1. **R2R_SUMMARY.txt** (Reference Card)
**Size:** ~17 KB | **Format:** Plain text quick reference

Quick-reference guide covering:
- Executive summary of R2R
- Core components and ports
- System architecture diagram
- Deployment options (Light, Full, Kubernetes)
- External dependencies checklist
- Environment variables reference
- Docker Compose quick start (7 steps)
- Key features by domain
- Production deployment checklist
- Python SDK quick reference
- Troubleshooting guide
- Monitoring & health checks

**Best for:** Quick lookup, deployment checklists, troubleshooting

### 2. **R2R_DEPLOYMENT_GUIDE.md** (Comprehensive)
**Size:** ~14 KB | **Format:** Markdown

Detailed deployment guide including:
- What is R2R and why use it (with capabilities list)
- Complete architecture breakdown (7 components explained)
- 3 deployment options with pros/cons
- Ports and services reference table
- All required and optional dependencies
- Full environment variables configuration
- Docker Compose YAML template (production)
- 8-step quick start guide
- Production deployment checklist
- 10 key features by category
- 11 monitoring & health checks
- 12 troubleshooting solutions
- 13 useful resources and links
- Summary comparison table

**Best for:** Initial setup, understanding architecture, deployment planning

### 3. **R2R_EXAMPLES.md** (Code Reference)
**Size:** ~19 KB | **Format:** Markdown with code samples

Practical code examples including:
- Installation & prerequisites
- Complete Docker Compose configurations (full + light modes)
- .env file template with all variables explained
- Python SDK examples:
  - Basic setup & authentication
  - Document management (upload, list, delete)
  - Basic search
  - Hybrid search with filters
  - Advanced filtering
  - RAG queries
  - Streaming RAG with events
  - Agentic RAG (deep research)
  - Collections & access control
  - Multi-turn conversations
- JavaScript SDK examples (parallel to Python)
- cURL API endpoint examples
- Advanced search patterns
- Monitoring & debugging commands

**Best for:** Implementation, copy-paste ready code, SDK usage

## Quick Navigation Guide

### "I want to understand what R2R is..."
→ Start with **R2R_SUMMARY.txt** (sections 1-2)

### "I need to deploy R2R immediately..."
→ Go to **R2R_DEPLOYMENT_GUIDE.md** (section 8: Quick Start)
→ Also check **R2R_EXAMPLES.md** (section 2: Docker Compose)

### "I need to understand the architecture..."
→ Read **R2R_DEPLOYMENT_GUIDE.md** (section 2: Components)
→ See **R2R_SUMMARY.txt** (section 3: System Architecture)

### "I need to write code using R2R..."
→ Check **R2R_EXAMPLES.md** (sections 4-7: SDK Examples)
→ Reference **R2R_SUMMARY.txt** (section 10: Python SDK Quick Reference)

### "My deployment is failing..."
→ Use **R2R_SUMMARY.txt** (section 11: Troubleshooting)
→ Check **R2R_EXAMPLES.md** (section 8: Monitoring & Debugging)

### "I need a production checklist..."
→ Review **R2R_DEPLOYMENT_GUIDE.md** (section 9: Production Checklist)
→ Also **R2R_SUMMARY.txt** (section 9: Production Deployment Checklist)

### "I need to configure environment variables..."
→ See **R2R_DEPLOYMENT_GUIDE.md** (section 6: Environment Variables)
→ Use template in **R2R_EXAMPLES.md** (section 3: .env File Template)

## Key Information At a Glance

### R2R Basics
- **Purpose:** Production-ready Retrieval-Augmented Generation (RAG) system
- **Creator:** SciPhi-AI
- **License:** MIT (Open Source)
- **GitHub:** https://github.com/SciPhi-AI/R2R
- **Official Docs:** https://r2r-docs.sciphi.ai/
- **Community:** https://discord.gg/p6KqD2kjtB

### Technical Stack
- **Language:** Python 3.12+ (Core), JavaScript (SDK)
- **Framework:** FastAPI for REST API
- **Database:** PostgreSQL 14+ with pgvector
- **Cache:** Redis 7+ (optional)
- **API Port:** 7272 (default, configurable)

### Deployment Options
1. **Light Mode** - Single command, SQLite (development)
2. **Full Mode** - Docker Compose with PostgreSQL (recommended)
3. **Kubernetes** - Enterprise-scale deployments

### Core Capabilities
- Semantic & Hybrid Search (vector + full-text with RRF)
- Knowledge Graphs (entity & relationship extraction)
- Agentic RAG (multi-step reasoning with tools)
- Document Management (multimodal: PDF, TXT, JSON, PNG, MP3, etc.)
- User & Access Control (authentication + collections)
- Web Integration (web search and scraping)

### External Dependencies
**Required:**
- Python 3.12+
- Docker & Docker Compose
- PostgreSQL 14+
- LLM API Key (OpenAI, Anthropic, or Azure)

**Optional:**
- Redis 7+ (caching)
- Serper API Key (web search)
- Firecrawl API Key (web scraping)

## File Locations

```
/Users/laptop/dev/agent0/
├── R2R_README.md              (This file - Navigation guide)
├── R2R_SUMMARY.txt            (Quick reference - 464 lines)
├── R2R_DEPLOYMENT_GUIDE.md    (Architecture & deployment - 461 lines)
├── R2R_EXAMPLES.md            (Code samples & configs - 881 lines)
└── docs/r2r/                  (Original documentation source)
    ├── README.md              (R2R Getting Started)
    ├── general/               (Documents, Collections, Users, etc.)
    ├── retrieval/             (Search, RAG, Agentic RAG)
    └── advanced/              (Deduplication, Enrichment)
```

## How to Use These Documents

### For Quick Reference
1. Open **R2R_SUMMARY.txt** in any text editor
2. Use Ctrl+F to search for specific topics
3. Each section is numbered for easy navigation

### For Learning
1. Start with **R2R_DEPLOYMENT_GUIDE.md** section 1-2
2. Review the architecture in section 2 and 3
3. Study the deployment options in section 3

### For Implementation
1. Use **R2R_EXAMPLES.md** to copy configuration templates
2. Reference the Python/JavaScript SDK examples
3. Adapt the code samples to your use case

### For Troubleshooting
1. Check **R2R_SUMMARY.txt** section 11
2. Look at **R2R_EXAMPLES.md** section 8 for debugging commands
3. Consult original docs at https://r2r-docs.sciphi.ai/

## Important Ports

| Service | Port | Protocol | Purpose |
|---------|------|----------|---------|
| R2R API | 7272 | HTTP/WebSocket | Main REST API |
| PostgreSQL | 5432 | TCP | Database |
| Redis | 6379 | TCP | Cache (optional) |
| PgAdmin | 5050 | HTTP | DB Management (dev) |

## Deployment Quick Command

```bash
# Clone repository
git clone https://github.com/SciPhi-AI/R2R.git && cd R2R

# Setup environment
export R2R_CONFIG_NAME=full
export OPENAI_API_KEY=sk-your-key
export POSTGRES_PASSWORD=your-password

# Start services
docker compose -f compose.full.yaml --profile postgres up -d

# Verify
curl http://localhost:7272/v3/health
```

## Next Steps

1. **Review the architecture** → Read R2R_DEPLOYMENT_GUIDE.md section 2
2. **Plan your deployment** → Use R2R_SUMMARY.txt section 4
3. **Prepare environment** → Copy template from R2R_EXAMPLES.md section 3
4. **Deploy R2R** → Follow R2R_DEPLOYMENT_GUIDE.md section 8
5. **Test with code** → Use examples from R2R_EXAMPLES.md sections 4-7
6. **Monitor deployment** → Reference R2R_SUMMARY.txt section 12

## Resources

- **Official Documentation:** https://r2r-docs.sciphi.ai/
- **GitHub Repository:** https://github.com/SciPhi-AI/R2R
- **Python SDK:** https://pypi.org/project/r2r/
- **JavaScript SDK:** https://www.npmjs.com/package/r2r-js
- **Community Discord:** https://discord.gg/p6KqD2kjtB

---

**Report Generated:** 2024-11-12  
**Source:** R2R Official Documentation + GitHub  
**Total Lines:** 1,806 across 3 documents  
**Completeness:** Comprehensive (covers architecture, deployment, examples, and troubleshooting)
