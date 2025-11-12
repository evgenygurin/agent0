# FAQs - Mem0
Source: https://docs.mem0.ai/platform/faqs
Downloaded: 2025-11-12 21:20:18
================================================================================


How does Mem0 work?
`add``search`
What are the key features of Mem0?
- User, Session, and AI Agent Memory: Retains information across sessions and interactions for users and AI agents, ensuring continuity and context.
- Adaptive Personalization: Continuously updates memories based on user interactions and feedback.
- Developer-Friendly API: Offers a straightforward API for seamless integration into various applications.
- Platform Consistency: Ensures consistent behavior and data across different platforms and devices.
- Managed Service: Provides a hosted solution for easy deployment and maintenance.
- Cost Savings: Saves costs by adding relevant memories instead of complete transcripts to context window

How is Mem0 different from traditional RAG?
- Entity Relationships: Mem0 can understand and relate entities across different interactions, unlike RAG which retrieves information from static documents. This leads to a deeper understanding of context and relationships.
- Contextual Continuity: Mem0 retains information across sessions, maintaining continuity in conversations and interactions, which is essential for long-term engagement applications like virtual companions or personalized learning assistants.
- Adaptive Learning: Mem0 improves its personalization based on user interactions and feedback, making the memory more accurate and tailored to individual users over time.
- Dynamic Updates: Mem0 can dynamically update its memory with new information and interactions, unlike RAG which relies on static data. This allows for real-time adjustments and improvements, enhancing the user experience.

What are the common use-cases of Mem0?
- Personalized Learning Assistants: Long-term memory allows learning assistants to remember user preferences, strengths and weaknesses, and progress, providing a more tailored and effective learning experience.
- Customer Support AI Agents: By retaining information from previous interactions, customer support bots can offer more accurate and context-aware assistance, improving customer satisfaction and reducing resolution times.
- Healthcare Assistants: Long-term memory enables healthcare assistants to keep track of patient history, medication schedules, and treatment plans, ensuring personalized and consistent care.
- Virtual Companions: Virtual companions can use long-term memory to build deeper relationships with users by remembering personal details, preferences, and past conversations, making interactions more delightful.
- Productivity Tools: Long-term memory helps productivity tools remember user habits, frequently used documents, and task history, streamlining workflows and enhancing efficiency.
- Gaming AI: In gaming, AI with long-term memory can create more immersive experiences by remembering player choices, strategies, and progress, adapting the game environment accordingly.

Why aren't my memories being created?
- When users input definitional questions (e.g., “What is backpropagation?”)
- For general concept explanations that don’t contain personal or experiential information
- Technical definitions and theoretical explanations
- General knowledge statements without personal context
- Abstract or theoretical content

```
Input: "What is machine learning?"
No memories extracted - Content is definitional and does not meet memory classification criteria.

Input: "Yesterday I learned about machine learning in class"
Memory extracted - Contains personal experience and temporal context.

```
- Include temporal markers (when events occurred)
- Add personal context or experiences
- Frame information in terms of real-world applications or experiences
- Include specific examples or cases rather than general definitions

How do I configure Mem0 for AWS Lambda?
`/tmp``MEM0_DIR``/tmp`
```
MEM0_DIR=/tmp/.mem0

```

```
# Change from
home_dir = os.path.expanduser("~")
mem0_dir = os.environ.get("MEM0_DIR") or os.path.join(home_dir, ".mem0")

# To
mem0_dir = os.environ.get("MEM0_DIR", "/tmp/.mem0")

```
`/tmp`
How can I use metadata with Mem0?
`add`- Pre-filtering: Include metadata parameters in your initial search query to narrow down the memory pool
- Post-processing: Retrieve a broader set of memories based on query, then apply metadata filters to refine the results
- Contextual information: Location, time, device type, application state
- User attributes: Preferences, skill levels, demographic information
- Interaction details: Conversation topics, sentiment, urgency levels
- Custom tags: Any domain-specific categorization relevant to your application

How do I disable telemetry in Mem0?
`MEM0_TELEMETRY``False`
```
MEM0_TELEMETRY=False

```

```
import os
os.environ["MEM0_TELEMETRY"] = "False"

```
