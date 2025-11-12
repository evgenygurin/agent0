# Webhooks - Mem0
Source: https://docs.mem0.ai/platform/features/webhooks
Downloaded: 2025-11-12 21:20:19
================================================================================


## ​Overview
[​](https://docs.mem0.ai/platform/features/webhooks#overview)
## ​Managing Webhooks
[​](https://docs.mem0.ai/platform/features/webhooks#managing-webhooks)
### ​Create Webhook
[​](https://docs.mem0.ai/platform/features/webhooks#create-webhook)
```
import os
from mem0 import MemoryClient

os.environ["MEM0_API_KEY"] = "your-api-key"

client = MemoryClient()

# Create webhook in a specific project
webhook = client.create_webhook(
    url="https://your-app.com/webhook",
    name="Memory Logger",
    project_id="proj_123",
    event_types=["memory_add"]
)
print(webhook)

```

### ​Get Webhooks
[​](https://docs.mem0.ai/platform/features/webhooks#get-webhooks)
```
# Get webhooks for a specific project
webhooks = client.get_webhooks(project_id="proj_123")
print(webhooks)

```

### ​Update Webhook
[​](https://docs.mem0.ai/platform/features/webhooks#update-webhook)`webhook_id`
```
# Update webhook for a specific project
updated_webhook = client.update_webhook(
    name="Updated Logger",
    url="https://your-app.com/new-webhook",
    event_types=["memory_update", "memory_add"],
    webhook_id="wh_123"
)
print(updated_webhook)

```

### ​Delete Webhook
[​](https://docs.mem0.ai/platform/features/webhooks#delete-webhook)`webhook_id`
```
# Delete webhook from a specific project
response = client.delete_webhook(webhook_id="wh_123")
print(response)

```

## ​Event Types
[​](https://docs.mem0.ai/platform/features/webhooks#event-types)- memory_add: Triggered when a memory is added.
`memory_add`- memory_update: Triggered when an existing memory is updated.
`memory_update`- memory_delete: Triggered when a memory is deleted.
`memory_delete`
## ​Webhook Payload
[​](https://docs.mem0.ai/platform/features/webhooks#webhook-payload)
```
{
    "event_details": {
        "id": "a1b2c3d4-e5f6-4g7h-8i9j-k0l1m2n3o4p5",
            "data": {
            "memory": "Name is Alex"
            },
        "event": "ADD"
    }
}

```

## ​Best Practices
[​](https://docs.mem0.ai/platform/features/webhooks#best-practices)- Implement Retry Logic: Ensure your webhook endpoint can handle temporary failures.
- Verify Webhook Source: Implement security measures to verify that webhook requests originate from Mem0.
- Process Events Asynchronously: Process webhook events asynchronously to avoid timeouts and ensure reliable handling.
- Monitor Webhook Health: Regularly review your webhook logs to ensure functionality and promptly address delivery failures.
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
