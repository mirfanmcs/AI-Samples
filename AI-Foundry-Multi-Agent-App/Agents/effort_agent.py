# Agent - Effort agent definition
# This agent estimates the effort required to complete each ticket.

from azure.ai.agents.models import ConnectedAgentTool

def create_effort_agent(agents_client, deployment):
    effort_agent_name = "effort_agent"
    effort_agent_instructions = """
    Estimate how much work each ticket will require.

    Use the following scale:
    - Small: Can be completed in a day
    - Medium: 2-3 days of work
    - Large: Multi-day or cross-team effort

    Base your estimate on the complexity implied by the ticket. Respond with the effort level and a brief justification.
    """
    # Create the Effort agent on the Azure AI agent service. You can use custom tools if you want.
    effort_agent = agents_client.create_agent(
        model=deployment,
        name=effort_agent_name,
        instructions=effort_agent_instructions
    )

    # Create a connected agent tool for the Effort agent
    effort_agent_tool = ConnectedAgentTool(
        id=effort_agent.id,
        name=effort_agent_name,
        description="Determines the effort required to complete the ticket"
    )
    return effort_agent, effort_agent_tool
