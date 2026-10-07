import asyncio
import os
from typing import Any

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv


load_dotenv()

AGENT_INSTRUCTIONS = """
You are a Work IQ-only assistant.

First determine whether the user's request can be answered using the signed-in user's Microsoft 365 work data through Work IQ.

If the request is clearly outside Work IQ's scope, do not call any tool and reply exactly: "I can only answer questions using Work IQ."

For requests within Work IQ's scope, use the configured Work IQ MCP tools. Answer only with information returned by Work IQ for that request. Do not use web search, general model knowledge, assumptions, or any other source.

Do not answer general knowledge, coding, creative-writing, or other questions unrelated to the user's Microsoft 365 work data.

If Work IQ returns no relevant information, is unavailable, or authentication fails, reply exactly: "I can only answer questions using Work IQ, and I couldn't retrieve an answer from Work IQ."

Never fill gaps with inferred or invented information.
""".strip()

WORKIQ_MCP_URL = os.getenv(
    "WORKIQ_MCP_URL",
    "https://workiq.svc.cloud.microsoft/mcp",
)
WORKIQ_CONNECTION_ID = os.getenv(
    "WORKIQ_CONNECTION_ID",
    "Irf-Work-IQ-MCP",
)


def create_foundry_tools() -> list[dict[str, Any]]:
    return [
        {
            "type": "mcp",
            "server_label": "workiq",
            "server_url": WORKIQ_MCP_URL,
            "require_approval": "never",
            "project_connection_id": WORKIQ_CONNECTION_ID,
        }
    ]


async def main() -> None:
    credential = DefaultAzureCredential()
    client = FoundryChatClient(
        project_endpoint=os.environ["PROJECT_ENDPOINT"],
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        credential=credential,
        allow_preview=True,
    )
    with credential:
        async with Agent(
            client=client,
            instructions=AGENT_INSTRUCTIONS,
            name="WorkIQ-Ask-python",
            description="Hosted assistant that answers only from Work IQ.",
            tools=create_foundry_tools(),
            default_options={
                "store": False,
                "reasoning": {
                    "effort": "low",
                },
            },
        ) as agent:
            server = ResponsesHostServer(agent)
            await server.run_async()


if __name__ == "__main__":
    asyncio.run(main())
