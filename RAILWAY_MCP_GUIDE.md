# Railway MCP Server Integration Guide

## What is Railway MCP?

The **Model Context Protocol (MCP)** is a standardized interface that allows AI assistants (Claude, via Cursor/VS Code/Claude Desktop) to interact with Railway programmatically.

Instead of manually running CLI commands, you can describe what you want to do in natural language, and the AI assistant will translate it to appropriate Railway CLI commands.

---

## Installation & Setup

### For Claude Code Users

```bash
claude mcp add Railway npx @railway/mcp-server
```

This installs the Railway MCP server and enables it for Claude Code integration.

### Verification

After installation, verify Railway CLI is set up:

```bash
railway login      # Authenticate if needed
railway whoami     # Should return user info
```

---

## Using Railway MCP with Claude Code

### Example 1: Create and Deploy a Full Stack App

**Natural Language Request**:
```
Create a Next.js application in this directory and deploy it to Railway.
Also create a PostgreSQL database and set up a Redis service.
Configure the environment variables for the database connection.
```

**What Claude Code Will Do**:
1. Create project: `railway init`
2. Create Next.js boilerplate
3. Add PostgreSQL: `railway add` → select PostgreSQL
4. Add Redis: `railway add` → select Redis
5. Set variables: `railway variables set DATABASE_URL='${{ PostgreSQL.DATABASE_URL }}'`
6. Deploy: `railway up`
7. Generate domain: `railway domain`

### Example 2: Deploy from Template

**Natural Language Request**:
```
Deploy a Django REST API application to Railway from a template.
Make sure it uses PostgreSQL database.
Generate a Railway domain for it.
```

**What Claude Code Will Do**:
1. List templates: `railway init`
2. Deploy Django template
3. Add PostgreSQL
4. Configure database connection
5. Generate public domain
6. Show deployment logs

### Example 3: Pull Environment Variables

**Natural Language Request**:
```
Show me all environment variables for this project.
Save them to a .env file locally.
```

**What Claude Code Will Do**:
1. Link to project if needed
2. List variables: `railway variables`
3. Format for .env file
4. Save to `.env` (hidden in git)

### Example 4: Create Development Environment

**Natural Language Request**:
```
Create a development environment called 'dev' by cloning production.
Link it to my current directory.
Show me the environment variables.
```

**What Claude Code Will Do**:
1. Clone environment: `railway environment create dev --duplicate production`
2. Link environment: `railway environment`
3. List variables for new environment
4. Update local context

### Example 5: Debug Deployment Issues

**Natural Language Request**:
```
The deployment is failing. Show me the build logs and explain what's wrong.
```

**What Claude Code Will Do**:
1. Fetch build logs: `railway logs`
2. Analyze for errors
3. Suggest fixes (build command, dependencies, etc.)
4. Recommend solutions

---

## Available MCP Tools Explained

### Status Tools

#### `check-railway-status`
Verifies that Railway CLI is installed and authenticated.

**Use When**:
- Setting up Railway for first time
- Troubleshooting authentication issues
- Starting new work session

**Example**:
```
Check if Railway CLI is properly installed and authenticated.
```

### Project Management Tools

#### `list-projects`
Lists all Railway projects for current account.

**Use When**:
- Discovering available projects
- Finding project ID or name
- Understanding current project landscape

**Example**:
```
Show me all my Railway projects and their status.
```

#### `create-project-and-link`
Creates new Railway project and links current directory.

**Use When**:
- Starting new application
- Creating isolated environment for project
- Setting up from scratch

**Example**:
```
Create a new Railway project called 'my-api' and link it here.
```

### Service Management Tools

#### `list-services`
Lists all services in current project.

**Use When**:
- Understanding project structure
- Finding service names for reference
- Checking what's deployed

**Example**:
```
What services are deployed in this project?
```

#### `link-service`
Links specific service to current directory.

**Use When**:
- Switching between services in monorepo
- Setting up CLI for specific service
- Deploying to non-default service

**Example**:
```
Link me to the 'backend' service in this project.
```

#### `deploy`
Deploys current service.

**Use When**:
- After code changes
- Redeploying with environment variable changes
- Testing deployment pipeline

**Example**:
```
Deploy the current application to Railway.
```

#### `deploy-template`
Deploys pre-built template to Railway.

**Use When**:
- Creating starter application
- Using best-practice setup
- Rapid prototyping

**Example**:
```
Deploy the FastAPI template to Railway.
```

### Environment Management Tools

#### `create-environment`
Creates new environment (dev, staging, prod, etc.)

**Use When**:
- Setting up dev/staging/prod pipeline
- Cloning production for testing
- Creating ephemeral environments

**Example**:
```
Create a staging environment by cloning production.
Link it to my current directory.
```

#### `link-environment`
Links current directory to specific environment.

**Use When**:
- Switching between environments
- Working on specific environment
- Managing multi-environment projects

**Example**:
```
Switch me to the development environment.
```

### Configuration Tools

#### `list-variables`
Lists environment variables for current service/environment.

**Use When**:
- Reviewing configuration
- Checking what variables are set
- Understanding environment setup

**Example**:
```
Show me all environment variables for this service.
```

#### `set-variables`
Sets environment variables for service/environment.

**Use When**:
- Configuring application
- Adding secrets
- Updating configuration

**Example**:
```
Set DATABASE_URL to reference the PostgreSQL service.
Set API_KEY to [secret-value] (sealed).
```

#### `generate-domain`
Generates Railway domain for public access.

**Use When**:
- Making service publicly accessible
- Setting up API endpoint
- Creating website domain

**Example**:
```
Generate a public Railway domain for this service.
```

### Monitoring Tools

#### `get-logs`
Retrieves service logs (build or deployment).

**Use When**:
- Debugging deployment failures
- Monitoring application health
- Understanding application behavior

**Example**:
```
Show me the deployment logs for the last 50 lines.
```

---

## Practical Workflow Examples

### Workflow 1: Complete Project Setup

```
Step 1: "Create a new Railway project called 'marketplace'"
→ Uses: create-project-and-link

Step 2: "Deploy a Django REST backend application"
→ Uses: deploy-template (Django template)

Step 3: "Add PostgreSQL and Redis databases"
→ Uses: railway add (CLI command)

Step 4: "Configure database connection variables"
→ Uses: set-variables
→ Set: DATABASE_URL = ${{ PostgreSQL.DATABASE_URL }}
→ Set: REDIS_URL = ${{ Redis.REDIS_URL }}

Step 5: "Create a staging environment"
→ Uses: create-environment
→ Clone from production

Step 6: "Generate a public domain"
→ Uses: generate-domain

Step 7: "Deploy the application"
→ Uses: deploy
```

### Workflow 2: Multi-Service Monorepo

```
Step 1: "Link to the API service"
→ Uses: link-service (select: api)

Step 2: "Deploy the API service"
→ Uses: deploy

Step 3: "Switch to the frontend service"
→ Uses: link-service (select: web)

Step 4: "Set frontend environment variables to reference API"
→ Uses: set-variables
→ Set: API_URL = https://${{ api.RAILWAY_PUBLIC_DOMAIN }}

Step 5: "Deploy the frontend"
→ Uses: deploy

Step 6: "Check all services are running"
→ Uses: list-services
```

### Workflow 3: Debugging & Fixing Issues

```
Step 1: "Show me the deployment logs"
→ Uses: get-logs

Step 2: "What services are running?"
→ Uses: list-services

Step 3: "List all environment variables"
→ Uses: list-variables

Step 4: "Set ENVIRONMENT to 'production'"
→ Uses: set-variables

Step 5: "Redeploy after the variable change"
→ Uses: deploy (or manual: railway redeploy)

Step 6: "Check if the fix worked"
→ Uses: get-logs
```

### Workflow 4: Environment Management

```
Step 1: "Show me all my projects"
→ Uses: list-projects

Step 2: "Create a 'development' environment from production"
→ Uses: create-environment

Step 3: "Link to the development environment"
→ Uses: link-environment (select: development)

Step 4: "Pull environment variables to .env file"
→ Uses: list-variables (save to file)

Step 5: "Run application locally with Railway variables"
→ Uses: railway run (CLI - not MCP)
```

---

## Security & Best Practices with MCP

### Do's

✅ **Do** review CLI commands before execution
- Claude will suggest commands; review them
- Understand what each command will do
- Never blindly accept suggestions

✅ **Do** use sealed variables for secrets
- Request: "Set API_KEY to [secret] (sealed)"
- Prevents exposure in logs/UI

✅ **Do** use reference variables
- Request: "Set DATABASE_URL to reference PostgreSQL"
- Better than hardcoding connection strings

✅ **Do** work in preview/staging first
- Create dev environment before production
- Test changes before deploying to prod

✅ **Do** check environment before operations
- Verify you're in correct environment
- Confirm service selection
- Review logs after deployment

### Don'ts

❌ **Don't** run destructive commands without confirmation
- Deleting services is NOT exposed in MCP (by design)
- Always review before confirming

❌ **Don't** commit sealed variables
- They can't be exported/unsealed
- MCP won't include them in .env files

❌ **Don't** assume MCP has all capabilities
- MCP is experimental (some features may be missing)
- Fall back to CLI for advanced operations

❌ **Don't** skip testing in non-production
- Use PR environments or staging
- Never test in production

❌ **Don't** share token with MCP
- CLI uses local authentication
- MCP inherits Railway session (safer)

---

## Limitations & Workarounds

### Current Limitations

1. **No file operations**: Cannot directly read/write local files
   - **Workaround**: Claude will provide content to paste/copy

2. **No destructive operations**: Cannot delete services/environments
   - **Reason**: Safety by design
   - **Workaround**: Delete via Dashboard if needed

3. **Sealed variables not exported**: Cannot retrieve sealed variable values
   - **Reason**: Security feature (values hidden)
   - **Workaround**: Reseal variable only when needed

4. **Limited to CLI operations**: Only supports Railway CLI functionality
   - **Workaround**: Use Railway Dashboard for advanced settings

### Workarounds

**For file operations**:
```
Claude: "I'll create a .env file content for you"
Content:
DATABASE_URL=...
API_KEY=...
(Copy and paste to .env)
```

**For complex operations**:
```
Claude: "For this advanced configuration, use the Dashboard:
Settings → Variables → [operation]"
```

---

## Integration with Other Tools

### With GitHub Actions (CI/CD)

MCP helps set up Railway, then GitHub Actions handles automation:

1. Claude sets up Railway project via MCP
2. Configure GitHub integration via Dashboard
3. Push code triggers auto-deployment
4. GitHub Actions can use `RAILWAY_TOKEN` for additional operations

### With Local Development

MCP + local CLI:

```bash
# Use MCP through Claude for project setup
# Use CLI for daily development

railway shell              # Get Railway vars locally
npm start                  # Run with Railway config
railway run npm start      # Alternative: direct run
```

### With Infrastructure as Code

MCP for quick setup, IaC for maintainability:

```
# Use MCP for rapid prototyping
# Export configuration
# Convert to Terraform/other IaC
# Commit IaC to version control
```

---

## Troubleshooting MCP Issues

### Problem: "Railway CLI not found"

**Solution**:
```bash
railway login          # Authenticate
railway whoami         # Verify installation
```

### Problem: "Permission denied" in MCP

**Solution**:
- Ensure Railway account has access to project
- Use appropriate token type (RAILWAY_TOKEN for project operations)
- Verify team membership for team operations

### Problem: MCP operations timing out

**Solution**:
- Check internet connection
- Verify Railway service status
- Retry operation (sometimes transient)
- Use CLI directly if MCP continues failing

### Problem: Variables not reflecting after MCP sets them

**Solution**:
- MCP only stages changes
- Use `deploy` tool to apply variables
- Or manually: `railway redeploy`

### Problem: "Check railway-status" fails

**Solution**:
```bash
# Reinstall Railway CLI
brew install railway    # macOS
npm install -g @railway/cli  # Any OS

# Re-authenticate
railway login
```

---

## Examples: Natural Language → MCP Tools

### Natural Language to Tool Mapping

| Request | MCP Tool | CLI Equivalent |
|---------|----------|---|
| "Show me my projects" | `list-projects` | `railway list` |
| "Create a new project" | `create-project-and-link` | `railway init` |
| "What services are running?" | `list-services` | `railway service` |
| "Deploy my changes" | `deploy` | `railway up` |
| "Show deployment logs" | `get-logs` | `railway logs` |
| "Set DATABASE_URL" | `set-variables` | `railway variables set` |
| "Create dev environment" | `create-environment` | `railway environment create` |
| "Get public domain" | `generate-domain` | `railway domain` |

---

## Advanced: Chaining Operations

### Multi-Step Request Pattern

```
"I want to:
1. Create a new project called 'api-server'
2. Deploy the FastAPI template
3. Add PostgreSQL database
4. Set DATABASE_URL to reference PostgreSQL
5. Create a staging environment by cloning production
6. Generate a domain
7. Show me the logs"
```

Claude Code will:
1. Execute operations in sequence
2. Handle dependencies (create before deploy)
3. Show progress and results
4. Highlight any issues

### Conditional Operations

```
"Check the deployment logs. If there are errors,
suggest fixes. If successful, generate a domain
and show me the public URL."
```

Claude Code will:
1. Run `get-logs`
2. Analyze output
3. Execute conditional operations based on results
4. Provide next steps

---

## Next Steps

1. **Install Railway CLI**: `brew install railway`
2. **Authenticate**: `railway login`
3. **Install MCP**: `claude mcp add Railway npx @railway/mcp-server`
4. **Start using**: Ask Claude to create/deploy Railway projects
5. **Learn patterns**: Refer to workflow examples above
6. **Report issues**: Use Railway GitHub for bugs

---

**Railway MCP Server Status**: Experimental (improving rapidly)
**Last Updated**: 2025
**Documentation**: https://docs.railway.com/reference/mcp-server

