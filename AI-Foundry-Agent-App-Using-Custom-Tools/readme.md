# Azure AI Foundry Agent Application Using Custom Tools

A console-based AI Agent application that uses Azure AI Foundry agent service and custom function as a custom tools through the Azure AI Foundry Python SDK.

## Overview

This application demonstrates how to:
- Connect to the AI Foundry project for your agent, using the project endpoint and Entra ID authentication.
- Deploy the model your agent will use.
- Create the agent if it doens't exists by specifiying
   - The model deployment in the project that the agent should use to interpret and respond to prompts.
   - Instructions that determine the functionality and behavior of the agent.
   - Custom function as a Custom Tool the agent can use to perform tasks.
- Custom function will take `email_address` and `description` as input and create the text file in the app folder. You can extend this functionality to create ticket in your ITSM system. Or you can direclty use OpenAPI spec as a custom tool to create ticket in your ITSM.
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
`I have a technical problem`
View the response. The agent may ask for your email address and a description of the issue.
The tool should have saved support tickets in the app folder.


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
Simple-Console-AI-Foundry-Chat-App/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── readme.md          # This file
├── install.sh         # Installation script (if applicable)
├── user_functions.py    # custom function
└── .env               # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.