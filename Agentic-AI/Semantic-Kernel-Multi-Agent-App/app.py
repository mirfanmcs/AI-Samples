# This code is using Azure AI Foundry Python SDK
# This code uses Semantic Kernel Magentic Orchestration

import os
import asyncio
from dotenv import load_dotenv
from pathlib import Path
import shutil
from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents import AgentGroupChat
from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.utils.author_role import AuthorRole
from semantic_kernel.functions.kernel_function_decorator import kernel_function
from plugins.devops_plugin import DevOpsPlugin
from plugins.logfile_plugin import LogFilePlugin
from strategy.selection_strategy import SelectionStrategy
from strategy.temination_strategy import ApprovalTerminationStrategy
from instructions.instructions import (
    INCIDENT_MANAGER_AGENT_NAME,
    INCIDENT_MANAGER_INSTRUCTIONS,
    DEVOPS_ASSISTANT_AGENT_NAME,
    DEVOPS_ASSISTANT_INSTRUCTIONS
)

async def main():

    print("Getting log files...\n")
    script_dir = Path(__file__).parent  # Get the directory of the script
    src_path = script_dir / "sample_logs"
    file_path = script_dir / "logs"
    shutil.copytree(src_path, file_path, dirs_exist_ok=True)

    # Run the async agent code
    await run_agent (file_path)


async def run_agent(file_path):
    # Get configuration settings. Load the config from .env file and set the AI agent configs.
    # Environment variable name should be like this:
    # AZURE_AI_AGENT_ENDPOINT="your_project_endpoint"
    # AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME="your_model_deployment"
    load_dotenv()
    ai_agent_settings = AzureAIAgentSettings()

    # Connect to the Azure AI Foundry project
    async with (
        DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True) as creds,
        AzureAIAgent.create_client(
            credential=creds
        ) as project_client,
    ):
        # Create agents
        incident_manager_agent = await create_incident_manager_agent(project_client, ai_agent_settings)
        devops_assistant_agent = await create_devops_assistant_agent(project_client, ai_agent_settings)
        group_chat_agent = create_group_chat_agent(incident_manager_agent, devops_assistant_agent)
        await process_log_files(group_chat_agent, file_path)

# Create an Azure AI agent definition for Incident Manager agent
# Create a semantic kernel agent for the Azure AI Incident Manager agent
# Use the LogFilePlugin 
async def create_incident_manager_agent(project_client, ai_agent_settings):
    incident_manager_agent_definition = await project_client.agents.create_agent(
        model=ai_agent_settings.model_deployment_name,
        name=INCIDENT_MANAGER_AGENT_NAME,
        instructions=INCIDENT_MANAGER_INSTRUCTIONS
    )
    return AzureAIAgent(
        client=project_client,
        definition=incident_manager_agent_definition,
        plugins=[LogFilePlugin()]
    )

# Create an Azure AI agent definition for DevOps Assistant agent
# Create a semantic kernel agent for the Azure AI DevOps Assistant agent
# Use the DevOpsPlugin 
async def create_devops_assistant_agent(project_client, ai_agent_settings):
    devops_assistant_agent_definition = await project_client.agents.create_agent(
        model=ai_agent_settings.model_deployment_name,
        name=DEVOPS_ASSISTANT_AGENT_NAME,
        instructions=DEVOPS_ASSISTANT_INSTRUCTIONS
    )
    return AzureAIAgent(
        client=project_client,
        definition=devops_assistant_agent_definition,
        plugins=[DevOpsPlugin()]
    )

# Add the agents to a group chat with a custom termination and selection strategy
# In this code, you create an agent group chat object with the incident manager and devops agents. 
# You also define the termination and selection strategies for the chat. 
# Notice that the ApprovalTerminationStrategy is tied to the incident manager agent only, and not the devops agent. 
# This makes the incident manager agent is responsible for signaling the end of the chat. 
# The SelectionStrategy includes all agents that should take a turn in the chat.
# Note that the automatic reset flag will automatically clear the chat when it ends. 
# This way, the agent can continue analyzing the files without the chat history object using too many unnecessary tokens.
def create_group_chat_agent(incident_manager_agent, devops_assistant_agent):
    return AgentGroupChat(
        agents=[incident_manager_agent, devops_assistant_agent],
        termination_strategy=ApprovalTerminationStrategy(
            agents=[incident_manager_agent], 
            maximum_iterations=10, 
            automatic_reset=True
        ),
        selection_strategy=SelectionStrategy(agents=[incident_manager_agent, devops_assistant_agent]),      
    )

# Process log files
async def process_log_files(group_chat_agent, file_path):
    for filename in os.listdir(file_path):
        logfile_msg = ChatMessageContent(role=AuthorRole.USER, content=f"USER > {file_path}/{filename}")
        await asyncio.sleep(30) # Wait to reduce TPM
        print(f"\nReady to process log file: {filename}\n")

        # Append the current log file to the chat
        await group_chat_agent.add_chat_message(logfile_msg)
        print()

        try:
            print()
            # Invoke a response from the agents
            async for response in group_chat_agent.invoke():
                if response is None or not response.name:
                    continue
                print(f"{response.content}")
        except Exception as e:
            print(f"Error during chat invocation: {e}")
            # If TPM rate exceeded, wait 60 secs
            if "Rate limit is exceeded" in str(e):
                print ("Waiting...")
                await asyncio.sleep(60)
                continue
            else:
                break

        




# Start the app
if __name__ == "__main__":
    asyncio.run(main())


