# Voice-First AI Companion - Mem0
Source: https://docs.mem0.ai/cookbooks/companions/voice-companion-openai
Downloaded: 2025-11-12 21:20:21
================================================================================


## ​Prerequisites
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#prerequisites)- Installed OpenAI Agents SDK with voice dependencies:

```
pip install 'openai-agents[voice]'

```
- Installed Mem0 SDK:

```
pip install mem0ai

```
- Installed other required dependencies:

```
pip install numpy sounddevice pydantic

```
- Set up your API keys:OpenAI API key for the Agents SDKMem0 API key from the Mem0 Platform
- OpenAI API key for the Agents SDK
- Mem0 API key from the Mem0 Platform

## ​Code Breakdown
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#code-breakdown)
### ​1. Setting Up Dependencies and Environment
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#1-setting-up-dependencies-and-environment)
```
# OpenAI Agents SDK imports
from agents import (
    Agent,
    function_tool
)
from agents.voice import (
    AudioInput,
    SingleAgentVoiceWorkflow,
    VoicePipeline
)
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions

# Mem0 imports
from mem0 import AsyncMemoryClient

# Set up API keys (replace with your actual keys)
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["MEM0_API_KEY"] = "your-mem0-api-key"

# Define a global user ID for simplicity
USER_ID = "voice_user"

# Initialize Mem0 client
mem0_client = AsyncMemoryClient()

```
- Importing required modules from OpenAI Agents SDK and Mem0
- Setting up environment variables for API keys
- Defining a simple user identification system (using a global variable)
- Initializing the Mem0 client that will handle memory operations

### ​2. Memory Tools with Function Decorators
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#2-memory-tools-with-function-decorators)`@function_tool`
#### ​Storing User Memories
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#storing-user-memories)
```
import logging

# Set up logging at the top of your file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger("memory_voice_agent")

# Then use logger in your function tools
@function_tool
async def save_memories(
    memory: str
) -> str:
    """Store a user memory in memory."""
    # This will be visible in your console
    logger.debug(f"Saving memory: {memory} for user {USER_ID}")
    
    # Store the preference in Mem0
    memory_content = f"User memory - {memory}"
    await mem0_client.add(
        memory_content,
        user_id=USER_ID,
    )

    return f"I've saved your memory: {memory}"

```
- Takes a memory string
- Creates a formatted memory string
- Stores it in Mem0 using theadd()method
`add()`- Includes metadata to categorize the memory for easier retrieval
- Returns a confirmation message that the agent will speak

#### ​Finding Relevant Memories
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#finding-relevant-memories)
```
@function_tool
async def search_memories(
    query: str
) -> str:
    """
    Find memories relevant to the current conversation.
    Args:
        query: The search query to find relevant memories
    """
    print(f"Finding memories related to: {query}")
    results = await mem0_client.search(
        query,
        user_id=USER_ID,
        limit=5,
        threshold=0.7,  # Higher threshold for more relevant results
        
    )
    
    # Format and return the results
    if not results.get('results', []):
        return "I don't have any relevant memories about this topic."
    
    memories = [f"• {result['memory']}" for result in results.get('results', [])]
    return "Here's what I remember that might be relevant:\n" + "\n".join(memories)

```
- Takes a search query string
- Passes it to Mem0’s semantic search to find related memories
- Sets a threshold for relevance to ensure quality results
- Returns a formatted list of relevant memories or a default message

### ​3. Creating the Voice Agent
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#3-creating-the-voice-agent)
```
def create_memory_voice_agent():
    # Create the agent with memory-enabled tools
    agent = Agent(
        name="Memory Assistant",
        instructions=prompt_with_handoff_instructions(
            """You're speaking to a human, so be polite and concise.
            Always respond in clear, natural English.
            You have the ability to remember information about the user.
            Use the save_memories tool when the user shares an important information worth remembering.
            Use the search_memories tool when you need context from past conversations or user asks you to recall something.
            """,
        ),
        model="gpt-4.1-nano-2025-04-14",
        tools=[save_memories, search_memories],
    )
    
    return agent

```
- Creates an OpenAI Agent with specific instructions
- Configures it to use gpt-4.1-nano (you can use other models)
- Registers the memory-related tools with the agent
- Usesprompt_with_handoff_instructionsto include standard voice agent behaviors
`prompt_with_handoff_instructions`
### ​4. Microphone Recording Functionality
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#4-microphone-recording-functionality)
```
async def record_from_microphone(duration=5, samplerate=24000):
    """Record audio from the microphone for a specified duration."""
    print(f"Recording for {duration} seconds...")
    
    # Create a buffer to store the recorded audio
    frames = []
    
    # Callback function to store audio data
    def callback(indata, frames_count, time_info, status):
        frames.append(indata.copy())
    
    # Start recording
    with sd.InputStream(samplerate=samplerate, channels=1, callback=callback, dtype=np.int16):
        await asyncio.sleep(duration)
    
    # Combine all frames into a single numpy array
    audio_data = np.concatenate(frames)
    return audio_data

```
- Creates a simple asynchronous microphone recording function
- Uses the sounddevice library to capture audio input
- Stores frames in a buffer during recording
- Combines frames into a single numpy array when complete
- Returns the audio data for processing

### ​5. Main Loop and Voice Processing
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#5-main-loop-and-voice-processing)
```
async def main():
    # Create the agent
    agent = create_memory_voice_agent()
    
    # Set up the voice pipeline
    pipeline = VoicePipeline(
        workflow=SingleAgentVoiceWorkflow(agent)
    )
    
    # Configure TTS settings
    pipeline.config.tts_settings.voice = "alloy"
    pipeline.config.tts_settings.speed = 1.0
    
    try:
        while True:
            # Get user input
            print("\nPress Enter to start recording (or 'q' to quit)...")
            user_input = input()
            if user_input.lower() == 'q':
                break
            
            # Record and process audio
            audio_data = await record_from_microphone(duration=5)
            audio_input = AudioInput(buffer=audio_data)
            result = await pipeline.run(audio_input)
            
            # Play response and handle events
            player = sd.OutputStream(samplerate=24000, channels=1, dtype=np.int16)
            player.start()
            
            agent_response = ""
            print("\nAgent response:")
            
            async for event in result.stream():
                if event.type == "voice_stream_event_audio":
                    player.write(event.data)
                elif event.type == "voice_stream_event_content":
                    content = event.data
                    agent_response += content
                    print(content, end="", flush=True)
            
            # Save the agent's response to memory
            if agent_response:
                try:
                    await mem0_client.add(
                        f"Agent response: {agent_response}", 
                        user_id=USER_ID,
                        metadata={"type": "agent_response"}
                    )
                except Exception as e:
                    print(f"Failed to store memory: {e}")
    
    except KeyboardInterrupt:
        print("\nExiting...")

```
- Creates the memory-enabled voice agent
- Sets up the voice pipeline with TTS settings
- Implements an interactive loop for recording and processing voice input
- Handles streaming of response events (both audio and text)
- Automatically saves the agent’s responses to memory
- Includes proper error handling and exit mechanisms

## ​Create a Memory-Enabled Voice Agent
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#create-a-memory-enabled-voice-agent)
```
import asyncio
import os
import logging
from typing import Optional, List, Dict, Any
import numpy as np
import sounddevice as sd
from pydantic import BaseModel

# OpenAI Agents SDK imports
from agents import (
    Agent,
    function_tool
)
from agents.voice import (
    AudioInput,
    SingleAgentVoiceWorkflow,
    VoicePipeline
)
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions

# Mem0 imports
from mem0 import AsyncMemoryClient

# Set up API keys (replace with your actual keys)
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["MEM0_API_KEY"] = "your-mem0-api-key"

# Define a global user ID for simplicity
USER_ID = "voice_user"

# Initialize Mem0 client
mem0_client = AsyncMemoryClient()

# Create tools that utilize Mem0's memory
@function_tool
async def save_memories(
    memory: str
) -> str:
    """
    Store a user memory in memory.
    Args:
        memory: The memory to save
    """
    print(f"Saving memory: {memory} for user {USER_ID}")

    # Store the preference in Mem0
    memory_content = f"User memory - {memory}"
    await mem0_client.add(
        memory_content,
        user_id=USER_ID,
    )

    return f"I've saved your memory: {memory}"

@function_tool
async def search_memories(
    query: str
) -> str:
    """
    Find memories relevant to the current conversation.
    Args:
        query: The search query to find relevant memories
    """
    print(f"Finding memories related to: {query}")
    results = await mem0_client.search(
        query,
        user_id=USER_ID,
        limit=5,
        threshold=0.7,  # Higher threshold for more relevant results
        
    )
    
    # Format and return the results
    if not results.get('results', []):
        return "I don't have any relevant memories about this topic."
    
    memories = [f"• {result['memory']}" for result in results.get('results', [])]
    return "Here's what I remember that might be relevant:\n" + "\n".join(memories)

# Create the agent with memory-enabled tools
def create_memory_voice_agent():
    # Create the agent with memory-enabled tools
    agent = Agent(
        name="Memory Assistant",
        instructions=prompt_with_handoff_instructions(
            """You're speaking to a human, so be polite and concise.
            Always respond in clear, natural English.
            You have the ability to remember information about the user.
            Use the save_memories tool when the user shares an important information worth remembering.
            Use the search_memories tool when you need context from past conversations or user asks you to recall something.
            """,
        ),
        model="gpt-4.1-nano-2025-04-14",
        tools=[save_memories, search_memories],
    )
    
    return agent

async def record_from_microphone(duration=5, samplerate=24000):
    """Record audio from the microphone for a specified duration."""
    print(f"Recording for {duration} seconds...")
    
    # Create a buffer to store the recorded audio
    frames = []
    
    # Callback function to store audio data
    def callback(indata, frames_count, time_info, status):
        frames.append(indata.copy())
    
    # Start recording
    with sd.InputStream(samplerate=samplerate, channels=1, callback=callback, dtype=np.int16):
        await asyncio.sleep(duration)
    
    # Combine all frames into a single numpy array
    audio_data = np.concatenate(frames)
    return audio_data

async def main():
    print("Starting Memory Voice Agent")
    
    # Create the agent and context
    agent = create_memory_voice_agent()
    
    # Set up the voice pipeline
    pipeline = VoicePipeline(
        workflow=SingleAgentVoiceWorkflow(agent)
    )
    
    # Configure TTS settings
    pipeline.config.tts_settings.voice = "alloy"
    pipeline.config.tts_settings.speed = 1.0
    
    try:
        while True:
            # Get user input
            print("\nPress Enter to start recording (or 'q' to quit)...")
            user_input = input()
            if user_input.lower() == 'q':
                break
            
            # Record and process audio
            audio_data = await record_from_microphone(duration=5)
            audio_input = AudioInput(buffer=audio_data)
            
            print("Processing your request...")
            
            # Process the audio input
            result = await pipeline.run(audio_input)
            
            # Create an audio player
            player = sd.OutputStream(samplerate=24000, channels=1, dtype=np.int16)
            player.start()
            
            # Store the agent's response for adding to memory
            agent_response = ""
            
            print("\nAgent response:")
            # Play the audio stream as it comes in
            async for event in result.stream():
                if event.type == "voice_stream_event_audio":
                    player.write(event.data)
                elif event.type == "voice_stream_event_content":
                    # Accumulate and print the text response
                    content = event.data
                    agent_response += content
                    print(content, end="", flush=True)
            
            print("\n")
            
            # Example of saving the conversation to Mem0 after completion
            if agent_response:
                try:
                    await mem0_client.add(
                        f"Agent response: {agent_response}", 
                        user_id=USER_ID,
                        metadata={"type": "agent_response"}
                    )
                except Exception as e:
                    print(f"Failed to store memory: {e}")
    
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    asyncio.run(main())

```

## ​Key Features of This Implementation
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#key-features-of-this-implementation)- Simplified User Management: Uses a globalUSER_IDvariable for simplicity, but can be extended to manage multiple users.
`USER_ID`- Real Microphone Input: Includes arecord_from_microphone()function that captures actual voice input from your microphone.
`record_from_microphone()`- Interactive Voice Loop: Implements a continuous interaction loop, allowing for multiple back-and-forth exchanges.
- Memory Management Tools:save_memories: Stores user memories in Mem0search_memories: Searches for relevant past information
- save_memories: Stores user memories in Mem0
`save_memories`- search_memories: Searches for relevant past information
`search_memories`- Voice Configuration: Demonstrates how to configure TTS settings for the voice response.

## ​Running the Example
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#running-the-example)- Replace the placeholder API keys with your actual keys
- Make sure your microphone is properly connected
- Run the script with Python 3.8 or newer
- Press Enter to start recording, then speak your request
- Press ‘q’ to quit the application

## ​Best Practices for Voice Agents with Memory
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#best-practices-for-voice-agents-with-memory)- Optimizing Memory for Voice: Keep memories concise and relevant for voice responses.
- Forgetting Mechanism: Implement a way to delete or expire memories that are no longer relevant.
- Context Preservation: Store enough context with each memory to make retrieval effective.
- Error Handling: Implement robust error handling for memory operations, as voice interactions should continue smoothly even if memory operations fail.

## ​Conclusion
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#conclusion)
## ​Debugging Function Tools
[​](https://docs.mem0.ai/cookbooks/companions/voice-companion-openai#debugging-function-tools)`print()``@function_tool``logging`
```
import logging

# Set up logging at the top of your file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger("memory_voice_agent")

# Then use logger in your function tools
@function_tool
async def save_memories(
    memory: str
) -> str:
    """Store a user memory in memory."""
    # This will be visible in your console
    logger.debug(f"Saving memory: {memory} for user {USER_ID}")

    # Rest of your function...

```
[Multimodal SupportLearn how to add vision and audio memory alongside voice interactions.](https://docs.mem0.ai/platform/features/multimodal-support)
## Multimodal Support
[Build a Mem0 CompanionMaster the core patterns for building memory-powered companions.](https://docs.mem0.ai/cookbooks/essentials/building-ai-companion)
## Build a Mem0 Companion
