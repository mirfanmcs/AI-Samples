# Semantic Kernel Agent Application

Semantic Kernel Agent application that uses `AzureAIAgent` class. The `AzureAIAgent` class provides a seamless way to build and interact with AI agents using the Azure AI Foundry Agent Service. It abstracts the complexity of managing AI agents by offering a more structured and intuitive interface within the Semantic Kernel Agent Framework.

Following are the key components of `AzureAIAgent` class:
- `AzureAISAgentSettings` - an object that automatically includes the Azure AI Agent settings from the environment configuration. These settings will be used by the AzureAIAgents you create.
- `AzureAIAgent` client - an object that manages the connection to your Azure AI Foundry project. This object allows you to access the services and models associated with your project.
- Agent service - the `AzureAIAgent` client also contains an agent operations service. This service helps streamline the process of creating, managing, and running the agents for your project.
- Agent definition - the AzureAI Agent model created via the AzureAI Project client. This definition specifies the AI deployment model that should be used, and the name and instructions for the agent.
- `AzureAIAgentThread` - automatically maintains the conversation history between agents and users, and the state. You can add messages to a thread and use the agent to invoke a response from the LLM.


## Overview

This application demonstrates how to:
- Use Semantic Kernel to connect to an Azure AI Foundry project.
- Create Foundry Agent Service agents using the Semantic Kernel SDK.
- Integrate Email plugin functions with your AI agent.
- Use the data.txt as grounded data for Knowledge

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

3. The application will start and prompt you to enter messages. Type your questions or prompts and press Enter.

4. The AI will respond in a streaming fashion (text appears as it's generated).

5. Type `quit` to exit the application.

6. Use these prompts:
`Submit an expense claim`


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
Semantic Kernel-Agent-App/
├── app.py              # Main application file
├── plugins/                    # Semantic Kernel plugins
│   ├── email_plugin.py         # Email plugin
├── requirements.txt    # Python dependencies
├── readme.md          # This file
├── install.sh         # Installation script (if applicable)
├── data.txt         # Sample data file
└── .env               # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.