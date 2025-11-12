# Custom Instructions - Mem0
Source: https://docs.mem0.ai/platform/features/custom-instructions
Downloaded: 2025-11-12 21:20:18
================================================================================


## ​What are Custom Instructions?
[​](https://docs.mem0.ai/platform/features/custom-instructions#what-are-custom-instructions%3F)
```
# Simple example: Health app focusing on wellness
prompt = """
Extract only health and wellness information:
- Symptoms, medications, and treatments
- Exercise routines and dietary habits
- Doctor appointments and health goals

Exclude: Personal identifiers, financial data
"""

client.project.update(custom_instructions=prompt)

```

## ​Why Use Custom Instructions?
[​](https://docs.mem0.ai/platform/features/custom-instructions#why-use-custom-instructions%3F)- Focus on What Matters: Only capture information relevant to your application
- Maintain Privacy: Explicitly exclude sensitive data like passwords or personal identifiers
- Ensure Consistency: All memories follow the same extraction rules across your project
- Improve Quality: Filter out noise and irrelevant conversations

## ​How to Set Custom Instructions
[​](https://docs.mem0.ai/platform/features/custom-instructions#how-to-set-custom-instructions)
### ​Basic Setup
[​](https://docs.mem0.ai/platform/features/custom-instructions#basic-setup)
```
# Set instructions for your project
client.project.update(custom_instructions="Your guidelines here...")

# Retrieve current instructions
response = client.project.get(fields=["custom_instructions"])
print(response["custom_instructions"])

```

### ​Best Practice Template
[​](https://docs.mem0.ai/platform/features/custom-instructions#best-practice-template)
```
Your Task: [Brief description of what to extract]

Information to Extract:
1. [Category 1]:
   - [Specific details]
   - [What to look for]

2. [Category 2]:
   - [Specific details]
   - [What to look for]

Guidelines:
- [Processing rules]
- [Quality requirements]

Exclude:
- [Sensitive data to avoid]
- [Irrelevant information]

```

## ​Real-World Examples
[​](https://docs.mem0.ai/platform/features/custom-instructions#real-world-examples)- E-commerce Customer Support
- Personalized Learning Platform
- AI Financial Advisor

```
instructions = """
Extract customer service information for better support:

1. Product Issues:
   - Product names, SKUs, defects
   - Return/exchange requests
   - Quality complaints

2. Customer Preferences:
   - Preferred brands, sizes, colors
   - Shopping frequency and habits
   - Price sensitivity

3. Service Experience:
   - Satisfaction with support
   - Resolution time expectations
   - Communication preferences

Exclude: Payment card numbers, passwords, personal identifiers.
"""

client.project.update(custom_instructions=instructions)

```

## ​Advanced Techniques
[​](https://docs.mem0.ai/platform/features/custom-instructions#advanced-techniques)
### ​Conditional Processing
[​](https://docs.mem0.ai/platform/features/custom-instructions#conditional-processing)
```
advanced_prompt = """
Extract information based on conversation context:

IF customer support conversation:
- Issue type, severity, resolution status
- Customer satisfaction indicators

IF sales conversation:
- Product interests, budget range
- Decision timeline and influencers

IF onboarding conversation:
- User experience level
- Feature interests and priorities

Always exclude personal identifiers and maintain professional context.
"""

client.project.update(custom_instructions=advanced_prompt)

```

### ​Testing Your Instructions
[​](https://docs.mem0.ai/platform/features/custom-instructions#testing-your-instructions)
```
# Test with sample messages
messages = [
    {"role": "user", "content": "I'm having billing issues with my subscription"},
    {"role": "assistant", "content": "I can help with that. What's the specific problem?"},
    {"role": "user", "content": "I'm being charged twice each month"}
]

# Add the messages and check extracted memories
result = client.add(messages, user_id="test_user")
memories = client.get_all(user_id="test_user")

# Review if the right information was extracted
for memory in memories:
    print(f"Extracted: {memory['memory']}")

```

## ​Best Practices
[​](https://docs.mem0.ai/platform/features/custom-instructions#best-practices)
### ​✅ Do
[​](https://docs.mem0.ai/platform/features/custom-instructions#%E2%9C%85-do)- Be specificabout what information to extract
- Use clear categoriesto organize your instructions
- Test with real conversationsbefore deploying
- Explicitly state exclusionsfor privacy and compliance
- Start simpleand iterate based on results

### ​❌ Don’t
[​](https://docs.mem0.ai/platform/features/custom-instructions#%E2%9D%8C-don%E2%80%99t)- Make instructions too long or complex
- Create conflicting rules within your guidelines
- Be overly restrictive (balance specificity with flexibility)
- Forget to exclude sensitive information
- Skip testing with diverse conversation examples

## ​Common Issues and Solutions
[​](https://docs.mem0.ai/platform/features/custom-instructions#common-issues-and-solutions)