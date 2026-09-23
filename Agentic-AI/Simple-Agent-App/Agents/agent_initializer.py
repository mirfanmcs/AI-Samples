from azure.ai.agents import AgentsClient
from azure.ai.agents.models import Agent, ListSortOrder, ToolSet


def find_agent_by_name(agent_client: AgentsClient, name: str) -> Agent | None:
    agents = agent_client.list_agents(order=ListSortOrder.DESCENDING)
    return next((agent for agent in agents if agent.name == name), None)


def initialize_agent(
    agent_client: AgentsClient,
    model: str,
    name: str,
    description: str,
    instructions: str,
    toolset: ToolSet,
) -> Agent:
    existing_agent = find_agent_by_name(agent_client, name)
    if existing_agent:
        agent = agent_client.update_agent(
            agent_id=existing_agent.id,
            model=model,
            name=name,
            description=description,
            instructions=instructions,
            toolset=toolset,
        )
        print(f"Updated {name} agent, ID: {agent.id}")
        return agent

    agent = agent_client.create_agent(
        model=model,
        name=name,
        description=description,
        instructions=instructions,
        toolset=toolset,
    )
    print(f"Created {name} agent, ID: {agent.id}")
    return agent
