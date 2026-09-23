import os
from pathlib import Path
from typing import Any

from azure.ai.agents import AgentsClient
from azure.ai.agents.models import (
    FunctionTool,
    ListSortOrder,
    MessageRole,
    RequiredMcpToolCall,
    RunHandler,
    ThreadRun,
    ToolApproval,
)
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

from user_functions import user_functions


PROJECT_ROOT = Path(__file__).resolve().parent


class McpApprovalHandler(RunHandler):
    def __init__(self, approved_server_labels: set[str]) -> None:
        self.approved_server_labels = approved_server_labels

    def submit_mcp_tool_approval(
        self,
        *,
        run: ThreadRun,
        tool_call: RequiredMcpToolCall,
        **kwargs: Any,
    ) -> ToolApproval:
        approved = tool_call.server_label in self.approved_server_labels
        action = "Approving" if approved else "Rejecting"
        print(
            f"{action} MCP tool '{tool_call.name}' "
            f"from server '{tool_call.server_label}'."
        )
        return ToolApproval(tool_call_id=tool_call.id, approve=approved)


def get_required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")

    endpoint = get_required_setting("PROJECT_ENDPOINT")
    agent_id = get_required_setting("AGENT_ID")
    approved_server_labels = {
        label.strip()
        for label in get_required_setting("MCP_APPROVED_SERVER_LABELS").split(",")
        if label.strip()
    }
    run_handler = McpApprovalHandler(approved_server_labels)

    agent_client = AgentsClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True,
        ),
    )

    with agent_client:
        agent_client.enable_auto_function_calls(FunctionTool(user_functions))
        agent = agent_client.get_agent(agent_id)
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
                run_handler=run_handler,
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
