# Custom Fact Extraction Prompt - Mem0
Source: https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt
Downloaded: 2025-11-12 21:20:19
================================================================================

- A project needs domain-specific facts (order numbers, customer info) without storing casual chatter.
- You already have a clear schema for memories and want the LLM to follow it.
- You must prevent irrelevant details from entering long-term storage.

## ​Feature anatomy
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#feature-anatomy)- Prompt instructions:Describe which entities or phrases to keep. Specific guidance keeps the extractor focused.
- Few-shot examples:Show positive and negative cases so the model copies the right format.
- Structured output:Responses return JSON with afactsarray that Mem0 converts into individual memories.
`facts`- LLM configuration:custom_fact_extraction_prompt(Python) orcustomPrompt(TypeScript) lives alongside your model settings.
`custom_fact_extraction_prompt``customPrompt`
Prompt blueprint
- State the allowed fact types.
- Include short examples that mirror production messages.
- Show both empty ([]) and populated outputs.
`[]`- Remind the model to return JSON with afactskey only.
`facts`
## ​Configure it
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#configure-it)
### ​Write the custom prompt
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#write-the-custom-prompt)
```
custom_fact_extraction_prompt = """
Please only extract entities containing customer support information, order details, and user information. 
Here are some few shot examples:

Input: Hi.
Output: {"facts" : []}

Input: The weather is nice today.
Output: {"facts" : []}

Input: My order #12345 hasn't arrived yet.
Output: {"facts" : ["Order #12345 not received"]}

Input: I'm John Doe, and I'd like to return the shoes I bought last week.
Output: {"facts" : ["Customer name: John Doe", "Wants to return shoes", "Purchase made last week"]}

Input: I ordered a red shirt, size medium, but received a blue one instead.
Output: {"facts" : ["Ordered red shirt, size medium", "Received blue shirt instead"]}

Return the facts and customer information in a json format as shown above.
"""

```

### ​Load the prompt in configuration
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#load-the-prompt-in-configuration)
```
from mem0 import Memory

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4.1-nano-2025-04-14",
            "temperature": 0.2,
            "max_tokens": 2000,
        }
    },
    "custom_fact_extraction_prompt": custom_fact_extraction_prompt,
    "version": "v1.1"
}

m = Memory.from_config(config_dict=config)

```
`add`
## ​See it in action
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#see-it-in-action)
### ​Example: Order support memory
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#example%3A-order-support-memory)
```
m.add("Yesterday, I ordered a laptop, the order id is 12345", user_id="alice")

```

### ​Example: Irrelevant message filtered out
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#example%3A-irrelevant-message-filtered-out)
```
m.add("I like going to hikes", user_id="alice")

```
`results`
## ​Verify the feature is working
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#verify-the-feature-is-working)- Log every call during rollout and confirm thefactsarray matches your schema.
`facts`- Check that unrelated messages return an emptyresultsarray.
`results`- Run regression samples whenever you edit the prompt to ensure previously accepted facts still pass.

## ​Best practices
[​](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt#best-practices)- Be precise:Call out the exact categories or fields you want to capture.
- Show negative cases:Include examples that should produce[]so the model learns to skip them.
`[]`- Keep JSON strict:Avoid extra keys; only returnfactsto simplify downstream parsing.
`facts`- Version prompts:Track prompt changes with a version number so you can roll back quickly.
- Review outputs regularly:Spot-check stored memories to catch drift early.
[Review Add OperationsRefresh how Mem0 stores memories and how prompts influence fact creation.](https://docs.mem0.ai/core-concepts/memory-operations/add)
## Review Add Operations
[Automate Support TriageApply custom extraction to route customer requests in a full workflow.](https://docs.mem0.ai/cookbooks/operations/support-inbox)
## Automate Support Triage
