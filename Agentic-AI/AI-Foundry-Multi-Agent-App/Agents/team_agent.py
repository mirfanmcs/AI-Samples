# Agent - Team allocation agent definition
# This agent decides which team should own each ticket.

from azure.ai.agents.models import ConnectedAgentTool

def create_team_agent(agents_client, deployment):
    team_agent_name = "team_agent"
    team_agent_instructions = """
    Decide which team should own each ticket.

    Choose from the following teams:
    - Frontend
    - Backend
    - Infrastructure
    - Marketing

    Base your answer on the content of the ticket. Respond with the team name and a very brief explanation.
    """
    
    # Create the Team agent on the Azure AI agent service.You can use custom tools if you want.
    team_agent = agents_client.create_agent(
        model=deployment,
        name=team_agent_name,
        instructions=team_agent_instructions
    )

    # Create a connected agent tool for the Team agent
    team_agent_tool = ConnectedAgentTool(
        id=team_agent.id,
        name=team_agent_name,
        description="Determines which team should take the ticket"
    )
    return team_agent, team_agent_tool
