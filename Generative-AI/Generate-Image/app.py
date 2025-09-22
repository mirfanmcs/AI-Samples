# This code is using Azure AI Foundry Python SDK

import os
import json
import requests

from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from pydash import result

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

    img_no = 0
    # Loop until the user types 'quit'
    while True:
        # Get input text
        input_text = input("Enter the prompt (or type 'quit' to exit): ")
        if input_text.lower() == "quit":
            break
        if len(input_text) == 0:
            print("Please enter a prompt.")
            continue
        
        # Generate an image
        result = openai_client.images.generate(
        model=deployment,
        prompt=input_text,
        n=1
        )

        json_response = json.loads(result.model_dump_json())
        image_url = json_response["data"][0]["url"] 

        # save the image
        img_no += 1
        file_name = f"image_{img_no}.png"
        save_image (image_url, file_name)


    

def save_image (image_url, file_name):
    # Set the directory for the stored image
    image_dir = os.path.join(os.getcwd(), 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, file_name)

    # Retrieve the generated image
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)
    print (f"Image saved as {image_path}")




if __name__ == "__main__":
    main()
    