# Multi-Agent Collaboration - Mem0
Source: https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#overview)- LlamaIndex AgentWorkflowfor multi-agent orchestration
- Mem0for persistent, shared memory across agents
- Multiple agentsthat collaborate on teaching tasks
- TutorAgent: Primary instructor for explanations and concept teaching
- PracticeAgent: Generates exercises and tracks learning progress

## ​Key Features
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#key-features)- Persistent Memory: Agents remember previous interactions across sessions
- Multi-Agent Collaboration: Agents can hand off tasks to each other
- Personalized Learning: Adapts to individual student needs and learning styles
- Progress Tracking: Monitors learning patterns and skill development
- Memory-Driven Teaching: References past struggles and successes

## ​Prerequisites
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#prerequisites)
```
pip install llama-index-core llama-index-memory-mem0 openai python-dotenv

```
- MEM0_API_KEY: Your Mem0 Platform API key
`MEM0_API_KEY`- OPENAI_API_KEY: Your OpenAI API key
`OPENAI_API_KEY`[Mem0 Platform](https://app.mem0.ai)
## ​Complete Implementation
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#complete-implementation)
```
"""
Multi-Agent Personal Learning System: Mem0 + LlamaIndex AgentWorkflow Example

INSTALLATIONS:
!pip install llama-index-core llama-index-memory-mem0 openai

You need MEM0_API_KEY and OPENAI_API_KEY to run the example.
"""

import asyncio
from datetime import datetime
from dotenv import load_dotenv

# LlamaIndex imports
from llama_index.core.agent.workflow import AgentWorkflow, FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool

# Memory integration
from llama_index.memory.mem0 import Mem0Memory

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()


class MultiAgentLearningSystem:
    """
    Multi-Agent Architecture:
    - TutorAgent: Main teaching and explanations
    - PracticeAgent: Exercises and skill reinforcement
    - Shared Memory: Both agents learn from student interactions
    """

    def __init__(self, student_id: str):
        self.student_id = student_id
        self.llm = OpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.2)

        # Memory context for this student
        self.memory_context = {"user_id": student_id, "app": "learning_assistant"}
        self.memory = Mem0Memory.from_client(
            context=self.memory_context
        )

        self._setup_agents()

    def _setup_agents(self):
        """Setup two agents that work together and share memory"""

        # TOOLS
        async def assess_understanding(topic: str, student_response: str) -> str:
            """Assess student's understanding of a topic and save insights"""
            # Simulate assessment logic
            if "confused" in student_response.lower() or "don't understand" in student_response.lower():
                assessment = f"STRUGGLING with {topic}: {student_response}"
                insight = f"Student needs more help with {topic}. Prefers step-by-step explanations."
            elif "makes sense" in student_response.lower() or "got it" in student_response.lower():
                assessment = f"UNDERSTANDS {topic}: {student_response}"
                insight = f"Student grasped {topic} quickly. Can move to advanced concepts."
            else:
                assessment = f"PARTIAL understanding of {topic}: {student_response}"
                insight = f"Student has basic understanding of {topic}. Needs reinforcement."

            return f"Assessment: {assessment}\nInsight saved: {insight}"

        async def track_progress(topic: str, success_rate: str) -> str:
            """Track learning progress and identify patterns"""
            progress_note = f"Progress on {topic}: {success_rate} - {datetime.now().strftime('%Y-%m-%d')}"
            return f"Progress tracked: {progress_note}"

        # Convert to FunctionTools
        tools = [
            FunctionTool.from_defaults(async_fn=assess_understanding),
            FunctionTool.from_defaults(async_fn=track_progress)
        ]

        # AGENTS
        # Tutor Agent - Main teaching and explanation
        self.tutor_agent = FunctionAgent(
            name="TutorAgent",
            description="Primary instructor that explains concepts and adapts to student needs",
            system_prompt="""
            You are a patient, adaptive programming tutor. Your key strength is REMEMBERING and BUILDING on previous interactions.

            Key Behaviors:
            1. Always check what the student has learned before (use memory context)
            2. Adapt explanations based on their preferred learning style
            3. Reference previous struggles or successes
            4. Build progressively on past lessons
            5. Use assess_understanding to evaluate responses and save insights

            MEMORY-DRIVEN TEACHING:
            - "Last time you struggled with X, so let's approach Y differently..."
            - "Since you prefer visual examples, here's a diagram..."
            - "Building on the functions we covered yesterday..."

            When student shows understanding, hand off to PracticeAgent for exercises.
            """,
            tools=tools,
            llm=self.llm,
            can_handoff_to=["PracticeAgent"]
        )

        # Practice Agent - Exercises and reinforcement
        self.practice_agent = FunctionAgent(
            name="PracticeAgent",
            description="Creates practice exercises and tracks progress based on student's learning history",
            system_prompt="""
            You create personalized practice exercises based on the student's learning history and current level.

            Key Behaviors:
            1. Generate problems that match their skill level (from memory)
            2. Focus on areas they've struggled with previously
            3. Gradually increase difficulty based on their progress
            4. Use track_progress to record their performance
            5. Provide encouraging feedback that references their growth

            MEMORY-DRIVEN PRACTICE:
            - "Let's practice loops again since you wanted more examples..."
            - "Here's a harder version of the problem you solved yesterday..."
            - "You've improved a lot in functions, ready for the next level?"

            After practice, can hand back to TutorAgent for concept review if needed.
            """,
            tools=tools,
            llm=self.llm,
            can_handoff_to=["TutorAgent"]
        )

        # Create the multi-agent workflow
        self.workflow = AgentWorkflow(
            agents=[self.tutor_agent, self.practice_agent],
            root_agent=self.tutor_agent.name,
            initial_state={
                "current_topic": "",
                "student_level": "beginner",
                "learning_style": "unknown",
                "session_goals": []
            }
        )

    async def start_learning_session(self, topic: str, student_message: str = "") -> str:
        """
        Start a learning session with multi-agent memory-aware teaching
        """

        if student_message:
            request = f"I want to learn about {topic}. {student_message}"
        else:
            request = f"I want to learn about {topic}."

        # The magic happens here - multi-agent memory is automatically shared!
        response = await self.workflow.run(
            user_msg=request,
            memory=self.memory
        )

        return str(response)

    async def get_learning_history(self) -> str:
        """Show what the system remembers about this student"""
        try:
            # Search memory for learning patterns
            memories = self.memory.search(
                user_id=self.student_id,
                query="learning machine learning"
            )

            if memories and memories.get('results'):
                history = "\n".join(f"- {m['memory']}" for m in memories['results'])
                return history
            else:
                return "No learning history found yet. Let's start building your profile!"

        except Exception as e:
            return f"Memory retrieval error: {str(e)}"


async def run_learning_agent():

    learning_system = MultiAgentLearningSystem(student_id="Alexander")

    # First session
    print("Session 1:")
    response = await learning_system.start_learning_session(
        "Vision Language Models",
        "I'm new to machine learning but I have good hold on Python and have 4 years of work experience.")
    print(response)

    # Second session - multi-agent memory will remember the first
    print("\nSession 2:")
    response2 = await learning_system.start_learning_session(
        "Machine Learning", "what all did I cover so far?")
    print(response2)

    # Show what the multi-agent system remembers
    print("\nLearning History:")
    history = await learning_system.get_learning_history()
    print(history)


if __name__ == "__main__":
    """Run the example"""
    print("Multi-agent Learning System powered by LlamaIndex and Mem0")

    async def main():
        await run_learning_agent()

    asyncio.run(main())

```

## ​How It Works
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#how-it-works)
### ​1. Memory Context Setup
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#1-memory-context-setup)
```
# Memory context for this student
self.memory_context = {"user_id": student_id, "app": "learning_assistant"}
self.memory = Mem0Memory.from_client(context=self.memory_context)

```

### ​2. Agent Collaboration
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#2-agent-collaboration)
```
# Agents can hand off to each other
can_handoff_to=["PracticeAgent"]  # TutorAgent can hand off to PracticeAgent
can_handoff_to=["TutorAgent"]     # PracticeAgent can hand off back

```

### ​3. Shared Memory
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#3-shared-memory)
```
# Both agents share the same memory instance
response = await self.workflow.run(
    user_msg=request,
    memory=self.memory  # Shared across all agents
)

```

### ​4. Memory-Driven Interactions
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#4-memory-driven-interactions)- Reference previous learning sessions
- Adapt to discovered learning styles
- Build progressively on past lessons
- Track and respond to learning patterns

## ​Running the Example
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#running-the-example)
```
# Initialize the learning system
learning_system = MultiAgentLearningSystem(student_id="Alexander")

# Start a learning session
response = await learning_system.start_learning_session(
    "Vision Language Models",
    "I'm new to machine learning but I have good hold on Python and have 4 years of work experience."
)

# Continue learning in a new session (memory persists)
response2 = await learning_system.start_learning_session(
    "Machine Learning",
    "what all did I cover so far?"
)

# Check learning history
history = await learning_system.get_learning_history()

```

## ​Expected Output
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#expected-output)
```
Session 1:
I understand you want to learn about Vision Language Models and you mentioned you're new to machine learning but have a strong Python background with 4 years of experience. That's a great foundation to build on!

Let me start with an explanation tailored to your programming background...
[Agent provides explanation and may hand off to PracticeAgent for exercises]

Session 2:
Based on our previous session, I remember we covered Vision Language Models and I noted that you have a strong Python background with 4 years of experience. You mentioned being new to machine learning, so we started with foundational concepts...
[Agent references previous session and builds upon it]

```

## ​Key Benefits
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#key-benefits)- Persistent Learning: Agents remember across sessions, creating continuity
- Collaborative Teaching: Multiple specialized agents work together seamlessly
- Personalized Adaptation: System learns and adapts to individual learning styles
- Scalable Architecture: Easy to add more specialized agents
- Memory Efficiency: Shared memory prevents duplication and ensures consistency

## ​Best Practices
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#best-practices)- Clear Agent Roles: Define specific responsibilities for each agent
- Memory Context: Use descriptive context for memory isolation
- Handoff Strategy: Design clear handoff criteria between agents
- Memory Hygiene: Regularly review and clean memory for optimal performance

## ​Help & Resources
[​](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-multiagent#help-%26-resources)- LlamaIndex Agent Workflows
[LlamaIndex Agent Workflows](https://docs.llamaindex.ai/en/stable/use_cases/agents/)- Mem0 Platform
[Mem0 Platform](https://app.mem0.ai/)[LlamaIndex ReAct with Mem0Start with single-agent patterns before scaling to multi-agent systems.](https://docs.mem0.ai/cookbooks/frameworks/llamaindex-react)
## LlamaIndex ReAct with Mem0
[Build AI with PersonalityLearn how to scope memories across multiple agents and users.](https://docs.mem0.ai/cookbooks/essentials/building-ai-with-personality)
## Build AI with Personality
