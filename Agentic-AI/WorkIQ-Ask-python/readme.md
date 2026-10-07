# WorkIQ Ask Python - Hosted Agent

`WorkIQ-Ask-python` is a Python hosted agent for the Microsoft Foundry project
`test_irf_foundry_project`. It attaches the Work IQ MCP server directly to the
Agent Framework agent using the existing `Irf-Work-IQ-MCP` project connection.
It answers only from the signed-in user's Microsoft 365 work data returned by
Work IQ.

## Architecture

The runtime follows the direct Foundry-native MCP tool pattern used by the
Smart Sales Order hosted agent. The MCP tool dictionary supplies the Work IQ
server URL and `project_connection_id`, so Foundry uses the existing connection
and the calling user's delegated OAuth context. It does not create another
connection or a toolbox.

```text
User -> WorkIQ-Ask-python -> Irf-Work-IQ-MCP -> Work IQ
```

## Project structure

```text
WorkIQ-Ask-python/
|-- Agents/
|   |-- .dockerignore
|   |-- .env.example
|   |-- Dockerfile
|   |-- deploy_hosted_agent.py
|   |-- hosted_agent_definition.py
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

Copy `.env.example` to `.env`. The defaults target the existing project,
agent, model, Work IQ MCP endpoint, and `Irf-Work-IQ-MCP` connection. Set
`HOSTED_AGENT_IMAGE` to the immutable ACR image URI.

## Run locally

```powershell
cd Agents
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --editable .
$env:PROJECT_ENDPOINT = "https://test-irf-foundry-resource.services.ai.azure.com/api/projects/test_irf_foundry_project"
$env:MODEL_DEPLOYMENT_NAME = "gpt-5-mini"
$env:WORKIQ_MCP_URL = "https://workiq.svc.cloud.microsoft/mcp"
$env:WORKIQ_CONNECTION_ID = "Irf-Work-IQ-MCP"
.\.venv\Scripts\python.exe hosted_agent_definition.py
```

The local Responses endpoint listens on port `8088`.

## Build and deploy

Build and push the Linux AMD64 container:

```powershell
az login
az acr build `
  --registry "<acr-name>" `
  --image "workiq-ask-python:<unique-tag>" `
  --platform linux/amd64 `
  Agents
```

Install deployment dependencies and deploy:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --requirement requirements.txt
.\.venv\Scripts\python.exe Agents\deploy_hosted_agent.py
```

The deployment validates that `Irf-Work-IQ-MCP` exists, creates a hosted-agent
version, waits for it to become active, and routes 100% of traffic to the new
version. It does not provision a toolbox or another MCP connection.

The deployer needs `Foundry Project Manager` on the project. The Foundry
project's managed identity needs `Container Registry Repository Reader` (or
`AcrPull`) on the registry.

## User consent

Work IQ uses delegated authentication. On first use, Foundry may show an Open
consent action or consent URL. The user must sign in and grant consent, then
retry the request. The hosted agent does not and cannot replace this with an
app-only agent identity.

## GitHub Actions

`.github/workflows/deploy-workiq-ask-python.yaml` follows the same build and
Python SDK deployment pattern as the Simple Hosted Agent workflow.

Required repository secrets:

- `ENV`: `.env` content containing `PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT`,
  `HOSTED_AGENT_NAME`, `WORKIQ_MCP_URL`, and `WORKIQ_CONNECTION_ID`.
- `AZURE_CREDENTIALS_AGENT_DEPLOY`: service-principal credentials used by
  `azure/login`, ACR build, and the Python SDK deployer.

Required repository variable:

- `ACR_NAME`: Azure Container Registry name.

## Chat with the deployed agent

```powershell
python client-app\app.py
```
