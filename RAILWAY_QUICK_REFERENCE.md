# Railway Quick Reference Card

## Most Essential Commands

### Initial Setup
```bash
brew install railway              # Install CLI
railway login                      # Authenticate
railway init                       # Create new project
railway link                       # Link to existing project
```

### Deployment
```bash
railway up                         # Deploy with logs
railway up --detach                # Deploy without waiting
railway redeploy                   # Redeploy without code changes
```

### Environment & Configuration
```bash
railway environment                # Switch environment
railway variables                  # List variables
railway variables set KEY=value    # Set environment variable
railway add                        # Add database service
```

### Development
```bash
railway run npm start              # Run command with Railway vars
railway shell                      # Interactive shell with vars
railway logs                       # View logs
railway ssh                        # SSH into service
```

---

## Token Types Quick Reference

| Token Type | Use Case | Can Do | Cannot Do |
|-----------|----------|---------|-----------|
| **RAILWAY_TOKEN** (Project) | CI/CD pipelines | deploy, logs, redeploy | init, whoami, link |
| **RAILWAY_API_TOKEN** (Account/Team) | Account operations | init, whoami, all operations | - |

---

## Variable Reference Syntax

```bash
# Shared variable
${{ shared.API_KEY }}

# Another service's variable
${{ PostgreSQL.DATABASE_URL }}
${{ backend.RAILWAY_PUBLIC_DOMAIN }}

# Same service variable
${{ BASE_URL }}/{{ AUTH_PATH }}
```

---

## Deployment Sources Comparison

| Source | Setup | Auto-Deploy | Speed | Control |
|--------|-------|------------|-------|---------|
| **GitHub Repo** | Connect repo | Yes | Medium | Medium |
| **Docker Image** | Specify image | Optional | Fast | High |
| **Local Dir** | `railway up` | No | Fast | Full |
| **Monorepo** | Select service | Yes | Medium | Medium |

---

## Database Connection Pattern

```bash
# Add database
railway add
# Select: PostgreSQL (or other)

# Reference in another service
railway variables set DATABASE_URL='${{ PostgreSQL.DATABASE_URL }}'

# Use in code
import os
db_url = os.environ.get('DATABASE_URL')
```

---

## Environment Setup Pattern

```bash
# Create development environment
railway environment create development

# Clone from production
railway environment create staging --duplicate production

# Link to environment
railway environment
# Select from interactive list
```

---

## SSH Command Pattern

```bash
# Copy from dashboard or build command
railway ssh --project=<id> --environment=<id> --service=<id>

# Or after linking
railway ssh

# Execute single command
railway ssh -- python manage.py migrate
railway ssh -- ls -la /app
```

---

## Railway MCP Installation

```bash
# Claude Code
claude mcp add Railway npx @railway/mcp-server

# Cursor (.cursor/mcp.json)
{
  "mcpServers": {
    "Railway": {
      "command": "npx",
      "args": ["-y", "@railway/mcp-server"]
    }
  }
}

# VS Code (.vscode/mcp.json)
{
  "servers": {
    "Railway": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@railway/mcp-server"]
    }
  }
}
```

---

## Common Deployment Patterns

### FastAPI + PostgreSQL
```bash
railway init
railway add  # PostgreSQL
railway variables set DATABASE_URL='${{ PostgreSQL.DATABASE_URL }}'
railway up
```

### Node.js + Redis
```bash
railway init
railway add  # Redis
railway variables set REDIS_URL='${{ Redis.REDIS_URL }}'
railway up
```

### Docker Image (Private)
```bash
railway init
# Dashboard: Service → Settings → Source → Docker Image
# Enter: myregistry.com/myapp:1.0.0, credentials
railway up
```

---

## Performance Optimization Checklist

- [ ] Enable replicas for high-traffic services
- [ ] Use specific Docker image tags (not `latest`)
- [ ] Enable Redis for caching
- [ ] Set up database connection pooling
- [ ] Monitor CPU/memory metrics
- [ ] Optimize build time (cache dependencies)
- [ ] Use multi-stage Docker builds
- [ ] Enable auto-updates for Docker images

---

## Security Checklist

- [ ] Use sealed variables for secrets
- [ ] Set RAILWAY_TOKEN (not API_TOKEN) for CI/CD
- [ ] Enable branch protection on GitHub
- [ ] Review environment variables regularly
- [ ] Use reference variables (not hardcoded URLs)
- [ ] Regular dependency updates
- [ ] Enable PR environments for testing
- [ ] Audit team member access
- [ ] Use custom domains for production
- [ ] Enable backups for databases

---

## Troubleshooting Quick Map

| Problem | Solution |
|---------|----------|
| Build fails | Check Dockerfile location or custom build command |
| Variables not working | Redeploy after adding variables |
| DB connection fails | Use reference variables: `${{ Service.VAR }}` |
| SSH timeout | Service must be running; check metrics |
| Docker image old | Use specific tags; `:latest` needs redeploy |
| No deploy on push | Check GitHub integration; enable auto-deploy |
| Environment var conflicts | Use different env names or reference properly |
| Memory/CPU maxed | Enable replicas; optimize code; check logs |

---

## Common Commands by Workflow

### Daily Development
```bash
railway environment          # Switch env if needed
railway shell               # Get Railway vars
railway logs                # Check logs
```

### Before Production Push
```bash
railway environment          # Ensure on prod
railway logs                 # Review recent logs
railway variables            # Verify config
git push                     # Trigger auto-deploy
railway logs --follow        # Monitor deployment
```

### Debugging Production Issue
```bash
railway ssh                  # Connect to service
# Run diagnostics, check logs, etc.
railway logs                 # Review full logs
railway variables            # Check configuration
# Make code fixes locally
git push                     # Deploy fix
railway logs --follow        # Verify fix
```

### Database Maintenance
```bash
railway ssh -- psql          # Connect to PostgreSQL
# Run migrations, queries
# Or:
railway run python manage.py migrate
railway logs                 # Verify success
```

---

## Worth Remembering

- Variables require **redeploy** to take effect
- Sealed variables **cannot** be unsealed
- Project tokens limited to specific projects
- SSH uses **WebSocket**, not standard SSH protocol
- Private networking is **default** (railway.internal)
- Default storage is **10GB ephemeral** (use volumes for persistence)
- Auto-suggest works with **.env** files in repo root
- Reference variables use **${{ }}** template syntax
- Build cache helps with **repeated deployments**
- Replicas cost extra but improve **reliability**

---

## Useful Links

| Resource | URL |
|----------|-----|
| Main Docs | https://docs.railway.com/ |
| CLI Reference | https://docs.railway.com/guides/cli |
| Public API | https://docs.railway.com/reference/public-api |
| MCP Server | https://docs.railway.com/reference/mcp-server |
| Templates | https://railway.app/templates |
| GitHub Integration | https://github.com/apps/railway-app |

