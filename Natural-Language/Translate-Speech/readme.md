# Translate Speech

A sample application that uses Azure AI Foundry Speech Service for real-time speech translation. It translates spoken English into French, Spanish, and Hindi, and can synthesize translated audio output or play it live.


## Overview

This application performs the following tasks:
- Creates a `SpeechTranslationConfig` for source language `en-US` and target languages `fr`, `es`, `hi`.
- Creates a separate `SpeechConfig` for text-to-speech synthesis.
- Runs two one-shot flows in sequence: (1) translate from station.wav and save synthesized result to output.wav, (2) live mic - translation and speak result to default speaker.
- Selects a neural voice per language (Henri, Elvira, Madhur) before synthesis.
- Writes audio to file for the first flow; plays directly to speaker for the second.


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- An Azure AI Speech Service

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
# AI Foundry Speech Service Endpoint
SPEECH_SERVICE_REGION=your-speech-service-region
SPEECH_SERVICE_KEY=your-speech-service-key
```

**How to find these values:**

- **SPEECH_SERVICE_REGION**: In Azure portal, go to your speech Service you created → Keys and Endpoint → find the "Location/Region"
- **SPEECH_SERVICE_KEY**: In Azure portal, go to your speech Service you created → Keys and Endpoint → find the "KEY 1"

## Running the Application

1. Run the application:
   ```bash
   python app.py
   ```
2. Listen generated `output.wav`. Listen to output from speaker

## Dependencies

- `azure-cognitiveservices-speech`: Azure AI Speech Service
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Check that your SPEECH_SERVICE_REGION is correct
3. Check that your SPEECH_SERVICE_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade azure-identity azure-cognitiveservices-speech`

## Project Structure

```
Text-Analysis/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── readme.md            # This file
├── station.wav             # Test wav file
└── install.sh           # Installation script
```


## License

These samples are provided for educational and demonstration purposes.