# Azure OpenAI Audio Enabled UI Based Chat Application

A modern web-based chat interface for Azure OpenAI with real-time streaming responses. Built with Flask backend and vanilla JavaScript frontend, featuring a clean separation of concerns and responsive design.
This app uses browser speech recognition API in Javascript and passes the speech to text in the chat completion. You can enable speech feature using the Azure AI Speech to text service and pass the text in the prompt in chat completion. You can also use the multimodel (e.g Phi-4) and pass audio as a input. 


## 🌟 Features

- **Real-time streaming**: AI responses stream word-by-word for natural conversation flow
- **Clean architecture**: Separated frontend and backend for maintainability
- **Session management**: Each user gets their own conversation history
- **Modern UI**: Responsive design with animations and typing indicators
- **Message formatting**: Support for markdown-like formatting (bold, italic, code, lists)
- **One-click deployment**: Single command to run the entire application
- **Clear chat functionality**: Reset conversation history anytime
- **Azure OpenAI integration**: Seamless integration with Azure OpenAI services

## 📁 Project Structure

```
├── frontend/
│   ├── templates/
│   │   └── index.html          # Main chat interface template
│   └── static/
│       ├── style.css           # Modern styling and animations
│       └── script.js           # Chat functionality and streaming
├── backend/
│   └── chat_service.py         # Azure OpenAI integration service
├── app.py                      # Flask application (main entry point)
├── requirements.txt            # Python dependencies
├── install.sh                  # Installation script
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Azure OpenAI API access
- pip (Python package manager)

### 1. Clone or Download

If you have git:
```bash
git clone <repository-url>
cd Simple-UI-Chat-App
```

Or download and extract the project files.

### 2. Install Dependencies

#### Option A: Using pip (Recommended)
```bash
pip install -r requirements.txt --user
```

#### Option B: Using the install script (Linux/Mac)
```bash
chmod +x install.sh
./install.sh
```

#### Option C: Manual installation
```bash
pip install flask flask-cors openai python-dotenv
```

### 3. Azure Setup 
- Create Azure Open AI resource in [https://portal.azure.com/](https://portal.azure.com/)
- Deploy `gpt-4o` model 


### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
ENDPOINT_URL=https://your-resource.openai.azure.com/
DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_API_KEY=your-api-key
```

**How to get these values:**

1. **ENDPOINT_URL**: Go to Azure Portal → Your OpenAI Resource → Keys and Endpoint
2. **DEPLOYMENT_NAME**: The name you gave your model deployment (e.g., "gpt-4", "gpt-35-turbo")
3. **AZURE_OPENAI_API_KEY**: From the same Keys and Endpoint page

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`

Open your web browser and navigate to that URL to start chatting!

## 🎯 Usage

1. **Start chatting**: Type your message in the input box and press Enter
2. **See real-time responses**: Watch as the AI responds word by word
3. **Use formatting**: The AI's responses support basic markdown formatting
4. **Clear chat**: Click the "Clear Chat" button to start a new conversation
5. **Multi-line input**: Use Shift+Enter to add new lines in your message

## 🛠️ Technical Details

### Backend Architecture

- **Flask**: Lightweight web framework for Python
- **Server-Sent Events (SSE)**: Real-time streaming of AI responses
- **Session Management**: Each browser session maintains its own conversation history
- **Azure OpenAI Client**: Official OpenAI Python client with Azure support

### Frontend Architecture

- **Vanilla JavaScript**: No framework dependencies for simplicity
- **Modern CSS**: Responsive design with CSS Grid and Flexbox
- **Real-time Updates**: Streaming chat responses with typing indicators
- **Message Formatting**: Auto-formatting for code, lists, and emphasis

### API Endpoints

- `GET /`: Main chat interface
- `POST /api/chat`: Streaming chat endpoint
- `POST /api/clear`: Clear conversation history
- `GET /api/history`: Get conversation history
- `GET /api/health`: Health check endpoint

## 🎨 Customization

### Modify System Message

Edit the system prompt in `backend/chat_service.py`:

```python
self.system_message = {
    "role": "system",
    "content": [
        {
            "type": "text",
            "text": "Your custom system message here"
        }
    ]
}
```

### Customize Appearance

Modify `frontend/static/style.css` to change:
- Color scheme (update CSS custom properties)
- Layout and spacing
- Animations and transitions
- Responsive breakpoints

### Adjust AI Parameters

In `backend/chat_service.py`, modify the chat completion parameters:

```python
response = self.client.chat.completions.create(
    model=self.deployment,
    messages=messages,
    max_tokens=800,        # Response length
    temperature=0.7,       # Creativity (0.0-2.0)
    top_p=0.95,           # Response diversity
    frequency_penalty=0,   # Reduce repetition
    presence_penalty=0,    # Encourage new topics
    stream=True
)
```

## 🔧 Development

### Running in Development Mode

For auto-reload during development:

```bash
export FLASK_ENV=development  # Linux/Mac
# or
set FLASK_ENV=development     # Windows

python app.py
```

### Testing the API

Test individual endpoints:

```bash
# Health check
curl http://127.0.0.1:5000/api/health

# Send a chat message
curl -X POST http://127.0.0.1:5000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello!"}'

# Clear conversation
curl -X POST http://127.0.0.1:5000/api/clear
```

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**
   ```bash
   pip install -r requirements.txt --user
   ```

2. **Environment variables not loaded**
   - Ensure `.env` file exists in the root directory
   - Check that all required variables are set
   - Restart the application after creating/updating `.env`

3. **Port already in use**
   - Change the port in `app.py`:
   ```python
   app.run(host='127.0.0.1', port=5001, debug=True)  # Use different port
   ```

4. **Azure OpenAI connection issues**
   - Verify your endpoint URL format
   - Check that your API key is correct
   - Ensure your deployment name matches exactly
   - Confirm your Azure OpenAI resource is active

5. **CORS issues (if accessing from different origin)**
   - Flask-CORS is already configured
   - Check browser console for specific CORS errors

### Debug Mode

Enable detailed logging by setting Flask debug mode:

```python
app.run(host='127.0.0.1', port=5000, debug=True)
```

Check the console output for detailed error messages.

### Browser Developer Tools

- Open browser DevTools (F12)
- Check Console tab for JavaScript errors
- Check Network tab for API request/response details

## 📚 Dependencies

- **Flask** (3.0.0): Web framework
- **Flask-CORS** (4.0.0): Cross-Origin Resource Sharing
- **openai** (1.60.2): Official OpenAI Python client
- **python-dotenv** (1.0.0): Environment variable management

## 🔄 Upgrading

To upgrade dependencies:

```bash
pip install --upgrade -r requirements.txt --user
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

These samples are provided for educational and demonstration purposes.

## 🆘 Support

### Getting Help

1. **Check this README** for common solutions
2. **Verify your Azure OpenAI setup** in the Azure Portal
3. **Check the console logs** for detailed error messages
4. **Test API endpoints individually** using curl or Postman

### Environment Setup Help

If you're having trouble with the `.env` file:

1. Copy the example below and save as `.env`:
```env
ENDPOINT_URL=https://your-resource-name.openai.azure.com/
DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_API_KEY=your-32-character-api-key
```

2. Replace the placeholders with your actual values from Azure Portal

### Performance Tips

- **Adjust max_tokens**: Lower values for faster responses
- **Modify temperature**: Lower values (0.1-0.3) for more focused responses
- **Use appropriate deployment**: Choose the right model for your use case

For additional help, please refer to the [Azure OpenAI documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/openai/) or create an issue in the repository.
