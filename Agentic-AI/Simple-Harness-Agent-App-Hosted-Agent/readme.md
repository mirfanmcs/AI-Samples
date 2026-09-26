# Simple Harness Agent App - Hosted Agent

This sample combines Microsoft Agent Framework **Agent Harness** with the
Microsoft Foundry hosted-agent Responses protocol. It follows the same Python
SDK, Docker, ACR, client, and GitHub Actions deployment pattern as
`Simple-Agent-App-Hosted-Agent`.

The sample is a software-delivery planning assistant that demonstrates:

- Harness planning, todo tracking, modes, and context compaction.
- A writable Harness file workspace and file memory.
- A bundled `delivery-planning` skill.
- A delegated `DeliveryRiskAnalyst` background agent.
- The custom `calculate_delivery_risk` function tool.
- The custom `save_project_brief` artifact tool.
- Context7 MCP for current software-library documentation.
- Microsoft Foundry hosting through Responses protocol `2.0.0`.

Agent Harness documentation:

- [Agent Harness release announcement](https://devblogs.microsoft.com/agent-framework/the-microsoft-agent-framework-harness-is-now-released/)
- [Agent Harness concepts](https://learn.microsoft.com/agent-framework/concepts/harness?pivots=programming-language-python)
- [Official Python Harness samples](https://github.com/microsoft/agent-framework/tree/main/python/samples/02-agents/harness)

## Example prompts

```text
Plan the delivery of a FastAPI service that processes uploaded invoices.
Use current FastAPI documentation, assess delivery risk, and include milestones.
```

```text
Compare two implementation approaches for a background job system, write your
working notes to the workspace, and ask the risk analyst to review the plan.
```

```text
Create and save a project brief for migrating a Flask API to FastAPI.
```

## Project structure

```text
Simple-Harness-Agent-App-Hosted-Agent/
|-- Agents/
|   |-- skills/
|   |   `-- delivery-planning/
|   |       `-- SKILL.md
|   |-- .dockerignore
|   |-- .env.example
|   |-- Dockerfile
|   |-- deploy_harness_agent.py
|   |-- harness_tools.py
|   |-- hosted_harness_agent_definition.py
|   `-- pyproject.toml
|-- client-app/
|   `-- app.py
|-- .env.example
|-- .gitignore
|-- install.sh
|-- requirements.txt
`-- readme.md
```

## Configuration

Copy `.env.example` to `.env` at the project root:

```env
PROJECT_ENDPOINT=https://your-account.services.ai.azure.com/api/projects/your-project
MODEL_DEPLOYMENT=your-model-deployment-name
HOSTED_AGENT_NAME=simple-harness-agent-hosted
HOSTED_AGENT_IMAGE=your-registry.azurecr.io/simple-harness-agent-hosted:your-tag
CONTEXT7_MCP_URL=https://mcp.context7.com/mcp
HARNESS_WORKSPACE_DIR=/tmp/harness-workspace
HARNESS_MEMORY_DIR=/tmp/harness-memory
HARNESS_ARTIFACTS_DIR=/tmp/harness-artifacts
```

`PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT`, and `HOSTED_AGENT_IMAGE` are required
for SDK deployment. The remaining settings have the defaults shown above.

## Harness composition

[hosted_harness_agent.py](./Agents/hosted_harness_agent.py) uses
`create_harness_agent` with:

- `InMemoryHistoryProvider(load_messages=False)` because the Responses host
  owns persisted conversation history;
- `FileSystemAgentFileStore` for workspace access and Harness memory;
- file read/write approvals disabled for this self-contained demonstration;
- `SkillsProvider` and `FileSkillsSource` for the bundled planning skill;
- a background risk-analysis agent for delegated review;
- custom function tools and a streamable HTTP MCP tool;
- `default_options={"store": False}` for the underlying model calls.

The workspace, memory, and artifact directories are container-local and
ephemeral. They are suitable for a sample but not shared durable storage.
For production or multi-user workloads, use an external `AgentFileStore` and
durable artifact storage. Background agents are currently an experimental
Harness feature.

## Run the hosted agent locally

From the `Agents` directory:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --editable .
Copy-Item .env.example .env
.\.venv\Scripts\python.exe hosted_harness_agent.py
```

The local Responses endpoint listens on port `8088`.

## Run the client

After deploying the hosted agent, run from the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --requirement requirements.txt
.\.venv\Scripts\python.exe client-app\app.py
```

The client calls the deployed hosted agent through the Foundry Responses API
and maintains multi-turn context with `previous_response_id`.

## Build and push the Docker image

```powershell
az login
az acr build `
  --registry "<acr-name>" `
  --image "simple-harness-agent-hosted:<unique-tag>" `
  --platform linux/amd64 `
  Agents
```

Use an immutable image tag rather than `latest`.

## Deploy with the Python SDK

The deployment script follows the same SDK container registration pattern as
`Simple-Agent-App-Hosted-Agent`: it creates a hosted-agent version, polls until
the version is active, and routes 100 percent of endpoint traffic to it.

```powershell
az login
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --requirement requirements.txt
.\.venv\Scripts\python.exe Agents\deploy_harness_agent.py
```

The caller requires `Foundry Project Manager` on the project. The Foundry
project managed identity requires `Container Registry Repository Reader` or
`AcrPull` on the registry.

## GitHub Actions

The workflow
`.github/workflows/deploy-simple-harness-hosted-agent.yaml` mirrors the Simple
Hosted Agent workflow:

1. Authenticate with `AZURE_CREDENTIALS_AGENT_DEPLOY`.
2. Build and push Linux AMD64 with `az acr build`.
3. Pass the immutable image URI from `Build` to `Deploy`.
4. Recreate `.env` from the `ENV` secret.
5. Run `Agents/deploy_harness_agent.py`.

Required repository secrets:

- `ENV`: complete project `.env` content.
- `AZURE_CREDENTIALS_AGENT_DEPLOY`: Azure service-principal credentials.

Required repository variable:

- `ACR_NAME`: Azure Container Registry name.

Context7 is an external MCP service. Review its terms and availability before
using this sample in production.
