#!/usr/bin/env python3
"""
Simple runner script for the Flask AI Chat Application
Checks dependencies and starts the Flask server
"""

import os
import sys
import subprocess
import webbrowser
import time
import threading
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = ['flask', 'openai', 'dotenv', 'flask_cors']
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'dotenv':
                import dotenv
            elif package == 'flask_cors':
                import flask_cors
            else:
                __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing dependencies: {', '.join(missing_packages)}")
        print("📦 Please install dependencies by running:")
        print("   pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed")
    return True

def check_env_file():
    """Check if .env file exists with required variables"""
    env_path = Path(".env")
    if not env_path.exists():
        print("❌ .env file not found")
        print("📝 Please create a .env file with the following variables:")
        print("   ENDPOINT_URL=https://your-resource.openai.azure.com/")
        print("   DEPLOYMENT_NAME=your-deployment-name")
        print("   AZURE_OPENAI_API_KEY=your-api-key")
        return False
    
    # Check if required env vars are present
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            content = f.read()
            required_vars = ['ENDPOINT_URL', 'DEPLOYMENT_NAME', 'AZURE_OPENAI_API_KEY']
            missing_vars = []
            
            for var in required_vars:
                if var not in content:
                    missing_vars.append(var)
            
            if missing_vars:
                print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
                return False
    except Exception as e:
        print(f"❌ Error reading .env file: {e}")
        return False
    
    print("✅ Environment configuration found")
    return True

def open_browser():
    """Open browser after a short delay"""
    time.sleep(2)  # Wait for server to start
    try:
        webbrowser.open("http://127.0.0.1:5000")
        print("🌐 Opening browser...")
    except Exception as e:
        print(f"⚠️  Could not open browser automatically: {e}")
        print("🌐 Please open http://127.0.0.1:5000 in your browser manually")

def main():
    """Main function to run the application"""
    print("🤖 Flask AI Chat Application")
    print("=" * 40)
    print()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment configuration
    if not check_env_file():
        sys.exit(1)
    
    print()
    print("🚀 Starting Flask application...")
    print("📍 Server will be available at: http://127.0.0.1:5000")
    print("🔄 Press Ctrl+C to stop the server")
    print()
    
    # Open browser in background
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start Flask app
    try:
        from app import app
        app.run(host='127.0.0.1', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down server...")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
