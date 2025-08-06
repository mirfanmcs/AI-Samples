import os
import base64
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

endpoint = os.getenv("ENDPOINT_URL", "")            
deployment = os.getenv("DEPLOYMENT_NAME", "")       
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "")  
embedding_model = os.getenv("EMBEDDING_MODEL", "")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "")
search_key = os.getenv("SEARCH_KEY", "")
index_name = os.getenv("INDEX_NAME", "")


# Initialize the Azure OpenAI cient with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)        

# Initialize prompt with system message
chat_prompt = [
       {"role": "system", "content": "You are a travel assistant that provides information on travel services."}
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
    chat_prompt.append({"role": "user", "content": input_text})

    # Additional parameters to apply RAG pattern using the AI Search index
    rag_params = {
        "data_sources": [
            {
                # he following params are used to search the index
                "type": "azure_search",
                "parameters": {
                "endpoint": search_endpoint,
                "index_name": index_name,
                "authentication": {
                    "type": "api_key",
                    "key": search_key,
                },
                # The following params are used to vectorize the query
                "query_type": "vector",
                "embedding_dependency": {
                    "type": "deployment_name",
                    "deployment_name": embedding_model,
                },
              }
            }
        ],
    }
     
    # Generate the completion
    response = client.chat.completions.create(
       model=deployment,
       messages=chat_prompt,
       extra_body=rag_params,
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
    