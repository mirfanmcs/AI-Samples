# Semantic Kernel Multi Agent Application

This project demonstrates a multi-agent orchestration using the Azure AI Foundry Python SDK and Semantic Kernel. It is designed to automate incident management and DevOps actions by processing log files and coordinating two specialized agents.

## Key Features
- Uses Azure AI Foundry and Semantic Kernel for agent orchestration
- This code uses Semantic Kernel Magentic Orchestration
- Two agents: Incident Manager and DevOps Assistant
- Custom plugins for log file analysis and DevOps actions
- Group chat with custom selection and termination strategies
- Processes log files and recommends/executes corrective actions

## What This Code Does
- Loads configuration and log files
- Connects to Azure AI Foundry project
- Creates two agents:
  - **Incident Manager Agent**: Analyzes logs and recommends actions (restart, rollback, redeploy, increase quota, escalate, or no action)
  - **DevOps Assistant Agent**: Executes recommended actions using DevOps plugin
- Sets up a group chat with both agents, using:
  - **ApprovalTerminationStrategy**: Incident Manager signals end of chat
  - **SelectionStrategy**: Determines which agent responds next
- Iterates through log files, sending each to the agent group chat
- Handles rate limits and errors gracefully


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- Azure CLI installed and configured
- An Azure AI Foundry project with a deployed OpenAI model

## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry project in Azure AI Foundry [https://ai.azure.com/](https://ai.azure.com/)
- Deploy `gpt-4o` model


### 4. Azure Authentication

This application uses Microsoft Entra ID authentication through Azure CLI. You need to sign in to Azure:

```bash
az login
```

Make sure you're logged in with an account that has access to your Azure AI Foundry project.


### 5. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Project Endpoint
AZURE_AI_AGENT_ENDPOINT=https://your-project-name.cognitiveservices.azure.com/
AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME=your_model_deployment

```

**How to find these values:**

- **AZURE_AI_AGENT_ENDPOINT**: In Azure AI Foundry, go to your project → Settings → find the "Project endpoint"
- **AZURE_AI_AGENT_MODEL_DEPLOYMENT_NAME**: In Azure AI Foundry, go to your project → Deployments → find your model deployment name

## Running the Application

1. Ensure you're authenticated with Azure CLI:
   ```bash
   az login
   ```

2. Run the application:
   ```bash
   python app.py
   ```

4. You should see some output similar to the following:

```
 INCIDENT_MANAGER > /home/.../logs/log1.log | Restart service ServiceX
 DEVOPS_ASSISTANT > Service ServiceX restarted successfully.
 INCIDENT_MANAGER > No action needed.

 INCIDENT_MANAGER > /home/.../logs/log2.log | Rollback transaction for transaction ID 987654.
 DEVOPS_ASSISTANT > Transaction rolled back successfully.
 INCIDENT_MANAGER > No action needed.

 INCIDENT_MANAGER > /home/.../logs/log3.log | Increase quota.
 DEVOPS_ASSISTANT > Successfully increased quota.
 (continued)
```



5. Verify that the log files in the logs folder are updated with resolution operation messages from the DevOps Assistant agent.



## Dependencies

- `azure-ai-projects`: Azure AI Projects SDK for connecting to Azure AI Foundry
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file
- `semantic-kernel`: Semantic Kernel SDK
- `azure-ai-agents`: Azure AI Agents


## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Make sure you're logged in with `az login`
2. Verify your account has access to the Azure AI Foundry project
3. Check that your PROJECT_ENDPOINT is correct

### Model Deployment Issues

If you get model-related errors:
1. Verify your MODEL_DEPLOYMENT name is correct
2. Ensure the model is deployed and running in Azure AI Foundry
3. Check that you have permissions to use the deployed model

### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade azure-ai-projects azure-identity`

## Project Structure

```
Semantic-Kernel-Multi-Agent-App/
├── app.py              # Main application file
├── plugins/                    # Semantic Kernel plugins
│   ├── devops_plugin.py         # DevOps plugin
│   ├── logfile_plugin.py         # Logfile plugin
├── strategy/                    # Semantic Kernel plugins
│   ├── selection_strategy.py         # Selection strategy
│   ├── temination_strategy.py         # Termination strategy
├── instruction/*    # AI Agent instructions
├── requirements.txt    # Python dependencies
├── readme.md          # This file
├── install.sh         # Installation script (if applicable)
├── sample_logs/*         # Sample log file
└── .env               # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.