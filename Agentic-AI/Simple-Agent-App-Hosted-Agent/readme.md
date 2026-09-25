# Simple Agent App - Hosted Agent

The hosted implementation runs custom Python code in Microsoft Foundry and
exposes the Responses protocol. It supports:

- Creating support-ticket files with a local hosted Python tool.
- Searching official Microsoft documentation with the Microsoft Learn MCP
  server.
- Refusing requests outside those tool capabilities.

## Chat client

`client-app/app.py` invokes the deployed hosted agent through its Responses
endpoint:

```bash
python client-app/app.py
```

## Project structure

```text
Simple-Agent-App-Hosted-Agent/
|-- Agents/
|   |-- .dockerignore
|   |-- Dockerfile
|   |-- deploy_hosted_agent.py
|   |-- hosted_agent_definition.py
|   |-- pyproject.toml
|   |-- user_functions.py
|   `-- .env.example
|-- client-app/
|   `-- app.py
|-- requirements.txt
|-- .env.example
|-- .gitignore
`-- readme.md
```

## Configure an existing Foundry project

Create `.env` from `.env.example` and set:

```env
PROJECT_ENDPOINT=https://your-account.services.ai.azure.com/api/projects/your-project
MODEL_DEPLOYMENT=your-model-deployment-name
HOSTED_AGENT_NAME=simple-agent-hosted
HOSTED_AGENT_IMAGE=your-container-registry-name.azurecr.io/simple-agent-hosted:your-tag
TICKET_OUTPUT_DIR=/tmp/support-tickets
```

## Run locally

From the `Agents` directory, create a virtual environment and install the
hosted runtime:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --editable .
$env:FOUNDRY_PROJECT_ENDPOINT = "<project-endpoint>"
$env:MODEL_DEPLOYMENT_NAME = "<model-deployment>"
.\.venv\Scripts\python.exe hosted_agent_definition.py
```

The local Responses endpoint listens on port `8088`.

The support-ticket implementation is in `Agents/user_functions.py` and is
registered as a tool by `Agents/hosted_agent_definition.py`.
`client-app/app.py` only invokes the deployed hosted agent; it does not execute
custom tools locally. Tool calls run inside the hosted container.

## Build and push the Docker image

Use an Azure Container Registry remote build to build Linux AMD64 and push the
image in one command:

```powershell
az login
az acr build `
  --registry "<acr-name>" `
  --image "simple-agent-hosted:<unique-tag>" `
  --platform linux/amd64 `
  Agents
```

Use a unique immutable image tag instead of `latest`. Set `HOSTED_AGENT_IMAGE`
in `.env` to the pushed image URI.

## Deploy with the Python SDK

The deployment script follows the Microsoft Foundry
[Python SDK container deployment approach](https://learn.microsoft.com/azure/foundry/agents/how-to/deploy-hosted-agent?pivots=python).
It calls `AIProjectClient.agents.create_version` with a
`ContainerConfiguration`, waits for the version to become active, and routes
100% of endpoint traffic to the new version.

Install the deployment dependencies and run the script from the project root:

```powershell
az login
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --requirement requirements.txt
.\.venv\Scripts\python.exe Agents\deploy_hosted_agent.py
```

The service principal or signed-in user must have the `Foundry Project Manager`
role on the target project and permission to push the image to ACR. The
Foundry project's managed identity must have `Container Registry Repository
Reader` (or `AcrPull`) on the registry. The script uses the existing Foundry
project, model deployment, and ACR; it does not provision infrastructure.

## GitHub Actions

The workflow `.github/workflows/deploy-simple-hosted-agent.yaml` deploys the
hosted agent when this project changes or when manually triggered.

Required repository secrets:

- `ENV`: `.env` content for this project. It must include `PROJECT_ENDPOINT`
  and `MODEL_DEPLOYMENT`; it can optionally override `HOSTED_AGENT_NAME`.
- `AZURE_CREDENTIALS_AGENT_DEPLOY`: JSON service-principal credentials used by
  `azure/login`, the ACR build, and `DefaultAzureCredential`.

Required repository variable:

- `ACR_NAME`: Name of the Azure Container Registry used by `az acr build`.

The `Build` job uses `az acr build` to build and push
`simple-agent-hosted:${{ github.sha }}`. It passes the resulting image URI to
the `Deploy` job. The deploy job creates `.env` from the `ENV` secret, and the
Python SDK deployer reads `PROJECT_ENDPOINT` and `MODEL_DEPLOYMENT` from that
file before registering and routing the image.

## Hosted ticket storage

Ticket files are written to `/tmp/support-tickets` by default. Hosted agent
filesystem storage is ephemeral and local to the hosted container. A custom
`TICKET_OUTPUT_DIR` must be a writable Linux container path; it is not a path
on the client computer. Replace this tool with an external durable ticket
system for production use.
