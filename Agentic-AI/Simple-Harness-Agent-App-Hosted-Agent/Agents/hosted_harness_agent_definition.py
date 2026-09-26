import asyncio
import os
from pathlib import Path

from agent_framework import (
    Agent,
    FileSkillsSource,
    FileSystemAgentFileStore,
    InMemoryHistoryProvider,
    MCPStreamableHTTPTool,
    SkillsProvider,
    create_harness_agent,
)
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

from harness_tools import calculate_delivery_risk, save_project_brief


load_dotenv()

AGENT_INSTRUCTIONS = """
You are a software delivery planning agent powered by Agent Harness.

For substantial requests:
1. Use Harness planning and todo capabilities to break the work into verifiable
   steps.
2. Use the delivery-planning skill for the required workflow and output shape.
3. Use Context7 MCP when current library or framework documentation is needed.
4. Use calculate_delivery_risk before assigning a final delivery risk band.
5. Use the file workspace for working notes and intermediate artifacts.
6. Use save_project_brief only when the user asks to persist the final brief.

Clearly distinguish verified documentation from assumptions. Never claim that
an artifact was saved unless the tool returns a successful result.
"""

RISK_ANALYST_INSTRUCTIONS = """
Review a proposed software delivery plan. Identify missing dependencies,
unfamiliar technology, complexity, and deadline pressure. Use
calculate_delivery_risk and return a concise risk assessment with mitigations.
"""


async def main() -> None:
    credential = DefaultAzureCredential()
    client = FoundryChatClient(
        project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        credential=credential,
    )

    context7 = MCPStreamableHTTPTool(
        name="context7",
        description="Retrieve current documentation for software libraries.",
        url=os.getenv("CONTEXT7_MCP_URL", "https://mcp.context7.com/mcp"),
        approval_mode="never_require",
        load_prompts=False,
        use_progressive_disclosure=True,
    )

    risk_analyst = Agent(
        client=client,
        name="DeliveryRiskAnalyst",
        description="Reviews delivery plans and calculates implementation risk.",
        instructions=RISK_ANALYST_INSTRUCTIONS,
        tools=[calculate_delivery_risk],
        default_options={"store": False},
    )

    agent_root = Path(__file__).resolve().parent
    workspace_dir = Path(
        os.getenv("HARNESS_WORKSPACE_DIR", "/tmp/harness-workspace")
    )
    memory_dir = Path(
        os.getenv("HARNESS_MEMORY_DIR", "/tmp/harness-memory")
    )
    workspace_dir.mkdir(parents=True, exist_ok=True)
    memory_dir.mkdir(parents=True, exist_ok=True)

    skills_provider = SkillsProvider(
        FileSkillsSource(agent_root / "skills"),
        disable_load_skill_approval=True,
        disable_read_skill_resource_approval=True,
        disable_run_skill_script_approval=True,
    )

    agent = create_harness_agent(
        client=client,
        name="SoftwareDeliveryHarness",
        description=(
            "Plans software delivery using Harness orchestration, tools, "
            "skills, workspace files, memory, delegation, and MCP."
        ),
        agent_instructions=AGENT_INSTRUCTIONS,
        tools=[calculate_delivery_risk, save_project_brief, context7],
        max_context_window_tokens=128_000,
        max_output_tokens=16_384,
        history_provider=InMemoryHistoryProvider(load_messages=False),
        file_memory_store=FileSystemAgentFileStore(memory_dir),
        file_access_store=FileSystemAgentFileStore(workspace_dir),
        file_access_disable_readonly_tool_approval=True,
        file_access_disable_write_tool_approval=True,
        skills_provider=skills_provider,
        background_agents=[risk_analyst],
        disable_web_search=True,
        default_options={"store": False},
    )

    await ResponsesHostServer(agent).run_async()


if __name__ == "__main__":
    asyncio.run(main())
