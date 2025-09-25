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
        doc_file = 'docs/sample-invoice.pdf'

        if len(sys.argv) > 1:
            doc_file = sys.argv[1]


        # Get config settings
        load_dotenv()
        endpoint = os.getenv('AI_ENDPOINT')
        key = os.getenv('AI_KEY')


        # Set analysis settings
        fileLocale = "en-US"
        fileModelId = "prebuilt-invoice"

        print(f"\nConnecting to Forms Recognizer at: {endpoint}")
        print(f"Analyzing invoice at: {doc_file}")


        # Create the client
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )


        # Analyse the invoice
        with open(doc_file, "rb") as f:
            poller = document_analysis_client.begin_analyze_document(
                fileModelId, document=f, locale=fileLocale
            )

        

        # Display invoice information to the user
        display_invoice_result(poller)

            


    except Exception as ex:
        print(ex)

    print("\nAnalysis complete.\n")

def display_invoice_result(poller):
   # Display invoice information to the user
    receipts = poller.result()
        
    for idx, receipt in enumerate(receipts.documents):
        
        vendor_name = receipt.fields.get("VendorName")
        if vendor_name:
            print(f"\nVendor Name: {vendor_name.value}, with confidence {vendor_name.confidence}.")

        customer_name = receipt.fields.get("CustomerName")
        if customer_name:
            print(f"Customer Name: '{customer_name.value}, with confidence {customer_name.confidence}.")


        invoice_total = receipt.fields.get("InvoiceTotal")
        if invoice_total:
            print(f"Invoice Total: '{invoice_total.value.symbol}{invoice_total.value.amount}, with confidence {invoice_total.confidence}.")


if __name__ == "__main__":
    main()        