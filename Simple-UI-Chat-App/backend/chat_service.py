import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ChatService:
    def __init__(self):
        self.endpoint = os.getenv("ENDPOINT_URL", "")
        self.deployment = os.getenv("DEPLOYMENT_NAME", "")
        self.subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "")
        
        # Initialize Azure OpenAI client
        self.client = AzureOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self.subscription_key,
            api_version="2025-01-01-preview",
        )
        
        # System message that stays constant
        self.system_message = {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are an AI assistant that helps people find information."
                }
            ]
        }
    
    def create_chat_prompt(self, conversation_history):
        """
        Create chat prompt with system message and conversation history
        """
        chat_prompt = [self.system_message]
        chat_prompt.extend(conversation_history)
        return chat_prompt
    
    def stream_chat_response(self, conversation_history):
        """
        Stream chat response from Azure OpenAI
        """
        try:
            messages = self.create_chat_prompt(conversation_history)
            
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=messages,
                max_tokens=800,
                temperature=0.7,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None,
                stream=True
            )
            
            for update in response:
                if update.choices and update.choices[0].delta.content:
                    content = update.choices[0].delta.content
                    yield content
                    
        except Exception as e:
            yield f"Error: {str(e)}"
    
    def format_user_message(self, user_input):
        """
        Format user input into the required message structure
        """
        return {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_input
                }
            ]
        }
    
    def format_assistant_message(self, assistant_response):
        """
        Format assistant response into the required message structure
        """
        return {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": assistant_response
                }
            ]
        }
    
    def close(self):
        """Close the OpenAI client"""
        if hasattr(self.client, 'close'):
            self.client.close()
