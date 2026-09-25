import os
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def get_required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    endpoint = get_required_setting("PROJECT_ENDPOINT")
    hosted_agent_name = get_required_setting("HOSTED_AGENT_NAME")
    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True,
        ),
    )
    previous_response_id: str | None = None
    conversation_log: list[tuple[str, str]] = []

    with project_client:
        client = project_client.get_openai_client(agent_name=hosted_agent_name)
        print(f"You're chatting with: {hosted_agent_name}")

        while True:
            input_text = input("Enter the prompt (or type 'quit' to exit): ").strip()
            if input_text.lower() == "quit":
                break
            if not input_text:
                print("Please enter a prompt.")
                continue

            conversation_log.append(("user", input_text))

            if previous_response_id:
                response = client.responses.create(
                    input=input_text,
                    previous_response_id=previous_response_id,
                )
            else:
                response = client.responses.create(input=input_text)

            if response.status == "failed":
                print(f"Run failed: {response.error}")
                continue

            previous_response_id = response.id
            if response.output_text:
                conversation_log.append(("agent", response.output_text))
                print(f"Agent: {response.output_text}")

        print("\nConversation Log:\n")
        for role, content in conversation_log:
            print(f"{role}: {content}\n")


if __name__ == "__main__":
    main()
