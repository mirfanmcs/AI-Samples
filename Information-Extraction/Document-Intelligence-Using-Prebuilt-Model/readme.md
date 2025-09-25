# Document Intelligence Using Prebuilt Model

A sample application that uses Azure AI Foundry Document Intelligence Service pre build model to analyze, extract, and structure information from documents. It supports processing forms, invoices, receipts, and other document types using advanced AI models.


## Overview

This application:
- Reads a local invoice PDF file (default or from command-line)
- Connects to Azure Document Intelligence service
- Analyzes the invoice using a prebuilt model
- Extracts vendor name, customer name, and invoice total
- Prints extracted data and confidence scores to the console
  

## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- An Azure AI Foundry Hub and project


## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry Hub and project in Azure AI Foundry [https://ai.azure.com/](https://ai.azure.com/)


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Hub Project Endpoint
AI_ENDPOINT=https://your-ai-foundry-resource-name..cognitiveservices.azure.com/
AI_KEY=your-ai-serice-key

```

**How to find these values:**

- **AI_ENDPOINT**: In Azure AI Foundry, go to your hub project → Overview → find the "Azure AI Services"
- **AI_KEY**: In Azure AI Foundry, go to your hub project → Overview → find "API Key"



## Running the Application

1. Run the application:
   ```bash
   python app.py docs/sample-invoice.pdf
   ```


## Dependencies

- `python-dotenv`: For loading environment variables from .env file
- `azure-ai-formrecognizer`: AI Form Recognizer`
- `azure-identity`: Azure authentication library

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Verify your account has access to the Azure AI Foundry project
2. Check that your AI_ENDPOINT and AI_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade python-dotenv azure-identity azure-ai-formrecognizer==3.3.3`

## Project Structure

```
Document-Intelligence-Using-Prebuilt-Model/
├── app.py              # Main application file
├── requirements.txt     # Python dependencies
├── readme.md            # This file
├── install.sh           # Installation script (if applicable)
├── docs/                # Sample document to analyse
└── .env                 # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.