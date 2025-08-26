
import os
from dotenv import load_dotenv
import json
from datetime import date
from classes.date_time_helper import DateTimeHelper
from dateutil.parser import parse as is_date

from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient


def main():
    # Load environment variables from .env file
    load_dotenv()

    endpoint = os.getenv("LANGUAGE_SERVICE_ENDPOINT", "")            
    ai_key = os.getenv("LANGUAGE_SERVICE_KEY", "")       
    cl_project_name = os.getenv('CL_PROJECT_NAME')
    cl_deployment_name = os.getenv('CL_DEPLOYMENT_NAME')

    # Create a client for the ConversationalLanguage service model
    credential = AzureKeyCredential(ai_key)
    ai_client = ConversationAnalysisClient(endpoint=endpoint, credential=credential)

    # Create helper instance
    dt_helper = DateTimeHelper()

    # Get user input (until they enter "quit")
    inputText = ''
    while inputText.lower() != 'quit':
        inputText = input('\nEnter some text ("quit" to stop)\n')
        if inputText.lower() != 'quit':
            result = analyze_text(ai_client, cl_project_name, cl_deployment_name, inputText)
            top_intent = result["result"]["prediction"]["topIntent"]
            entities = result["result"]["prediction"]["entities"]
            print_analysis(result)
            handle_intent(top_intent, entities, dt_helper)

    ai_client.close()


def analyze_text(ai_client, cl_project_name, cl_deployment_name, query):
    return ai_client.analyze_conversation(
        task={
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": query
                },
                "isLoggingEnabled": False
            },
            "parameters": {
                "projectName": cl_project_name,
                "deploymentName": cl_deployment_name,
                "verbose": True
            }
        }
    )

def print_analysis(result):
    print("view top intent:")
    print("\ttop intent: {}".format(result["result"]["prediction"]["topIntent"]))
    print("\tcategory: {}".format(result["result"]["prediction"]["intents"][0]["category"]))
    print("\tconfidence score: {}\n".format(result["result"]["prediction"]["intents"][0]["confidenceScore"]))

    print("view entities:")
    for entity in result["result"]["prediction"]["entities"]:
        print("\tcategory: {}".format(entity["category"]))
        print("\ttext: {}".format(entity["text"]))
        print("\tconfidence score: {}".format(entity["confidenceScore"]))

    print("query: {}".format(result["result"]["query"]))

def handle_intent(top_intent, entities, dt_helper):
    if top_intent == 'GetTime':
        location = 'local'
        # Check for entities
        if len(entities) > 0:
            # Check for a location entity
            for entity in entities:
                if 'Location' == entity["category"]:
                    # ML entities are strings, get the first one
                    location = entity["text"]
        # Get the time for the specified location
        print(dt_helper.get_time(location))

    elif top_intent == 'GetDay':
        date_string = date.today().strftime("%m/%d/%Y")
        # Check for entities
        if len(entities) > 0:
            # Check for a Date entity
            for entity in entities:
                if 'Date' == entity["category"]:
                    # Regex entities are strings, get the first one
                    date_string = entity["text"]
        # Get the day for the specified date
        print(dt_helper.get_day(date_string))

    elif top_intent == 'GetDate':
        day = 'today'
        # Check for entities
        if len(entities) > 0:
            # Check for a Weekday entity
            for entity in entities:
                if 'Weekday' == entity["category"]:
                # List entities are lists
                    day = entity["text"]
        # Get the date for the specified day
        print(dt_helper.get_date(day))

    else:
        # Some other intent (for example, "None") was predicted
        print('Try asking me for the time, the day, or the date.')



if __name__ == "__main__":
    main()