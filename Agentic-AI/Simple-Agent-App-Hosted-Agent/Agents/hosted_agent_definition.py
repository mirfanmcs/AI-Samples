#This code is building an agent that can route user requests to the appropriate tools.


import asyncio
import os

from agent_framework import Agent, MCPStreamableHTTPTool
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

from user_functions import submit_support_ticket


load_dotenv()

AGENT_INSTRUCTIONS = """
You are a tool-routing agent with exactly two supported capabilities:

1. Support tickets:
   - Use `submit_support_ticket` only when the user wants to create or submit a
     technical support ticket.
   - Before calling it, collect both the user's email address and a description
     of the technical issue. Ask only for a missing required value.
   - Report only the result returned by the tool.

2. Microsoft documentation:
   - Use the `mslearn` MCP tools only when the user asks a question that can be
     answered from official Microsoft documentation.
   - Always call the relevant MCP tool before answering. Base the answer only on
     the tool results and include source links returned by the tool.

Do not answer from your own knowledge and do not perform or claim any action
outside these tool capabilities. Never use both tool categories unless the user
explicitly requests both capabilities. For unsupported requests, briefly state
that you can only submit support tickets or retrieve Microsoft documentation.
"""


async def main() -> None:
    client = FoundryChatClient(
        project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        credential=DefaultAzureCredential(),
    )
    microsoft_learn = MCPStreamableHTTPTool(
        name="mslearn",
        description="Search and fetch official Microsoft documentation.",
        url="https://learn.microsoft.com/api/mcp",
        approval_mode="never_require",
        load_prompts=False,
    )
    async with Agent(
        client=client,
        instructions=AGENT_INSTRUCTIONS,
        tools=[submit_support_ticket, microsoft_learn],
        default_options={"store": False},
    ) as agent:
        server = ResponsesHostServer(agent)
        await server.run_async()


if __name__ == "__main__":
    asyncio.run(main())
