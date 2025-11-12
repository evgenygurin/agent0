# Railway Documentation Analysis Report
## Comprehensive Guide to Deployment, CLI, and Best Practices

Generated: November 12, 2025

---

## TABLE OF CONTENTS

1. [Railway CLI Installation & Setup](#railway-cli)
2. [Project & Service Management](#project-service-management)
3. [Environment Variables & Configuration](#environment-variables)
4. [Deployment Methods](#deployment-methods)
5. [Database Setup](#database-setup)
6. [Docker Deployments](#docker-deployments)
7. [Railway MCP Server](#railway-mcp-server)
8. [Advanced Features](#advanced-features)
9. [CLI Commands Reference](#cli-commands-reference)
10. [Best Practices](#best-practices)

---

## RAILWAY CLI INSTALLATION & SETUP {#railway-cli}

### Installation Methods

#### 1. **Homebrew (macOS)**
```bash
brew install railway
```

#### 2. **npm (macOS, Linux, Windows)**
```bash
npm install -g @railway/cli
# Requires Node.js >= v16
```

#### 3. **Shell Script (macOS, Linux, Windows via WSL)**
```bash
bash <(curl -fsSL cli.new)
```

#### 4. **Scoop (Windows)**
```powershell
scoop install railway
```

#### 5. **Pre-built Binaries**
Available on GitHub repository for direct download

### Authentication

#### Standard Login (with browser)
```bash
railway login
```
Opens browser tab for Railway authentication at https://railway.com

#### Manual Login (browserless - SSH sessions, CI/CD)
```bash
railway login --browserless
```
Generates a pairing code for manual authentication

### Token-Based Authentication

#### Project Token (RAILWAY_TOKEN)
- Scoped to specific project and environment
- Used for CI/CD pipelines
- Can perform: `railway up`, `railway redeploy`, `railway logs`
- Cannot perform: `railway init`, `railway whoami`, `railway link`

```bash
export RAILWAY_TOKEN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
railway up
```

#### Account Token (RAILWAY_API_TOKEN)
- Personal Account Token: Access to all resources
- Team Token: Access only to team projects within team scope
- Can perform: `railway init`, `railway whoami`
- Team tokens cannot: `railway whoami`, `railway link`

```bash
export RAILWAY_API_TOKEN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
railway whoami
```

**Important**: Only one token type can be active. RAILWAY_TOKEN takes precedence over RAILWAY_API_TOKEN.

---

## PROJECT & SERVICE MANAGEMENT {#project-service-management}

### Project Lifecycle Commands

#### Create a New Project
```bash
railway init
```
- Interactive prompt for project name and team selection
- Creates new project in Railway dashboard
- Links to current directory

#### Link to Existing Project
```bash
railway link
```
- Select team, project, and environment
- Associates current directory with project
- All future commands run against this project/environment

#### View Project Info
```bash
railway whoami
```
- Displays current user and account information
- Shows active token information

#### List All Projects
```bash
railway list
# (via MCP: list-projects)
```

### Service Management

#### Link to Specific Service
```bash
railway service
```
- Prompts to select service within linked project
- Sets default service for deployment commands

#### Add Database Service
```bash
railway add
```
- Interactive prompt to select databases
- Provisions PostgreSQL, Redis, MongoDB, MySQL, etc.
- Automatically creates service in project

#### Deploy Service
```bash
railway up
```
- Deploys current directory code/configuration
- Shows build logs in real-time
- Returns deployment status

#### Deploy (Non-blocking)
```bash
railway up --detach
```
- Uploads code and returns immediately
- Doesn't wait for build completion
- Useful for CI/CD pipelines

#### Redeploy Existing Deployment
```bash
railway redeploy
```
- Redeploys current service without code changes
- Useful for environment variable updates

---

## ENVIRONMENT VARIABLES & CONFIGURATION {#environment-variables}

### Variable Types

#### 1. **Service Variables** (Scoped to Individual Service)
- Defined via Dashboard → Service → Variables tab
- Service-specific configuration
- Not shared across services by default

#### 2. **Shared Variables** (Project-level)
- Defined via Dashboard → Project Settings → Shared Variables
- Access format: `${{ shared.VARIABLE_KEY }}`
- Reduce duplication across services

#### 3. **Reference Variables** (Cross-service)
- Reference variables from other services or shared variables
- Syntax: `${{ SERVICE_NAME.VAR }}`
- Example: `DATABASE_URL=${{ PostgreSQL.DATABASE_URL }}`

#### 4. **Railway-Provided Variables**
- **RAILWAY_PUBLIC_DOMAIN**: Public domain for service
- **RAILWAY_PRIVATE_DOMAIN**: Internal IPv6 domain (railway.internal)
- **RAILWAY_TCP_PROXY_PORT**: TCP proxy port for connections
- Auto-injected into all services

### Managing Variables via CLI

#### List Environment Variables
```bash
railway variables
```
Returns all variables for current service/environment

#### Set Environment Variables
```bash
railway variables set KEY=value
```
Sets single or multiple variables interactively

#### Run with Local Variables
```bash
railway run <command>
```
Executes local command with Railway environment variables
```bash
railway run npm start
railway run python manage.py migrate
```

#### Shell with Railway Variables
```bash
railway shell
```
Opens new shell session with Railway environment variables

### Variable Configuration Best Practices

#### Suggested Variables
- Railway scans GitHub repos for .env files
- Auto-detects and suggests variables:
  - `.env`
  - `.env.example`
  - `.env.local`
  - `.env.production`
  - `.env.<suffix>`

#### Sealed Variables (Extra Security)
```
Dashboard → Service Variables → Menu → Seal
```
- Values never visible in UI
- Not retrievable via API
- Cannot be un-sealed
- Cannot be used with `railway run` / `railway variables`

#### Multiline Variables
- Use Ctrl+Enter (Cmd+Enter on Mac) for newlines in UI
- Paste directly in Raw Editor mode

---

## DEPLOYMENT METHODS {#deployment-methods}

### 1. Git Repository Deployment (GitHub)

#### Setup Process
1. Connect Railway App to GitHub (one-time)
2. Select repository during service creation
3. Choose branch for deployment
4. Railway auto-deploys on branch updates

#### Configuration
```
Dashboard → Service → Settings → Source
- Select "Connect Repo"
- Choose repository and branch
- Set custom build/start commands if needed
```

#### Auto-Deployment with Environment Variables
- Check `.env` files in repo root
- Railway auto-suggests variables
- Deploy on every push to connected branch

### 2. Docker Image Deployment

#### Public Docker Images

**Sources**:
- Docker Hub: `bitnami/redis`
- GitHub Container Registry: `ghcr.io/railwayapp-templates/postgres-ssl:latest`
- GitLab Container Registry: `registry.gitlab.com/gitlab-cicd15/django-project`
- Quay.io: `quay.io/username/repo:tag`
- Microsoft Container Registry: `mcr.microsoft.com/dotnet/aspire-dashboard`

```bash
# Example deployment
railway init
# Select "Docker Image" as source
# Enter image path: nginx:latest
```

#### Private Docker Images (Pro Plan Required)

```bash
# Provide credentials during setup
- Registry URL: private-registry.com
- Username: your-username
- Password: your-password
```

For GitHub Container Registry:
- Use Personal Access Token (classic) for authentication
- Ensure token has proper scope

#### Docker Image Updates
- Railway monitors images for new versions
- Update button appears in service settings
- Can enable automatic updates with custom schedule
- Version tags (e.g., `nginx:1.25.3`) stage new versions
- Latest tags redeploy to pull newest digest

### 3. Local Directory Deployment

```bash
# Step 1: Create empty service in Dashboard
# Step 2: Navigate to project directory
cd /path/to/project

# Step 3: Link to Railway project
railway link
# Interactive: select team → project → environment

# Step 4: Deploy from local directory
railway up
# Deploys current directory code to selected service
```

**Supported Project Types**:
- Node.js
- Python (Django, Flask, FastAPI)
- Ruby on Rails
- Go
- Rust
- Java
- PHP
- .NET
- Static sites

### 4. Monorepo Deployment

```bash
# Railway detects monorepo structure
railway up
# Prompted to select which service to deploy
# Uses workspace root for deployment
```

---

## DATABASE SETUP {#database-setup}

### PostgreSQL Setup

#### Via Dashboard
```
Right-click on Project Canvas → Create → Database → PostgreSQL
```

#### Via CLI
```bash
railway add
# Select PostgreSQL from list
# Or directly: railway add-database postgresql
```

#### Connection in Services

**Reference PostgreSQL variables in other services**:
```
Service Variables → DATABASE_URL=${{ PostgreSQL.DATABASE_URL }}
```

**Auto-provided PostgreSQL variables**:
- `DATABASE_URL`: Full connection string
- `PGHOST`: Hostname
- `PGPORT`: Port (typically 5432)
- `PGUSER`: Username
- `PGPASSWORD`: Password
- `PGDATABASE`: Database name

### Redis Setup

#### Via Dashboard
```
Right-click on Project Canvas → Create → Database → Redis
```

#### Via CLI
```bash
railway add
# Select Redis from list
```

#### Connection Example
```
REDIS_URL=${{ Redis.REDIS_URL }}
```

### MongoDB, MySQL, and Other Databases

Railway supports multiple databases:
- **PostgreSQL**: Most common for web apps
- **Redis**: Caching, job queues (e.g., Sidekiq, Celery)
- **MongoDB**: NoSQL option
- **MySQL**: Alternative relational database
- **ClickHouse**: Analytics database (single node or distributed)

#### Add Any Database
```bash
railway add
# Select database from interactive list
```

### Database Best Practices

1. **Private Networking**: All databases connected via private network
   - Services access via `SERVICE_NAME.VARIABLE_NAME`
   - No public internet exposure unless configured

2. **Backups**: Available for services with volumes
   - Manual backups with "Create Backup" button
   - Automatic backup scheduling
   - Point-in-time restore capability
   - Incremental backups (pay only for changes)

3. **Volumes**: Persistent storage for databases
   - Default: 10GB ephemeral storage per service
   - Enable volume for data persistence
   - View metrics: disk usage, capacity
   - Snapshot and restore capabilities

4. **Migrations**: Run during deployment
   - Use `railway run <migration-command>`
   - Example: `railway run python manage.py migrate`
   - Or via SSH: `railway ssh -- python manage.py migrate`

---

## DOCKER DEPLOYMENTS {#docker-deployments}

### Deployment Sources

#### From Dockerfile in Repository
```
Dashboard → Service → Settings → Source → Connect Repo
- Railway auto-detects Dockerfile
- Builds OCI-compliant image
- Deploys automatically
```

#### From Public Docker Image
```
Dashboard → Service → Settings → Source → Docker Image
- Enter image name: nginx:latest
- Railway pulls and deploys
- Monitor updates in settings
```

#### From Private Docker Registry
```
Dashboard → Service → Settings → Source → Docker Image
- Enter image path
- Provide credentials:
  * Username
  * Password
  * Optional: Registry URL (if not Docker Hub)
```

### Custom Build Configuration

#### Custom Build Command
```
Dashboard → Service → Settings → Custom Build Command
```
Override default build process
```bash
# Example: Custom build for monorepo
npm install --workspace=api && npm run build --workspace=api
```

#### Custom Start Command
```
Dashboard → Service → Settings → Custom Start Command
```
Override default start process
```bash
# Example: Python with Gunicorn
gunicorn -w 4 -b 0.0.0.0:$PORT app:app

# Example: Node with custom port
PORT=$PORT node server.js
```

### Deployment Monitoring

#### View Build Logs
```bash
railway up
# Shows real-time build logs
```

#### View Deployment Logs
```bash
railway logs
# Shows deployment/runtime logs
```

#### Filter Build Logs
```bash
railway logs --deployment=<deployment-id> --build
```

---

## RAILWAY MCP SERVER {#railway-mcp-server}

### What is Railway MCP?

The **Model Context Protocol (MCP)** enables AI applications (Cursor, VS Code, Claude Desktop, Windsurf) to interact with Railway through standardized tool-based interface.

**Architecture**:
- **Hosts**: IDE applications (Cursor, Claude Desktop, etc.)
- **Clients**: MCP client layer within host
- **Servers**: Railway MCP Server exposing tools

### Installation

#### Claude Code (Recommended)
```bash
claude mcp add Railway npx @railway/mcp-server
```

#### Cursor
Add to `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "Railway": {
      "command": "npx",
      "args": ["-y", "@railway/mcp-server"]
    }
  }
}
```

#### VS Code
Add to `.vscode/mcp.json`:
```json
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

### Prerequisites for MCP
- Railway CLI installed
- Authenticated with `railway login`
- Working directory set to project root

### Available MCP Tools

#### Status
- `check-railway-status`: Verify CLI installation and authentication

#### Project Management
- `list-projects`: List all Railway projects
- `create-project-and-link`: Create new project and link to current directory

#### Service Management
- `list-services`: List services in current project
- `link-service`: Link specific service to current directory
- `deploy`: Deploy current service
- `deploy-template`: Deploy from Railway Template Library

#### Environment Management
- `create-environment`: Create new environment
- `link-environment`: Link environment to current directory

#### Configuration
- `list-variables`: List environment variables
- `set-variables`: Set environment variables
- `generate-domain`: Generate Railway domain for service

#### Monitoring
- `get-logs`: Retrieve service logs

### Usage Examples

#### Create and Deploy Next.js App
```
"Create a Next.js app in this directory and deploy it to Railway.
Also assign it a domain."
```

#### Deploy Database
```
"Deploy a Postgres database"
"Deploy a single node ClickHouse database"
```

#### Pull Environment Variables
```
"Pull environment variables for my project and save them to .env file"
```

#### Create Development Environment
```
"Create a development environment called `development` 
cloned from production and set it as linked"
```

### Security Considerations

**Important**: 
- Railway MCP is experimental (destructive operations excluded by design)
- Always review tool executions before running
- Restrict access to trusted users only
- Avoid production usage during testing phase
- Sealed variables NOT provided via MCP

---

## ADVANCED FEATURES {#advanced-features}

### SSH Access to Services

#### Copy SSH Command from Dashboard
```
Dashboard → Service → Right-click → Copy SSH Command
```

#### Interactive SSH Session
```bash
railway ssh --project=<project-id> --environment=<env-id> --service=<service-id>
```

#### Execute Single Command via SSH
```bash
railway ssh -- ls
railway ssh -- python manage.py migrate
```

### SSH Limitations & Workarounds

**Limitations**:
- No traditional SSH protocol (uses WebSocket)
- No SCP/sFTP file transfer
- No SSH tunneling or port forwarding
- Cannot use VS Code Remote-SSH

**Workarounds**:
- **File transfer**: Use HTTP endpoints with curl
- **Database access**: Use Tailscale subnet router
- **Private services**: Deploy file explorer service with volume mount

### Environments

#### Create Environment
```bash
railway environment create <name>
```

#### Duplicate Environment
```bash
railway environment create <new-name> --duplicate <existing-name>
```

#### Link to Environment
```bash
railway environment
# Interactive: select environment from list
```

#### Environment Isolation
- Each environment has separate databases and services
- Different configurations per environment (dev, staging, prod)
- Enable PR environments for automatic preview deployments

#### PR Environments
```
Dashboard → Project Settings → Environments → Enable PR Environments
```
- Creates preview environment for each GitHub PR
- Tests before merging to production
- Automatic cleanup after PR closure

### Networking

#### Private Network (Default)
- IPv6 Wireguard mesh (railway.internal)
- Services automatically connected within project
- Service DNS: `service-name.railway.internal`
- Only accessible to Railway services in same project

#### Generate Public Domain
```bash
railway domain
```
- Railway provides `*.railway.app` domain
- Must configure service to listen on port in environment

#### Custom Domain
```
Dashboard → Service → Settings → Networking → Add Custom Domain
```

### Volumes & Persistent Storage

#### Add Volume to Service
```
Dashboard → Service → Settings → Volumes → Create Volume
```

#### Volume Monitoring
```
Dashboard → Service → Volume Metrics
```
- Track disk usage over time
- Monitor capacity

#### Backup Management
```
Dashboard → Service → Backups
```
- Manual backup creation
- Automatic backup scheduling
- Point-in-time restore
- Backup locking (prevent accidental deletion)

---

## CLI COMMANDS REFERENCE {#cli-commands-reference}

### Authentication & Account
```bash
railway login                    # Browser-based authentication
railway login --browserless      # Pairing code authentication
railway logout                   # Logout current user
railway whoami                   # Show current user/account info
```

### Project Management
```bash
railway init                     # Create new project
railway link                     # Link to existing project
railway list                     # List all projects
```

### Service Management
```bash
railway service                  # Select/link service
railway add                      # Add database service
railway deploy                   # Deploy service
railway redeploy                 # Redeploy current deployment
railway up                       # Deploy with build logs (blocking)
railway up --detach              # Deploy without waiting (non-blocking)
```

### Configuration
```bash
railway environment              # Switch/select environment
railway variables                # View variables
railway variables set KEY=value  # Set environment variables
railway domain                   # Generate Railway domain
```

### Development
```bash
railway run <command>            # Run command with Railway env vars
railway shell                    # Open shell with Railway env vars
railway logs                     # View service logs
railway logs --deployment=<id>   # Logs for specific deployment
```

### SSH & Remote Access
```bash
railway ssh                      # Interactive SSH session
railway ssh -- <command>         # Execute single command via SSH
```

### Monitoring
```bash
railway logs                     # View deployment logs
railway logs --build             # View build logs only
```

---

## BEST PRACTICES {#best-practices}

### 1. Environment Management

**Do**:
- Use separate environments for dev, staging, production
- Clone production environment for development testing
- Use PR environments for preview deployments
- Reference database URLs via service variables

**Don't**:
- Hardcode environment variables in code
- Commit secrets to repository
- Use same database credentials across environments
- Test in production environment

### 2. Variable Management

**Do**:
- Use Reference Variables for cross-service communication
- Seal sensitive variables (API keys, passwords)
- Use shared variables to reduce duplication
- Take advantage of auto-suggested variables from .env files
- Document expected environment variables in README

**Don't**:
- Store secrets in code
- Use plain text for sensitive data
- Expose sealed variable values in logs
- Rely on unsealing (it's not possible)

### 3. Deployment Strategy

**Do**:
- Use GitHub integration for automatic deployments
- Enable branch protection and require PR reviews
- Test in preview environments before production
- Use meaningful commit messages for tracking
- Monitor deployment logs for issues

**Don't**:
- Deploy directly to production without testing
- Use `--detach` for critical deployments without monitoring
- Deploy during peak traffic without communication
- Skip build/deployment log review

### 4. Database Best Practices

**Do**:
- Always backup databases before migrations
- Run migrations via SSH or CLI before deployment
- Use volumes for persistent storage
- Monitor database disk usage
- Use reference variables for connection strings
- Implement connection pooling for high-traffic apps

**Don't**:
- Store database passwords in code
- Skip database migrations
- Assume ephemeral storage persists
- Connect to databases without authentication
- Use production database for testing

### 5. Docker Deployments

**Do**:
- Use specific image tags (not latest)
- Enable automatic image updates for patch versions
- Test images locally before deploying
- Use multi-stage builds for optimization
- Configure health checks in container

**Don't**:
- Use `latest` tag for production (limits debugging)
- Deploy untested images
- Skip image scanning for security vulnerabilities
- Use root user in containers
- Store credentials in Docker image

### 6. CLI Usage in CI/CD

**Do**:
- Use Project Token for deployment pipelines
- Set `RAILWAY_TOKEN` environment variable
- Use `--detach` flag for non-blocking deployments
- Implement proper error handling
- Log deployment status for audit trail

**Don't**:
- Commit tokens to repository
- Hardcode token values
- Use Account Token in CI/CD (use Project Token)
- Ignore deployment failures silently

### 7. SSH Access Best Practices

**Do**:
- Use SSH for debugging and temporary fixes
- Document SSH-based changes in issue tracker
- Implement changes via proper deployment cycle
- Monitor SSH usage periodically

**Don't**:
- Make permanent configuration changes via SSH
- Forget to implement fixes in code after SSH session
- Grant SSH access to untrusted users
- Use SSH for routine administrative tasks

### 8. Performance Optimization

**Do**:
- Enable replicas for high-traffic services
- Monitor CPU/memory metrics
- Implement caching (Redis)
- Use connection pooling for databases
- Optimize build times (cache dependencies)

**Don't**:
- Ignore resource utilization metrics
- Deploy inefficient code to production
- Use single replica for critical services
- Leave unused services running (affects billing)

### 9. Security

**Do**:
- Use sealed variables for secrets
- Implement environment-specific configurations
- Regular dependency updates
- Enable branch protection on GitHub
- Use IP whitelisting if available
- Audit team member access regularly

**Don't**:
- Share API tokens or credentials
- Commit environment files to git
- Deploy without security scanning
- Use default passwords/credentials
- Grant unnecessary permissions to team members

### 10. Monitoring & Observability

**Do**:
- Check deployment logs after each deployment
- Monitor service metrics (CPU, memory, network)
- Set up log aggregation for multi-service projects
- Track deployment frequency and success rate
- Alert on service failures

**Don't**:
- Ignore build or deployment failures
- Deploy without monitoring
- Skip log review before production push
- Assume services are healthy without verification

---

## WORKFLOW EXAMPLES

### Example 1: FastAPI + PostgreSQL Deployment

```bash
# 1. Create new Railway project
railway init

# 2. Connect GitHub repository
# (Optional - via Dashboard)
# Dashboard → Service → Connect Repo

# 3. Add PostgreSQL database
railway add
# Select: PostgreSQL

# 4. Set environment variables
railway variables set \
  DATABASE_URL='${{ PostgreSQL.DATABASE_URL }}' \
  ALLOWED_HOSTS='localhost,127.0.0.1' \
  DEBUG=False

# 5. Create development environment
railway environment create development

# 6. Run migrations locally
railway run alembic upgrade head

# 7. Deploy
railway up

# 8. Verify deployment
railway logs
```

### Example 2: Node.js + Redis + GitHub Auto-Deploy

```bash
# 1. Create project
railway init

# 2. Add Redis
railway add
# Select: Redis

# 3. Set Redis connection
railway variables set REDIS_URL='${{ Redis.REDIS_URL }}'

# 4. Connect GitHub (via Dashboard)
# Settings → Source → Connect Repo

# 5. Auto-deploy on push
git add .
git commit -m "feat: add Redis caching"
git push
# Railway automatically builds and deploys

# 6. Monitor deployment
railway logs --follow
```

### Example 3: Private Docker Image Deployment

```bash
# 1. Create service for Docker image
railway init

# 2. Configure Docker source (via Dashboard)
# Service → Settings → Source → Docker Image
# Image: myregistry.azurecr.io/myapp:1.0.0
# Credentials: username, password

# 3. Set environment variables
railway variables set APP_ENV=production

# 4. Enable auto-updates
# Dashboard → Service → Settings → Auto Update
# Schedule: Weekly on Sunday 2 AM

# 5. Test with railway run
railway run python manage.py health_check

# 6. Deploy
railway up --detach
```

---

## TROUBLESHOOTING

### Common Issues

**Issue**: Build fails with "Dockerfile not found"
- **Solution**: Ensure Dockerfile is in project root
- Or specify custom build command in service settings

**Issue**: Environment variables not available
- **Solution**: Redeploy after adding variables
- Variables require staged changes to be deployed

**Issue**: Database connection refused
- **Solution**: Use reference variables `${{ PostgreSQL.DATABASE_URL }}`
- Ensure database service is running in same environment

**Issue**: SSH connection timeout
- **Solution**: Service must be running (check metrics)
- Serverless services may need wake-up request
- Check firewall/network restrictions

**Issue**: Docker image updates not reflected
- **Solution**: Use specific version tags for versioning
- `:latest` tag requires explicit redeploy

---

## USEFUL RESOURCES

### Official Documentation
- **Main Docs**: https://docs.railway.com/
- **CLI Reference**: https://docs.railway.com/guides/cli
- **Public API**: https://docs.railway.com/reference/public-api
- **MCP Server**: https://docs.railway.com/reference/mcp-server
- **Templates**: https://railway.app/templates

### External Tools
- **Railway Templates**: Pre-built applications ready to deploy
- **GitHub Integration**: https://github.com/apps/railway-app/
- **Railway CLI GitHub**: Open source repository

---

**End of Report**

