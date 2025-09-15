# Translate Text

A sample application that uses Azure AI Foundry Translate Service to translate text between languages.


## Overview

This application performs the following tasks:
- Loads environment variables from a .env file using dotenv.
- Retrieves Azure Translator service region and key from environment variables.
- Initializes an Azure Text Translation client with the provided credentials and region.
- Fetches and displays the number of supported translation languages.
- Prompts the user to enter a target language code, validating it against supported languages.
- Enters a loop where the user can input text to translate (or type "quit" to exit).
- For each input, sends the text to Azure Translator and receives the translation.
- Prints the original text, detected source language, target language, and translated text.
- Continues until the user types "quit".


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- An Azure AI Translate Service

## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry Translate Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/). 


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Translate Service Endpoint
TRANSLATE_SERVICE_REGION=your-translate-service-region
TRANSLATE_SERVICE_KEY=your-translate-service-key
```

**How to find these values:**

- **TRANSLATE_SERVICE_REGION**: In Azure portal, go to your translate Service you created → Keys and Endpoint → find the "Location/Region"
- **TRANSLATE_SERVICE_KEY**: In Azure portal, go to your translate Service you created → Keys and Endpoint → find the "KEY 1"

## Running the Application

1. Run the application:
   ```bash
   python app.py
   ```

2. Enter target language code for example `en`. Enter text `C'est un test`. Text will be translated from french to english `This is a test`.


## Dependencies

- `azure-ai-translation-text`: Azure AI Translate Text
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Check that your TRANSLATE_SERVICE_REGION is correct
3. Check that your TRANSLATE_SERVICE_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade azure-identity azure-ai-translation-text==1.0.1`

## Project Structure

```
Text-Analysis/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── readme.md            # This file
└── install.sh           # Installation script
```


## License

These samples are provided for educational and demonstration purposes.