from semantic_kernel.agents.strategies import TerminationStrategy


# class for temination strategy
# This class helps signal when the goal is completed and the conversation can be ended.
# The kernel invokes this function after the agent’s response to determine if the completion criteria are met. In this case, the goal is met when the incident manager agenet responds with "No action needed."" This phrase is defined in the incident manager agent instructions.

class ApprovalTerminationStrategy(TerminationStrategy):
    """A strategy for determining when an agent should terminate."""

    # End the chat if the agent has indicated there is no action needed
    async def should_agent_terminate(self, agent, history):
     """Check if the agent should terminate."""
     return "no action needed" in history[-1].content.lower()