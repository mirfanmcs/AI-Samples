from dotenv import load_dotenv
import os
import time

from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region


def main():
    
    global training_client
    global custom_vision_project

    # Load environment variables from .env file
    load_dotenv()

    training_endpoint = os.getenv("CUSTOM_VISION_TRAINING_ENDPOINT", "")            
    training_key = os.getenv("CUSTOM_VISION_TRAINING_KEY", "")       
    project_id = os.getenv("CUSTOM_VISION_PROJECT_ID", "")       
    

    # Create client using endpoint and key
    credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
    training_client = CustomVisionTrainingClient(training_endpoint, credentials)
    
    # Get the Custom Vision project
    custom_vision_project = training_client.get_project(project_id)
    
    # Upload and tag images
    Upload_Images('training-images')

    # Train the model
    Train_Model()
        
    

def Upload_Images(folder):
    print("Uploading images...")
    tags = training_client.get_tags(custom_vision_project.id)
    for tag in tags:
        print(tag.name)
        for image in os.listdir(os.path.join(folder,tag.name)):
            image_data = open(os.path.join(folder,tag.name,image), "rb").read()
            training_client.create_images_from_data(custom_vision_project.id, image_data, [tag.id])


def Train_Model():
    print("Training ...")
    iteration = training_client.train_project(custom_vision_project.id)
    while (iteration.status != "Completed"):
        iteration = training_client.get_iteration(custom_vision_project.id, iteration.id)
        print (iteration.status, '...')
        time.sleep(5)
    print ("Model trained!")

    

if __name__ == "__main__":
    main()