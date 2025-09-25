# Audio Enabled Chat Application

A chat application that uses Azure AI Foundry to interact with OpenAI models through the Azure AI Foundry Python SDK. It uses multimodel to send text and audio prompt.

## Overview

This application demonstrates how to:
- Connect to Azure AI Foundry using Microsoft Entra ID authentication
- Use the Azure AI Projects SDK to get an OpenAI client
- Create a streaming chat interface in the console
- Maintain conversation history throughout the session
- This app is using multimodal (Phi-4) to enable speech prompt. If you want to use only a monomodel i.e. gpt-4o, you can still enable speech prompt by first using speech to text AI service to convert speech to text and than pass text prompt to chat completions.

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
- Deploy `Phi-4-multimodal-instruct` model


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

## Features

- **Streaming responses**: See the AI response being generated in real-time
- **Conversation history**: The app maintains context throughout the session
- **Simple interface**: Clean console-based interaction
- **Secure authentication**: Uses Azure CLI authentication (no API keys stored in code)

## Dependencies

- `azure-ai-projects`: Azure AI Projects SDK for connecting to Azure AI Foundry
- `azure-identity`: Azure authentication library
- `openai`: OpenAI Python SDK (used internally by azure-ai-projects)
- `python-dotenv`: For loading environment variables from .env file
- `sounddevice`: For sound service 

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
2. Try upgrading packages: `pip install --upgrade azure-ai-projects azure-identity sounddevice`

## Project Structure

```
Audio-Enabled-Chat-App/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── readme.md          # This file
├── install.sh         # Installation script (if applicable)
└── .env               # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.