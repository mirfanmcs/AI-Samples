# This script deploys the hosted Simple Harness Agent container.

import argparse
import os
import time
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    AgentEndpointConfig,
    AgentEndpointProtocol,
    ContainerConfiguration,
    FixedRatioVersionSelectionRule,
    HostedAgentDefinition,
    ProtocolConfiguration,
    ProtocolVersionRecord,
    ResponsesProtocolConfiguration,
    VersionSelector,
)
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
POLL_INTERVAL_SECONDS = 10
MAX_POLL_ATTEMPTS = 60


def get_required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Register and route a Foundry hosted-agent container."
    )
    parser.add_argument("--project-endpoint")
    parser.add_argument("--model-deployment")
    parser.add_argument("--image")
    return parser.parse_args()


def wait_for_active_version(
    project_client: AIProjectClient,
    agent_name: str,
    agent_version: str,
) -> None:
    for attempt in range(1, MAX_POLL_ATTEMPTS + 1):
        time.sleep(POLL_INTERVAL_SECONDS)
        details = project_client.agents.get_version(
            agent_name=agent_name,
            agent_version=agent_version,
        )
        status = details["status"]
        print(
            f"Provisioning status: {status} "
            f"(attempt {attempt}/{MAX_POLL_ATTEMPTS})"
        )

        if status == "active":
            return
        if status == "failed":
            raise RuntimeError(
                f"Hosted agent provisioning failed: {dict(details)}"
            )

    raise TimeoutError(
        f"Timed out waiting for hosted agent version {agent_version} "
        "to become active."
    )


def deploy(
    project_endpoint: str | None = None,
    model_deployment_name: str | None = None,
    image_uri: str | None = None,
) -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    endpoint = project_endpoint or get_required_setting("PROJECT_ENDPOINT")
    model_deployment = model_deployment_name or get_required_setting("MODEL_DEPLOYMENT")
    image = image_uri or get_required_setting("HOSTED_AGENT_IMAGE")
    agent_name = os.getenv(
        "HOSTED_AGENT_NAME",
        "simple-harness-agent-hosted",
    )
    context7_mcp_url = os.getenv(
        "CONTEXT7_MCP_URL",
        "https://mcp.context7.com/mcp",
    )
    workspace_dir = os.getenv(
        "HARNESS_WORKSPACE_DIR",
        "/tmp/harness-workspace",
    )
    memory_dir = os.getenv("HARNESS_MEMORY_DIR", "/tmp/harness-memory")
    artifacts_dir = os.getenv(
        "HARNESS_ARTIFACTS_DIR",
        "/tmp/harness-artifacts",
    )

    with (
        DefaultAzureCredential() as credential,
        AIProjectClient(
            endpoint=endpoint,
            credential=credential,
        ) as project_client,
    ):
        created = project_client.agents.create_version(
            agent_name=agent_name,
            description=(
                "Hosted software delivery planning Agent Harness sample."
            ),
            definition=HostedAgentDefinition(
                cpu="1",
                memory="2Gi",
                container_configuration=ContainerConfiguration(image=image),
                environment_variables={
                    "MODEL_DEPLOYMENT_NAME": model_deployment,
                    "CONTEXT7_MCP_URL": context7_mcp_url,
                    "HARNESS_WORKSPACE_DIR": workspace_dir,
                    "HARNESS_MEMORY_DIR": memory_dir,
                    "HARNESS_ARTIFACTS_DIR": artifacts_dir,
                },
                protocol_versions=[
                    ProtocolVersionRecord(
                        protocol=AgentEndpointProtocol.RESPONSES,
                        version="2.0.0",
                    )
                ],
            ),
        )
        print(
            f"Created hosted agent {agent_name} version {created.version} "
            f"from {image}."
        )

        wait_for_active_version(
            project_client,
            agent_name,
            created.version,
        )

        project_client.agents.update_details(
            agent_name=agent_name,
            agent_endpoint=AgentEndpointConfig(
                version_selector=VersionSelector(
                    version_selection_rules=[
                        FixedRatioVersionSelectionRule(
                            agent_version=created.version,
                            traffic_percentage=100,
                        )
                    ]
                ),
                protocol_configuration=ProtocolConfiguration(
                    responses=ResponsesProtocolConfiguration()
                ),
            ),
        )
        print(
            f"Routed 100% of {agent_name} traffic to version "
            f"{created.version}."
        )


if __name__ == "__main__":
    arguments = parse_args()
    deploy(
        project_endpoint=arguments.project_endpoint,
        model_deployment_name=arguments.model_deployment,
        image_uri=arguments.image,
    )
