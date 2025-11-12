# Async Memory - Mem0
Source: https://docs.mem0.ai/open-source/features/async-memory
Downloaded: 2025-11-12 21:20:19
================================================================================

`AsyncMemory``asyncio`- Your agent already runs in an async framework and you need memory calls to await cleanly.
- You want to embed Mem0’s storage locally without sending requests through the synchronous client.
- You plan to mix memory operations with other async APIs (OpenAI, HTTP calls, databases).
`AsyncMemory``async def``asyncio.run()``Memory``AsyncMemory`
## ​Feature anatomy
[​](https://docs.mem0.ai/open-source/features/async-memory#feature-anatomy)- Direct storage access:AsyncMemorytalks to the same backends as the synchronous client but keeps everything in-process for lower latency.
`AsyncMemory`- Method parity:Each memory operation (add,search,get_all,delete, etc.) mirrors the synchronous API, letting you reuse payload shapes.
`add``search``get_all``delete`- Concurrent execution:Non-blocking I/O lets you schedule multiple memory tasks withasyncio.gather.
`asyncio.gather`- Scoped organization:Continue usinguser_id,agent_id, andrun_idto separate memories across sessions and agents.
`user_id``agent_id``run_id`
Async method parity
`await memory.add(...)``Memory.add``await memory.search(...)``results``await memory.get_all(...)``user_id``agent_id``run_id``await memory.get(memory_id=...)``ValueError``await memory.update(memory_id=..., data=...)``await memory.delete(memory_id=...)``await memory.delete_all(...)``await memory.history(memory_id=...)`
## ​Configure it
[​](https://docs.mem0.ai/open-source/features/async-memory#configure-it)
### ​Initialize the client
[​](https://docs.mem0.ai/open-source/features/async-memory#initialize-the-client)
```
import asyncio
from mem0 import AsyncMemory

# Default configuration
memory = AsyncMemory()

# Custom configuration
from mem0.configs.base import MemoryConfig
custom_config = MemoryConfig(
    # Your custom configuration here
)
memory = AsyncMemory(config=custom_config)

```
`await memory.search(...)`
### ​Manage lifecycle and concurrency
[​](https://docs.mem0.ai/open-source/features/async-memory#manage-lifecycle-and-concurrency)
```
import asyncio
from contextlib import asynccontextmanager
from mem0 import AsyncMemory

@asynccontextmanager
async def get_memory():
    memory = AsyncMemory()
    try:
        yield memory
    finally:
        # Clean up resources if needed
        pass

async def safe_memory_usage():
    async with get_memory() as memory:
        return await memory.search("test query", user_id="alice")

```

```
async def batch_operations():
    memory = AsyncMemory()

    tasks = [
        memory.add(
            messages=[{"role": "user", "content": f"Message {i}"}],
            user_id=f"user_{i}"
        )
        for i in range(5)
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
        else:
            print(f"Task {i} completed successfully")

```
`results`
### ​Add resilience with retries
[​](https://docs.mem0.ai/open-source/features/async-memory#add-resilience-with-retries)
```
import asyncio
from mem0 import AsyncMemory

async def with_timeout_and_retry(operation, max_retries=3, timeout=10.0):
    for attempt in range(max_retries):
        try:
            return await asyncio.wait_for(operation(), timeout=timeout)
        except asyncio.TimeoutError:
            print(f"Timeout on attempt {attempt + 1}")
        except Exception as exc:
            print(f"Error on attempt {attempt + 1}: {exc}")

        if attempt < max_retries - 1:
            await asyncio.sleep(2 ** attempt)

    raise Exception(f"Operation failed after {max_retries} attempts")

async def robust_memory_search():
    memory = AsyncMemory()

    async def search_operation():
        return await memory.search("test query", user_id="alice")

    return await with_timeout_and_retry(search_operation)

```

## ​See it in action
[​](https://docs.mem0.ai/open-source/features/async-memory#see-it-in-action)
### ​Core operations
[​](https://docs.mem0.ai/open-source/features/async-memory#core-operations)
```
# Create memories
result = await memory.add(
    messages=[
        {"role": "user", "content": "I'm travelling to SF"},
        {"role": "assistant", "content": "That's great to hear!"}
    ],
    user_id="alice"
)

# Search memories
results = await memory.search(
    query="Where am I travelling?",
    user_id="alice"
)

# List memories
all_memories = await memory.get_all(user_id="alice")

# Get a specific memory
specific_memory = await memory.get(memory_id="memory-id-here")

# Update a memory
updated_memory = await memory.update(
    memory_id="memory-id-here",
    data="I'm travelling to Seattle"
)

# Delete a memory
await memory.delete(memory_id="memory-id-here")

# Delete scoped memories
await memory.delete_all(user_id="alice")

```
`results``delete_all``user_id``agent_id``run_id`
### ​Scoped organization
[​](https://docs.mem0.ai/open-source/features/async-memory#scoped-organization)
```
await memory.add(
    messages=[{"role": "user", "content": "I prefer vegetarian food"}],
    user_id="alice",
    agent_id="diet-assistant",
    run_id="consultation-001"
)

all_user_memories = await memory.get_all(user_id="alice")
agent_memories = await memory.get_all(user_id="alice", agent_id="diet-assistant")
session_memories = await memory.get_all(user_id="alice", run_id="consultation-001")
specific_memories = await memory.get_all(
    user_id="alice",
    agent_id="diet-assistant",
    run_id="consultation-001"
)

history = await memory.history(memory_id="memory-id-here")

```
`history`
### ​Blend with other async APIs
[​](https://docs.mem0.ai/open-source/features/async-memory#blend-with-other-async-apis)
```
import asyncio
from openai import AsyncOpenAI
from mem0 import AsyncMemory

async_openai_client = AsyncOpenAI()
async_memory = AsyncMemory()

async def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    search_result = await async_memory.search(query=message, user_id=user_id, limit=3)
    relevant_memories = search_result["results"]
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories)

    system_prompt = (
        "You are a helpful AI. Answer the question based on query and memories.\n"
        f"User Memories:\n{memories_str}"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message},
    ]

    response = await async_openai_client.chat.completions.create(
        model="gpt-4.1-nano-2025-04-14",
        messages=messages
    )

    assistant_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_response})
    await async_memory.add(messages, user_id=user_id)

    return assistant_response

```
`add`
### ​Handle errors gracefully
[​](https://docs.mem0.ai/open-source/features/async-memory#handle-errors-gracefully)
```
from mem0 import AsyncMemory
from mem0.configs.base import MemoryConfig

async def handle_initialization_errors():
    try:
        config = MemoryConfig(
            vector_store={"provider": "chroma", "config": {"path": "./chroma_db"}},
            llm={"provider": "openai", "config": {"model": "gpt-4.1-nano-2025-04-14"}}
        )
        AsyncMemory(config=config)
        print("AsyncMemory initialized successfully")
    except ValueError as err:
        print(f"Configuration error: {err}")
    except ConnectionError as err:
        print(f"Connection error: {err}")

async def handle_memory_operation_errors():
    memory = AsyncMemory()
    try:
        await memory.get(memory_id="non-existent-id")
    except ValueError as err:
        print(f"Invalid memory ID: {err}")

    try:
        await memory.search(query="", user_id="alice")
    except ValueError as err:
        print(f"Invalid search query: {err}")

```
`ValueError`
### ​Serve through FastAPI
[​](https://docs.mem0.ai/open-source/features/async-memory#serve-through-fastapi)
```
from fastapi import FastAPI, HTTPException
from mem0 import AsyncMemory

app = FastAPI()
memory = AsyncMemory()

@app.post("/memories/")
async def add_memory(messages: list, user_id: str):
    try:
        result = await memory.add(messages=messages, user_id=user_id)
        return {"status": "success", "data": result}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@app.get("/memories/search")
async def search_memories(query: str, user_id: str, limit: int = 10):
    try:
        result = await memory.search(query=query, user_id=user_id, limit=limit)
        return {"status": "success", "data": result}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

```
`AsyncMemory`
### ​Instrument logging
[​](https://docs.mem0.ai/open-source/features/async-memory#instrument-logging)
```
import logging
import time
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_async_operation(operation_name):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            logger.info(f"Starting {operation_name}")
            try:
                result = await func(*args, **kwargs)
                duration = time.time() - start_time
                logger.info(f"{operation_name} completed in {duration:.2f}s")
                return result
            except Exception as exc:
                duration = time.time() - start_time
                logger.error(f"{operation_name} failed after {duration:.2f}s: {exc}")
                raise
        return wrapper
    return decorator

@log_async_operation("Memory Add")
async def logged_memory_add(memory, messages, user_id):
    return await memory.add(messages=messages, user_id=user_id)

```

## ​Verify the feature is working
[​](https://docs.mem0.ai/open-source/features/async-memory#verify-the-feature-is-working)- Run a quick add/search cycle and confirm the returned memory content matches your input.
- Inspect application logs to ensure async tasks complete without blocking the event loop.
- In FastAPI or other frameworks, hit health endpoints to verify the shared client handles concurrent requests.
- Monitor retry counters—unexpected spikes indicate configuration or connectivity issues.

## ​Best practices
[​](https://docs.mem0.ai/open-source/features/async-memory#best-practices)- Keep operations awaited:Forgettingawaitis the fastest way to miss writes—lint for it or add helper wrappers.
`await`- Scope deletions carefully:Always supplyuser_id,agent_id, orrun_idto avoid purging too much data.
`user_id``agent_id``run_id`- Batch writes thoughtfully:Useasyncio.gatherfor throughput but cap concurrency based on backend capacity.
`asyncio.gather`- Log errors with context:Capture user and agent scopes to triage failures quickly.
- Reuse clients:InstantiateAsyncMemoryonce per worker to avoid repeated backend handshakes.
`AsyncMemory`
## ​Troubleshooting
[​](https://docs.mem0.ai/open-source/features/async-memory#troubleshooting)`MemoryConfig`[Master Memory OperationsReview how add, search, update, and delete behave across synchronous and async clients.](https://docs.mem0.ai/core-concepts/memory-operations/add)
## Master Memory Operations
[Connect Async AgentsFollow a full workflow that mixes AsyncMemory with OpenAI tool-call automation.](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls)
## Connect Async Agents
