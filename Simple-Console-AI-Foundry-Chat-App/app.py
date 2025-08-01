# This code is using Azure AI Foundry Python SDK

import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

# Load environment variables from .env file
load_dotenv()

endpoint = os.getenv("PROJECT_ENDPOINT", "")            
deployment = os.getenv("MODEL_DEPLOYMENT", "")       


# Use Azure AI Foundry Project Client. Use Microsoft Entra ID authentication
# Use AZ Login on command line to authenticate
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=endpoint,
)



# Get OpenAI chat client
openai_client = project_client.get_openai_client(api_version="2024-10-21")

# Initialize prompt with system message
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    }
]         

# Loop until the user types 'quit'
while True:
    # Get input text
    input_text = input("Enter the prompt (or type 'quit' to exit): ")
    if input_text.lower() == "quit":
        break
    if len(input_text) == 0:
        print("Please enter a prompt.")
        continue
            
    # Get a chat completion
    chat_prompt.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": input_text
                }
            ]
        }
    ) 
    # Generate the completion
    response = openai_client.chat.completions.create(
       model=deployment,
       messages=chat_prompt,
       max_tokens=800,
       temperature=0.7,
       top_p=0.95,
       frequency_penalty=0,
       presence_penalty=0,
       stop=None,
       stream=True  #for streaming output. Set to False for direct output
    ) 

    # Stream output
    collected_content = ""
    for update in response:
       if update.choices:
           content = update.choices[0].delta.content or ""
           print(content, end="")
           collected_content += content

    print()  # Add newline after streaming
    chat_prompt.append({"role": "assistant", "content": collected_content})

openai_client.close()
    