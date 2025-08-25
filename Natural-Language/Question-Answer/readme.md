# Question Answer

A sample application that uses Azure AI Foundry Language Service for Question Answering. It answer questions on user input.


## Overview

This application performs the following tasks:
- Loads environment variables for Azure Language Service credentials and project info.
- Initializes an Azure QuestionAnsweringClient using the provided endpoint and key.
- Prompts the user for questions in a loop until "quit" is entered.
- Sends each question to the Azure QnA service and prints the answer, confidence score, and source.
- Displays results in the console


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
- Create Azure AI Foundry Language Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/)
- Create `Custom question answering` project in Language Studio portal [https://language.cognitive.azure.com/](https://language.cognitive.azure.com/)
- Open the project you created and add folloiwng data sources in the language project you created
  - URL `https://docs.microsoft.com/en-us/learn/support/faq`
  - Chitchat. Select `Friendly`
- Open the project you created and click `Edit knowledge base`. Add new question and enter:
  - Source: `https://docs.microsoft.com/en-us/learn/support/faq`
  - Question: `What are Microsoft credentials?`
  - Answer: `Microsoft credentials enable you to validate and prove your skills with Microsoft technologies.`
- Expand Alternate questions. Then add the alternate question `How can I demonstrate my Microsoft technology skills?`
- Expand Follow-up prompts and add the following follow-up prompt:
  - Text displayed in the prompt to the user: `Learn more about credentials`
  - Select the Create link to new pair tab, and enter this text: `You can learn more about credentials on the [Microsoft credentials page](https://docs.microsoft.com/learn/credentials/)`
  - Select `Show in contextual flow only`. This option ensures that the answer is only ever returned in the context of a follow-up question from the original certification question.
- Open the project you created and click `Deploy knowledge base`
  - projectName: The name of your project
  - deploymentName: The name of your deployment (which should be production)


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Language Service Endpoint
LANGUAGE_SERVICE_ENDPOINT=https://your-language-service-name.cognitiveservices.azure.com/
LANGUAGE_SERVICE_KEY=your-language-service-key
QA_PROJECT_NAME=QA project name you created in Language Studio
QA_DEPLOYMENT_NAME=QA deployment name of QA project in Language Studio
```

**How to find these values:**

- **LANGUAGE_SERVICE_ENDPOINT**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "Endpoint"
- **LANGUAGE_SERVICE_KEY**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "KEY 1"
- **QA_PROJECT_NAME**: In Language Studio, find the QA project name
- **QA_DEPLOYMENT_NAME**: In Language Studio, find the QA deployment name

## Running the Application

1. Run the application:
   ```bash
   python app.py
   ```

2. Enter the question `What is a learning path?`


## Dependencies

- `azure-ai-language-questionanswering`: Azure AI Question Answering
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
2. Try upgrading packages: `pip install --upgrade azure-identity azure-ai-language-questionanswering`

## Project Structure

```
Text-Analysis/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── readme.md          # This file
└── install.sh          # Installation script
```


## License

These samples are provided for educational and demonstration purposes.