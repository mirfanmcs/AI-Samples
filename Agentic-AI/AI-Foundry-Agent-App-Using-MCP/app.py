# This code is using Azure AI Foundry Python SDK

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import McpTool, ToolSet


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

# MCP server configuration
mcp_server_url = "https://learn.microsoft.com/api/mcp"
mcp_server_label = "mslearn"

# Initialize agent MCP tool
mcp_tool = McpTool(
     server_label=mcp_server_label,
     server_url=mcp_server_url,
)
    
mcp_tool.set_approval_mode("never")
    
toolset = ToolSet()
toolset.add(mcp_tool)


with agent_client:

    # Define an agent. Create agent if it doesn't exist.
    agent = agent_client.create_agent(
        model=deployment,
        name="my-mcp-agent",
        instructions="""
     You have access to an MCP server called `microsoft.docs.mcp` - this tool allows you to 
     search through Microsoft's latest official documentation. Use the available MCP tools 
     to answer questions and perform tasks."""
    )
    print(f"Using agent: {agent.name}")

    # Create a thread for the conversation
    thread = agent_client.threads.create()
    print(f"Created thread, ID: {thread.id}")

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
            content=input_text,
        )
        print(f"Created message, ID: {message.id}")

        # Create and process agent run in thread with MCP tools. 
        # Passing the toolset in the agent run gives flexibility to use different MCP Server as needed.
        run = agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id, toolset=toolset)
        print(f"Created run, ID: {run.id}")

        # Check the run status for failures
        if run.status == "failed":
            print(f"Run failed: {run.last_error}")

        
        # Display run steps and tool calls
        run_steps = agent_client.run_steps.list(thread_id=thread.id, run_id=run.id)

        for step in run_steps:
            print(f"Step {step['id']} status: {step['status']}")

            # Check if there are tool calls in the step details
            step_details = step.get("step_details", {})
            tool_calls = step_details.get("tool_calls", [])

            if tool_calls:
                # Display the MCP tool call details
                print("  MCP Tool calls:")
                for call in tool_calls:
                    print(f"    Tool Call ID: {call.get('id')}")
                    print(f"    Type: {call.get('type')}")
                    print(f"    Type: {call.get('name')}")

            print()  # add an extra newline between steps


        # Fetch and log all messages
        messages = agent_client.messages.list(thread_id=thread.id)
        print("\nConversation:")
        print("-" * 50)
        for msg in messages:
            if msg.text_messages:
                last_text = msg.text_messages[-1]
                print(f"{msg.role.upper()}: {last_text.text.value}")
                print("-" * 50)

    # Clean up
    agent_client.delete_agent(agent.id)

    
# Use these prompts:
#   Give me the Azure CLI commands to create an Azure Container App with a managed identity.
