# OpenAI Compatibility - Mem0
Source: https://docs.mem0.ai/open-source/features/openai_compatibility
Downloaded: 2025-11-12 21:20:19
================================================================================

- Your app already relies on OpenAI chat completions and you want Mem0 to feel familiar.
- You need to reuse existing middleware that expects OpenAI-compatible responses.
- You plan to switch between Mem0 Platform and the self-hosted client without rewriting code.

## ​Feature
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#feature)- Drop-in client:client.chat.completions.create(...)works the same as OpenAI’s method signatures.
`client.chat.completions.create(...)`- Shared parameters:Mem0 acceptsmessages,model, and optional memory-scoping fields (user_id,agent_id,run_id).
`messages``model``user_id``agent_id``run_id`- Memory-aware responses:Each call saves relevant facts so future prompts automatically reflect past conversations.
- OSS parity:Use the same API surface whether you call the hosted proxy or the OSS configuration.
`user_id`
## ​Configure it
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#configure-it)
### ​Call the managed Mem0 proxy
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#call-the-managed-mem0-proxy)
```
from mem0.proxy.main import Mem0

client = Mem0(api_key="m0-xxx")

messages = [
    {"role": "user", "content": "I love Indian food but I cannot eat pizza since I'm allergic to cheese."}
]

chat_completion = client.chat.completions.create(
    messages=messages,
    model="gpt-4.1-nano-2025-04-14",
    user_id="alice"
)

```

### ​Use the OpenAI-compatible OSS client
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#use-the-openai-compatible-oss-client)
```
from mem0.proxy.main import Mem0

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

client = Mem0(config=config)

chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "What's the capital of France?"}],
    model="gpt-4.1-nano-2025-04-14"
)

```

## ​See it in action
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#see-it-in-action)
### ​Memory-aware restaurant recommendation
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#memory-aware-restaurant-recommendation)
```
from mem0.proxy.main import Mem0

client = Mem0(api_key="m0-xxx")

# Store preferences
client.chat.completions.create(
    messages=[{"role": "user", "content": "I love Indian food but I'm allergic to cheese."}],
    model="gpt-4.1-nano-2025-04-14",
    user_id="alice"
)

# Later conversation reuses the memory
response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Suggest dinner options in San Francisco."}],
    model="gpt-4.1-nano-2025-04-14",
    user_id="alice"
)

print(response.choices[0].message.content)

```

## ​Verify the feature is working
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#verify-the-feature-is-working)- Compare responses from Mem0 vs. OpenAI for identical prompts—both should return the same structure (choices,usage, etc.).
`choices``usage`- Inspect stored memories after each request to confirm the fact extraction captured the right details.
- Test switching between hosted (Mem0(api_key=...)) and OSS configurations to ensure both respect the same request body.
`Mem0(api_key=...)`
## ​Best practices
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#best-practices)- Scope context intentionally:Pass identifiers only when you want conversations to persist; skip them for one-off calls.
- Log memory usage:Inspectresponse.metadata.memories(if enabled) to see which facts the model recalled.
`response.metadata.memories`- Reuse middleware:Point your existing OpenAI client wrappers to the Mem0 proxy URL to avoid code drift.
- Handle fallbacks:Keep a code path for plain OpenAI calls in case Mem0 is unavailable, then resync memory later.

## ​Parameter reference
[​](https://docs.mem0.ai/open-source/features/openai_compatibility#parameter-reference)`user_id``str``agent_id``str``run_id``str``metadata``dict``filters``dict``limit``int`[Connect Vision ModelsReview LLM options that support OpenAI-compatible calls in Mem0.](https://docs.mem0.ai/components/llms/models/openai)
## Connect Vision Models
[Automate OpenAI Tool CallsSee a full workflow that layers Mem0 memories on top of tool-calling agents.](https://docs.mem0.ai/cookbooks/integrations/openai-tool-calls)
## Automate OpenAI Tool Calls
