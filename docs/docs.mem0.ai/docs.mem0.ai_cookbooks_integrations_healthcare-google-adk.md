# Healthcare Coach with ADK - Mem0
Source: https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Overview
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#overview)- Remembering their medical history and symptoms
- Providing general health information
- Scheduling appointment reminders
- Maintaining a personalized experience across conversations

## ​Setup
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#setup)
```
pip install google-adk mem0ai python-dotenv

```

## ​Code Breakdown
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#code-breakdown)
```
# Import dependencies
import os
import asyncio
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from mem0 import MemoryClient
from dotenv import load_dotenv

load_dotenv()

# Set up environment variables
# os.environ["GOOGLE_API_KEY"] = "your-google-api-key"
# os.environ["MEM0_API_KEY"] = "your-mem0-api-key"

# Define a global user ID for simplicity
USER_ID = "Alex"

# Initialize Mem0 client
mem0 = MemoryClient()

```

## ​Define Memory Tools
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#define-memory-tools)
```
def save_patient_info(information: str) -> dict:
    """Saves important patient information to memory."""

    # Store in Mem0
    response = mem0_client.add(
        [{"role": "user", "content": information}],
        user_id=USER_ID,
        run_id="healthcare_session",
        metadata={"type": "patient_information"}
    )


def retrieve_patient_info(query: str) -> dict:
    """Retrieves relevant patient information from memory."""

    # Search Mem0
    results = mem0_client.search(
        query,
        user_id=USER_ID,
        limit=5,
        threshold=0.7  # Higher threshold for more relevant results
    )

    # Format and return the results
    if results and len(results) > 0:
        memories = [memory["memory"] for memory in results.get('results', [])]
        return {
            "status": "success",
            "memories": memories,
            "count": len(memories)
        }
    else:
        return {
            "status": "no_results",
            "memories": [],
            "count": 0
        }

```

## ​Define Healthcare Tools
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#define-healthcare-tools)
```
def schedule_appointment(date: str, time: str, reason: str) -> dict:
    """Schedules a doctor's appointment."""
    # In a real app, this would connect to a scheduling system
    appointment_id = f"APT-{hash(date + time) % 10000}"

    return {
        "status": "success",
        "appointment_id": appointment_id,
        "confirmation": f"Appointment scheduled for {date} at {time} for {reason}",
        "message": "Please arrive 15 minutes early to complete paperwork."
    }

```

## ​Create the Healthcare Assistant Agent
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#create-the-healthcare-assistant-agent)
```
# Create the agent
healthcare_agent = Agent(
    name="healthcare_assistant",
    model="gemini-1.5-flash",  # Using Gemini for healthcare assistant
    description="Healthcare assistant that helps patients with health information and appointment scheduling.",
    instruction="""You are a helpful Healthcare Assistant with memory capabilities.

Your primary responsibilities are to:
1. Remember patient information using the 'save_patient_info' tool when they share symptoms, conditions, or preferences.
2. Retrieve past patient information using the 'retrieve_patient_info' tool when relevant to the current conversation.
3. Help schedule appointments using the 'schedule_appointment' tool.

IMPORTANT GUIDELINES:
- Always be empathetic, professional, and helpful.
- Save important patient information like symptoms, conditions, allergies, and preferences.
- Check if you have relevant patient information before asking for details they may have shared previously.
- Make it clear you are not a doctor and cannot provide medical diagnosis or treatment.
- For serious symptoms, always recommend consulting a healthcare professional.
- Keep all patient information confidential.
""",
    tools=[save_patient_info, retrieve_patient_info, schedule_appointment]
)

```

## ​Set Up Session and Runner
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#set-up-session-and-runner)
```
# Set up Session Service and Runner
session_service = InMemorySessionService()

# Define constants for the conversation
APP_NAME = "healthcare_assistant_app"
USER_ID = "Alex"
SESSION_ID = "session_001"

# Create a session
session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)

# Create the runner
runner = Runner(
    agent=healthcare_agent,
    app_name=APP_NAME,
    session_service=session_service
)

```

## ​Interact with the Healthcare Assistant
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#interact-with-the-healthcare-assistant)
```
# Function to interact with the agent
async def call_agent_async(query, runner, user_id, session_id):
    """Sends a query to the agent and returns the final response."""
    print(f"\n>>> Patient: {query}")

    # Format the user's message
    content = types.Content(
        role='user',
        parts=[types.Part(text=query)]
    )

    # Set user_id for tools to access
    save_patient_info.user_id = user_id
    retrieve_patient_info.user_id = user_id

    # Run the agent
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                response = event.content.parts[0].text
                print(f"<<< Assistant: {response}")
                return response

    return "No response received."

# Example conversation flow
async def run_conversation():
    # First interaction - patient introduces themselves with key information
    await call_agent_async(
        "Hi, I'm Alex. I've been having headaches for the past week, and I have a penicillin allergy.",
        runner=runner,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    # Request for health information
    await call_agent_async(
        "Can you tell me more about what might be causing my headaches?",
        runner=runner,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    # Schedule an appointment
    await call_agent_async(
        "I think I should see a doctor. Can you help me schedule an appointment for next Monday at 2pm?",
        runner=runner,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    # Test memory - should remember patient name, symptoms, and allergy
    await call_agent_async(
        "What medications should I avoid for my headaches?",
        runner=runner,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

# Run the conversation example
if __name__ == "__main__":
    asyncio.run(run_conversation())

```

## ​How It Works
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#how-it-works)- Memory Storage: When Alex mentions her headaches and penicillin allergy, the agent stores this information in Mem0 using thesave_patient_infotool.
`save_patient_info`- Contextual Retrieval: When Alex asks about headache causes, the agent uses theretrieve_patient_infotool to recall her specific situation.
`retrieve_patient_info`- Memory Application: When discussing medications, the agent remembers Alex’s penicillin allergy without her needing to repeat it, providing safer and more personalized advice.
- Conversation Continuity: The agent maintains context across the entire conversation session, creating a more natural and efficient interaction.

## ​Key Implementation Details
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#key-implementation-details)
## ​User ID Management
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#user-id-management)
```
# Set user_id for tools to access
save_patient_info.user_id = user_id
retrieve_patient_info.user_id = user_id

```

```
# Get user_id from session state or use default
user_id = getattr(save_patient_info, 'user_id', 'default_user')

```

## ​Mem0 Integration
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#mem0-integration)- mem0_client.add()- Stores new information with appropriate metadata
`mem0_client.add()`- mem0_client.search()- Retrieves relevant memories using semantic search
`mem0_client.search()``threshold`
## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/integrations/healthcare-google-adk#conclusion)[Tag and Organize MemoriesCategorize patient data by symptoms, history, and visit context.](https://docs.mem0.ai/cookbooks/essentials/tagging-and-organizing-memories)
## Tag and Organize Memories
[Support Inbox with Mem0Apply similar memory patterns to customer support workflows.](https://docs.mem0.ai/cookbooks/operations/support-inbox)
## Support Inbox with Mem0
