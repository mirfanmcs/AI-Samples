# Agent Orchestration Application

AI agent application that uses Microsoft Foundry and the Microsoft Agent Framework to process customer feedback through a sequential multi-agent workflow.

## Overview

This application demonstrates how to:
- Connect to a Microsoft Foundry project using the project endpoint and Microsoft Entra ID authentication.
- Use a deployed model through `FoundryChatClient`.
- Create three specialized agents:
  - A summarizer that condenses customer feedback into one sentence.
  - A classifier that labels the feedback as Positive, Negative, or Feature request.
  - An action agent that recommends the next step.
- Build a sequential orchestration with `SequentialBuilder`.
- Pass each agent's output through the workflow in order.
- Collect and display the output from every participating agent.

The included example processes feedback requesting a dark mode and prints the summary, classification, and recommended action.

## Prerequisites

- Python 3.10 or higher
- Azure subscription with access to Microsoft Foundry
- Azure CLI installed and configured
- A Microsoft Foundry project with a deployed chat model

## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

Alternatively, on a system with a POSIX-compatible shell, run:

```bash
sh install.sh
```

### 3. Microsoft Foundry Setup

- Create a project in [Microsoft Foundry](https://ai.azure.com/).
- Deploy a chat model that is supported by the Agent Framework.
- Make a note of the project endpoint and model deployment name.

### 4. Azure Authentication

This application uses Microsoft Entra ID authentication through Azure CLI. Sign in to Azure:

```bash
az login
```

Make sure you are signed in with an account that has access to your Microsoft Foundry project and model deployment.

### 5. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# Microsoft Foundry project endpoint
PROJECT_ENDPOINT=https://your-project-name.services.ai.azure.com/api/projects/your-project-name
MODEL_DEPLOYMENT=your-model-deployment-name
```

**How to find these values:**

- **PROJECT_ENDPOINT**: In Microsoft Foundry, open your project and copy its project endpoint.
- **MODEL_DEPLOYMENT**: In Microsoft Foundry, open the project's model deployments and copy the deployment name.

## Running the Application

1. Ensure you are authenticated with Azure CLI:

   ```bash
   az login
   ```

2. Run the application:

   ```bash
   python app.py
   ```

3. The application submits the customer feedback defined in `app.py` to the sequential workflow.

4. The workflow prints the output from each agent in this order:
   - Summarizer
   - Classifier
   - Action recommender

To process different feedback, update the `feedback` value in `app.py` and run the application again.

## Dependencies

- `agent-framework-core`: Core message and agent abstractions for the Microsoft Agent Framework
- `agent-framework-foundry`: Microsoft Foundry chat client integration
- `agent-framework-orchestrations`: Sequential multi-agent workflow orchestration
- `azure-identity`: Microsoft Entra ID authentication through `AzureCliCredential`
- `python-dotenv`: Loads project configuration from the `.env` file

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Make sure you are signed in with `az login`.
2. Verify that the selected Azure account has access to the Microsoft Foundry project.
3. Check that `PROJECT_ENDPOINT` contains the complete project endpoint.

### Model Deployment Issues

If you get model-related errors:
1. Verify that `MODEL_DEPLOYMENT` exactly matches the deployment name.
2. Ensure the model deployment is available in the configured project.
3. Check that your account has permission to use the deployed model.

### Package Issues

If you encounter package import errors:
1. Install all dependencies with `pip install -r requirements.txt --user`.
2. Confirm that you are running Python 3.10 or higher.
3. If you use a virtual environment, make sure it is activated before installing dependencies or running the application.

## Project Structure

```text
Agent-Orchestration/
├── app.py              # Defines the agents and sequential workflow
├── requirements.txt    # Python dependencies
├── readme.md           # Project documentation
├── install.sh          # Dependency installation script
├── .env                # Environment variables (create this file)
└── .gitignore          # Files excluded from source control
```

## License

These samples are provided for educational and demonstration purposes.
