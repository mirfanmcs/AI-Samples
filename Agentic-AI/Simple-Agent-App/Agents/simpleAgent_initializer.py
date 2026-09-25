import os
import sys
from pathlib import Path

from azure.ai.agents import AgentsClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from Agents.agent_definition import (
    AGENT_INSTRUCTIONS,
    DEFAULT_AGENT_NAME,
    create_toolset,
)
from Agents.agent_initializer import initialize_agent


def get_required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    endpoint = get_required_setting("PROJECT_ENDPOINT")
    deployment = get_required_setting("MODEL_DEPLOYMENT")
    agent_name = os.getenv("AGENT_NAME", DEFAULT_AGENT_NAME)

    agent_client = AgentsClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True,
        ),
    )

    with agent_client:
        agent = initialize_agent(
            agent_client=agent_client,
            model=deployment,
            name=agent_name,
            description="Support ticket and Microsoft documentation agent",
            instructions=AGENT_INSTRUCTIONS,
            toolset=create_toolset(),
        )
        print(
            f"Set AGENT_ID={agent.id} in .env before running "
            "client-app/app.py"
        )


if __name__ == "__main__":
    main()
