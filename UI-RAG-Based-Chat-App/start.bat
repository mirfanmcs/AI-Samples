@echo off
echo 🤖 Azure OpenAI Simple UI Based Chat Application
echo ==================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo 📥 Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo ❌ .env file not found
    echo.
    echo 📝 Please create a .env file with your Azure OpenAI credentials:
    echo    ENDPOINT_URL=https://your-resource.openai.azure.com/
    echo    DEPLOYMENT_NAME=your-deployment-name
    echo    AZURE_OPENAI_API_KEY=your-api-key
    echo.
    echo 💡 You can copy .env.example to .env and edit it
    pause
    exit /b 1
)

echo ✅ Starting Azure OpenAI Simple UI Based Chat Application...
echo 📍 Server will be available at: http://127.0.0.1:5000
echo 🔄 Press Ctrl+C to stop the server
echo.

REM Start the Flask application
python app.py

pause
