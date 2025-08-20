from semantic_kernel.agents.strategies import SequentialSelectionStrategy
from semantic_kernel.contents.utils.author_role import AuthorRole
from instructions.instructions import (
    INCIDENT_MANAGER_AGENT_NAME,
    DEVOPS_ASSISTANT_AGENT_NAME,
)

# class for selection strategy
# This class identifies which agent should take the next turn
# This code runs on every turn to determine which agent should respond, checking the chat history to see who last responded
class SelectionStrategy(SequentialSelectionStrategy):
    """A strategy for determining which agent should take the next turn in the chat."""
    

    # Select the next agent that should take the next turn in the chat
    async def select_agent(self, agents, history):
        """"Check which agent should take the next turn in the chat."""

        # The Incident Manager agent should go after the User or the Devops Assistant agent
        if (history[-1].name == DEVOPS_ASSISTANT_AGENT_NAME or history[-1].role == AuthorRole.USER):
            agent_name = INCIDENT_MANAGER_AGENT_NAME
            return next((agent for agent in agents if agent.name == agent_name), None)
        # Otherwise it is the Devops Assistant agent's turn
        return next((agent for agent in agents if agent.name == DEVOPS_ASSISTANT_AGENT_NAME), None)