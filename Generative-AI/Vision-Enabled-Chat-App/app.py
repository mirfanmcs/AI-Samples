# This code is using Azure AI Foundry Python SDK

import os
import sys
import base64
from pathlib import Path

from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

def main():
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

    # Get image
    image_file = 'images/mystery-fruit.jpeg'
    #input image file name from command line
    if len(sys.argv) > 1:
        image_file = sys.argv[1]


    # Initialize prompts
    system_message = "You are an AI assistant in a grocery store that sells fruit. You provide detailed answers to questions about produce."
    prompt = ""        

    data_url = get_image_data(image_file)

    # Loop until the user types 'quit'
    while True:
        prompt = input("\nAsk a question about the image\n(or type 'quit' to exit)\n")
        if prompt.lower() == "quit":
            break
        elif len(prompt) == 0:
                print("Please enter a question.\n")
        else:
            print("Getting a response ...\n")


            # Get a response to image input
            get_response(openai_client, deployment, system_message, prompt, data_url)


def get_image_data(image_file):
    # Get a response to image input
    script_dir = Path(__file__).parent  # Get the directory of the script
    mime_type = "image/jpeg"

    # Read and encode the image file
    with open(image_file, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Include the image file data in the prompt
    data_url = f"data:{mime_type};base64,{base64_encoded_data}"

    return data_url



def get_response(openai_client, model_deployment, system_message, prompt, data_url):

    response = openai_client.chat.completions.create(
        model=model_deployment,
        messages=[
            {"role": "system", "content": system_message},
            { "role": "user", "content": [  
                { "type": "text", "text": prompt},
                { "type": "image_url", "image_url": {"url": data_url}}
            ] } 
        ]
    )
    print(response.choices[0].message.content)
  




if __name__ == "__main__":
    main()
    