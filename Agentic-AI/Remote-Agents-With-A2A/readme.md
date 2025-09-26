# Remote Agents With A2A

A sample application that demonstrates how to use Azure AI Foundry Agent-to-Agent (A2A) communication to orchestrate and coordinate remote agents. It enables distributed AI workflows and collaboration between agents across different environments.


## Overview

- **client.py**: 
  - Command-line client that sends user prompts to the routing agent and displays responses.
  - Handles user input and output loop.
  - Connects to the routing agent via HTTP.

- **run_all.py**:
  - Orchestrates the startup of all agent servers and the client.
  - Loads environment variables and launches each agent as a subprocess.
  - Ensures all services are running for end-to-end testing.

- **requirements.txt**:
  - Lists all Python dependencies required for the project.

- **outline_agent/**:
  - `agent.py`: Implements the OutlineAgent using Azure AI Foundry to generate outlines.
  - `agent_executor.py`: Defines the executor logic for processing outline generation requests.
  - `server.py`: FastAPI/Starlette server exposing the outline agent as an HTTP API.

- **routing_agent/**:
  - `agent.py`: Implements the RoutingAgent, which routes user prompts to the appropriate specialized agent (title or outline).
  - `server.py`: FastAPI server that receives client messages and interacts with the RoutingAgent.

- **title_agent/**:
  - `agent.py`: Implements the TitleAgent using Azure AI Foundry to generate titles.
  - `agent_executor.py`: Defines the executor logic for processing title generation requests.
  - `server.py`: FastAPI/Starlette server exposing the title agent as an HTTP API.

## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- Azure CLI installed and configured
- An Azure AI Foundry project with deployed OpenAI models

## Setup Instructions

1. **Clone or Download the Project**

   Download or clone this project to your local machine.

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt --user
   ```

3. **Azure Setup**
   - Create an Azure AI Foundry project at https://ai.azure.com/
   - Deploy the required models (e.g., gpt-4o)

4. **Azure Authentication**

   Sign in to Azure:
   ```bash
   az login
   ```

5. **Configure Environment Variables**

   Create a `.env` file in the project root with the following variables:
   ```env
   SERVER_URL=localhost
   ROUTING_AGENT_PORT=8000
   TITLE_AGENT_PORT=8001
   OUTLINE_AGENT_PORT=8002
   PROJECT_ENDPOINT=https://your-project-name.cognitiveservices.azure.com/
   MODEL_DEPLOYMENT_NAME=your-model-deployment-name
   ```

## Running the Application

1. Ensure you're authenticated with Azure CLI:
   ```bash
   az login
   ```
2. Start all agent servers and the client:
   ```bash
   python run_all.py
   ```
3. Enter prompts following prompt in the client terminal. Type `quit` to exit.
    `Create a title and outline for an article about React programming.`

## Troubleshooting

- **Authentication Issues**: Ensure you are logged in with `az login` and have access to the Azure AI Foundry project.
- **Model Deployment Issues**: Verify the model deployment name and status in Azure AI Foundry.
- **Package Issues**: Ensure all dependencies are installed with `pip install -r requirements.txt --user`.

## Project Structure

```
Remote-Agents-With-A2A/
├── client.py
├── run_all.py
├── requirements.txt
├── outline_agent/
│   ├── agent.py
│   ├── agent_executor.py
│   └── server.py
├── routing_agent/
│   ├── agent.py
│   └── server.py
├── title_agent/
│   ├── agent.py
│   ├── agent_executor.py
│   └── server.py
└── .env
```

## License

This project is provided for educational and demonstration purposes.