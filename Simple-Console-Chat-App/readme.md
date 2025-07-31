# Azure OpenAI Simple Console Chat Application

A simple Python console chat application that demonstrates how to interact with Azure OpenAI services using the GPT-4o model for chat completions.

## Overview

This project showcases a basic implementation of Azure OpenAI integration, featuring:
- Chat completion with streaming output
- Environment-based configuration
- Multi-turn conversation handling
- Error handling and best practices

## Prerequisites

- Python 3.7 or higher
- An Azure OpenAI resource with a deployed GPT-4o model
- Valid Azure OpenAI API key and endpoint

## Project Structure

```
.
├── .env                 # Environment variables (not tracked in git)
├── install.sh          # Installation script for dependencies
├── requirements.txt    # Python dependencies
├── run_model.py        # Main application file
└── README.md           # This file
```

## Setup Instructions

### 1. Clone or Download the Project

Ensure you have all the project files in your working directory.

### 2. Install Dependencies

#### Using the install script (Linux/macOS):
```bash
chmod +x install.sh
./install.sh
```

#### Manual installation:
```bash
pip install -r requirements.txt --user
```

#### Using pip directly:
```bash
pip install openai~=1.60.2 python-dotenv~=1.0.0
```

### 3. Configure Environment Variables

The `.env` file contains your Azure OpenAI configuration. Update it with your actual values:

```env
ENDPOINT_URL="https://your-resource-name.cognitiveservices.azure.com/openai/deployments/your-deployment/chat/completions?api-version=2025-01-01-preview"
DEPLOYMENT_NAME="your-deployment-name"
AZURE_OPENAI_API_KEY="your-api-key"
```

**Important**: Never commit the `.env` file to version control as it contains sensitive API keys.

## Running the Application

Execute the main script:

```bash
python run_model.py
```

The application will:
1. Load configuration from the `.env` file
2. Initialize the Azure OpenAI client
3. Send a predefined conversation to the model
4. Stream the response in real-time
5. Close the connection

## Code Features

### Streaming Output
The application uses streaming mode (`stream=True`) to display the response in real-time as it's generated.

### Multi-turn Conversation
The code includes a conversation history with:
- System message defining the AI's role
- Previous user questions about Paris
- Assistant responses
- A follow-up question

### Configuration Parameters
- **Temperature**: 0.7 (controls randomness)
- **Max Tokens**: 800 (maximum response length)
- **Top P**: 0.95 (nucleus sampling)
- **Frequency/Presence Penalty**: 0 (no repetition penalties)

## Customization

### Modify the Conversation
Edit the `chat_prompt` list in [`run_model.py`](run_model.py) to change the conversation:

```python
chat_prompt = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Your custom question here"
            }
        ]
    }
]
```

### Add Image Support
Uncomment and modify the image processing section:

```python
IMAGE_PATH = "path/to/your/image.jpg"
encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
```

### Change Output Mode
Switch between streaming and direct output by modifying the `stream` parameter:

```python
# For direct output
stream=False

# For streaming output
stream=True
```

## Security Best Practices

1. **Never hardcode API keys** in your source code
2. **Use environment variables** for sensitive configuration
3. **Add `.env` to `.gitignore`** to prevent accidental commits
4. **Rotate API keys regularly**
5. **Use least privilege access** for your Azure OpenAI resource

## Troubleshooting

### Common Issues

1. **Import Error**: Ensure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Authentication Error**: Verify your API key and endpoint URL in `.env`

3. **Model Not Found**: Check that your deployment name matches the one in Azure

4. **Permission Error**: Ensure your API key has the necessary permissions

### Error Handling
The current implementation doesn't include comprehensive error handling. Consider adding try-catch blocks for production use.

## Dependencies

- **openai**: Official OpenAI Python client library
- **python-dotenv**: Load environment variables from .env file
- **ansible-core**: (Note: This seems unrelated to the project and may be removed)

## License

These samples are provided for educational and demonstration purposes.

## Contributing

Feel free to submit issues and pull requests to improve this example application.