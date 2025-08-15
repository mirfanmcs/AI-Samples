# Project Structure Overview

```
Simple-UI-Chat-App/
│
├── 📁 frontend/                    # Frontend assets and templates
│   ├── 📁 templates/
│   │   └── 📄 index.html          # Main chat interface (Jinja2 template)
│   └── 📁 static/
│       ├── 📄 style.css           # Modern CSS styling with animations
│       └── 📄 script.js           # Chat functionality and SSE handling
│
├── 📁 backend/                     # Backend services
│   ├── 📄 __init__.py             # Python package initialization
│   └── 📄 chat_service.py         # Azure OpenAI integration service
│
├── 📄 app.py                       # 🚀 Main Flask application (Entry point)
├── 📄 run.py                       # Alternative runner with checks
├── 📄 start.bat                    # Windows batch file for easy starting
│
├── 📄 requirements.txt             # Python dependencies
├── 📄 install.sh                   # Installation script (Linux/Mac)
│
├── 📄 .env.example                 # Environment variables template
├── 📄 .env                         # Your actual environment variables (create this)
│
└── 📄 README.md                    # Comprehensive documentation
```

## 🎯 Key Files Explained

### **app.py** - Main Application Entry Point
- Flask application setup and configuration
- API endpoints for chat, clear, health check
- Template rendering and static file serving
- Session management for conversation history

### **backend/chat_service.py** - AI Integration
- Azure OpenAI client initialization
- Message formatting and conversation management
- Streaming response handling
- Error handling and connection management

### **frontend/templates/index.html** - UI Template
- Modern chat interface with avatars and timestamps
- Responsive design for mobile and desktop
- Typing indicators and status displays
- Form handling for message input

### **frontend/static/style.css** - Styling
- Modern gradient backgrounds
- Animated typing indicators
- Responsive breakpoints
- Smooth transitions and hover effects

### **frontend/static/script.js** - Client Logic
- Real-time streaming via Server-Sent Events
- Message formatting and display
- User interaction handling
- API communication and error handling

## 🚀 Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt --user

# Copy environment template
cp .env.example .env
# (Edit .env with your Azure OpenAI credentials)

# Run the application
python app.py
# or
python run.py
# or (Windows)
start.bat
```

## 🌐 Access Points

- **Main Application**: http://127.0.0.1:5000
- **Health Check**: http://127.0.0.1:5000/api/health
- **Chat API**: POST http://127.0.0.1:5000/api/chat
- **Clear API**: POST http://127.0.0.1:5000/api/clear

## 🔧 Configuration

All configuration is handled through environment variables in the `.env` file:

- `ENDPOINT_URL`: Your Azure OpenAI resource endpoint
- `DEPLOYMENT_NAME`: Your model deployment name
- `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key

## 📱 Features

✅ Real-time streaming responses  
✅ Session-based conversation history  
✅ Mobile-responsive design  
✅ Message formatting (markdown-like)  
✅ Typing indicators  
✅ Clear conversation functionality  
✅ Error handling and status indicators  
✅ Cross-browser compatibility  

## 🛠️ Technology Stack

- **Backend**: Flask 3.0, Python 3.8+
- **Frontend**: Vanilla JavaScript, Modern CSS
- **AI**: Azure OpenAI API
- **Communication**: Server-Sent Events (SSE)
- **Styling**: CSS Grid, Flexbox, Animations
