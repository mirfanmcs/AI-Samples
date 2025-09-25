# Generate Image

A sample application that uses Azure AI Foundry Vision Service to generate images from textual descriptions. It leverages advanced generative AI models to create visuals based on user-provided prompts.

## Overview

This application demonstrates how to:
- Loads environment variables from a `.env` file.
- Authenticates with Azure using `DefaultAzureCredential`.
- Initializes an `AIProjectClient` to interact with Azure AI Foundry services.
- Retrieves an OpenAI client for image generation.
- Continuously prompts the user for text input to generate images.
- Sends the input prompt to the OpenAI model and retrieves the generated image URL.
- Downloads and saves the generated image in a local images directory.


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
- Deploy `dall-e-3` model


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
Enter prompt `Create an image of a robot eating pizza`. See generated image in the images folder. Try different prompts to see different images generated.

5. Type `quit` to exit the application.

## Features
- **Simple interface**: Clean console-based interaction
- **Secure authentication**: Uses Azure CLI authentication (no API keys stored in code)

## Dependencies

- `azure-ai-projects`: Azure AI Projects SDK for connecting to Azure AI Foundry
- `azure-identity`: Azure authentication library
- `openai`: OpenAI Python SDK (used internally by azure-ai-projects)
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
Generate-Image/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── readme.md          # This file
├── install.sh         # Installation script (if applicable)
└── .env               # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.