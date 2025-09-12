
import os
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def main():
    # Load environment variables from .env file
    load_dotenv()

    endpoint = os.getenv("LANGUAGE_SERVICE_ENDPOINT", "")            
    ai_key = os.getenv("LANGUAGE_SERVICE_KEY", "")       
    ner_project_name = os.getenv('NER_PROJECT_NAME')
    ner_deployment_name = os.getenv('NER_DEPLOYMENT_NAME')


    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    ai_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

    

    # Read each text file in the ads folder
    batchedDocuments = []
    ads_folder = 'ads'
    files = os.listdir(ads_folder)
    for file_name in files:
        # Read the file contents
        text = open(os.path.join(ads_folder, file_name), encoding='utf8').read()
        batchedDocuments.append(text)

    # Code reads all of the files in the ads  folder and creates a list containing their contents. Then find the comment Extract entities.
     
    # Extract entities
    operation = ai_client.begin_recognize_custom_entities(
        batchedDocuments,
        project_name=ner_project_name,
        deployment_name=ner_deployment_name
    )

    document_results = operation.result()

    for doc, custom_entities_result in zip(files, document_results):
        print(doc)
        if custom_entities_result.kind == "CustomEntityRecognition":
            for entity in custom_entities_result.entities:
                print(
                    "\tEntity '{}' has category '{}' with confidence score of '{}'".format(
                        entity.text, entity.category, entity.confidence_score
                    )
                )
        elif custom_entities_result.is_error is True:
            print("\tError with code '{}' and message '{}'".format(
                custom_entities_result.error.code, custom_entities_result.error.message
                )
            )
            

    
if __name__ == "__main__":
    main()