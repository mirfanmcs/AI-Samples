from dotenv import load_dotenv
import os
import sys
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient


def main():

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    try:

        # Get the document to analyze
        doc_file = 'docs/test1.jpg'

        if len(sys.argv) > 1:
            doc_file = sys.argv[1]


        # Get config settings
        load_dotenv()
        endpoint = os.getenv('DOC_INTELLIGENCE_ENDPOINT')
        key = os.getenv('DOC_INTELLIGENCE_KEY')
        model_id = os.getenv("MODEL_ID")

        # Create the client
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )


        # Analyse the form
        with open(doc_file, "rb") as f:
            poller = document_analysis_client.begin_analyze_document(
                model_id, document=f
            )

        # Display form information to the user
        display_form_result(poller)


    except Exception as ex:
        print(ex)

    print("\nAnalysis complete.\n")

def display_form_result(poller):
   # Display form information to the user
    result = poller.result()
        
    for idx, document in enumerate(result.documents):
        print("--------Analyzing document #{}--------".format(idx + 1))
        print("Document has type {}".format(document.doc_type))
        print("Document has confidence {}".format(document.confidence))
        print("Document was analyzed by model with ID {}".format(result.model_id))
        for name, field in document.fields.items():
            field_value = field.value if field.value else field.content
            print("Found field '{}' with value '{}' and with confidence {}".format(name, field_value, field.confidence))

    print("-----------------------------------")


if __name__ == "__main__":
    main()        