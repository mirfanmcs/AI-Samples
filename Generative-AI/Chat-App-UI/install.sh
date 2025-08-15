#!/bin/sh

echo "🚀 Installing Azure OpenAI Simple UI Based Chat Application dependencies..."
echo ""

# Install Python dependencies
echo "📦 Installing Python packages..."
pip install -r requirements.txt --user

echo ""
echo "✅ Installation complete!"
echo ""
echo "📋 Next steps:"
echo "1. Create a .env file with your Azure OpenAI credentials:"
echo "   ENDPOINT_URL=https://your-resource.openai.azure.com/"
echo "   DEPLOYMENT_NAME=your-deployment-name"
echo "   AZURE_OPENAI_API_KEY=your-api-key"
echo ""
echo "2. Run the application:"
echo "   python app.py"
echo ""
echo "3. Open your browser and go to:"
echo "   http://127.0.0.1:5000"
echo ""
echo "🎉 Happy chatting!"