# This code is using Azure AI Foundry Python SDK

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import MessageRole, ListSortOrder
from Agents.priority_agent import create_priority_agent
from Agents.team_agent import create_team_agent
from Agents.effort_agent import create_effort_agent


# Load environment variables from .env file
load_dotenv()

endpoint = os.getenv("PROJECT_ENDPOINT", "")
deployment = os.getenv("MODEL_DEPLOYMENT", "")

# Instructions for the main/primary agent
main_agent_instructions = """
Triage the given ticket. Use the connected tools to determine the ticket's priority, 
which team it should be assigned to, and how much effort it may take.
"""

agents_client = AgentsClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential
    (exclude_environment_credential=True, 
     exclude_managed_identity_credential=True)
)
with agents_client:
    
    # Create agents using referenced agent modules
    priority_agent, priority_agent_tool = create_priority_agent(agents_client, deployment)
    team_agent, team_agent_tool = create_team_agent(agents_client, deployment)
    effort_agent, effort_agent_tool = create_effort_agent(agents_client, deployment)

    # Create a main agent with the Connected Agent tools. Use Connected Agent tools as a custom tool.
    main_agent = agents_client.create_agent(
        model=deployment,
        name="main-agent",
        instructions=main_agent_instructions,
        tools=[
            priority_agent_tool.definitions[0],
            team_agent_tool.definitions[0],
            effort_agent_tool.definitions[0]
        ]
    )
    print(f"Using agent: {main_agent.name}")
    thread = agents_client.threads.create()

    # Loop until the user types 'quit'
    while True:
        input_text = input("Enter the prompt (or type 'quit' to exit): ")
        if input_text.lower() == "quit":
            break
        if len(input_text) == 0:
            print("Please enter a prompt.")
            continue
        message = agents_client.messages.create(
            thread_id=thread.id,
            role="user",
            content=input_text,
        )
        run = agents_client.runs.create_and_process(thread_id=thread.id, agent_id=main_agent.id)
        if run.status == "failed":
            print(f"Run failed: {run.last_error}")
        last_msg = agents_client.messages.get_last_message_text_by_role(
            thread_id=thread.id,
            role=MessageRole.AGENT,
        )
        if last_msg:
            print(f"Last Message: {last_msg.text.value}")

    # Get the conversation history
    print("\nConversation Log:\n")
    messages = agents_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
    for message in messages:
        if message.text_messages:
            last_msg = message.text_messages[-1]
            print(f"{message.role}: {last_msg.text.value}\n")

    # Clean up
    agents_client.delete_agent(main_agent.id)
    agents_client.delete_agent(priority_agent.id)
    agents_client.delete_agent(team_agent.id)
    agents_client.delete_agent(effort_agent.id)
    
    # Use these prompts:
    #   Users can't reset their password from the mobile app.
