import os
import base64
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

endpoint = os.getenv("ENDPOINT_URL", "")            
deployment = os.getenv("DEPLOYMENT_NAME", "")       
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "")  

# Initialize the Azure OpenAI cient with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)        

# Initialize prompt with system message
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are a travel assistant that provides information on travel services."
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
            
    # Add user input message to the prompt
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
    response = client.chat.completions.create(
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

client.close()
    