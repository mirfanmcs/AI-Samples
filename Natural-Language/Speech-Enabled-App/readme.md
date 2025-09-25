# Speech Enabled App

A sample application that uses Azure AI Foundry Speech Service to enable speech in applications. It can transcribe spoken commands from audio files or microphone and synthesize speech responses.


## Overview

This application performs the following tasks:
- Loads environment variables for Azure Speech Service credentials and region using `dotenv`.
- Initializes Azure Speech Service configuration with the loaded credentials.
- Defines functions to transcribe spoken commands from a WAV file (`TranscribeCommand_from_speech_file`) and from the microphone - (`TranscribeCommand_from_mic`).
- Defines synthesize_speech to respond with the current time using speech synthesis if the recognized command is "what time is it?" (from WAV file).
- Defines `synthesize_with_customization` to respond with the current time and a custom SSML message ("Time to end this lab!") using a different voice, if the command matches.
- Defines `synthesize_speech_mic_speaker` to respond with the current time using speech synthesis through the default speaker, triggered by the spoken command from the microphone.




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
2. Listen generated `output.wav` and `output_with_customization.wav`. Listen to output from speaker

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
2. Try upgrading packages: `pip install --upgrade azure-identity azure-cognitiveservices-speech==1.42.0`

## Project Structure

```
Speech-Enabled-App/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── readme.md            # This file
├── time.wav             # Test wav file
└── install.sh           # Installation script
```


## License

These samples are provided for educational and demonstration purposes.