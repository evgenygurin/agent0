# vLLM - Mem0
Source: https://docs.mem0.ai/components/llms/models/vllm
Downloaded: 2025-11-12 21:20:19
================================================================================

[vLLM](https://docs.vllm.ai/)
## ​Prerequisites
[​](https://docs.mem0.ai/components/llms/models/vllm#prerequisites)- Install vLLM:CopyAsk AIpipinstallvllm

```
pip install vllm

```
- Start vLLM server:CopyAsk AI# For testing with a small modelvllmservemicrosoft/DialoGPT-medium--port8000# For production with a larger model (requires GPU)vllmserveQwen/Qwen2.5-32B-Instruct--port8000

```
# For testing with a small model
vllm serve microsoft/DialoGPT-medium --port 8000

# For production with a larger model (requires GPU)
vllm serve Qwen/Qwen2.5-32B-Instruct --port 8000

```

## ​Usage
[​](https://docs.mem0.ai/components/llms/models/vllm#usage)
```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key"  # used for embedding model

config = {
    "llm": {
        "provider": "vllm",
        "config": {
            "model": "Qwen/Qwen2.5-32B-Instruct",
            "vllm_base_url": "http://localhost:8000/v1",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)
messages = [
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},
    {"role": "user", "content": "I'm not a big fan of thrillers, but I love sci-fi movies."},
    {"role": "assistant", "content": "Got it! I'll avoid thrillers and suggest sci-fi movies instead."}
]
m.add(messages, user_id="alice", metadata={"category": "movies"})

```

## ​Configuration Parameters
[​](https://docs.mem0.ai/components/llms/models/vllm#configuration-parameters)`model``"Qwen/Qwen2.5-32B-Instruct"``vllm_base_url``"http://localhost:8000/v1"``VLLM_BASE_URL``api_key``"vllm-api-key"``VLLM_API_KEY``temperature``0.1``max_tokens``2000`
## ​Environment Variables
[​](https://docs.mem0.ai/components/llms/models/vllm#environment-variables)
```
export VLLM_BASE_URL="http://localhost:8000/v1"
export VLLM_API_KEY="your-vllm-api-key"
export OPENAI_API_KEY="your-openai-api-key"  # for embeddings

```

## ​Benefits
[​](https://docs.mem0.ai/components/llms/models/vllm#benefits)- High Performance: 2-24x faster inference than standard implementations
- Memory Efficient: Optimized memory usage with PagedAttention
- Local Deployment: Keep your data private and reduce API costs
- Easy Integration: Drop-in replacement for other LLM providers
- Flexible: Works with any model supported by vLLM

## ​Troubleshooting
[​](https://docs.mem0.ai/components/llms/models/vllm#troubleshooting)- Server not responding: Make sure vLLM server is runningCopyAsk AIcurlhttp://localhost:8000/health

```
curl http://localhost:8000/health

```
- 404 errors: Ensure correct base URL formatCopyAsk AI"vllm_base_url":"http://localhost:8000/v1"# Note the /v1

```
"vllm_base_url": "http://localhost:8000/v1"  # Note the /v1

```
- Model not found: Check model name matches server
- Out of memory: Try smaller models or reducemax_model_lenCopyAsk AIvllmserveQwen/Qwen2.5-32B-Instruct--max-model-len4096
`max_model_len`
```
vllm serve Qwen/Qwen2.5-32B-Instruct --max-model-len 4096

```

## ​Config
[​](https://docs.mem0.ai/components/llms/models/vllm#config)`vllm`[Master List of All Params in Config](https://docs.mem0.ai/components/llms/config)