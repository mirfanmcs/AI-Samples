import os
from pathlib import Path

from azure.ai.agents import AgentsClient
from azure.ai.agents.models import ListSortOrder, MessageRole
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

from Agents.agent_definition import DEFAULT_AGENT_NAME, create_toolset
from Agents.agent_initializer import find_agent_by_name


PROJECT_ROOT = Path(__file__).resolve().parent


def get_required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    endpoint = get_required_setting("PROJECT_ENDPOINT")
    agent_name = os.getenv("AGENT_NAME", DEFAULT_AGENT_NAME)

    agent_client = AgentsClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True,
        ),
    )
    toolset = create_toolset()

    with agent_client:
        agent_client.enable_auto_function_calls(toolset)
        agent = find_agent_by_name(agent_client, agent_name)
        if not agent:
            raise RuntimeError(
                f"Agent '{agent_name}' was not found. Create it first with: "
                "python Agents/simpleAgent_initializer.py"
            )

        thread = agent_client.threads.create()
        print(f"You're chatting with: {agent.name} ({agent.id})")

        while True:
            input_text = input("Enter the prompt (or type 'quit' to exit): ").strip()
            if input_text.lower() == "quit":
                break
            if not input_text:
                print("Please enter a prompt.")
                continue

            agent_client.messages.create(
                thread_id=thread.id,
                role="user",
                content=input_text,
            )
            run = agent_client.runs.create_and_process(
                thread_id=thread.id,
                agent_id=agent.id,
                toolset=toolset,
            )

            if run.status == "failed":
                print(f"Run failed: {run.last_error}")
                continue

            last_message = agent_client.messages.get_last_message_text_by_role(
                thread_id=thread.id,
                role=MessageRole.AGENT,
            )
            if last_message:
                print(f"Agent: {last_message.text.value}")

        print("\nConversation Log:\n")
        messages = agent_client.messages.list(
            thread_id=thread.id,
            order=ListSortOrder.ASCENDING,
        )
        for message in messages:
            if message.text_messages:
                text_message = message.text_messages[-1]
                print(f"{message.role}: {text_message.text.value}\n")


if __name__ == "__main__":
    main()
