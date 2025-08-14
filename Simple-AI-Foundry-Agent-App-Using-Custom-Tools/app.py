# This code is using Azure AI Foundry Python SDK

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FunctionTool, ToolSet, ListSortOrder, MessageRole
from user_functions import user_functions


# Load environment variables from .env file
load_dotenv()

endpoint = os.getenv("PROJECT_ENDPOINT", "")            
deployment = os.getenv("MODEL_DEPLOYMENT", "")       



# Use AgentClient to connect to AI Foundry. Use Azure credentials to connect. 
agent_client = AgentsClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential
        (exclude_environment_credential=True,
         exclude_managed_identity_credential=True)
)

with agent_client:

    functions = FunctionTool(user_functions)
    toolset = ToolSet()
    toolset.add(functions)
    agent_client.enable_auto_function_calls(toolset)

     # Define an agent that uses the custom function. Create agent if it doesn't exist.        
    agent = agent_client.create_agent(
        model=deployment,
        name="support-agent",
        instructions="""You are a technical support agent.
                        When a user has a technical issue, you get their email address and a description of the issue.
                        Then you use those values to submit a support ticket using the function available to you.
                        If a file is saved, tell the user the file name.
                     """,
        toolset=toolset
    )

    # Create a thread for the conversation
    thread = agent_client.threads.create()
    print(f"You're chatting with: {agent.name} ({agent.id})")


# Loop until the user types 'quit'
    while True:
        # Get input text
        input_text = input("Enter the prompt (or type 'quit' to exit): ")
        if input_text.lower() == "quit":
            break
        if len(input_text) == 0:
            print("Please enter a prompt.")
            continue



        # Send a prompt to the agent
        message = agent_client.messages.create(
            thread_id=thread.id,
            role="user",
            content=input_text
        )
        run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)

        # Check the run status for failures
        if run.status == "failed":
            print(f"Run failed: {run.last_error}")

        
        # Show the latest response from the agent
        last_msg = agent_client.messages.get_last_message_text_by_role(
            thread_id=thread.id,
            role=MessageRole.AGENT,
        )
        if last_msg:
            print(f"Last Message: {last_msg.text.value}")



    # Get the conversation history
    print("\nConversation Log:\n")
    messages = agent_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
    for message in messages:
        if message.text_messages:
            last_msg = message.text_messages[-1]
            print(f"{message.role}: {last_msg.text.value}\n")

    # Clean up
    agent_client.delete_agent(agent.id)

    
# Use these prompts:
#   I have a technical problem
# View the response. The agent may ask for your email address and a description of the issue.
# The tool should have saved support tickets in the app folder.