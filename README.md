# Azure AI Samples

A collection of sample applications demonstrating different approaches to building chat interfaces with Azure OpenAI services.

## 📁 Projects Overview

This repository contains two distinct chat application implementations, each showcasing different interaction patterns and complexity levels:

### 🖥️ [Simple Console Chat App](./Simple-Console-Chat-App/)
A lightweight Python console-based chat application perfect for:
- Learning Azure OpenAI API basics
- Quick testing and prototyping
- Command-line environments
- Minimal dependencies

**Key Features:**
- Console-based interaction
- Streaming responses
- Multi-turn conversations
- Environment-based configuration

### 🌐 [Simple UI Chat App](./Simple-UI-Chat-App/)
A modern web-based chat interface offering:
- Rich user experience
- Real-time streaming responses
- Responsive design
- Session management

**Key Features:**
- Flask backend with REST API
- Modern JavaScript frontend
- Real-time message streaming
- Markdown formatting support
- Clean architecture with separated concerns

## 🚀 Quick Start

Choose the application that best fits your needs:

1. **For console/terminal usage**: Navigate to `Simple-Console-Chat-App/`
2. **For web interface**: Navigate to `Simple-UI-Chat-App/`

Each project includes its own detailed README with setup instructions, prerequisites, and usage examples.

## 📋 Prerequisites

Both applications require:
- Python 3.7+ (3.8+ recommended)
- Azure OpenAI resource with deployed model
- Valid Azure OpenAI API credentials

## 🛠️ Common Setup Steps

1. **Azure OpenAI Setup**: Ensure you have an Azure OpenAI resource with a deployed GPT model
2. **Environment Configuration**: Both apps use environment variables for API credentials
3. **Dependencies**: Each project includes its own `requirements.txt` and installation scripts

## 📚 Learning Path

**Recommended progression:**

1. **Start with Console App**: Understand the basic Azure OpenAI integration
2. **Move to UI App**: Learn about web-based implementations and streaming
3. **Compare approaches**: Understand the trade-offs between different architectures

## 🔧 Architecture Comparison

| Feature | Console App | UI App |
|---------|-------------|---------|
| Interface | Command line | Web browser |
| Complexity | Minimal | Moderate |
| Dependencies | Few | More (Flask, web assets) |
| Deployment | Single file | Multi-component |
| User Experience | Developer-focused | End-user friendly |
| Real-time Updates | Console output | Web streaming |

## 📖 Documentation

- Each project contains detailed documentation in its respective directory
- Check individual README files for specific setup instructions
- Review code comments for implementation details

## 🤝 Contributing

When contributing to these samples:
- Follow the existing code style and structure
- Update documentation for any new features
- Test changes with different Azure OpenAI models
- Consider both beginner and advanced use cases

## 📄 License

These samples are provided for educational and demonstration purposes.

## 🆘 Troubleshooting

Common issues and solutions:

- **API Key Issues**: Verify your Azure OpenAI credentials and endpoint configuration
- **Model Deployment**: Ensure your chosen model is properly deployed in Azure OpenAI
- **Dependencies**: Use the provided installation scripts or manually install requirements
- **Network Issues**: Check firewall settings and Azure OpenAI service availability

For project-specific issues, refer to the individual README files in each project directory.
