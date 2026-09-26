# Azure AI Samples

A collection of AI sample applications demonstrating different implementation approaches.

## Agentic-AI

### [🤖 Azure AI Foundry Agent Application](./Agentic-AI/AI-Foundry-Agent-App/readme.md)
AI Agent application that uses Azure AI Foundry agent service through the Azure AI Foundry Python SDK.

### [🛠️ Azure AI Foundry Agent Application Using Custom Tools](./Agentic-AI/AI-Foundry-Agent-App-Using-Custom-Tools/readme.md)
AI Agent application that uses Azure AI Foundry agent service and custom function as a custom tools through the Azure AI Foundry Python SDK.

### [🖧 Azure AI Foundry Agent Application Using MCP](./Agentic-AI/AI-Foundry-Agent-App-Using-MCP/readme.md)
AI Agent application that uses Azure AI Foundry agent service and MCP through the Azure AI Foundry Python SDK.

### [🤖 Azure AI Foundry Multi Agent Application](./Agentic-AI/AI-Foundry-Multi-Agent-App/readme.md)
AI Multi Agent application that uses Azure AI Foundry agent service through the Azure AI Foundry Python SDK.

### [🌐 Remote Agents With A2A](./Agentic-AI/Remote-Agents-With-A2A/readme.md)
A sample application that demonstrates how to use Azure AI Foundry Agent-to-Agent (A2A) communication to orchestrate and coordinate remote agents. It enables distributed AI workflows and collaboration between agents across different environments.

### [🧠 Semantic Kernel Agent Application](./Agentic-AI/Semantic-Kernel-Agent-App/readme.md)
Semantic Kernel Agent application that uses the `AzureAIAgent` class to build and interact with AI agents using the Azure AI Foundry Agent Service.

### [🧠 Semantic Kernel Multi Agent Application](./Agentic-AI/Semantic-Kernel-Multi-Agent-App/readme.md)
Demonstrates multi-agent orchestration using Azure AI Foundry Python SDK and Semantic Kernel. Automates incident management and DevOps actions by coordinating specialized agents and custom plugins for log analysis and DevOps tasks.

### [🧰 Simple Agent App](./Agentic-AI/Simple-Agent-App/readme.md)
AI Agent application that combines a custom support-ticket function and Microsoft Learn MCP in one Azure AI Foundry agent. It uses strict tool routing so the agent performs only the supported tool actions.

### [☁️ Simple Agent App Hosted Agent](./Agentic-AI/Simple-Agent-App-Hosted-Agent/readme.md)
Hosted version of the Simple Agent App that runs the custom function and MCP integration inside a Docker container. It uses the Microsoft Foundry hosted-agent Responses protocol, Python SDK deployment, and an Azure Container Registry build workflow.

### [🧭 Simple Harness Agent App Hosted Agent](./Agentic-AI/Simple-Harness-Agent-App-Hosted-Agent/readme.md)
Hosted Microsoft Agent Framework Harness sample for software-delivery planning. It demonstrates Harness planning and todos, workspace files, file memory, skills, a background agent, custom tools, Context7 MCP, and Python SDK container deployment to Microsoft Foundry.

## Computer-Vision

### [🏷️ Classify Images](./Computer-Vision/Classify-Images/readme.md)
A sample application that uses Azure AI Foundry Custom Vision Service to classify images into predefined categories. It provides insights into the content of images based on trained models.

### [👤 Detect and Analyze Faces](./Computer-Vision/Detect-Analyze-Faces/readme.md)
A sample application that uses Azure AI Foundry Face Service to detect and analyze faces in images. It provides information about dedected faces.

### [🔍 Detect Objects In Image](./Computer-Vision/Detect-Object-In-Image/readme.md)
A sample application that uses Azure AI Foundry Custom Vision Service to detect and identify objects within images. It can locate multiple objects and provide bounding boxes with confidence scores.

### [🖼️ Image Analysis](./Computer-Vision/Image-Analysis/readme.md)
A sample application that uses Azure AI Foundry Vision Service for image analysis. It analyzes images to detect aptions, tags, objects, and people.

### [🖼️ Read Image Text](./Computer-Vision/Read-Image-Text/readme.md)
A sample application that uses Azure AI Foundry Computer Vision Service to extract text from images using OCR (Optical Character Recognition). It can read printed and handwritten text from images and return the extracted content.

## Generative-AI

### [⚡ Azure AI Foundry Chat Application](./Generative-AI/AI-Foundry-Chat-App/readme.md)
A chat application that uses Azure AI Foundry to interact with OpenAI models through the Azure AI Foundry Python SDK.

### [🔊 Audio Enabled Chat App](./Generative-AI/Audio-Enabled-Chat-App/readme.md)
A chat application that uses Azure AI Foundry to interact with OpenAI models through the Azure AI Foundry Python SDK. It uses multimodel to send text and audio prompt.

### [🔊 Azure OpenAI Audio Enabled UI Based Chat Application](./Generative-AI/Audio-Enabled-Chat-App-UI/README.md)
A modern web-based chat interface for Azure OpenAI with real-time streaming responses and audio input support. Built with Flask backend and vanilla JavaScript frontend, using browser speech-to-text API to enable audio-enabled chat.

### [🌐 Azure OpenAI UI Based Chat Application](./Generative-AI/Chat-App-UI/README.md)
A modern web-based chat interface for Azure OpenAI with real-time streaming responses. Built with Flask backend and vanilla JavaScript frontend.

### [🖌️ Generate Image](./Generative-AI/Generate-Image/readme.md)
A sample application that uses Azure AI Foundry Vision Service to generate images from textual descriptions. It leverages advanced generative AI models to create visuals based on user-provided prompts.

### [🖥️ Azure OpenAI Chat Application](./Generative-AI/OpenAI-Chat-App/readme.md)
A Python application that demonstrates how to interact with Azure OpenAI's chat completion API with streaming responses.

### [🔄 Prompt Flow Chat App](./Generative-AI/Prompt-Flow-Chat-App/README.md)
A comprehensive travel chat application built with Microsoft PromptFlow, featuring an intelligent chat bot and automated evaluation system with Azure OpenAI integration.

### [📚 Azure OpenAI RAG Based Chat Application](./Generative-AI/RAG-Based-Chat-App/readme.md)
A Python application that demonstrates how to interact with Azure OpenAI's chat completion API using RAG pattern with command-line interface.

### [🌐📚 Azure OpenAI UI RAG Based Chat Application](./Generative-AI/RAG-Based-Chat-App-UI/README.md)
A modern web-based chat interface for Azure OpenAI using RAG pattern. Built with Flask backend and vanilla JavaScript frontend with clean separation of concerns.

### [🖼️ Vision Enabled Chat App](./Generative-AI/Vision-Enabled-Chat-App/readme.md)
A chat application that uses Azure AI Foundry to interact with OpenAI models through the Azure AI Foundry Python SDK. It uses multimodel to send text and image data and answer questions about image.

## Information-Extraction

### [🗂️ Document Intelligence Using Custom Model](./Information-Extraction/Document-Intelligence-Using-Custom-Model/readme.md)
A sample application that uses Azure AI Foundry Document Intelligence Service with a custom model to analyze, extract, and structure information from documents. It enables tailored extraction for specific document types and custom fields defined by the user.

### [�️ Document Intelligence Using Prebuilt Model](./Information-Extraction/Document-Intelligence-Using-Prebuilt-Model/readme.md)
A sample application that uses Azure AI Foundry Document Intelligence Service pre build model to analyze, extract, and structure information from documents. It supports processing forms, invoices, receipts, and other document types using advanced AI models.

### [🧾 Extract Info Using AI Content Understanding](./Information-Extraction/Extract-Info-Using-AI-Content-Understanding/readme.md)
A sample application that uses Azure AI Foundry Content Understanding Service to extract structured information from documents and images. It leverages AI models to identify key fields, entities, and relationships within unstructured content.

### [🔍 Knowledge Mining Using AI Search](./Information-Extraction/Knowledge-Mining-Using-AI-Search/readme.md)
A sample application that uses Azure AI Search to perform knowledge mining operations on large datasets. It demonstrates how to create search indexes, extract insights from unstructured data, and build intelligent search experiences.

## Natural-Language

### [💬 Conversational Language Understanding](./Natural-Language/Conversational-Language-Understanding/readme.md)
A sample application that uses Azure AI Foundry Language Service for conversational language understanding. It uses Conversation Analysis API to detect intent and extract entities.

### [🔍 Custom Named Entity Recognition](./Natural-Language/Custom-Named-Entity-Recognition/readme.md)
A sample application that uses Azure AI Foundry Language Service for custom named entity recognition. It reads ads and extracts entities using Azure Text Analytics.

### [🏷️ Custom-Text-Classification](./Natural-Language/Custom-Text-Classification/readme.md)
A sample application that uses Azure AI Foundry Language Service for text classification. It reads articles and classifies their content using Azure Text Analytics.

### [❓ Question Answer](./Natural-Language/Question-Answer/readme.md)
A sample application that uses Azure AI Foundry Language Service for Question Answering. It answers questions on user input.

### [🗣️ Speech Enabled App](./Natural-Language/Speech-Enabled-App/readme.md)
A sample application that uses Azure AI Foundry Speech Service to enable speech in applications. It can transcribe spoken commands from audio files or microphone and synthesize speech responses.

### [📝 Text Analysis](./Natural-Language/Text-Analysis/readme.md)
A sample application that uses Azure AI Foundry Language Service for Text Analysis. It analyzes text files for language detection, sentiment analysis, key phrases extraction, detect entities, and linked entities.

### [🎤 Translate Speech](./Natural-Language/Translate-Speech/readme.md)
A sample application that uses Azure AI Foundry Translate Service for real-time speech translation. It translates spoken English into French, Spanish, and Hindi, and can synthesize translated audio output or play it live.

### [🌎 Translate Text](./Natural-Language/Translate-Text/readme.md)
A sample application that uses Azure AI Foundry Translate Service to translate text between languages.

## Quick Start

1. Choose a project based on your needs
2. Navigate to the project folder
3. Follow the setup instructions in each project's README
4. Configure your Azure credentials
5. Run the application

Each project includes detailed setup instructions and documentation in its respective README file.
