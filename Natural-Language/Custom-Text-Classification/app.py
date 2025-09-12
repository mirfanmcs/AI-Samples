
import os
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def main():
    # Load environment variables from .env file
    load_dotenv()

    endpoint = os.getenv("LANGUAGE_SERVICE_ENDPOINT", "")            
    ai_key = os.getenv("LANGUAGE_SERVICE_KEY", "")       
    tc_project_name = os.getenv('TC_PROJECT_NAME')
    tc_deployment_name = os.getenv('TC_DEPLOYMENT_NAME')


    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    ai_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

    

    # Read each text file in the articles folder
    batchedDocuments = []
    articles_folder = 'articles'
    files = os.listdir(articles_folder)
    for file_name in files:
        # Read the file contents
        text = open(os.path.join(articles_folder, file_name), encoding='utf8').read()
        batchedDocuments.append(text)

    # Code reads all of the files in the articles folder and creates a list containing their contents. 
     
    # Get Classifications    
    operation = ai_client.begin_single_label_classify(
        batchedDocuments,
        project_name=tc_project_name,
        deployment_name=tc_deployment_name
    )

    document_results = operation.result()

    for doc, classification_result in zip(files, document_results):
        if classification_result.kind == "CustomDocumentClassification":
            classification = classification_result.classifications[0]
            print("{} was classified as '{}' with confidence score {}.".format(
                doc, classification.category, classification.confidence_score)
            )
        elif classification_result.is_error is True:
            print("{} has an error with code '{}' and message '{}'".format(
                doc, classification_result.error.code, classification_result.error.message)
            )
            

    
if __name__ == "__main__":
    main()