# Tag and Organize Memories - Mem0
Source: https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Setup
[​](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories#setup)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

```
`client.project.update()`
## ​The Problem
[​](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories#the-problem)
```
# Joseph (support agent) stores various customer interactions
client.add(
    "Maria called about her account password reset",
    user_id="maria",
)

client.add(
    "Maria was charged twice for last month's subscription",
    user_id="maria",
)

client.add(
    "Maria wants to upgrade to the premium plan",
    user_id="maria",
)

# Now try to find just billing issues
all_memories = client.get_all(filters={"user_id": "maria"})
print(f"Total memories: {len(all_memories['results'])}")

for memory in all_memories['results']:
    print(f"- {memory['memory']}")


```

```
Total memories: 3
- Maria called about her account password reset
- Maria was charged twice for last month's subscription
- Maria wants to upgrade to the premium plan


```

## ​Custom Categories
[​](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories#custom-categories)
```
custom_categories = [
    {"support_tickets": "Customer issues and resolutions"},
    {"account_info": "Account details and preferences"},
    {"billing": "Payment history and billing questions"},
    {"product_feedback": "Feature requests and feedback"},
]

client.project.update(custom_categories=custom_categories)


```

## ​Tagging Memories
[​](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories#tagging-memories)
```
# Billing issue - automatically tagged as "billing"
client.add(
    "Maria was charged twice for last month's subscription",
    user_id="maria",
    metadata={"priority": "high", "source": "phone_call"}
)

# Account update - automatically tagged as "account_info"
client.add(
    "Maria changed her email to [email protected]",
    user_id="maria",
    metadata={"source": "web_portal"}
)

# Product feedback - automatically tagged as "product_feedback"
client.add(
    "Maria requested a dark mode feature for the dashboard",
    user_id="maria",
    metadata={"source": "chat"}
)


```
[[email protected]](https://docs.mem0.ai/cdn-cgi/l/email-protection)
## ​Retrieving by Category
[​](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories#retrieving-by-category)
```
# Joseph needs to pull all billing issues for audit
billing_issues = client.get_all(
    filters={
        "AND": [
            {"user_id": "maria"},
            {"categories": {"in": ["billing"]}}
        ]
    }
)

print("Billing issues:")
for memory in billing_issues['results']:
    print(f"- {memory['memory']}")


```

```
Billing issues:
- Maria was charged twice for last month's subscription


```

```
# Get both account info and billing
account_and_billing = client.get_all(
    filters={
        "AND": [
            {"user_id": "maria"},
            {"categories": {"in": ["account_info", "billing"]}}
        ]
    }
)

for memory in account_and_billing['results']:
    print(f"[{memory['categories'][0]}] {memory['memory']}")


```

```
[account_info] Maria changed her email to [email protected]
[billing] Maria was charged twice for last month's subscription


```
[[email protected]](https://docs.mem0.ai/cdn-cgi/l/email-protection)
## ​Updating Categories
[​](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories#updating-categories)
```
# Find memories that need re-categorization
needs_update = client.get_all(
    filters={
        "AND": [
            {"user_id": "maria"},
            {"categories": {"in": ["misc"]}}
        ]
    }
)

# Update memory content to trigger re-categorization
for memory in needs_update['results']:
    client.update(
        memory_id=memory['id'],
        data=memory['memory']  # Re-process with current category definitions
    )


```

## ​What You Built
[​](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories#what-you-built)- Project-wide categories- Support tickets, billing, account info, and product feedback auto-classified
- Automatic tagging- Mem0 assigns categories based on content semantics, no manual tagging
- Filtered retrieval- Pull only billing issues or only account updates usingcategories: {in: [...]}
`categories: {in: [...]}`- Re-categorization- Update memory content to trigger re-analysis against new category definitions
- Multi-category support- Memories can belong to multiple categories when appropriate

## ​Summary
[​](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories#summary)`client.project.update()``categories: {in: [...]}`[Control Memory IngestionKeep categories meaningful by filtering noise before it lands in storage.](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion)
## Control Memory Ingestion
[Export Tagged MemoriesUse categories to drive audits, migrations, and compliance reports.](https://docs.mem0.ai/cookbooks/essentials/exporting-memories)
## Export Tagged Memories
