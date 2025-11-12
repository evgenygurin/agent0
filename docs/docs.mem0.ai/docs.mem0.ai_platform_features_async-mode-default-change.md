# Async Mode Default Change - Mem0
Source: https://docs.mem0.ai/platform/features/async-mode-default-change
Downloaded: 2025-11-12 21:20:18
================================================================================

`async_mode``true`
## ​Overview
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#overview)
## ​What’s Changing
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#what%E2%80%99s-changing)`async_mode``true``false`
## ​Behavior Comparison
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#behavior-comparison)
### ​Old Default Behavior (async_mode = false)
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#old-default-behavior-async-mode-%3D-false)`async_mode``false`
```
{
  "results": [
    {
      "id": "de0ee948-af6a-436c-835c-efb6705207de",
      "event": "ADD",
      "memory": "User Order #1234 was for a 'Nova 2000'",
      "structured_attributes": {
        "day": 13,
        "hour": 16,
        "year": 2025,
        "month": 10,
        "minute": 59,
        "quarter": 4,
        "is_weekend": false,
        "day_of_week": "monday",
        "day_of_year": 286,
        "week_of_year": 42
      }
    }
  ]
}

```

### ​New Default Behavior (async_mode = true)
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#new-default-behavior-async-mode-%3D-true)`async_mode``true`
```
{
  "results": [
    {
      "message": "Memory processing has been queued for background execution",
      "status": "PENDING",
      "event_id": "d7b5282a-0031-4cc2-98ba-5a02d8531e17"
    }
  ]
}

```

## ​Migration Guide
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#migration-guide)
### ​If You Need Synchronous Processing
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#if-you-need-synchronous-processing)`async_mode``false`
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

# Explicitly set async_mode=False to preserve synchronous behavior
messages = [
    {"role": "user", "content": "I ordered a Nova 2000"}
]

result = client.add(
    messages,
    user_id="user-123",
    async_mode=False  # This ensures synchronous processing
)

```

### ​If You Want to Adopt Asynchronous Processing
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#if-you-want-to-adopt-asynchronous-processing)- Removeany explicitasync_mode=Falseparameters from your code
`async_mode=False`- Use webhooksto receive notifications when memory processing completes
[Webhooks](https://docs.mem0.ai/platform/features/webhooks)
## ​Benefits of Asynchronous Processing
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#benefits-of-asynchronous-processing)- Faster API Response Times: Your application doesn’t wait for memory processing
- Better Scalability: Handle more memory additions concurrently
- Improved User Experience: Reduced latency in your application
- Resource Efficiency: Background processing optimizes server resources

## ​Important Notes
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#important-notes)- The default behavior is nowasync_mode=truefor asynchronous processing
`async_mode=true`- Explicitly setasync_mode=falseif you need synchronous behavior
`async_mode=false`- Use webhooks to receive notifications when memories are processed

## ​Monitoring Memory Processing
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#monitoring-memory-processing)[Configure WebhooksLearn how to set up webhooks for memory processing events](https://docs.mem0.ai/platform/features/webhooks)
## Configure Webhooks

```
# Retrieve all memories for a user
memories = client.get_all(user_id="user-123")

```

## ​Need Help?
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#need-help%3F)[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support

## ​Related Documentation
[​](https://docs.mem0.ai/platform/features/async-mode-default-change#related-documentation)[Async ClientLearn about the asynchronous client for Mem0](https://docs.mem0.ai/platform/features/async-client)
## Async Client
[Add Memories APIView the complete API reference for adding memories](https://docs.mem0.ai/api-reference/memory/add-memories)
## Add Memories API
[WebhooksConfigure webhooks for memory processing events](https://docs.mem0.ai/platform/features/webhooks)
## Webhooks
[Memory OperationsUnderstand memory addition operations](https://docs.mem0.ai/core-concepts/memory-operations/add)
## Memory Operations
