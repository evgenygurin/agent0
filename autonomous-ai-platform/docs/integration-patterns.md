# Integration Patterns for Autonomous AI Development Platform

## Overview

This document provides detailed integration patterns for connecting R2R, Codegen, Linear, and Claude Code into a cohesive autonomous development system.

## 1. R2R Integration Patterns

### 1.1 Connection Setup

```python
from r2r import R2RClient
import asyncio

class R2RMemorySystem:
    """
    Centralized memory system using R2R
    """

    def __init__(self, base_url: str = "http://localhost:7272"):
        self.client = R2RClient(base_url)
        self.collections = {}

    async def initialize(self):
        """
        Set up collections for different data types
        """
        collection_configs = [
            {
                "name": "codebase",
                "description": "Source code and documentation",
                "chunking_strategy": "recursive",
                "chunk_size": 1024,
                "overlap": 100
            },
            {
                "name": "tasks",
                "description": "Linear tasks and requirements",
                "chunking_strategy": "semantic",
                "chunk_size": 512
            },
            {
                "name": "patterns",
                "description": "Learned solution patterns",
                "chunking_strategy": "whole_document"
            },
            {
                "name": "decisions",
                "description": "Agent decisions and rationale",
                "chunking_strategy": "semantic",
                "chunk_size": 768
            }
        ]

        for config in collection_configs:
            collection = await self.client.create_collection(
                name=config["name"],
                description=config["description"]
            )
            self.collections[config["name"]] = collection

        # Enable GraphRAG for all collections
        await self.client.graphs.enable({
            "extraction_model": "gpt-4-turbo",
            "embedding_model": "text-embedding-3-large"
        })
```

### 1.2 Document Ingestion Pattern

```python
class CodebaseIngestion:
    """
    Ingest codebase into R2R with rich metadata
    """

    async def ingest_file(self, file_path: str, content: str):
        """
        Ingest a single file with AST analysis
        """
        # Parse code to extract metadata
        metadata = await self.analyze_code(file_path, content)

        # Ingest with metadata
        result = await self.r2r.ingest_documents([{
            "id": file_path,
            "text": content,
            "metadata": {
                "file_path": file_path,
                "language": metadata.language,
                "functions": metadata.functions,
                "classes": metadata.classes,
                "imports": metadata.imports,
                "complexity": metadata.complexity,
                "last_modified": metadata.timestamp,
                "author": metadata.author
            }
        }], collection="codebase")

        # Build knowledge graph relationships
        await self.create_relationships(file_path, metadata)

    async def create_relationships(self, file_path: str, metadata):
        """
        Create graph relationships for dependencies
        """
        for imported_file in metadata.imports:
            await self.r2r.graphs.create_relationship(
                source_id=file_path,
                target_id=imported_file,
                relationship_type="IMPORTS",
                properties={"type": "dependency"}
            )

        for function in metadata.functions:
            for called_func in function.calls:
                await self.r2r.graphs.create_relationship(
                    source_id=f"{file_path}:{function.name}",
                    target_id=called_func.full_name,
                    relationship_type="CALLS",
                    properties={"line": called_func.line}
                )
```

### 1.3 Hybrid Search Pattern

```python
class IntelligentSearch:
    """
    Multi-modal search combining vector, keyword, and graph
    """

    async def search_with_context(
        self,
        query: str,
        agent_context: dict = None,
        search_mode: str = "hybrid"
    ):
        """
        Context-aware search across collections
        """
        search_settings = {
            "use_vector_search": True,
            "use_kg_search": True,
            "filters": self.build_filters(agent_context),
            "limit": 10
        }

        # Hybrid search
        results = await self.r2r.search(
            query=query,
            search_settings=search_settings
        )

        # Re-rank based on context
        if agent_context:
            results = self.rerank_by_context(results, agent_context)

        return results

    def build_filters(self, agent_context):
        """
        Build dynamic filters based on agent context
        """
        filters = {}

        if agent_context:
            if "file_area" in agent_context:
                filters["file_path"] = {
                    "starts_with": agent_context["file_area"]
                }

            if "task_type" in agent_context:
                filters["task_type"] = agent_context["task_type"]

            if "recency_days" in agent_context:
                filters["last_modified"] = {
                    "gte": datetime.now() - timedelta(
                        days=agent_context["recency_days"]
                    )
                }

        return filters
```

### 1.4 GraphRAG Traversal Pattern

```python
class GraphTraversal:
    """
    Complex queries using knowledge graph
    """

    async def find_impact_radius(self, file_path: str, depth: int = 3):
        """
        Find all files affected by changes to a file
        """
        cypher_query = f"""
        MATCH (source:File {{path: $file_path}})
        -[:IMPORTS|CALLS*1..{depth}]->(affected:File)
        RETURN DISTINCT affected.path as file,
               length(path) as distance
        ORDER BY distance
        """

        results = await self.r2r.graphs.query(
            cypher_query,
            params={"file_path": file_path}
        )

        return results

    async def find_similar_implementations(self, task_description: str):
        """
        Find similar past implementations using graph + embeddings
        """
        # First, semantic search for similar tasks
        similar_tasks = await self.r2r.search(
            query=task_description,
            collection="tasks",
            limit=5
        )

        # Then, graph traversal to find implementations
        implementations = []
        for task in similar_tasks:
            cypher_query = """
            MATCH (task:Task {id: $task_id})
            -[:IMPLEMENTED_BY]->(code:Code)
            -[:HAS_TEST]->(test:Test {status: 'passing'})
            RETURN code, test
            """

            impl = await self.r2r.graphs.query(
                cypher_query,
                params={"task_id": task.id}
            )
            implementations.extend(impl)

        return implementations
```

### 1.5 Agentic RAG Pattern

```python
class AgenticRAG:
    """
    Use R2R's agent mode for multi-step reasoning
    """

    async def deep_research(self, query: str, max_iterations: int = 5):
        """
        Multi-step research using R2R agent
        """
        conversation = await self.r2r.conversations.create()

        response = await self.r2r.agent(
            message=query,
            conversation_id=conversation.id,
            rag_settings={
                "use_vector_search": True,
                "use_kg_search": True,
                "search_depth": "deep"
            },
            agent_settings={
                "max_iterations": max_iterations,
                "tool_selection": "auto",
                "thinking_budget": 2000
            },
            streaming=True
        )

        # Stream results
        thinking_events = []
        search_events = []
        final_answer = None

        async for event in response:
            if event.type == "thinking":
                thinking_events.append(event.content)
            elif event.type == "search":
                search_events.append(event.results)
            elif event.type == "final_answer":
                final_answer = event.content

        return {
            "answer": final_answer,
            "thinking": thinking_events,
            "sources": search_events
        }
```

---

## 2. Codegen Integration Patterns

### 2.1 Sandbox Management

```python
from codegen import CodegenClient

class CodegenSandboxManager:
    """
    Manage Codegen sandboxes for safe code execution
    """

    def __init__(self, api_key: str):
        self.client = CodegenClient(api_key=api_key)
        self.active_sandboxes = {}

    async def create_project_sandbox(
        self,
        project_id: str,
        git_repo: str,
        branch: str = "main"
    ):
        """
        Create sandbox for a specific project
        """
        sandbox = await self.client.sandboxes.create({
            "template": "node18-python311",
            "git": {
                "repo": git_repo,
                "branch": branch
            },
            "env": {
                "NODE_ENV": "development",
                "PYTHON_ENV": "development"
            },
            "preinstall": [
                "npm install",
                "pip install -r requirements.txt"
            ],
            "persistent": True,
            "ttl": 3600  # 1 hour
        })

        self.active_sandboxes[project_id] = sandbox
        return sandbox

    async def execute_code(
        self,
        sandbox_id: str,
        code_changes: dict,
        test_command: str
    ):
        """
        Execute code changes and run tests
        """
        sandbox = self.active_sandboxes[sandbox_id]

        try:
            # Apply code changes
            for file_path, content in code_changes.items():
                await sandbox.write_file(file_path, content)

            # Run tests
            test_result = await sandbox.exec(
                command=test_command,
                timeout=300  # 5 minutes
            )

            # Run linters
            lint_result = await sandbox.exec(
                command="npm run lint",
                timeout=60
            )

            return {
                "success": test_result.exit_code == 0,
                "tests": {
                    "stdout": test_result.stdout,
                    "stderr": test_result.stderr,
                    "exit_code": test_result.exit_code
                },
                "linting": {
                    "stdout": lint_result.stdout,
                    "exit_code": lint_result.exit_code
                }
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
```

### 2.2 MCP Server Integration

```python
class MCPIntegration:
    """
    Use Codegen's MCP servers for tool access
    """

    async def setup_mcp_tools(self, sandbox_id: str):
        """
        Configure MCP servers for agent tools
        """
        mcp_config = {
            "servers": {
                "github": {
                    "type": "github-mcp-server",
                    "config": {
                        "token": os.getenv("GITHUB_TOKEN")
                    }
                },
                "filesystem": {
                    "type": "filesystem-mcp-server",
                    "config": {
                        "allowed_paths": ["/workspace"]
                    }
                },
                "linear": {
                    "type": "linear-mcp-server",
                    "config": {
                        "api_key": os.getenv("LINEAR_API_KEY")
                    }
                }
            }
        }

        await self.client.sandboxes.configure_mcp(
            sandbox_id,
            mcp_config
        )

    async def execute_with_tools(
        self,
        sandbox_id: str,
        agent_prompt: str
    ):
        """
        Execute agent with MCP tool access
        """
        result = await self.client.agents.run(
            sandbox_id=sandbox_id,
            prompt=agent_prompt,
            tools=["github", "filesystem", "linear"],
            model="claude-sonnet-4",
            max_tokens=8000
        )

        return result
```

### 2.3 Agent Deployment Pattern

```python
class CodegenAgentDeployment:
    """
    Deploy persistent agents on Codegen platform
    """

    async def deploy_developer_agent(
        self,
        project_config: dict
    ):
        """
        Deploy a long-running developer agent
        """
        agent = await self.client.agents.deploy({
            "name": f"developer-agent-{project_config['name']}",
            "type": "persistent",
            "sandbox": {
                "template": project_config["template"],
                "git": project_config["git"],
                "mcp_servers": ["github", "filesystem", "linear"]
            },
            "triggers": [
                {
                    "type": "webhook",
                    "source": "linear",
                    "events": ["issue.created", "issue.updated"]
                },
                {
                    "type": "webhook",
                    "source": "github",
                    "events": ["pull_request.review_requested"]
                }
            ],
            "behavior": {
                "auto_create_prs": True,
                "auto_run_tests": True,
                "auto_request_reviews": True
            },
            "model": "claude-sonnet-4",
            "system_prompt": self.load_system_prompt("developer")
        })

        return agent
```

---

## 3. Linear Integration Patterns

### 3.1 GraphQL Client Setup

```python
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

class LinearClient:
    """
    Async Linear API client
    """

    def __init__(self, api_key: str):
        transport = AIOHTTPTransport(
            url="https://api.linear.app/graphql",
            headers={"Authorization": api_key}
        )
        self.client = Client(
            transport=transport,
            fetch_schema_from_transport=True
        )

    async def get_next_task(self, team_id: str = None):
        """
        Get highest priority unassigned task
        """
        query = gql("""
            query GetNextTask($teamId: String) {
                issues(
                    filter: {
                        assignee: { null: true }
                        state: { name: { eq: "Backlog" } }
                        team: { id: { eq: $teamId } }
                    }
                    orderBy: priority
                    first: 1
                ) {
                    nodes {
                        id
                        title
                        description
                        priority
                        labels {
                            nodes {
                                name
                            }
                        }
                        project {
                            name
                        }
                    }
                }
            }
        """)

        result = await self.client.execute(
            query,
            variable_values={"teamId": team_id}
        )

        issues = result.get("issues", {}).get("nodes", [])
        return issues[0] if issues else None

    async def assign_task_to_agent(
        self,
        issue_id: str,
        agent_name: str
    ):
        """
        Assign task to an AI agent (as a virtual user)
        """
        mutation = gql("""
            mutation AssignIssue($issueId: String!, $comment: String!) {
                issueUpdate(
                    id: $issueId
                    input: {
                        labelIds: ["ai-assigned"]
                    }
                ) {
                    success
                    issue {
                        id
                    }
                }
                commentCreate(
                    input: {
                        issueId: $issueId
                        body: $comment
                    }
                ) {
                    success
                }
            }
        """)

        result = await self.client.execute(
            mutation,
            variable_values={
                "issueId": issue_id,
                "comment": f"🤖 Assigned to {agent_name} for implementation"
            }
        )

        return result
```

### 3.2 Webhook Handler Pattern

```python
from fastapi import FastAPI, Request
import hmac
import hashlib

app = FastAPI()

class LinearWebhookHandler:
    """
    Handle Linear webhooks securely
    """

    def __init__(self, webhook_secret: str, event_bus):
        self.webhook_secret = webhook_secret
        self.event_bus = event_bus

    def verify_signature(self, payload: bytes, signature: str) -> bool:
        """
        Verify webhook signature
        """
        expected_signature = hmac.new(
            self.webhook_secret.encode(),
            payload,
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(signature, expected_signature)

    @app.post("/webhooks/linear")
    async def handle_webhook(self, request: Request):
        """
        Process Linear webhook events
        """
        # Verify signature
        signature = request.headers.get("Linear-Signature")
        payload = await request.body()

        if not self.verify_signature(payload, signature):
            return {"error": "Invalid signature"}, 403

        # Parse event
        event = await request.json()
        event_type = event.get("type")
        data = event.get("data")

        # Route to appropriate handler
        if event_type == "Issue":
            await self.handle_issue_event(event.get("action"), data)
        elif event_type == "Comment":
            await self.handle_comment_event(event.get("action"), data)

        return {"status": "ok"}

    async def handle_issue_event(self, action: str, data: dict):
        """
        Handle issue events
        """
        if action == "create":
            # New task created - notify agents
            await self.event_bus.emit({
                "type": "task_created",
                "task_id": data["id"],
                "title": data["title"],
                "priority": data["priority"],
                "labels": [label["name"] for label in data.get("labels", [])]
            })

        elif action == "update":
            # Task updated - check if agents need to react
            if data.get("state", {}).get("name") == "In Progress":
                await self.event_bus.emit({
                    "type": "task_started",
                    "task_id": data["id"]
                })
```

### 3.3 Bidirectional Sync Pattern

```python
class LinearBidirectionalSync:
    """
    Keep Linear in sync with agent activity
    """

    async def update_task_progress(
        self,
        task_id: str,
        progress_update: dict
    ):
        """
        Update Linear task with agent progress
        """
        # Update task description with progress
        comment_body = self.format_progress_comment(progress_update)

        await self.linear.create_comment(task_id, comment_body)

        # Update task state if needed
        if progress_update["stage"] == "testing":
            await self.linear.update_issue_state(
                task_id,
                "In Review"
            )
        elif progress_update["stage"] == "completed":
            await self.linear.update_issue_state(
                task_id,
                "Done"
            )

    def format_progress_comment(self, progress: dict) -> str:
        """
        Format agent progress as Markdown comment
        """
        return f"""
## 🤖 Agent Progress Update

**Stage**: {progress['stage']}
**Progress**: {progress['percentage']}%
**Time Elapsed**: {progress['time_elapsed']}

### Completed Steps
{self.format_steps(progress['completed_steps'])}

### Current Step
{progress['current_step']}

### Next Steps
{self.format_steps(progress['next_steps'])}

---
*Updated by {progress['agent_name']} at {progress['timestamp']}*
"""

    async def sync_pr_to_linear(
        self,
        task_id: str,
        pr_url: str,
        pr_status: dict
    ):
        """
        Link GitHub PR to Linear issue
        """
        await self.linear.create_comment(
            task_id,
            f"""
## 🔗 Pull Request Created

**PR**: [{pr_status['title']}]({pr_url})
**Status**: {pr_status['status']}
**Tests**: {'✅ Passing' if pr_status['tests_passing'] else '❌ Failing'}
**Review**: {pr_status['review_status']}

The agent has created a pull request for this issue.
"""
        )

        # Add PR link as attachment
        await self.linear.add_attachment(
            task_id,
            url=pr_url,
            title=pr_status['title']
        )
```

---

## 4. Cross-Platform Event Bus

### 4.1 Redis-Backed Event Bus

```python
import redis.asyncio as redis
import json

class EventBus:
    """
    Distributed event bus for agent coordination
    """

    def __init__(self, redis_url: str):
        self.redis = redis.from_url(redis_url)
        self.pubsub = self.redis.pubsub()

    async def emit(self, event: dict):
        """
        Emit event to all subscribers
        """
        channel = f"events:{event['type']}"
        payload = json.dumps({
            **event,
            "timestamp": datetime.now().isoformat(),
            "id": str(uuid.uuid4())
        })

        await self.redis.publish(channel, payload)

        # Also store in event log (R2R)
        await self.r2r.ingest_documents([{
            "text": json.dumps(event, indent=2),
            "metadata": {
                "type": "event",
                "event_type": event["type"],
                "timestamp": event["timestamp"]
            }
        }], collection="events")

    async def subscribe(
        self,
        event_types: list[str],
        handler: callable
    ):
        """
        Subscribe to specific event types
        """
        channels = [f"events:{event_type}" for event_type in event_types]
        await self.pubsub.subscribe(*channels)

        # Listen for events
        async for message in self.pubsub.listen():
            if message["type"] == "message":
                event = json.loads(message["data"])
                await handler(event)
```

### 4.2 Event-Driven Agent Coordination

```python
class EventDrivenAgent:
    """
    Base class for event-driven agents
    """

    def __init__(self, agent_id: str, event_bus: EventBus):
        self.agent_id = agent_id
        self.event_bus = event_bus
        self.handlers = {}

    async def start(self):
        """
        Start listening for events
        """
        # Subscribe to relevant events
        await self.event_bus.subscribe(
            self.get_relevant_event_types(),
            self.handle_event
        )

    def on_event(self, event_type: str):
        """
        Decorator for event handlers
        """
        def decorator(func):
            self.handlers[event_type] = func
            return func
        return decorator

    async def handle_event(self, event: dict):
        """
        Route event to appropriate handler
        """
        event_type = event["type"]
        handler = self.handlers.get(event_type)

        if handler:
            try:
                await handler(event)
            except Exception as e:
                logging.error(
                    f"Agent {self.agent_id} failed to handle "
                    f"{event_type}: {e}"
                )

                # Emit failure event
                await self.event_bus.emit({
                    "type": "agent_error",
                    "agent_id": self.agent_id,
                    "event": event,
                    "error": str(e)
                })


# Example usage
class DeveloperAgent(EventDrivenAgent):
    @on_event("task_created")
    async def handle_new_task(self, event):
        task_id = event["task_id"]

        # Check if I should handle this
        if await self.should_handle_task(task_id):
            # Claim the task
            claimed = await self.claim_task(task_id)

            if claimed:
                # Implement the task
                result = await self.implement_task(task_id)

                # Emit completion event
                await self.event_bus.emit({
                    "type": "task_implemented",
                    "task_id": task_id,
                    "agent_id": self.agent_id,
                    "pr_url": result.pr_url
                })
```

---

## 5. Complete Integration Example

### 5.1 End-to-End Workflow

```python
class AutonomousDevelopmentPlatform:
    """
    Complete integration of all systems
    """

    def __init__(self):
        # Initialize all clients
        self.r2r = R2RMemorySystem()
        self.linear = LinearClient(os.getenv("LINEAR_API_KEY"))
        self.github = GitHubClient(os.getenv("GITHUB_TOKEN"))
        self.codegen = CodegenSandboxManager(os.getenv("CODEGEN_API_KEY"))
        self.event_bus = EventBus(os.getenv("REDIS_URL"))

        # Initialize agents
        self.agents = {
            "architect": ArchitectAgent(self.r2r, self.event_bus),
            "developer": DeveloperAgent(
                self.r2r,
                self.codegen,
                self.github,
                self.event_bus
            ),
            "tester": TesterAgent(self.codegen, self.event_bus),
            "reviewer": ReviewerAgent(self.r2r, self.event_bus),
            "deployer": DeployerAgent(self.event_bus)
        }

    async def start(self):
        """
        Start the autonomous platform
        """
        # Initialize R2R collections
        await self.r2r.initialize()

        # Setup Linear webhooks
        await self.setup_linear_webhooks()

        # Start all agents
        await asyncio.gather(*[
            agent.start() for agent in self.agents.values()
        ])

        # Start monitoring loop
        await self.monitoring_loop()

    async def setup_linear_webhooks(self):
        """
        Configure Linear to send events to platform
        """
        webhook_url = f"{os.getenv('PLATFORM_URL')}/webhooks/linear"

        await self.linear.create_webhook(
            url=webhook_url,
            events=["Issue.create", "Issue.update", "Comment.create"]
        )

    async def monitoring_loop(self):
        """
        Monitor platform health
        """
        while True:
            metrics = await self.collect_metrics()
            await self.r2r.ingest_documents([{
                "text": json.dumps(metrics),
                "metadata": {
                    "type": "metrics",
                    "timestamp": datetime.now().isoformat()
                }
            }], collection="metrics")

            await asyncio.sleep(60)  # Every minute
```

---

## 6. Best Practices Summary

### R2R Integration
✅ Use separate collections for different data types
✅ Enable GraphRAG for relationship-based queries
✅ Implement hybrid search (vector + keyword + graph)
✅ Add rich metadata to all documents
✅ Use graph relationships to model dependencies

### Codegen Integration
✅ Reuse sandboxes per agent (don't create on every task)
✅ Configure MCP servers for tool access
✅ Use persistent sandboxes for long-running agents
✅ Always run tests in isolated environments
✅ Cache dependencies to speed up sandbox creation

### Linear Integration
✅ Use webhooks for real-time task updates
✅ Verify webhook signatures for security
✅ Keep Linear in sync with agent progress
✅ Use GraphQL for efficient queries
✅ Link PRs back to Linear issues

### Event Bus
✅ Use Redis Pub/Sub for low-latency events
✅ Store events in R2R for historical queries
✅ Include rich metadata in events
✅ Handle failures gracefully
✅ Implement idempotent event handlers

---

## 7. Deployment Architecture

```
                    ┌──────────────┐
                    │   Load       │
                    │   Balancer   │
                    └──────┬───────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
     ┌────▼────┐      ┌────▼────┐     ┌────▼────┐
     │ Agent   │      │ Agent   │     │ Agent   │
     │ Pod 1   │      │ Pod 2   │     │ Pod 3   │
     └────┬────┘      └────┬────┘     └────┬────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
     ┌────▼────┐      ┌────▼────┐     ┌────▼────┐
     │   R2R   │      │  Redis  │     │ Codegen │
     │(GraphRAG)│      │(Events) │     │(Sandbox)│
     └─────────┘      └─────────┘     └─────────┘
```

This architecture enables:
- Horizontal scaling of agents
- Shared memory through R2R
- Fast event propagation via Redis
- Isolated code execution in Codegen sandboxes
