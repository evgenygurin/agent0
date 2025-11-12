# Build a Companion with Mem0 - Mem0
Source: https://docs.mem0.ai/cookbooks/essentials/building-ai-companion
Downloaded: 2025-11-12 21:20:21
================================================================================

- Remembers user goals across sessions
- Recalls past workouts and progress
- Adapts its personality based on user preferences
- Handles both short-term context (today’s chat) and long-term memory (months of history)

## ​The Basic Loop with Memory
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#the-basic-loop-with-memory)
```
from openai import OpenAI
from mem0 import MemoryClient

openai_client = OpenAI(api_key="your-openai-key")
mem0_client = MemoryClient(api_key="your-mem0-key")

def chat(user_input, user_id):
    # Retrieve relevant memories
    memories = mem0_client.search(user_input, user_id=user_id, limit=5)
    context = "\\n".join(m["memory"] for m in memories["results"])

    # Call LLM with memory context
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You're Ray, a running coach. Memories:\\n{context}"},
            {"role": "user", "content": user_input}
        ]
    ).choices[0].message.content

    # Store the exchange
    mem0_client.add([
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": response}
    ], user_id=user_id)

    return response


```

```
chat("I want to run a marathon in under 4 hours", user_id="max")
# Output: "That's a solid goal. What's your current weekly mileage?"
# Stored in Mem0: "Max wants to run sub-4 marathon"


```

```
chat("What should I focus on today?", user_id="max")
# Output: "Based on your sub-4 marathon goal, let's work on building your aerobic base..."


```

## ​Organizing Memory by Type
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#organizing-memory-by-type)
### ​Separating Temporary from Permanent
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#separating-temporary-from-permanent)- Categories: AI-assigned by Mem0 based on content (you can’t force them)
- Metadata: Manually set by you for forced tagging

```
mem0_client.project.update(custom_categories=[
    {"goals": "Race targets and training objectives"},
    {"constraints": "Injuries, limitations, recovery needs"},
    {"preferences": "Training style, surfaces, schedules"}
])


```
`metadata`
```
# Add goal - Mem0 automatically tags it as "goals"
mem0_client.add(
    [{"role": "user", "content": "Sub-4 marathon is my A-race"}],
    user_id="max"
)

# Add constraint - Mem0 automatically tags it as "constraints"
mem0_client.add(
    [{"role": "user", "content": "My right knee flares up on downhills"}],
    user_id="max"
)


```
`metadata`
```
# Force tag using metadata (not categories)
mem0_client.add(
    [{"role": "user", "content": "Some workout note"}],
    user_id="max",
    metadata={"workout_type": "speed", "forced_tag": "custom_label"}
)


```

### ​Filtering by Category
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#filtering-by-category)
```
constraints = mem0_client.search(
    "injury concerns",
    user_id="max",
    filters={"categories": {"in": ["constraints"]}}
)
print([m["memory"] for m in constraints["results"]])
# Output: ["Max's right knee flares up on downhills"]


```

## ​Filtering What Gets Stored
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#filtering-what-gets-stored)
### ​The Problem
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#the-problem)
```
memories = mem0_client.get_all(user_id="max")
print([m["memory"] for m in memories["results"]])
# Output: ["Max wants to run marathon under 4 hours", "hey", "lol ok", "cool thanks", "gtg bye"]


```

### ​Custom Instructions
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#custom-instructions)
```
mem0_client.project.update(custom_instructions="""
Extract from running coach conversations:
- Training goals and race targets
- Physical constraints or injuries
- Training preferences (time of day, surfaces, weather)
- Progress milestones

Exclude:
- Greetings and filler
- Casual chatter
- Hypotheticals unless planning related
""")


```

```
chat("hey how's it going", user_id="max")
chat("I prefer trail running over roads", user_id="max")

memories = mem0_client.get_all(user_id="max")
print([m["memory"] for m in memories["results"]])
# Output: ["Max wants to run marathon under 4 hours", "Max prefers trail running over roads"]


```

## ​Agent Memory for Personality
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#agent-memory-for-personality)
### ​Why Agents Need Memory Too
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#why-agents-need-memory-too)
```
mem0_client.add(
    [{"role": "system", "content": "Max wants direct, data-driven feedback. Skip motivational language."}],
    agent_id="ray_coach"
)


```

```
# Get coach personality
agent_memories = mem0_client.search("coaching style", agent_id="ray_coach")
# Output: ["Max wants direct, data-driven feedback. Skip motivational language."]

# Store conversations with agent_id
mem0_client.add([
    {"role": "user", "content": "How'd my run look today?"},
    {"role": "assistant", "content": "Pace was 8:15/mile. Heart rate 152, zone 2."}
], user_id="max", agent_id="ray_coach")


```

## ​Managing Short-Term Context
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#managing-short-term-context)
### ​When to Store in Mem0
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#when-to-store-in-mem0)
```
# Store only meaningful exchanges in Mem0
mem0_client.add([
    {"role": "user", "content": "I want to run a marathon"},
    {"role": "assistant", "content": "Let's build a training plan"}
], user_id="max")

# Skip storing filler
# "hey" → don't store
# "cool thanks" → don't store

# Or rely on custom_instructions to filter automatically


```

## ​Time-Bound Memories
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#time-bound-memories)
### ​Auto-Expiring Facts
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#auto-expiring-facts)
```
from datetime import datetime, timedelta

expiration = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

mem0_client.add(
    [{"role": "user", "content": "Rolled my left ankle, needs rest"}],
    user_id="max",
    expiration_date=expiration
)


```

## ​Putting It All Together
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#putting-it-all-together)
```
from mem0 import MemoryClient
from datetime import datetime, timedelta

mem0_client = MemoryClient(api_key="your-mem0-key")

# Configure memory filtering and categories
mem0_client.project.update(
    custom_instructions="""
    Extract: goals, constraints, preferences, progress
    Exclude: greetings, filler, casual chat
    """,
    custom_categories=[
        {"name": "goals", "description": "Training targets"},
        {"name": "constraints", "description": "Injuries and limitations"},
        {"name": "preferences", "description": "Training style"}
    ]
)


```

```
mem0_client.add([
    {"role": "user", "content": "I want to run a sub-4 marathon"},
    {"role": "assistant", "content": "Got it. Let's build a training plan."}
], user_id="max", agent_id="ray", categories=["goals"])

mem0_client.add([
    {"role": "user", "content": "I prefer trail running over roads"}
], user_id="max", categories=["preferences"])


```

```
expiration = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
mem0_client.add(
    [{"role": "user", "content": "Rolled ankle, need light workouts"}],
    user_id="max",
    categories=["constraints"],
    expiration_date=expiration
)


```

```
memories = mem0_client.search("training plan", user_id="max", limit=5)
# Gets: marathon goal, trail preference, ankle injury (if still valid)


```

## ​Common Production Patterns
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#common-production-patterns)
### ​Episodic Stories with run_id
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#episodic-stories-with-run-id)
```
mem0_client.add(messages, user_id="max", run_id="boston-2025")
mem0_client.add(messages, user_id="max", run_id="nyc-2025")

# Retrieve only Boston memories
boston_memories = mem0_client.search(
    "training plan",
    user_id="max",
    run_id="boston-2025"
)


```

### ​Importing Historical Data
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#importing-historical-data)
```
old_logs = [
    [{"role": "user", "content": "Completed 20-mile long run"}],
    [{"role": "user", "content": "Hit 8:00 pace on tempo run"}],
]

for log in old_logs:
    mem0_client.add(log, user_id="max")


```

### ​Handling Contradictions
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#handling-contradictions)
```
# Find the old memory
memories = mem0_client.get_all(user_id="max")
goal_memory = [m for m in memories["results"] if "sub-4" in m["memory"]][0]

# Update it
mem0_client.update(goal_memory["id"], "Max wants to run sub-3:45 marathon")


```

### ​Multiple Agents
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#multiple-agents)
```
chat("easy run today", user_id="max", agent_id="ray")
chat("leg day workout", user_id="max", agent_id="jordan")


```

### ​Filtering by Date
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#filtering-by-date)
```
recent = mem0_client.search(
    "training progress",
    user_id="max",
    filters={"created_at": {"gte": "2025-10-01"}}
)


```

### ​Metadata Tagging
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#metadata-tagging)
```
mem0_client.add(
    [{"role": "user", "content": "10x400m intervals"}],
    user_id="max",
    metadata={"workout_type": "speed", "intensity": "high"}
)

# Later, find all speed workouts
speed_sessions = mem0_client.search(
    "speed work",
    user_id="max",
    filters={"metadata": {"workout_type": "speed"}}
)


```

### ​Pruning Old Memories
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#pruning-old-memories)
```
mem0_client.delete(memory_id="mem_xyz")

# Or clear an entire run_id
mem0_client.delete_all(user_id="max", run_id="old-training-cycle")


```

## ​What You Built
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#what-you-built)- Persists across sessions- Mem0 storage
- Filters noise- custom instructions
- Organizes by type- categories
- Adapts personality-agent_id
`agent_id`- Stays fast- short-term buffer
- Handles temporal facts- expiration
- Scales to production- batching, metadata, pruning

## ​Production Checklist
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion#production-checklist)- Set custom instructions for your domain
- Define 2-3 categories (goals, constraints, preferences)
- Add expiration strategy for time-bound facts
- Implement error handling for API calls
- Monitor memory quality in Mem0 dashboard
- Clear test data from production project
[Build AI with PersonalitySeparate user and agent memories so companions stay consistent across sessions.](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality)
## Build AI with Personality
[Tag Support MemoriesOrganize customer context to keep assistants responsive at scale.](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories)
## Tag Support Memories
