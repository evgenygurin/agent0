# Custom Categories - Mem0
Source: https://docs.mem0.ai/platform/features/custom-categories
Downloaded: 2025-11-12 21:20:18
================================================================================


# ​Custom Categories
[​](https://docs.mem0.ai/platform/features/custom-categories#custom-categories)- You need Mem0 to tag memories with names your product team already uses.
- You want clean reports or automations that rely on those tags.
- You’re moving from the open-source version and want the same labels here.
`custom_categories=...``client.add`
## ​Configure access
[​](https://docs.mem0.ai/platform/features/custom-categories#configure-access)- EnsureMEM0_API_KEYis set in your environment or pass it to the SDK constructor.
`MEM0_API_KEY`- If you scope work to a specific organization/project, initialize the client with those identifiers.

## ​How it works
[​](https://docs.mem0.ai/platform/features/custom-categories#how-it-works)- Default list— Each project starts with 15 broad categories liketravel,sports, andmusic.
`travel``sports``music`- Project override— When you callproject.update(custom_categories=[...]), that list replaces the defaults for future memories.
`project.update(custom_categories=[...])`- Automatic tags— As new memories come in, Mem0 picks the closest matches from your list and saves them in thecategoriesfield.
`categories``personal_details``family``professional_details``sports``travel``food``music``health``technology``hobbies``fashion``entertainment``milestones``user_preferences``misc`
## ​Configure it
[​](https://docs.mem0.ai/platform/features/custom-categories#configure-it)
### ​1. Set custom categories at the project level
[​](https://docs.mem0.ai/platform/features/custom-categories#1-set-custom-categories-at-the-project-level)
```
import os
from mem0 import MemoryClient

os.environ["MEM0_API_KEY"] = "your-api-key"

client = MemoryClient()

# Update custom categories
new_categories = [
    {"lifestyle_management_concerns": "Tracks daily routines, habits, hobbies and interests including cooking, time management and work-life balance"},
    {"seeking_structure": "Documents goals around creating routines, schedules, and organized systems in various life areas"},
    {"personal_information": "Basic information about the user including name, preferences, and personality traits"}
]

response = client.project.update(custom_categories=new_categories)
print(response)

```

### ​2. Confirm the active catalog
[​](https://docs.mem0.ai/platform/features/custom-categories#2-confirm-the-active-catalog)
```
# Get current custom categories
categories = client.project.get(fields=["custom_categories"])
print(categories)

```

## ​See it in action
[​](https://docs.mem0.ai/platform/features/custom-categories#see-it-in-action)
### ​Add a memory (uses the project catalog automatically)
[​](https://docs.mem0.ai/platform/features/custom-categories#add-a-memory-uses-the-project-catalog-automatically)
```
messages = [
    {"role": "user", "content": "My name is Alice. I need help organizing my daily schedule better. I feel overwhelmed trying to balance work, exercise, and social life."},
    {"role": "assistant", "content": "I understand how overwhelming that can feel. Let's break this down together. What specific areas of your schedule feel most challenging to manage?"},
    {"role": "user", "content": "I want to be more productive at work, maintain a consistent workout routine, and still have energy for friends and hobbies."},
    {"role": "assistant", "content": "Those are great goals for better time management. What's one small change you could make to start improving your daily routine?"},
]

# Add memories with project-level custom categories
client.add(messages, user_id="alice", async_mode=False)

```

### ​Retrieve memories and inspect categories
[​](https://docs.mem0.ai/platform/features/custom-categories#retrieve-memories-and-inspect-categories)
```
memories = client.get_all(filters={"user_id": "alice"})

```

```
{
  "id": "33d2***",
  "memory": "Trying to balance work and workouts",
  "user_id": "alice",
  "metadata": null,
  "categories": ["wellness"],  // ← matches the custom category we set
  "created_at": "2025-11-01T02:13:32.828364-07:00",
  "updated_at": "2025-11-01T02:13:32.830896-07:00",
  "expiration_date": null,
  "structured_attributes": {
    "day": 1,
    "hour": 9,
    "year": 2025,
    "month": 11,
    "minute": 13,
    "quarter": 4,
    "is_weekend": true,
    "day_of_week": "saturday",
    "day_of_year": 305,
    "week_of_year": 44
  }
}

```
`metadata`
## ​Default categories (fallback)
[​](https://docs.mem0.ai/platform/features/custom-categories#default-categories-fallback)
```
- personal_details
- family
- professional_details
- sports
- travel
- food
- music
- health
- technology
- hobbies
- fashion
- entertainment
- milestones
- user_preferences
- misc

```

```
import os
from mem0 import MemoryClient

os.environ["MEM0_API_KEY"] = "your-api-key"

client = MemoryClient()

messages = [
    {"role": "user", "content": "Hi, my name is Alice."},
    {"role": "assistant", "content": "Hi Alice, what sports do you like to play?"},
    {"role": "user", "content": "I love playing badminton, football, and basketball. I'm quite athletic!"},
    {"role": "assistant", "content": "That's great! Alice seems to enjoy both individual sports like badminton and team sports like football and basketball."},
    {"role": "user", "content": "Sometimes, I also draw and sketch in my free time."},
    {"role": "assistant", "content": "That's cool! I'm sure you're good at it."}
]

# Add memories with default categories
client.add(messages, user_id='alice', async_mode=False)

```

```
client.project.get(["custom_categories"])

```

## ​Verify the feature is working
[​](https://docs.mem0.ai/platform/features/custom-categories#verify-the-feature-is-working)- client.project.get(["custom_categories"])returns the category list you set.
`client.project.get(["custom_categories"])`- client.get_all(filters={"user_id": ...})shows populatedcategorieslists on new memories.
`client.get_all(filters={"user_id": ...})``categories`- The Mem0 dashboard (Project → Memories) displays the custom labels in the Category column.

## ​Best practices
[​](https://docs.mem0.ai/platform/features/custom-categories#best-practices)- Keep category descriptions concise but specific; the classifier uses them to disambiguate.
- Review memories with emptycategoriesto see where you might extend or rename your list.
`categories`- Stick with project-level overrides until per-request support is released; mixing approaches causes confusion.
[Advanced Memory OperationsExplore other ingestion tunables like custom prompts and selective writes.](https://docs.mem0.ai/platform/advanced-memory-operations)
## Advanced Memory Operations
[Travel Assistant CookbookSee custom tagging drive personalization in a full agent workflow.](https://docs.mem0.ai/cookbooks/companions/travel-assistant)
## Travel Assistant Cookbook
