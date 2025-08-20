# This code is using Azure AI Foundry Python SDK

import os
import asyncio
from dotenv import load_dotenv
from pathlib import Path
from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from plugins.email_plugin import EmailPlugin

async def main():
    
    # Display the data to be analyzed
    # Use this data for grounding.
    script_dir = Path(__file__).parent  # Get the directory of the script
    file_path = script_dir / 'data.txt'

    with file_path.open('r') as file:
        data = file.read() + "\n"

    # Run the async agent code
    await process_expenses_data (data)

async def process_expenses_data(expenses_data):

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
        
        # Define an Azure AI agent definition that sends an expense claim email
        expenses_agent_definition = await project_client.agents.create_agent(
        model= ai_agent_settings.model_deployment_name,
        name="expenses_agent",
        instructions="""You are an AI assistant for expense claim submission.
                        When a user submits expenses data and requests an expense claim, use the plug-in function to send an email to expenses@contoso.com with the subject 'Expense Claim`and a body that contains itemized expenses with a total.
                        Then confirm to the user that you've done so."""
)

        # Create a semantic kernel agent
        expenses_agent = AzureAIAgent(
            client=project_client,
            definition=expenses_agent_definition,
            plugins=[EmailPlugin()]
        )

        # Use the agent to process the expenses data
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
            # Use the agent to process the expenses data
            # If no thread is provided, a new thread will be
            # created and returned with the initial response
            thread: AzureAIAgentThread | None = None
            try:
                # Add the input prompt to a list of messages to be submitted
                prompt_messages = [f"{input_text}: {expenses_data}"]
                # Invoke the agent for the specified thread with the messages
                response = await expenses_agent.get_response(prompt_messages, thread=thread)
                # Display the response
                print(f"\n# {response.name}:\n{response}")
            except Exception as e:
                # Something went wrong
                print (e)
            finally:
                # Cleanup: Delete the thread and agent
                await thread.delete() if thread else None
                await project_client.agents.delete_agent(expenses_agent.id)





if __name__ == "__main__":
    asyncio.run(main())


# Use these prompts:
#  Submit an expense claim
