# Simple Prompt Flow Chat App

A comprehensive travel chat application built with Microsoft PromptFlow, featuring an intelligent chat bot and automated evaluation system. This project demonstrates end-to-end AI application development with Azure OpenAI integration, conversation memory, and quality assessment capabilities.

## 🌟 Project Overview

This repository contains two main PromptFlow applications that work together to create and evaluate an intelligent travel assistant:

### 🤖 [Chat Flow](./chat-flow/) - Travel Assistant Bot
An intelligent travel agent chat bot powered by Azure OpenAI GPT-4o that provides:
- **Expert Travel Advice** - Professional recommendations for destinations, timing, and logistics
- **Budget Planning** - Cost estimates and budget-friendly suggestions
- **Safety Guidance** - Travel safety tips and documentation requirements
- **Conversation Memory** - Maintains context across multiple interactions
- **Real-time Responses** - Fast, accurate travel information and planning assistance

**Key Features:**
- GPT-4o powered responses with optimized prompts
- Chat history management for conversation continuity
- Comprehensive test suite with 10+ travel scenarios
- Interactive testing modes and performance benchmarks

📖 **[Detailed Documentation](./chat-flow/README.md)**

### 📊 [Evaluation Flow](./evaluation-flow/) - Quality Assessment System
A sophisticated evaluation system that automatically assesses chat bot responses across multiple quality dimensions:
- **Relevance** - How well responses address travel questions
- **Helpfulness** - Practical value and actionability for travelers
- **Accuracy** - Factual correctness of travel information
- **Travel Expertise** - Professional knowledge and industry insights
- **Overall Assessment** - Comprehensive scoring with improvement recommendations

**Key Features:**
- Multi-dimensional scoring (1-5 scale for each metric)
- Automated evaluation with detailed feedback
- Sample test data covering diverse travel scenarios
- End-to-end testing from chat generation to quality assessment

📖 **[Detailed Documentation](./evaluation-flow/README.md)**

## 🏗️ Project Structure

```
Simple-Prompt-Flow-Chat-App/
├── chat-flow/                    # Main travel chat bot application
│   ├── flow.dag.yaml            # PromptFlow configuration
│   ├── chat.jinja2              # Travel agent prompt template
│   ├── requirements.txt         # Chat flow dependencies
│   ├── test_data.jsonl          # Test scenarios
│   ├── test_data_with_history.jsonl # Conversation tests
│   ├── quick_test.py            # Quick validation script
│   ├── test_chat_flow.py        # Comprehensive test suite
│   └── README.md                # Chat flow documentation
├── evaluation-flow/              # Automated evaluation system
│   ├── flow.dag.yaml            # Evaluation flow configuration
│   ├── relevance_eval.jinja2    # Relevance assessment prompt
│   ├── helpfulness_eval.jinja2  # Helpfulness assessment prompt
│   ├── accuracy_eval.jinja2     # Accuracy assessment prompt
│   ├── travel_expertise_eval.jinja2 # Expertise assessment prompt
│   ├── overall_summary.jinja2   # Overall evaluation summary
│   ├── requirements.txt         # Evaluation flow dependencies
│   ├── test_data.jsonl          # Sample evaluation data
│   ├── run_evaluation.py        # Standalone evaluation script
│   ├── run_chat_and_evaluate.py # End-to-end evaluation script
│   └── README.md                # Evaluation flow documentation
├── requirements.txt              # Project-wide dependencies
└── README.md                    # This file
```

## 🚀 Quick Start Guide

### Prerequisites

Before starting, ensure you have:
- **Python 3.9+** environment (recommended: use conda)
- **VS Code** with PromptFlow extension
- **Azure subscription** with Azure OpenAI service access
- **Azure AI Studio/Foundry** project setup
- **GPT-4o model** deployed in Azure OpenAI

## 📋 Prerequisites Setup

### Step 1: Install VS Code and PromptFlow Extension

#### 1.1 Install VS Code
1. Download and install [Visual Studio Code](https://code.visualstudio.com/)
2. Install [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

#### 1.2 Install PromptFlow Extension
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Prompt Flow"
4. Install [Prompt Flow for VS Code Extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow)


### Step 2: Install Conda

#### 2.1 Download and Install Miniconda
**Windows:**
```pwsh
# Download Miniconda installer
Invoke-WebRequest -Uri "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -OutFile "Miniconda3-latest-Windows-x86_64.exe"

# Run installer (follow GUI prompts)
.\Miniconda3-latest-Windows-x86_64.exe
```

**macOS:**
```bash
# Download and install Miniconda
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
```

**Linux:**
```bash
# Download and install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

#### 2.2 Verify Conda Installation
```bash
# Restart terminal/command prompt, then run:
conda --version
```

## 🐍 Python Environment Setup with Conda

### Step 1: Create and Activate Conda Environment

#### 1.1 Create Environment
```bash
# Create new conda environment with Python 3.11 or higher
conda create --name pf python=3.11

# Activate the environment
conda activate pf
```

#### 1.2 Verify Environment
```bash
# Check Python version
python --version
# Should show: Python 3.11.x

# Check pip version
pip --version
```

### Step 2: Install PromptFlow Dependencies

#### 2.1 Install Core PromptFlow Packages
```bash
# Install promptflow and related packages
pip install promptflow promptflow-tools promptflow-azure
```

#### 2.2 Alternative: Install from Requirements File
```bash
# Navigate to project directory
cd "Simple-Prompt-Flow-Chat-App"

# Install all dependencies from requirements.txt
pip install -r requirements.txt --user
```

#### 2.3 Verify Installation
```bash
# Check PromptFlow version - should print promptflow version, e.g. "0.1.0b3"
pf -v

# List installed packages
pip list | grep promptflow
```

### Step 3: Configure VS Code with Conda Environment

#### 3.1 Select Python Interpreter in VS Code
1. Open VS Code in your project directory
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
3. Type "Python: Select Interpreter"
4. Choose the conda environment: `~/miniconda3/envs/pf/bin/python` (or similar path)

## Azure Setup 
- Create Azure AI Foundry Hub project in Azure AI Foundry [https://ai.azure.com/](https://ai.azure.com/)
- Deploy `gpt-4o` model 


## 🚀 Local Setup and Development


### Step 1: Azure Configuration

#### 1.1 Azure Authentication
```bash
# Install Azure CLI if not already installed
# Windows (using winget):
winget install Microsoft.AzureCLI

# macOS:
brew install azure-cli

# Ubuntu/Debian:
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Login to Azure
az login

# Set default subscription (if needed)
az account set --subscription "your-subscription-id"

# Verify authentication
az account show
```

#### 1.2 Configure PromptFlow for Azure
```bash
# Set PromptFlow configuration
pf config set cloud.subscription_id="your-subscription-id"
pf config set cloud.resource_group="your-resource-group"
pf config set cloud.workspace_name="your-ai-studio-project"

# Verify configuration
pf config show
```

#### 1.3 Create Azure AI Foundry Connection

**Option A: Using PromptFlow CLI**
```bash
# Create connection file
cat > connection.yaml << EOF
name: ai-foundry-resource_aoai
type: azure_open_ai
api_base: https://your-openai-service.openai.azure.com/
api_key: your-api-key
api_version: 2024-02-15-preview
EOF

# Create connection
pf connection create --file connection.yaml
```

**Option B: Using VS Code Extension**
1. Open VS Code in your project
2. Click the PromptFlow icon in the sidebar
3. Go to "Connections" section
4. Click "+" to add new connection
5. Select "Azure OpenAI" and fill in details:
   - Name: `ai-foundry-resource_aoai`
   - API Base: Your Azure OpenAI endpoint
   - API Key: Your API key
   - API Version: `2024-02-15-preview`


#### 1.4 Verify Connection
```bash
# List all connections
pf connection list

# Test specific connection
pf connection show --name ai-foundry-resource_aoai
```

### Step 2: Test Local Setup

#### 2.1 Test Chat Flow
```bash
# Navigate to chat flow
cd chat-flow

# Test with single question
pf flow test --flow . --inputs question="What are the best places to visit in Japan during cherry blossom season?"

# Run quick validation test
python quick_test.py

# Run comprehensive test suite
python test_chat_flow.py

# Interactive testing
pf flow test --flow . --interactive
```

#### 2.2 Test Evaluation Flow
```bash
# Navigate to evaluation flow
cd ../evaluation-flow

# Run standalone evaluation
python run_evaluation.py

# Run end-to-end chat and evaluation
python run_chat_and_evaluate.py
```

#### 2.3 Open in VS Code Visual Editor
```bash
# Open VS Code in project directory
code .

# In VS Code:
# 1. Navigate to chat-flow/flow.dag.yaml
# 2. Click "Open in Visual Editor" button
# 3. View and edit the flow graphically
```


## 🔨 Build and Deployment Options

### Build Options

#### Option 1: Build Using PromptFlow CLI

##### 1.1 Build Chat Flow as Docker
```bash
# Navigate to chat flow directory
cd chat-flow

# Build flow as docker format
pf flow build --source . --output ../dist/chat-flow --format docker

# Build evaluation flow as docker format
cd ../evaluation-flow
pf flow build --source . --output ../dist/evaluation-flow --format docker
```

##### 1.2 Docker Build Structure
After building, you'll get this structure:
```
dist/
├── chat-flow/
│   ├── flow/                  # Flow files
│   ├── connections/           # Connection configurations
│   ├── Dockerfile            # Docker build file
│   ├── start.sh              # Startup script
│   ├── runit/                # Service management
│   ├── settings.json         # Docker image settings
│   └── README.md             # Docker deployment guide
└── evaluation-flow/
    └── [similar structure]
```

#### Option 2: Build Using VS Code Extension

1. **Open VS Code** in your project directory
2. **Navigate to flow.dag.yaml** in either chat-flow or evaluation-flow
3. **Click Build button** in the flow designer toolbar
4. **Select "Build as Docker"** as the Build type
5. **Choose output directory** for the Docker build

### Deployment Options

#### Option 1: Local Docker Deployment

##### 1.1 Build Docker Images
```bash
# Build chat-flow docker image
cd dist/chat-flow
docker build . -t travel-chat-bot

# Build evaluation-flow docker image
cd ../evaluation-flow
docker build . -t travel-evaluation
```

##### 1.2 Run Locally with Docker

**Run Chat Bot with Flask (Default):**
```bash
# Run chat bot container
docker run -p 8080:8080 \
  -e OPEN_AI_CONNECTION_API_KEY=your-api-key \
  -e PROMPTFLOW_WORKER_NUM=8 \
  -e PROMPTFLOW_WORKER_THREADS=1 \
  travel-chat-bot
```

**Run Chat Bot with FastAPI:**
```bash
# Run with FastAPI serving engine
docker run -p 8080:8080 \
  -e OPEN_AI_CONNECTION_API_KEY=your-api-key \
  -e PROMPTFLOW_SERVING_ENGINE=fastapi \
  -e PROMPTFLOW_WORKER_NUM=8 \
  travel-chat-bot
```

##### 1.3 Test Local Deployment
```bash
# Test the endpoint
curl http://localhost:8080/score \
  --data '{"question": "What should I pack for a trip to Iceland?", "chat_history": []}' \
  -X POST \
  -H "Content-Type: application/json"
```

#### Option 2: Kubernetes Deployment

##### 2.1 Prerequisites
```bash
# Install kubectl
# Windows (using winget):
winget install Kubernetes.kubectl

# macOS:
brew install kubectl

# Ubuntu/Debian:
sudo apt-get update && sudo apt-get install -y kubectl

# Install Minikube for local testing
# Windows:
winget install Kubernetes.minikube

# macOS:
brew install minikube

# Ubuntu/Debian:
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

##### 2.2 Create Kubernetes Deployment

**Create `deployment.yaml`:**
```yaml
---
kind: Namespace
apiVersion: v1
metadata:
  name: travel-chat-app
---
apiVersion: v1
kind: Secret
metadata:
  name: openai-connection-secret
  namespace: travel-chat-app
type: Opaque
data:
  # Base64 encoded API key: echo -n "your-api-key" | base64
  api-key: <your-base64-encoded-api-key>
---
apiVersion: v1
kind: Service
metadata:
  name: travel-chat-service
  namespace: travel-chat-app
spec:
  type: NodePort
  ports:
  - name: http
    port: 8080
    targetPort: 8080
    nodePort: 30123
  selector:
    app: travel-chat-bot
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: travel-chat-deployment
  namespace: travel-chat-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: travel-chat-bot
  template:
    metadata:
      labels:
        app: travel-chat-bot
    spec:
      containers:
      - name: travel-chat-container
        image: travel-chat-bot:latest
        imagePullPolicy: Never
        ports:
        - containerPort: 8080
        env:
        - name: OPEN_AI_CONNECTION_API_KEY
          valueFrom:
            secretKeyRef:
              name: openai-connection-secret
              key: api-key
        - name: PROMPTFLOW_WORKER_NUM
          value: "4"
        - name: PROMPTFLOW_SERVING_ENGINE
          value: "fastapi"
```

##### 2.3 Deploy to Kubernetes
```bash
# Start minikube (for local testing)
minikube start

# Apply deployment
kubectl apply -f deployment.yaml

# Check deployment status
kubectl get pods -n travel-chat-app
kubectl get services -n travel-chat-app

# Get service URL (Minikube)
minikube service travel-chat-service --url -n travel-chat-app
```

##### 2.4 Test Kubernetes Deployment
```bash
# Port forward for testing
kubectl port-forward svc/travel-chat-service 8080:8080 -n travel-chat-app

# Test endpoint
curl http://localhost:8080/score \
  --data '{"question": "Best time to visit Japan?", "chat_history": []}' \
  -X POST \
  -H "Content-Type: application/json"
```

#### Option 3: Azure Container Instances (ACI)

##### 3.1 Build and Push to Azure Container Registry
```bash
# Create Azure Container Registry
az acr create --resource-group your-rg --name yourregistry --sku Basic

# Login to ACR
az acr login --name yourregistry

# Tag and push image
docker tag travel-chat-bot yourregistry.azurecr.io/travel-chat-bot:latest
docker push yourregistry.azurecr.io/travel-chat-bot:latest
```

##### 3.2 Deploy to Azure Container Instances
```bash
# Deploy to ACI
az container create \
  --resource-group your-rg \
  --name travel-chat-aci \
  --image yourregistry.azurecr.io/travel-chat-bot:latest \
  --registry-login-server yourregistry.azurecr.io \
  --registry-username yourregistry \
  --registry-password $(az acr credential show --name yourregistry --query "passwords[0].value" -o tsv) \
  --dns-name-label travel-chat-unique \
  --ports 8080 \
  --environment-variables \
    OPEN_AI_CONNECTION_API_KEY=your-api-key \
    PROMPTFLOW_WORKER_NUM=4 \
    PROMPTFLOW_SERVING_ENGINE=fastapi

# Get URL
az container show --resource-group your-rg --name travel-chat-aci --query ipAddress.fqdn -o tsv
```

#### Option 4: Azure App Service

##### 4.1 Create App Service Plan
```bash
# Create App Service Plan
az appservice plan create \
  --name travel-chat-plan \
  --resource-group your-rg \
  --sku B1 \
  --is-linux

# Create Web App
az webapp create \
  --resource-group your-rg \
  --plan travel-chat-plan \
  --name travel-chat-webapp \
  --deployment-container-image-name yourregistry.azurecr.io/travel-chat-bot:latest
```

##### 4.2 Configure App Service
```bash
# Set container registry credentials
az webapp config container set \
  --name travel-chat-webapp \
  --resource-group your-rg \
  --container-image-name yourregistry.azurecr.io/travel-chat-bot:latest \
  --container-registry-url https://yourregistry.azurecr.io \
  --container-registry-user yourregistry \
  --container-registry-password $(az acr credential show --name yourregistry --query "passwords[0].value" -o tsv)

# Set environment variables
az webapp config appsettings set \
  --resource-group your-rg \
  --name travel-chat-webapp \
  --settings \
    OPEN_AI_CONNECTION_API_KEY=your-api-key \
    PROMPTFLOW_WORKER_NUM=4 \
    PROMPTFLOW_SERVING_ENGINE=fastapi \
    WEBSITES_PORT=8080

# Get app URL
az webapp show --resource-group your-rg --name travel-chat-webapp --query defaultHostName -o tsv
```

### Environment Variables Configuration

For all deployment options, you'll need these environment variables:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPEN_AI_CONNECTION_API_KEY` | Azure OpenAI API Key | - | Yes |
| `PROMPTFLOW_WORKER_NUM` | Number of worker processes | 8 | No |
| `PROMPTFLOW_WORKER_THREADS` | Threads per worker (Flask only) | 1 | No |
| `PROMPTFLOW_SERVING_ENGINE` | Serving engine (`flask` or `fastapi`) | `flask` | No |
| `WEBSITES_PORT` | Port for App Service | - | App Service only |

## 🔧 Advanced Configuration

### Custom Docker Configuration

#### Multi-stage Dockerfile Example
```dockerfile
# Custom Dockerfile for optimized builds
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim as runtime

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY flow/ ./flow/
COPY connections/ ./connections/
COPY start.sh ./

EXPOSE 8080
CMD ["./start.sh"]
```

### Production Considerations

#### Security Best Practices
```bash
# Use Azure Key Vault for secrets
az keyvault secret set --vault-name your-keyvault --name openai-api-key --value your-api-key

# Use managed identity in Azure deployments
az webapp identity assign --resource-group your-rg --name travel-chat-webapp
```

#### Monitoring and Logging
```bash
# Enable Application Insights
az extension add --name application-insights
az monitor app-insights component create \
  --app travel-chat-insights \
  --location eastus \
  --resource-group your-rg
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. Conda Environment Issues
```bash
# Conda command not found
export PATH="~/miniconda3/bin:$PATH"  # Add to ~/.bashrc or ~/.zshrc

# Environment activation problems
conda init bash  # or zsh, powershell
# Restart terminal

# Package conflicts
conda clean --all
conda create --name pf python=3.9 --force
```

#### 2. PromptFlow Installation Issues
```bash
# Permission errors
pip install --user promptflow promptflow-tools promptflow-azure

# Version conflicts
pip uninstall promptflow promptflow-tools promptflow-azure
pip install promptflow promptflow-tools promptflow-azure --no-cache-dir

# Connection keyring issues (WSL/Linux)
sudo apt-get install gnome-keyring  # Ubuntu/Debian
# or
pip install keyrings.alt
```

#### 3. Azure Connection Problems
```bash
# Re-authenticate
az logout
az login --use-device-code

# Check connection
pf connection test --name ai-foundry-resource_aoai

# Recreate connection
pf connection delete --name ai-foundry-resource_aoai
pf connection create --file connection.yaml
```

#### 4. Docker Build Issues
```bash
# Build context too large
echo "node_modules\n.git\n*.pyc\n__pycache__" > .dockerignore

# Permission denied
sudo docker build . -t travel-chat-bot

# Port already in use
docker ps  # Find container using port
docker stop <container-id>
```

#### 5. VS Code Extension Issues
```bash
# Extension not working
# 1. Reload VS Code window (Ctrl+Shift+P -> "Developer: Reload Window")
# 2. Check Python interpreter is set to conda environment
# 3. Verify PromptFlow extension is enabled

# Visual editor not opening
# 1. Right-click on flow.dag.yaml
# 2. Select "Open With" -> "Prompt Flow Visual Editor"
```

## 📚 Additional Resources

### Official Documentation
- **[PromptFlow Quick Start](https://github.com/microsoft/promptflow/blob/main/docs/how-to-guides/develop-a-dag-flow/quick-start.md)**
- **[PromptFlow Documentation](https://microsoft.github.io/promptflow/)**
- **[Deploy a Flow Guide](https://github.com/microsoft/promptflow/tree/main/docs/how-to-guides/deploy-a-flow)**
- **[Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)**
- **[Azure AI Studio](https://azure.microsoft.com/en-us/products/ai-studio/)**

### Tutorials and Examples
- **[PromptFlow Examples](https://github.com/microsoft/promptflow/tree/main/examples)**
- **[Getting Started Notebook](https://microsoft.github.io/promptflow/tutorials/quickstart.html)**
- **[Chat with PDF Tutorial](https://microsoft.github.io/promptflow/tutorials/chat-with-pdf.html)**
- **[Deployment Examples](https://github.com/microsoft/promptflow/tree/main/examples/tutorials/flow-deploy)**

## 🎯 Next Steps

1. **🔍 Explore Flows**: Review individual [chat-flow](./chat-flow/README.md) and [evaluation-flow](./evaluation-flow/README.md) documentation
2. **🎨 Customize Prompts**: Modify `chat.jinja2` for your specific travel use case
3. **📊 Extend Evaluation**: Add new evaluation criteria or metrics
4. **🚀 Deploy to Production**: Choose your preferred deployment option
5. **🔗 Integrate**: Connect to web applications or chat interfaces
6. **📈 Monitor**: Set up monitoring and performance tracking
7. **🔄 Iterate**: Use evaluation feedback to improve the chat experience

## 📝 License

These samples are provided for educational and demonstration purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Add tests for new functionality
5. Commit your changes (`git commit -am 'Add some feature'`)
6. Push to the branch (`git push origin feature/your-feature`)
7. Create a Pull Request

