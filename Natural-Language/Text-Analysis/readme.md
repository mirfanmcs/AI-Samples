# Text Analysis

A sample application that uses Azure AI Foundry Language Service for Text Analysis. It analyzes text files for language detection, sentiment analysis, key phrases extraction, detect entities, and linked entities.


## Overview

This application performs the following tasks:
- Loads environment variables from a `.env` file
- Connects to Azure AI Foundry Language Service using endpoint and key
- Reads all text files in the `reviews` folder
- For each review file:
  - Prints the file name and contents
  - Detects the language of the text
  - Analyzes sentiment (positive, negative, neutral, mixed)
  - Extracts key phrases from the text
  - Recognizes named entities (person, location, organization, etc.)
  - Finds linked entities (entities with associated URLs)
- Displays results in the console


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- An Azure AI Language service

## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry Language Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/)


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Language Service Endpoint
LANGUAGE_SERVICE_ENDPOINT=https://your-language-service-name.cognitiveservices.azure.com/
LANGUAGE_SERVICE_KEY=your-language-service-key
```

**How to find these values:**

- **LANGUAGE_SERVICE_ENDPOINT**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "Endpoint"
- **LANGUAGE_SERVICE_KEY**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "KEY 1"

## Running the Application

1. Run the application:
   ```bash
   python app.py
   ```

2. View the analysis results for each file in the console output.


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
├── install.sh          # Installation script
└── reviews/            # Folder containing text files to analyze
```


## License

These samples are provided for educational and demonstration purposes.