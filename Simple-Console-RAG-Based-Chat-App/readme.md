# Azure OpenAI Simple Console RAG Based Chat Application

A simple Python console application that demonstrates how to interact with Azure OpenAI's chat completion API using RAG pattern. This application provides a command-line interface for having conversations with an AI assistant.

## Features

- Interactive console chat interface
- Streaming responses for real-time output
- Conversation history maintained throughout the session
- Environment variable configuration for Azure OpenAI credentials
- Simple and clean code structure

## Prerequisites

- Python 3.7 or higher
- Azure OpenAI service instance
- Azure OpenAI API key and endpoint

## Installation

### Option 1: Using the install script (Linux/macOS)
```bash
chmod +x install.sh
./install.sh
```

### Option 2: Manual installation
```bash
pip install -r requirements.txt --user
```

### Option 3: Using virtual environment (recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt --user
```

## Azure Setup 
- Create Azure AI Foundry Hub project in Azure AI Foundry [https://ai.azure.com/](https://ai.azure.com/)
- Deploy `gpt-4o` model 
- Deploy `text-embedding-ada-002` model
- Create Azure AI Search Service
- Upload PDFs `brochures` folder from `/rag-data` under `Data+Index` in your AI Foundry Hub project 
- Create vector index name `brochures-index` on brochures data under `Data+Index` in your AI Foundry Hub project. Connect to AI Search service you created. 


## Configuration

1. Create a `.env` file in the project root directory with the following content:

```env
ENDPOINT_URL=your_azure_openai_endpoint_url
DEPLOYMENT_NAME=your_deployment_name
AZURE_OPENAI_API_KEY=your_api_key
EMBEDDING_MODEL=your_embedding_model
SEARCH_ENDPOINT=your_search_endpoint
SEARCH_KEY=your_search_api_key
INDEX_NAME=your_index
```

2. Replace the placeholder values with your actual Azure OpenAI credentials:
   - `ENDPOINT_URL`: Your Azure OpenAI service endpoint (e.g., `https://your-resource.openai.azure.com/`)
   - `DEPLOYMENT_NAME`: The name of your deployed model (e.g., `gpt-4`, `gpt-35-turbo`)
   - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
   - `EMBEDDING_MODEL`: Your_embedding model name (e.g., `text-embedding-ada-002`)
   - `SEARCH_ENDPOINT`: Your AI Search Endpoint
   - `SEARCH_KEY`: Your AI Search API Key
   - `INDEX_NAME`: Your Index name

## Usage

1. Ensure you have configured the `.env` file with your Azure OpenAI credentials
2. Run the application:

```bash
python app.py
```

3. The application will start and prompt you to enter a message
4. Type your message and press Enter to send it to the AI
5. The AI's response will be streamed in real-time
6. Continue the conversation by entering more messages
7. Type `quit` to exit the application

### Example Session

```
Enter the prompt (or type 'quit' to exit): Hello, how are you?
Hello! I'm doing well, thank you for asking. I'm here and ready to help you with any questions or tasks you might have. How are you doing today?

Enter the prompt (or type 'quit' to exit): What can you help me with?
I can help you with a wide variety of tasks including:

- Answering questions on various topics
- Writing and editing text
- Coding assistance and debugging
- Problem-solving and analysis
- Creative writing and brainstorming
- Educational explanations
- And much more!

Is there something specific you'd like assistance with today?

Enter the prompt (or type 'quit' to exit): quit
```

## Project Structure

```
Simple-Console-Chat-App/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── install.sh         # Installation script for Linux/macOS
├── readme.md          # This file
└── .env               # Environment variables (create this file)
```

## Dependencies

- `openai~=1.60.2`: Official OpenAI Python library for API interactions
- `python-dotenv~=1.0.0`: For loading environment variables from .env file

## Configuration Options

The application uses the following Azure OpenAI API parameters:

- `max_tokens`: 800 (maximum response length)
- `temperature`: 0.7 (response creativity/randomness)
- `top_p`: 0.95 (nucleus sampling parameter)
- `frequency_penalty`: 0 (penalize frequent tokens)
- `presence_penalty`: 0 (penalize present tokens)
- `stream`: True (enable streaming responses)

You can modify these parameters in the `app.py` file to customize the AI's behavior.

## Troubleshooting

### Common Issues

1. **Missing .env file**: Ensure you have created a `.env` file with the required environment variables
2. **Invalid credentials**: Verify your Azure OpenAI endpoint, deployment name, and API key
3. **Network issues**: Check your internet connection and firewall settings
4. **Package installation errors**: Ensure you have Python 3.7+ and pip installed

### Error Messages

- `"Please enter a prompt."`: You entered an empty message, try typing something
- Connection errors: Check your internet connection and Azure OpenAI service status
- Authentication errors: Verify your API key and endpoint URL in the `.env` file

## Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes.

## License

These samples are provided for educational and demonstration purposes.