# Conversational-Language-Understanding

A sample application that uses Azure AI Foundry Language Service for conversational language understanding. it uses Conversation Analysis API to detect intent and extract entities.


## Overview

This application performs the following tasks:
- Loads environment variables from a .env file for Azure Language Service configuration.
- Initializes an Azure Conversational Language Understanding client using endpoint and key.
- Prompts the user for text input in a loop until "quit" is entered.
- Sends user input to Azure's Conversation Analysis API to detect intent and extract entities.
- Prints the top intent, its category, confidence score, and detected entities.
- Based on the detected intent, performs one of three actions:
  - GetTime: Returns the current time for a specified location (supports a few cities).
  - GetDay: Returns the day of the week for a specified date (expects MM/DD/YYYY format).
  - GetDate: Returns the date for a specified weekday (assumes current week).
- Handles unrecognized intents by prompting the user to ask about time, day, or date.
- Closes the Azure client when finished.


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
- Create `conversational language understanding` project in Language Studio portal [https://language.cognitive.azure.com/](https://language.cognitive.azure.com/)
- Open the project you created and add folloiwng intent under `Schema definition` and `Intents` tab
  - `GetTime`
  - `GetDate`
  - `GetDay`
- Open the project you created and add folloiwng entity under `Schema definition` and `Entities` tab
  - Entity name `Location` of type `Learned` 
  - Entity name `Weekday` of type `List`. Under `List` section add weekdays `Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday` in the list with their respective synonyms `Mon, Tue, Tues, Wed, Weds, Thur, Thurs, Fri, Sat, Sun`
  - Entity name `Date` of type `Prebuilt`. Under `Prebuilt` section add prebuilt type as `DateTime`.
- Open the project you created and add folloiwng utterances under `Data labeling`
  - Select `GetTime` intent and add following utterances
    - `what's the time?`
    - `what time is it?`
    - `tell me the time`
    - `what time is it in London?`. Highlight the word `London` and select `Location` entity
    - `Tell me the time in Paris?`. Highlight the word `Paris` and select `Location` entity
    - `what's the time in New York?`. Highlight the word `New York` and select `Location` entity
  - Select `GetDay` intent and add following utterances
    - `what day is it?`
    - `what's the day?`
    - `what is the day today?`
    - `what day of the week is it?`
    - `what day was 01/01/1901?`. Highlight the word `01/01/1901` and select `Date` entity
    - `what day will it be on Dec 31st 2099?`. Highlight the word `Dec 31st 2099` and select `Date` entity
  - Select `GetDate` intent and add following utterances
    - `what date is it?`
    - `what's the date?`
    - `what is the date today?`
    - `what's today's date?`
    - `what date was it on Saturday?`. Highlight the word `Saturday` and select `Weekday` entity
    - `what date will it be on Friday?`. Highlight the word `Friday` and select `Weekday` entity
    - `what will the date be on Thurs?`. Highlight the word `Thurs` and select `Weekday` entity
- Train the model. Open the project you created, click `Training jobs` and `Start a training job`
- Deploy the model. Open the project you created, click `Deploying a model` and `Add deployment`. Give deployment name `production`
- Test the model. Open the project you created, click `Testing deployments`, select your deployment name `production`. Give folloiwng inputs.
  - `what's the time now?`
  - `tell me the time`
  - `what's the day today?`
  - `what's the time in Edinburgh?`
  - `what time is it in Tokyo?`
  - `what date is it on Friday?`
  - `what's the date on Weds?`
  - `what day was 01/01/2020?`
  - `what day will Mar 7th 2030 be?`


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Language Service Endpoint
LANGUAGE_SERVICE_ENDPOINT=https://your-language-service-name.cognitiveservices.azure.com/
LANGUAGE_SERVICE_KEY=your-language-service-key
CL_PROJECT_NAME=Conversational language understanding project name you created in Language Studio
CL_DEPLOYMENT_NAME=Dployment name of conversational language understanding model in Language Studio
```

**How to find these values:**

- **LANGUAGE_SERVICE_ENDPOINT**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "Endpoint"
- **LANGUAGE_SERVICE_KEY**: In Azure portal, go to your Language Service you created → Keys and Endpoint → find the "KEY 1"
- **CL_PROJECT_NAME**: In Language Studio, find the conversational language understanding project name
- **CL_DEPLOYMENT_NAME**: In Language Studio, find the conversational language understanding model deployment name

## Running the Application

1. Run the application:
   ```bash
   python app.py
   ```

2. Enter following questions and see response.
- `Hello`
- `What time is it?`
- `What’s the time in London?`
- `What’s the date?`
- `What date is Sunday?`
- `What day is it?`
- `What day is 01/01/2025?`


## Dependencies

- `azure-ai-language-conversations`: Azure AI conversational language understanding
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file
- `python-dateutil`: Date utilites


## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Check that your LANGUAGE_SERVICE_ENDPOINT is correct
3. Check that your LANGUAGE_SERVICE_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade azure-identity azure-ai-language-conversations`

## Project Structure

```
Conversational-Language-Understanding/
├── app.py              # Main application file
├── classes/                    # Classes
│   ├── date_time_helper.py              # Date time helper functions
├── requirements.txt    # Python dependencies
├── readme.md          # This file
└── install.sh          # Installation script
```


## License

These samples are provided for educational and demonstration purposes.