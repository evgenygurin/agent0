# REST API Server - Mem0
Source: https://docs.mem0.ai/open-source/features/rest-api
Downloaded: 2025-11-12 21:20:19
================================================================================

- Your services already talk to REST APIs and you want Mem0 to match that style.
- Teams on languages without the Mem0 SDK still need access to memories.
- You plan to explore or debug endpoints through the built-in OpenAPI page at/docs.
`/docs`
## ​Feature
[​](https://docs.mem0.ai/open-source/features/rest-api#feature)- CRUD endpoints:Create, retrieve, search, update, delete, and reset memories byuser_id,agent_id, orrun_id.
`user_id``agent_id``run_id`- Status health check:Access base routes to confirm the server is online.
- OpenAPI explorer:Visit/docsfor interactive testing and schema reference.
`/docs`
## ​Configure it
[​](https://docs.mem0.ai/open-source/features/rest-api#configure-it)
### ​Run with Docker Compose (development)
[​](https://docs.mem0.ai/open-source/features/rest-api#run-with-docker-compose-development)- Steps
- Createserver/.envwith your keys:
`server/.env`
```
OPENAI_API_KEY=your-openai-api-key

```
- Start the stack:

```
cd server
docker compose up

```
- Reach the API athttp://localhost:8888. Edits to the server or library auto-reload.
`http://localhost:8888`
### ​Run with Docker
[​](https://docs.mem0.ai/open-source/features/rest-api#run-with-docker)- Pull image
- Build locally

```
docker pull mem0/mem0-api-server

```
- Create a.envfile withOPENAI_API_KEY.
`.env``OPENAI_API_KEY`- Run the container:

```
docker run -p 8000:8000 --env-file .env mem0-api-server

```
- Visithttp://localhost:8000.
`http://localhost:8000`
### ​Run directly (no Docker)
[​](https://docs.mem0.ai/open-source/features/rest-api#run-directly-no-docker)
```
pip install -r requirements.txt
uvicorn main:app --reload

```
`systemd`
## ​See it in action
[​](https://docs.mem0.ai/open-source/features/rest-api#see-it-in-action)
### ​Create and search memories via HTTP
[​](https://docs.mem0.ai/open-source/features/rest-api#create-and-search-memories-via-http)
```
curl -X POST http://localhost:8000/memories \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "I love fresh vegetable pizza."}
    ],
    "user_id": "alice"
  }'

```
`ADD`
```
curl "http://localhost:8000/memories/search?user_id=alice&query=vegetable"

```

### ​Explore with OpenAPI docs
[​](https://docs.mem0.ai/open-source/features/rest-api#explore-with-openapi-docs)- Navigate tohttp://localhost:8000/docs.
`http://localhost:8000/docs`- Pick an endpoint (e.g.,POST /memories/search).
`POST /memories/search`- Fill in parameters and clickExecuteto try requests in-browser.
`curl`
## ​Verify the feature is working
[​](https://docs.mem0.ai/open-source/features/rest-api#verify-the-feature-is-working)- Hit the root route and/docsto confirm the server is reachable.
`/docs`- Run a full cycle:POST /memories→GET /memories/{id}→DELETE /memories/{id}.
`POST /memories``GET /memories/{id}``DELETE /memories/{id}`- Watch server logs for import errors or provider misconfigurations during startup.
- Confirm environment variables (API keys, vector store credentials) load correctly when containers restart.

## ​Best practices
[​](https://docs.mem0.ai/open-source/features/rest-api#best-practices)- Add authentication:Protect endpoints with API gateways, proxies, or custom FastAPI middleware.
- Use HTTPS:Terminate TLS at your load balancer or reverse proxy.
- Monitor uptime:Track request rates, latency, and error codes per endpoint.
- Version configs:Keep environment files and Docker Compose definitions in source control.
- Limit exposure:Bind to private networks unless you explicitly need public access.
[Configure OSS ComponentsFine-tune LLMs, vector stores, and graph backends that power the REST server.](https://docs.mem0.ai/open-source/configuration)
## Configure OSS Components
[Automate Agent IntegrationsSee how services call the REST endpoints as part of an automation pipeline.](https://docs.mem0.ai/cookbooks/integrations/agents-sdk-tool)
## Automate Agent Integrations
