# Criteria Retrieval - Mem0
Source: https://docs.mem0.ai/platform/features/criteria-retrieval
Downloaded: 2025-11-12 21:20:18
================================================================================

- Prioritize joyful memories when building a wellness assistant
- Downrank negative memories in a productivity-focused agent
- Highlight curiosity in a tutoring agent

## ​When to Use Criteria Retrieval
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#when-to-use-criteria-retrieval)- You’re building an agent that should react toemotionsorbehavioral signals
- You want to guide memory selection based oncontext, not just content
- You have domain-specific signals like “risk”, “positivity”, “confidence”, etc. that shape recall

## ​Setting Up Criteria Retrieval
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#setting-up-criteria-retrieval)
### ​Initialize the Client
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#initialize-the-client)`MemoryClient`
```
from mem0 import MemoryClient

client = MemoryClient(
    api_key="your_mem0_api_key",
    org_id="your_organization_id",
    project_id="your_project_id"
)

```

### ​Define Your Criteria
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#define-your-criteria)- Aname(used in scoring)
`name`- Adescription(interpreted by the LLM)
`description`- Aweight(how much it influences the final score)
`weight`
```
retrieval_criteria = [
    {
        "name": "joy",
        "description": "Measure the intensity of positive emotions such as happiness, excitement, or amusement expressed in the sentence. A higher score reflects greater joy.",
        "weight": 3
    },
    {
        "name": "curiosity",
        "description": "Assess the extent to which the sentence reflects inquisitiveness, interest in exploring new information, or asking questions. A higher score reflects stronger curiosity.",
        "weight": 2
    },
    {
        "name": "emotion",
        "description": "Evaluate the presence and depth of sadness or negative emotional tone, including expressions of disappointment, frustration, or sorrow. A higher score reflects greater sadness.",
        "weight": 1
    }
]

```

### ​Apply Criteria to Your Project
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#apply-criteria-to-your-project)
```
client.project.update(retrieval_criteria=retrieval_criteria)

```

## ​Example Walkthrough
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#example-walkthrough)
### ​Add Memories
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#add-memories)
```
messages = [
    {"role": "user", "content": "What a beautiful sunny day! I feel so refreshed and ready to take on anything!"},
    {"role": "user", "content": "I've always wondered how storms form—what triggers them in the atmosphere?"},
    {"role": "user", "content": "It's been raining for days, and it just makes everything feel heavier."},
    {"role": "user", "content": "Finally I get time to draw something today, after a long time!! I am super happy today."}
]

client.add(messages, user_id="alice")

```

### ​Run Standard vs. Criteria-Based Search
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#run-standard-vs-criteria-based-search)
```
# Search with criteria enabled
filters = {"user_id": "alice"}
results_with_criteria = client.search(
    query="Why I am feeling happy today?",
    filters=filters
)

# To disable criteria for a specific search
results_without_criteria = client.search(
    query="Why I am feeling happy today?",
    filters=filters,
    use_criteria=False  # Disable criteria-based scoring
)

```

### ​Compare Results
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#compare-results)
### ​Search Results (with Criteria)
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#search-results-with-criteria)
```
[
    {"memory": "User feels refreshed and ready to take on anything on a beautiful sunny day", "score": 0.666, ...},
    {"memory": "User finally has time to draw something after a long time", "score": 0.616, ...},
    {"memory": "User is happy today", "score": 0.500, ...},
    {"memory": "User is curious about how storms form and what triggers them in the atmosphere.", "score": 0.400, ...},
    {"memory": "It has been raining for days, making everything feel heavier.", "score": 0.116, ...}
]

```

### ​Search Results (without Criteria)
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#search-results-without-criteria)
```
[
    {"memory": "User is happy today", "score": 0.607, ...},
    {"memory": "User feels refreshed and ready to take on anything on a beautiful sunny day", "score": 0.512, ...},
    {"memory": "It has been raining for days, making everything feel heavier.", "score": 0.4617, ...},
    {"memory": "User is curious about how storms form and what triggers them in the atmosphere.", "score": 0.340, ...},
    {"memory": "User finally has time to draw something after a long time", "score": 0.336, ...},
]

```

## ​Search Results Comparison
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#search-results-comparison)- Memory Ordering: With criteria, memories with high joy scores (like feeling refreshed and drawing) are ranked higher. Without criteria, the most relevant memory (“User is happy today”) comes first.
- Score Distribution: With criteria, scores are more spread out (0.116 to 0.666) and reflect the criteria weights. Without criteria, scores are more clustered (0.336 to 0.607) and based purely on relevance.
- Trait Sensitivity: “Rainy day” content is penalized due to negative tone, while “Storm curiosity” is recognized and scored accordingly.

## ​Key Differences vs. Standard Search
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#key-differences-vs-standard-search)
## ​Best Practices
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#best-practices)- Choose 3-5 criteria that reflect your application’s intent
- Make descriptions clear and distinct; these are interpreted by an LLM
- Use stronger weights to amplify the impact of important traits
- Avoid redundant or ambiguous criteria (e.g., “positivity” and “joy”)
- Always handle empty result sets in your application logic

## ​How It Works
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#how-it-works)- Criteria Definition: Define custom criteria with a name, description, and weight. These describe what matters in a memory (e.g., joy, urgency, empathy).
- Project Configuration: Register these criteria usingproject.update(). They apply at the project level and automatically influence all searches.
`project.update()`- Memory Retrieval: When you perform a search, Mem0 first retrieves relevant memories based on the query.
- Weighted Scoring: Each retrieved memory is evaluated and scored against your defined criteria and weights.
`use_criteria=False`
## ​Summary
[​](https://docs.mem0.ai/platform/features/criteria-retrieval#summary)- Define what “relevant” means using criteria
- Apply them per project viaproject.update()
`project.update()`- Criteria-aware search activates automatically when criteria are configured
- Build agents that reason not just with relevance, butcontextual importance
[DiscordJoin our community](https://mem0.dev/DiD)
## Discord
[GitHubAsk questions on GitHub](https://github.com/mem0ai/mem0/discussions/new?category=q-a)
## GitHub
[SupportTalk to founders](https://cal.com/taranjeetio/meet)
## Support
