# Custom-Text-Classification

A sample application that uses Azure AI Foundry Language Service for text classification. It reads articles and classifies their content using Azure Text Analytics.


## Overview

This application performs the following tasks:
- Loads environment variables from a .env file using dotenv.
- Retrieves Azure Language Service endpoint, API key, project name, and deployment name from environment variables.
- Creates an Azure Text Analytics client using the endpoint and API key.
- Reads all text files in the articles folder and stores their contents in a list.
- Sends the list of article texts to Azure's Custom Text Classification model for single-label classification.
- Waits for the classification operation to complete and retrieves the results.
- For each article, prints its classification category and confidence score if successful.
- If an error occurs for any article, prints the error code and message.


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- An Azure AI Language Service

## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry Language Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/) and select `Custom text classification` under Custom features. Name the storage account associated. 
- Upgrade the associated storage account to `StorageV2` if not there.
- Open the associated storage account, create the container and upload files from the `training-data` folder. 
- Create `Custom text classification & extraction` project in Language Studio portal [https://language.cognitive.azure.com/](https://language.cognitive.azure.com/)
- Open the project in Language Studio, in Activity pane under Data Labeling add `Classifieds`, `Sports`, `News`, and `Entertainment` classes.
- Select each of the document and assign class and dataset to each of the document as: Article 1 (class: Sports, Dataset: Training), Article 2 (class: Sports, Dataset: Training), Article 3 (class: Classifieds, Dataset: Training), Article 4 (class: Classifieds, Dataset: Training), Article 5 (class: Entertainment, Dataset: Training), Article 6 (class: Entertainment, Dataset: Training), Article 7 (class: News, Dataset: Training), Article 8 (class: News, Dataset: Training), Article 9 (class: Entertainment, Dataset: Training), Article 10 (class: News, Dataset: Training), Article 11 (class: Entertainment, Dataset: Testing), Article 12 (class: News, Dataset: Testing), Article 13 (class: Sports, Dataset: Testing).
- Click on Start training job under Training job to jobs to train the model. Choose manual splitting option.
- Deploy your model under Deploying model pane. Give it a name. Note down deployment name and project name.


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Language Service Endpoint
LANGUAGE_SERVICE_ENDPOINT=https://your-language-service-name.cognitiveservices.azure.com/
LANGUAGE_SERVICE_KEY=your-language-service-key
TC_PROJECT_NAME=Custom text classification project name you created in Language Studio
TC_DEPLOYMENT_NAME=Custom text classification deployment name of Custom text classification project in Language Studio
```

**How to find these values:**

- **LANGUAGE_SERVICE_ENDPOINT**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "Endpoint"
- **LANGUAGE_SERVICE_KEY**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "KEY 1"
- **TC_PROJECT_NAME**: In Language Studio, find the Custom text classification project name
- **TC_DEPLOYMENT_NAME**: In Language Studio, find the Custom text classification deployment name

## Running the Application

1. Run the application:
   ```bash
   python app.py
   ```


## Dependencies

- `azure-ai-textanalytics`: Azure AI Text Analystics
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Check that your LANGUAGE_SERVICE_ENDPOINT is correct
3. Check that your LANGUAGE_SERVICE_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade azure-identity azure-ai-textanalytics`

## Project Structure

```
Text-Analysis/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── readme.md          # This file
├── articels           # articles for classification
├── training-data        # Training data to train the model
└── install.sh          # Installation script
```


## License

These samples are provided for educational and demonstration purposes.