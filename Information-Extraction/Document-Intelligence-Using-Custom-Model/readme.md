# Document Intelligence Using Prebuild Model

A sample application that uses Azure AI Foundry Document Intelligence Service custom model to analyze, extract, and structure information from documents. It supports processing forms, invoices, receipts, and other document types using advanced AI models.

## Overview

This application:
- Accepts a document image file path as a command-line argument (defaults to docs/test1.jpg).
- Initializes the Azure `DocumentAnalysisClient`.
- Sends the document image to Azure for analysis using a custom model.
- Waits for the analysis to complete and retrieves results.
- Prints document type, confidence, model ID, and extracted fields with their values and confidence.


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- Document intelligence service


## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry Document Intelligence Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/). Enable system managed identity when you create service. 
- Create the storage account in the same region where you created document intelligence service
- Open storage account you created. Under Access Control (IAM), give `Storage Blob Data Contributor` role to the managed identity of your document intelligence resource. 
- Create the blob container in your storage account and upload all files under `sample-forms` folder. This data will be used to train the custom model. Note that training data includes `.labels.json` and `.ocr.json` files. Additionaly it incldues `fields.json` file. These will be used to train model. You can generate these files for your training data using the document intelligence pre built models. 
- Open Document Intelligence Studio on [https://documentintelligence.ai.azure.com/studio](https://documentintelligence.ai.azure.com/studio).
- Create a project under Custom models → Custom extraction model.
- Select your storage account under training data source.
- Once the project is created, click Train. Under Build Mode, select `Template`. Note down the Model ID - it will be used in the API call to analyze the document.


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# Document Intelligence Endpoint
DOC_INTELLIGENCE_ENDPOINT=https://your-document-intellgence-resource-name.cognitiveservices.azure.com/
DOC_INTELLIGENCE_KEY=your-document-intellgence-key
MODEL_ID=your-model-id
```

**How to find these values:**

- **DOC_INTELLIGENCE_ENDPOINT**: In Azure portal, go to your document intelligence service you created → Keys and Endpoint → find the "Endpoint"
- **DOC_INTELLIGENCE_KEY**: In Azure portal, go to your document intelligence Service you created → Keys and Endpoint → find the "KEY 1"
- **MODEL_ID**: Under project in Azure Document Intellgence Studio  → Models → find "Model ID"


## Running the Application

1. Run the application:
   ```bash
   python app.py docs/test1.jpg
   ```


## Dependencies

- `python-dotenv`: For loading environment variables from .env file
- `azure-ai-formrecognizer`: AI Form Recognizer`
- `azure-identity`: Azure authentication library

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Verify your account has access to the Azure AI Foundry project
2. Check that your DOC_INTELLIGENCE_ENDPOINT and DOC_INTELLIGENCE_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade python-dotenv azure-identity azure-ai-formrecognizer==3.3.3`

## Project Structure

```
Document-Intelligence-Using-Custom-Model/
├── app.py              # Main application file
├── requirements.txt     # Python dependencies
├── readme.md            # This file
├── install.sh           # Installation script (if applicable)
├── docs/                # Sample form to analyse
├── sample-form/         # Sample forms to train the model
└── .env                 # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.