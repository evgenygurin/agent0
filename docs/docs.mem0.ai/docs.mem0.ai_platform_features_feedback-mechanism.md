# Feedback Mechanism - Mem0
Source: https://docs.mem0.ai/platform/features/feedback-mechanism
Downloaded: 2025-11-12 21:20:19
================================================================================


## ​How it works
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#how-it-works)
## ​Give Feedback
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#give-feedback)`feedback`
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your_api_key")

client.feedback(memory_id="your-memory-id", feedback="NEGATIVE", feedback_reason="I don't like this memory because it is not relevant.")

```

## ​Feedback Types
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#feedback-types)`feedback`- POSITIVE: The memory is useful.
`POSITIVE`- NEGATIVE: The memory is not useful.
`NEGATIVE`- VERY_NEGATIVE: The memory is not useful at all.
`VERY_NEGATIVE`
## ​Parameters
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#parameters)`feedback``memory_id``feedback``POSITIVE``NEGATIVE``VERY_NEGATIVE``feedback_reason``None``null``feedback``feedback_reason`
## ​Bulk Feedback Operations
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#bulk-feedback-operations)
```
from mem0 import MemoryClient

client = MemoryClient(api_key="your_api_key")

# Bulk feedback example
feedback_data = [
    {
        "memory_id": "memory-1", 
        "feedback": "POSITIVE", 
        "feedback_reason": "Accurately captured the user's preference"
    },
    {
        "memory_id": "memory-2", 
        "feedback": "NEGATIVE", 
        "feedback_reason": "Contains outdated information"
    }
]

for item in feedback_data:
    client.feedback(**item)

```

## ​Best Practices
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#best-practices)
### ​When to Provide Feedback
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#when-to-provide-feedback)- Immediately after memory retrieval when you can assess relevance
- During user interactions when users explicitly indicate satisfaction or dissatisfaction
- Through automated evaluation using your application’s success metrics

### ​Effective Feedback Reasons
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#effective-feedback-reasons)- “Contains outdated contact information”
- “Accurately captured the user’s dietary restrictions”
- “Irrelevant to the current conversation context”
- “Bad memory”
- “Wrong”
- “Not good”

### ​Feedback Strategy
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#feedback-strategy)- Be consistent: Apply the same criteria across similar memories
- Be specific: Detailed reasons help improve the system faster
- Monitor patterns: Regular feedback analysis helps identify improvement areas

## ​Error Handling
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#error-handling)
```
from mem0 import MemoryClient
from mem0.exceptions import MemoryNotFoundError, APIError

client = MemoryClient(api_key="your_api_key")

try:
    client.feedback(
        memory_id="memory-123", 
        feedback="POSITIVE", 
        feedback_reason="Helpful context for user query"
    )
    print("Feedback submitted successfully")
except MemoryNotFoundError:
    print("Memory not found")
except APIError as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

```

## ​Feedback Analytics
[​](https://docs.mem0.ai/platform/features/feedback-mechanism#feedback-analytics)- Feedback completion rates: What percentage of memories receive feedback
- Feedback distribution: Balance of positive vs. negative feedback
- Memory quality trends: How accuracy improves with feedback volume
- User satisfaction metrics: Correlation between feedback and user experience
