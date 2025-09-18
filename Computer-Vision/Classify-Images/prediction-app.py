from dotenv import load_dotenv
import os
import time

from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient


def main():
    
    global training_client
    global custom_vision_project

    # Load environment variables from .env file
    load_dotenv()

    prediction_endpoint = os.getenv("CUSTOM_VISION_PREDICTION_ENDPOINT", "")            
    prediction_key = os.getenv("CUSTOM_VISION_PREDICTION_KEY", "")       
    project_id = os.getenv("CUSTOM_VISION_PROJECT_ID", "")       
    model_name = os.getenv("CUSTOM_VISION_MODEL_NAME", "")


    # Create client using endpoint and key
    credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    prediction_client = CustomVisionPredictionClient(prediction_endpoint, credentials)
    
     # Classify test images
    for image in os.listdir('test-images'):
        image_data = open(os.path.join('test-images',image), "rb").read()
        results = prediction_client.classify_image(project_id, model_name, image_data)

        # Loop over each label prediction and print any with probability > 50%
        for prediction in results.predictions:
            if prediction.probability > 0.5:
                print(image, ': {} ({:.0%})'.format(prediction.tag_name, prediction.probability))

    

if __name__ == "__main__":
    main()