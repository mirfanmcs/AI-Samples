# Custom Named Entity Recognition

A sample application that uses Azure AI Foundry Language Service for custom named entity recognition. It reads ads and extract entities using Azure Text Analytics.


## Overview

This application performs the following tasks:
- Loads environment variables from a .env file using dotenv.
- Retrieves Azure Language Service endpoint, key, NER project name, and deployment name from environment variables.
- Creates an Azure Text Analytics client using the endpoint and key.
- Reads all text files in the ads folder and stores their contents in a list (`batchedDocuments`).
- Calls Azure's custom entity recognition API (`begin_recognize_custom_entities`) on the batch of ad texts, using the specified NER project and deployment.
- Waits for the operation to complete and gets the results.
- Iterates through each file and its corresponding result:
- If the result is successful, prints each recognized entity, its category, and confidence score.
- If there is an error, prints the error code and message.
- Runs the main function if the script is executed directly.


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
- Create `Custom named entity recognition extraction` project in Language Studio portal [https://language.cognitive.azure.com/](https://language.cognitive.azure.com/)
- Open the project in Language Studio, in Activity pane under Add entity add `ItemForSale`, `Price`, and `Location` entities.
- Click document `Ad 1.txt` to open the document. 
  - Highlight the text `face cord of firewood` and select the `ItemForSale` entity.
  - Highlight the text `Denver, CO` and select the `Location` entity.
  - Highlight the text `$90` and select the `Price` entity.
- Repeat above step for all documents.
- Click on Start training job under Training job to jobs to train the model. Choose auto splitting option.
- Deploy your model under Deploying model pane. Give it a name. Note down deployment name and project name.


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Language Service Endpoint
LANGUAGE_SERVICE_ENDPOINT=https://your-language-service-name.cognitiveservices.azure.com/
LANGUAGE_SERVICE_KEY=your-language-service-key
NER_PROJECT_NAME=Custom named entity recognition project name you created in Language Studio
NER_DEPLOYMENT_NAME=Custom named entity recognition deployment name of custom named entity recognition project in Language Studio
```

**How to find these values:**

- **LANGUAGE_SERVICE_ENDPOINT**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "Endpoint"
- **LANGUAGE_SERVICE_KEY**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "KEY 1"
- **NER_PROJECT_NAME**: In Language Studio, find the custom named entity recognition project name
- **NER_DEPLOYMENT_NAME**: In Language Studio, find the custom named entity recognition deployment name

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
Custom-Named-Entity-Recognition/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── readme.md            # This file
├── ads                  # Ads for entity recognition
├── training-data        # Training data to train the model
└── install.sh           # Installation script
```


## License

These samples are provided for educational and demonstration purposes.