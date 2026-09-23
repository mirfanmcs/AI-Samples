# Simple Agent App

This sample combines the functionality of
`AI-Foundry-Agent-App-Using-Custom-Tools` and
`AI-Foundry-Agent-App-Using-MCP` in one Azure AI Foundry agent.

The agent has two strictly limited capabilities:

- Create a local technical support ticket through the
  `submit_support_ticket` custom function.
- Retrieve current official Microsoft documentation through the Microsoft Learn
  MCP server at `https://learn.microsoft.com/api/mcp`.

The agent instructions require it to select the relevant tool from the user's
prompt. It does not answer from its own knowledge or perform actions outside
these two tool capabilities. Unsupported requests are refused.

Agent provisioning and chat are separated in a flat project structure:

- `Agents/simpleAgent_initializer.py` creates or updates the persistent
  Azure AI Foundry agent.
- `Agents/agent_initializer.py` contains shared create-or-update logic.
- `Agents/agent_definition.py` contains the instructions and tool definitions.
- `app.py` is a chat client that discovers the deployed agent by name.

## How tool routing works

| Prompt intent | Tool used | Behavior |
|---|---|---|
| Create a technical support ticket | `submit_support_ticket` | Collects a missing email address or issue description, then writes `ticket-<id>.txt` in the project folder. |
| Ask about Microsoft products or technologies | Microsoft Learn MCP tools | Searches official Microsoft documentation and answers only from the returned results, including source links. |
| Any other request | None | Explains that only support tickets and Microsoft documentation are supported. |

The two tool categories are not combined unless the user explicitly requests
both capabilities.

## Prerequisites

- Python 3.8 or later
- An Azure subscription with access to Azure AI Foundry
- Azure CLI installed
- An Azure AI Foundry project with a deployed model such as `gpt-4o`

## Setup

1. Open this project:

   ```bash
   cd Agentic-AI/Simple-Agent-App
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt --user
   ```

3. Sign in to Azure:

   ```bash
   az login
   ```

4. Copy `.env.example` to `.env` and set your Azure AI Foundry values:

   ```env
   PROJECT_ENDPOINT=https://your-project-name.cognitiveservices.azure.com/
   MODEL_DEPLOYMENT=your-model-deployment-name
   AGENT_NAME=simple-agent
   ```

   Find the project endpoint under your Azure AI Foundry project's settings and
   the deployment name under its model deployments. `AGENT_NAME` is optional
   and defaults to `simple-agent`.

## Create or update the agent

Run the initializer independently from the project root:

```bash
python Agents/simpleAgent_initializer.py
```

The initializer searches for `AGENT_NAME`. It updates the existing agent when
found or creates it when it does not exist, so repeated deployments do not
intentionally create duplicates.

## Run the chat client

```bash
python app.py
```

The chat client discovers `AGENT_NAME`, retrieves that persistent agent, and
creates a new conversation thread. Type `quit` to end the conversation. The
agent is not deleted when the chat client exits.

## GitHub Actions deployment

The repository workflow
`.github/workflows/deploy-simple-agent.yaml` creates or updates the agent when
the initializer, tools, prompt, requirements, or workflow changes. It can also
be run manually with `workflow_dispatch`.

Configure these GitHub Actions secrets:

- `ENV`: Complete `.env` content containing `PROJECT_ENDPOINT`,
  `MODEL_DEPLOYMENT`, and optionally `AGENT_NAME`.
- `AZURE_CREDENTIALS_AGENT_DEPLOY`: Azure service-principal credentials
  accepted by `azure/login`.

### Example support-ticket conversation

```text
I need to create a support ticket.
```

The agent asks for an email address and issue description if they were not
included. After the custom function runs, a `ticket-<id>.txt` file is created in
this folder.

### Example Microsoft Learn request

```text
Give me the Azure CLI commands to create an Azure Container App with a managed identity.
```

The agent invokes the Microsoft Learn MCP server and grounds its response in the
returned official documentation.

### Example unsupported request

```text
Write a poem.
```

The agent refuses because the request is outside the available tool
functionality.

## Project structure

```text
Simple-Agent-App/
|-- Agents/
|   |-- agent_definition.py       # Instructions and tool definitions
|   |-- agent_initializer.py      # Shared create-or-update logic
|   `-- simpleAgent_initializer.py # Executable agent deployment script
|-- app.py              # Chat client for the deployed agent
|-- user_functions.py   # Local support-ticket custom function
|-- requirements.txt    # Python dependencies
|-- install.sh          # Dependency installation helper
|-- .env.example        # Environment-variable template
|-- .gitignore          # Local and generated files excluded from Git
`-- readme.md            # Project documentation
```

## Troubleshooting

- **Missing environment variable**: Verify `.env` contains both
  `PROJECT_ENDPOINT` and `MODEL_DEPLOYMENT`.
- **Authentication failure**: Run `az login` and confirm that the signed-in
  identity can access the Azure AI Foundry project.
- **Model deployment failure**: Confirm that `MODEL_DEPLOYMENT` exactly matches
  a deployed model name in the project.
- **Agent not found**: Run `python Agents/simpleAgent_initializer.py` before
  starting `app.py`. Confirm both commands use the same `AGENT_NAME`.
- **Import failure**: Run `pip install -r requirements.txt --user` from the
  project root.
- **MCP failure**: Confirm that the machine can reach
  `https://learn.microsoft.com/api/mcp`.

## Dependencies

- `azure-ai-agents`: Agent, toolset, function-tool, and MCP-tool APIs
- `azure-ai-projects`: Azure AI Foundry project support
- `azure-identity`: Microsoft Entra ID authentication
- `python-dotenv`: Local environment-variable loading

## License

These samples are provided for educational and demonstration purposes.
