# Scope User vs Agent Memories - Mem0
Source: https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality
Downloaded: 2025-11-12 21:20:20
================================================================================


# ​Build AI with Distinct Personalities
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#build-ai-with-distinct-personalities)- user_id- Memories about specific users
- agent_id- Memories from the agent itself

## ​User Memories
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#user-memories)`user_id`
```
from openai import OpenAI
from mem0 import MemoryClient
import os

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
mem0_client = MemoryClient()

# Sarah logs her workout
mem0_client.add(
    "Completed 5K run in 28 minutes - felt great!",
    user_id="sarah"
)

# Mike logs his workout
mem0_client.add(
    "Bench press: 185 lbs x 10 reps, 3 sets",
    user_id="mike"
)


```

```
# Get Sarah's workout history
sarah_history = mem0_client.search(
    "What exercises has Sarah done recently?",
    filters={"user_id": "sarah"}
)

# Generate coaching advice
response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You're a supportive fitness coach."},
        {"role": "user", "content": f"Based on this history: {sarah_history}, suggest the next workout."}
    ]
)

print(response.choices[0].message.content)


```

```
Great job on that 5K! Your endurance is building nicely. Let's add some
strength work to complement your running. Try 3 sets of bodyweight squats
(15 reps each) to strengthen your legs and improve your running power.


```
`user_id`
## ​Adding Coach Personality
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#adding-coach-personality)`user_id`
```
# Adding coach personality for Sarah
mem0_client.add(
    "I'm a supportive fitness coach who celebrates every achievement and uses athlete-focused language",
    user_id="sarah"
)

# Adding the same personality for Mike
mem0_client.add(
    "I'm a supportive fitness coach who celebrates every achievement and uses athlete-focused language",
    user_id="mike"
)

# For 1,000 users, we'd repeat this 1,000 times...


```
- Duplication: We’re storing the same coaching personality 1,000 times for 1,000 users
- Hard to update: Want to change the coaching style? Update 1,000 memories
- Mixed with user data: Coach personality and user workouts are stored together, making queries complex
`user_id`
## ​Agent Memories
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#agent-memories)`agent_id`
```
# Store coach personality ONCE with agent_id
mem0_client.add(
    "I'm FitCoach - a supportive fitness coach who celebrates every achievement. "
    "I use motivational language, focus on progress over perfection, and help users build sustainable habits.",
    agent_id="fitcoach_v1"
)

# Sarah's workout (still private)
mem0_client.add(
    "Completed 5K run in 28 minutes",
    user_id="sarah"
)

# Mike's workout (still private)
mem0_client.add(
    "Bench press: 185 lbs x 10 reps, 3 sets",
    user_id="mike"
)


```

```
# Get both coach personality and Sarah's workouts
coaching_context = mem0_client.search(
    "coaching context for Sarah",
    filters={
        "OR": [
            {"agent_id": "fitcoach_v1"},  # Coach personality
            {"user_id": "sarah"}          # Sarah's workout history
        ]
    }
)

# Generate personalized coaching
response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": str(coaching_context)},
        {"role": "user", "content": "What should I focus on in my next workout?"}
    ]
)

print(response.choices[0].message.content)


```

```
Amazing work on that 5K! 🎉 You're crushing your running goals!

Now let's build some complementary strength. I recommend adding bodyweight
squats to your routine - they'll make you an even stronger runner. Start
with 3 sets of 15 reps, and remember: progress over perfection!


```
`agent_id``user_id`- ✅ Stored once, shared by all users
- ✅ Easy to update (change one memory, affects all users)
- ✅ Cleanly separated from user workout data
`agent_id``user_id`
## ​Combining Both: Relationship Memories
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#combining-both%3A-relationship-memories)`metadata`
```
# Coach personality (shared across all users)
mem0_client.add(
    "I'm FitCoach - supportive and motivational",
    agent_id="fitcoach_v1"
)

# Sarah's workout data (private to Sarah)
mem0_client.add(
    "Goal: Run a half marathon by June. Currently runs 5K comfortably.",
    user_id="sarah"
)

# Sarah-Coach relationship (stored as user memory with agent context in metadata)
mem0_client.add(
    "Sarah and I have an inside joke: 'No pain, no protein shake!' "
    "She responds best to gentle encouragement after tough workouts.",
    user_id="sarah",
    metadata={"agent_id": "fitcoach_v1", "type": "relationship"}
)

# Mike-Coach relationship (different from Sarah's)
mem0_client.add(
    "Mike prefers data-driven feedback with specific numbers and percentages. "
    "Less motivational talk, more concrete metrics.",
    user_id="mike",
    metadata={"agent_id": "fitcoach_v1", "type": "relationship"}
)


```

```
# Get Sarah's memories including relationship with fitcoach_v1
sarah_context = mem0_client.search(
    "How should I coach Sarah today?",
    user_id="sarah",
    filters={"metadata": {"agent_id": "fitcoach_v1"}}
)

# Get coach personality
coach_personality = mem0_client.search(
    "coaching personality",
    agent_id="fitcoach_v1"
)

# Combine both contexts
full_context = str(coach_personality) + "\\n" + str(sarah_context)

response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": full_context},
        {"role": "user", "content": "Just finished today's workout!"}
    ]
)

print(response.choices[0].message.content)


```

```
Awesome work today! 💪 No pain, no protein shake, right? 😄

You're making real progress toward that half marathon goal. Keep this
momentum going - your consistency is your superpower!


```

```
# Get Mike's memories including relationship with fitcoach_v1
mike_context = mem0_client.search(
    "How should I coach Mike today?",
    user_id="mike",
    filters={"metadata": {"agent_id": "fitcoach_v1"}}
)

coach_personality = mem0_client.search(
    "coaching personality",
    agent_id="fitcoach_v1"
)

full_context = str(coach_personality) + "\\n" + str(mike_context)

# ... same coaching code ...


```

```
Solid session. Your bench press shows 8% improvement over last week
(171 lbs avg to 185 lbs). Target: 200 lbs by end of month.
On track at current rate (+3.2% weekly).


```
`user_id``agent_id`
## ​Putting It All Together
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#putting-it-all-together)
```
from openai import OpenAI
from mem0 import MemoryClient
import os

# Initialize clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
mem0_client = MemoryClient()

# Layer 1: Agent personality (shared)
mem0_client.add(
    "I'm FitCoach - supportive, motivational, celebrates small wins",
    agent_id="fitcoach_v1",
    metadata={"type": "personality"}
)

# Layer 2: User profile (private)
mem0_client.add(
    "Sarah's goal: Run half marathon by June. Currently comfortable at 5K distance.",
    user_id="sarah",
    metadata={"type": "profile"}
)

# Layer 3: Relationship (stored as user memory with agent context in metadata)
mem0_client.add(
    "Sarah responds best to encouragement. Inside joke: 'No pain, no protein shake!'",
    user_id="sarah",
    metadata={"agent_id": "fitcoach_v1", "type": "relationship"}
)

# Log today's workout
mem0_client.add(
    "Completed 8K run in 45 minutes - new personal record!",
    user_id="sarah",
    metadata={"type": "workout", "date": "2025-01-23"}
)

# Generate coaching response
# Get Sarah's context (includes all her memories)
sarah_context = mem0_client.search(
    "Generate coaching advice for Sarah",
    user_id="sarah"
)

# Get coach personality
coach_personality = mem0_client.search(
    "coaching personality",
    agent_id="fitcoach_v1"
)

# Combine contexts
full_context = str(coach_personality) + "\\n" + str(sarah_context)

response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": full_context},
        {"role": "user", "content": "Just finished my run today!"}
    ]
)

print(response.choices[0].message.content)


```

```
🎉 YES! 8K is a HUGE milestone! You just crushed your previous distance!

Remember when you could barely do 5K? Look at you now! That half marathon
in June is looking more achievable every single day. No pain, no protein
shake - and today, you EARNED that shake! 💪

Next week, let's aim for 9K. You're ready for it!


```
- ✅ Motivational tone (agent personality)
- ✅ Specific goal reference (Sarah’s profile)
- ✅ Inside joke (relationship memory)
- ✅ Progress tracking (workout history)
- Agent memories(blue) - Shared personality and capabilities
- User memories(red) - Private workout data and goals
- Relationship memories(purple) - User memories with agent context stored in metadata

## ​When to Use What
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#when-to-use-what)
### ​Useuser_idonly (most apps)
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#use-user-id-only-most-apps)`user_id`- Todo lists
- Note-taking apps
- Personal finance trackers
- Support ticket history

```
mem0_client.add(
    "Bought groceries for $127.43",
    user_id="sarah"
)


```

### ​Useagent_idonly (rare)
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#use-agent-id-only-rare)`agent_id`- Calculator bots
- Language translators
- Company policy assistants (same policies for all)

```
mem0_client.add(
    "I can calculate: arithmetic, algebra, basic calculus. I cannot solve differential equations.",
    agent_id="calculator_v1"
)


```

### ​Use bothuser_idandagent_id(AI with personality)
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#use-both-user-id-and-agent-id-ai-with-personality)`user_id``agent_id`- Fitness coaches (this guide!)
- Educational tutors
- AI companions
- Therapy/mental health bots
- Game NPCs with character development

```
# Agent personality (shared across all users)
mem0_client.add(
    "Coaching personality and style",
    agent_id="agent_name"
)

# User data (private)
mem0_client.add(
    "User's goals and progress",
    user_id="user_name"
)

# Relationship (user memory with agent context in metadata)
mem0_client.add(
    "User's relationship with this specific agent",
    user_id="user_name",
    metadata={"agent_id": "agent_name", "type": "relationship"}
)


```

## ​Best Practices
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#best-practices)
### ​1. Use clear naming conventions
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#1-use-clear-naming-conventions)
```
# Good: Descriptive and versioned
agent_id="fitcoach_v1"
user_id="sarah_123"

# Bad: Generic and unclear
agent_id="agent1"
user_id="user_abc"


```

### ​2. Tag memories with metadata
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#2-tag-memories-with-metadata)
```
# For relationship memories, store agent context in metadata
mem0_client.add(
    content,
    user_id="sarah",
    metadata={
        "agent_id": "fitcoach_v1",
        "type": "relationship",
        "version": "v1"
    }
)


```

### ​3. Test data isolation
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#3-test-data-isolation)
```
# Get Mike's memories
mike_memories = mem0_client.get_all(filters={"user_id": "mike"})

# Get Sarah's memories
sarah_memories = mem0_client.get_all(filters={"user_id": "sarah"})

# Verify no overlap
assert len(set(mike_memories) & set(sarah_memories)) == 0, "Data leak detected!"


```

### ​4. Version your agents
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#4-version-your-agents)
```
# Version 1: Gentle and encouraging
mem0_client.add(
    "I'm supportive and celebrate small wins",
    agent_id="fitcoach_v1"
)

# Version 2: Data-driven and metric-focused
mem0_client.add(
    "I provide concrete metrics and percentage improvements",
    agent_id="fitcoach_v2"
)

# Assign users to different versions by storing version in metadata
mem0_client.add(
    "Sarah's workout preferences and relationship with coach",
    user_id="sarah",
    metadata={"agent_id": "fitcoach_v1"}
)
mem0_client.add(
    "Mike's workout preferences and relationship with coach",
    user_id="mike",
    metadata={"agent_id": "fitcoach_v2"}
)


```

## ​What You Built
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#what-you-built)- Agent personality (agent_id)- Shared coaching style across all users, updated once
- User profiles (user_id)- Private workout history, goals, and progress for each person
- Relationship memories (user_id + metadata)- Personalized interaction preferences per user-agent pair
- Data isolation- Sarah never sees Mike’s workouts, guaranteed by user_id filtering

## ​Summary
[​](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality#summary)`user_id``agent_id``user_id``user_id``agent_id`[Control What Gets StoredFilter low-signal conversations before they pollute long-term memory.](https://docs.mem0.ai/cookbooks/essentials/controlling-memory-ingestion)
## Control What Gets Stored
[Organize Support MemoriesCategorize customer context so teams can retrieve the right facts fast.](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories)
## Organize Support Memories
