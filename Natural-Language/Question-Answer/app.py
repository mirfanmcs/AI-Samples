
import os
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient



def main():
    # Load environment variables from .env file
    load_dotenv()

    endpoint = os.getenv("LANGUAGE_SERVICE_ENDPOINT", "")            
    ai_key = os.getenv("LANGUAGE_SERVICE_KEY", "")       
    qa_project_name = os.getenv('QA_PROJECT_NAME')
    qa_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

    # Create client using endpoint and key



    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    ai_client = QuestionAnsweringClient(endpoint=endpoint, credential=credential)

    # Submit a question and display the answer
    user_question = ''
    while True:
        user_question = input('\nQuestion:\n')
        if user_question.lower() == "quit":                
            break
        response = ai_client.get_answers(question=user_question,
                                        project_name=qa_project_name,
                                        deployment_name=qa_deployment_name)
        for candidate in response.answers:
            print(candidate.answer)
            print("Confidence: {}".format(candidate.confidence))
            print("Source: {}".format(candidate.source))


    
if __name__ == "__main__":
    main()