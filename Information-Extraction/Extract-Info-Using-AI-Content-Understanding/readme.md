# Extract Info Using AI Content Understanding

A sample application that uses Azure AI Foundry Content Understanding Service to extract structured information from documents and images. It leverages AI models to identify key fields, entities, and relationships within unstructured content.


## Overview

This application demonstrates how to:
- Create analyzer:
  - Reads a business card schema from biz-card.json.
  - Uses the Azure Content Understanding REST API to:
    - Delete any existing analyzer with the specified name.
    - Create a new analyzer using the provided schema.
- Extract information:
  - Selects a business card image to analyze (default or from command-line argument).
  - Reads the image file as binary data.
  - Sends the image to the Azure Content Understanding REST API using the specified analyzer.
  - Prints the extracted information to console.
  

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
OPEN_AI_ENDPOINT=https://your-ai-foundry-resource-name.openai.azure.com/
OPEN_AI_KEY=your-openai-key
ANALYZER_NAME=your-analyzer-name
```

**How to find these values:**

- **OPEN_AI_ENDPOINT**: In Azure AI Foundry, go to your hub project → Overview → find the "Azure OpenAI endpoint"
- **OPEN_AI_KEY**: In Azure AI Foundry, go to your hub project → Overview → find "API Key"
- **ANALYZER_NAME**: Name of analyzer to be created


## Running the Application

1. Create analyzer:
   ```bash
   python create-analyzer.py
   ```
   View the analyzer created under Content Understanding → Analyzer list

2. Read business card: 
   ```bash
   python read-card.py images/biz-card-1.png
   ```
   See the card details being printed on the console. Repeat this step for all images in the images folder.


## Dependencies

- `requests`: for HTTP REST calls
- `python-dotenv`: For loading environment variables from .env file


## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Verify your account has access to the Azure AI Foundry project
2. Check that your OPEN_AI_ENDPOINT and OPEN_AI_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade python-dotenv requests`

## Project Structure

```
Extract-Info-Using-AI-Content-Understanding/
├── create-analyzer.py   # Create analyzer in AI Foundry Hub project using REST API
├── read-card.py         # Extract contents using AI Foundry REST API
├── biz-card.json        # Schema of business card
├── images/              # Test business cards images
├── requirements.txt     # Python dependencies
├── readme.md            # This file
├── install.sh           # Installation script (if applicable)
└── .env                 # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.