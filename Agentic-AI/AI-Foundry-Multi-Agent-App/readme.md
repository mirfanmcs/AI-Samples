# Azure AI Foundry Multi Agent Application

AI Multi Agent application that uses Azure AI Foundry agent service through the Azure AI Foundry Python SDK.

## Overview

This application demonstrates how to:
- Connect to the AI Foundry project for your agent, using the project endpoint and Entra ID authentication.
- Deploy the model your agent will use.
- Create following agents if it doesn't exists:
   - Priority agent: This agent sets the priority level of each ticket.
   - Team agent: This agent decides which team should own each ticket.
   - Effort agent: This agent estimates the effort required to complete each ticket.
   - Main agent: This is the primary / main agent which will use natural language to orchestrate call to different agents
- Note that this code uses the same deployment model and without any Custom Tool for agents. You can use Custom Tool and differnet model for each of the agent as per requirements.
- Create a thread for a chat session with the agent. All conversations with an agent are conducted on a stateful thread that retains message history and data artifacts generated during the chat.
- Add messages to the thread and invoke it with the agent.
- Check the thread status, and when ready, retrieve the messages and data artifacts.
- Repeat the previous two steps as a chat loop until the conversation can be concluded.
- When finished, delete the agent and the thread to clean up the resources and delete data that is no longer required.

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
PROJECT_ENDPOINT=https://your-project-name.cognitiveservices.azure.com/
MODEL_DEPLOYMENT=your-model-deployment-name
```

**How to find these values:**

- **PROJECT_ENDPOINT**: In Azure AI Foundry, go to your project → Settings → find the "Project endpoint"
- **MODEL_DEPLOYMENT**: In Azure AI Foundry, go to your project → Deployments → find your model deployment name

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
`Users can't reset their password from the mobile app.`


## Dependencies

- `azure-ai-projects`: Azure AI Projects SDK for connecting to Azure AI Foundry
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file

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
AI-Foundry-Multi-Agent-App/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── readme.md          # This file
├── install.sh         # Installation script (if applicable)
├── Agents/                    # Agents
│   ├── effort_agent.py            # Effort agent definition
│   ├── priority_agent.py          # Priority agent definition
│   ├── team_agent.py              # team agent definition
└── .env               # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.