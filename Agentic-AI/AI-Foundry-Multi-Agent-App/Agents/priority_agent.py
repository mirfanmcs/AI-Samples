# Priority agent definition.
# This agent sets the priority level of each ticket.

from azure.ai.agents.models import ConnectedAgentTool

def create_priority_agent(agents_client, deployment):
    priority_agent_name = "priority_agent"
    priority_agent_instructions = """
    Assess how urgent a ticket is based on its description.

    Respond with one of the following levels:
    - High: User-facing or blocking issues
    - Medium: Time-sensitive but not breaking anything
    - Low: Cosmetic or non-urgent tasks

    Only output the urgency level and a very brief explanation.
    """
    
    # Create the Priority agent on the Azure AI agent service. You can use custom tools if you want.
    priority_agent = agents_client.create_agent(
        model=deployment,
        name=priority_agent_name,
        instructions=priority_agent_instructions
    )

    # Create a connected agent tool for the Priority agent
    priority_agent_tool = ConnectedAgentTool(
        id=priority_agent.id,
        name=priority_agent_name,
        description="Assess the priority of a ticket"
    )
    return priority_agent, priority_agent_tool
