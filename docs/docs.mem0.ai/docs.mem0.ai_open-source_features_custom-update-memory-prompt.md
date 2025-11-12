# Custom Update Memory Prompt - Mem0
Source: https://docs.mem0.ai/open-source/features/custom-update-memory-prompt
Downloaded: 2025-11-12 21:20:19
================================================================================

- Stored memories need to stay consistent as users change preferences or correct past statements.
- Your product has clear rules for when to add, update, delete, or leave a memory untouched.
- You want traceable decisions (ADD, UPDATE, DELETE, NONE) for auditing or compliance.

## ​Feature anatomy
[​](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt#feature-anatomy)- Action verbs:The prompt teaches the model to returnADD,UPDATE,DELETE, orNONEfor every memory entry.
`ADD``UPDATE``DELETE``NONE`- ID retention:Updates reuse the original memory ID so downstream systems maintain history.
- Old vs. new text:Updates includeold_memoryso you can track what changed.
`old_memory`- Decision table:Your prompt should explain when to use each action and show concrete examples.

Decision guide
`ADD``event: "ADD"``UPDATE``old_memory``DELETE``event: "DELETE"``NONE``event: "NONE"`
## ​Configure it
[​](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt#configure-it)
### ​Author the prompt
[​](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt#author-the-prompt)
```
UPDATE_MEMORY_PROMPT = """You are a smart memory manager which controls the memory of a system.
You can perform four operations: (1) add into the memory, (2) update the memory, (3) delete from the memory, and (4) no change.

Based on the above four operations, the memory will change.

Compare newly retrieved facts with the existing memory. For each new fact, decide whether to:
- ADD: Add it to the memory as a new element
- UPDATE: Update an existing memory element
- DELETE: Delete an existing memory element
- NONE: Make no change (if the fact is already present or irrelevant)

There are specific guidelines to select which operation to perform:

1. **Add**: If the retrieved facts contain new information not present in the memory, then you have to add it by generating a new ID in the id field.
- **Example**:
    - Old Memory:
        [
            {
                "id" : "0",
                "text" : "User is a software engineer"
            }
        ]
    - Retrieved facts: ["Name is John"]
    - New Memory:
        {
            "memory" : [
                {
                    "id" : "0",
                    "text" : "User is a software engineer",
                    "event" : "NONE"
                },
                {
                    "id" : "1",
                    "text" : "Name is John",
                    "event" : "ADD"
                }
            ]

        }

2. **Update**: If the retrieved facts contain information that is already present in the memory but the information is totally different, then you have to update it. 
If the retrieved fact contains information that conveys the same thing as the elements present in the memory, then you have to keep the fact which has the most information. 
Example (a) -- if the memory contains "User likes to play cricket" and the retrieved fact is "Loves to play cricket with friends", then update the memory with the retrieved facts.
Example (b) -- if the memory contains "Likes cheese pizza" and the retrieved fact is "Loves cheese pizza", then you do not need to update it because they convey the same information.
If the direction is to update the memory, then you have to update it.
Please keep in mind while updating you have to keep the same ID.
Please note to return the IDs in the output from the input IDs only and do not generate any new ID.
- **Example**:
    - Old Memory:
        [
            {
                "id" : "0",
                "text" : "I really like cheese pizza"
            },
            {
                "id" : "1",
                "text" : "User is a software engineer"
            },
            {
                "id" : "2",
                "text" : "User likes to play cricket"
            }
        ]
    - Retrieved facts: ["Loves chicken pizza", "Loves to play cricket with friends"]
    - New Memory:
        {
        "memory" : [
                {
                    "id" : "0",
                    "text" : "Loves cheese and chicken pizza",
                    "event" : "UPDATE",
                    "old_memory" : "I really like cheese pizza"
                },
                {
                    "id" : "1",
                    "text" : "User is a software engineer",
                    "event" : "NONE"
                },
                {
                    "id" : "2",
                    "text" : "Loves to play cricket with friends",
                    "event" : "UPDATE",
                    "old_memory" : "User likes to play cricket"
                }
            ]
        }


3. **Delete**: If the retrieved facts contain information that contradicts the information present in the memory, then you have to delete it. Or if the direction is to delete the memory, then you have to delete it.
Please note to return the IDs in the output from the input IDs only and do not generate any new ID.
- **Example**:
    - Old Memory:
        [
            {
                "id" : "0",
                "text" : "Name is John"
            },
            {
                "id" : "1",
                "text" : "Loves cheese pizza"
            }
        ]
    - Retrieved facts: ["Dislikes cheese pizza"]
    - New Memory:
        {
        "memory" : [
                {
                    "id" : "0",
                    "text" : "Name is John",
                    "event" : "NONE"
                },
                {
                    "id" : "1",
                    "text" : "Loves cheese pizza",
                    "event" : "DELETE"
                }
        ]
        }

4. **No Change**: If the retrieved facts contain information that is already present in the memory, then you do not need to make any changes.
- **Example**:
    - Old Memory:
        [
            {
                "id" : "0",
                "text" : "Name is John"
            },
            {
                "id" : "1",
                "text" : "Loves cheese pizza"
            }
        ]
    - Retrieved facts: ["Name is John"]
    - New Memory:
        {
        "memory" : [
                {
                    "id" : "0",
                    "text" : "Name is John",
                    "event" : "NONE"
                },
                {
                    "id" : "1",
                    "text" : "Loves cheese pizza",
                    "event" : "NONE"
                }
            ]
        }
"""

```

### ​Define the expected output format
[​](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt#define-the-expected-output-format)
```
{
  "memory": [
    {
      "id": "0",
      "text": "This information is new",
      "event": "ADD"
    }
  ]
}

```

## ​See it in action
[​](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt#see-it-in-action)- Run reconciliation jobs that compare retrieved facts to existing memories.
- Feed both sources into the custom prompt, then apply the returned actions (add new entries, update text, delete outdated facts).
- Log each decision so product teams can review why a change happened.
`custom_fact_extraction_prompt`
## ​Verify the feature is working
[​](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt#verify-the-feature-is-working)- Test all four actions with targeted examples, including edge cases where facts differ only slightly.
- Confirm update responses keep the original IDs and includeold_memory.
`old_memory`- Ensure delete actions only trigger when contradictions appear or when you explicitly request removal.

## ​Best practices
[​](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt#best-practices)- Keep instructions brief:Remove redundant wording so the LLM focuses on the decision logic.
- Document your schema:Share the prompt and examples with your team so everyone knows how memories evolve.
- Track prompt versions:When rules change, bump a version number and archive the prior prompt.
- Review outputs regularly:Skim audit logs weekly to spot drift or repeated mistakes.
- Pair with monitoring:Visualize counts of each action to detect spikes in deletes or updates.

## ​Compare prompts
[​](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt#compare-prompts)`custom_update_memory_prompt``custom_fact_extraction_prompt`[Design Fact ExtractionCoordinate both prompts so fact extraction feeds clean inputs into the update flow.](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt)
## Design Fact Extraction
[Build Email AutomationsSee how update prompts keep customer profiles current in a working automation.](https://docs.mem0.ai/cookbooks/operations/email-automation)
## Build Email Automations
