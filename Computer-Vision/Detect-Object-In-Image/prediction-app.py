from dotenv import load_dotenv
import os
import time
import sys
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np

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
    
     # Get image
    image_file = 'test-images/image1.jpg'
    #input image file name from command line
    if len(sys.argv) > 1:
        image_file = sys.argv[1]

    print('Detecting objects in', image_file)
    with open(image_file, mode="rb") as image_data:
        results = prediction_client.detect_image(project_id, model_name, image_data)

    # Loop over each prediction
    for prediction in results.predictions:
        # Get each prediction with a probability > 50%
        if (prediction.probability*100) > 50:
            print(prediction.tag_name)

    # Create and save an annotated image
    save_tagged_images(image_file, results.predictions)    
    

def save_tagged_images(source_path, detected_objects):
    #Load the image using Pillow
    image = Image.open(source_path)
    h, w, ch = np.array(image).shape
    # Create a figure for the results
    fig = plt.figure(figsize=(8, 8))
    plt.axis('off')

    # Display the image with boxes around each detected object
    draw = ImageDraw.Draw(image)
    lineWidth = int(w/100)
    color = 'magenta'
    for detected_object in detected_objects:
        # Only show objects with a > 50% probability
        if (detected_object.probability*100) > 50:
            # Box coordinates and dimensions are proportional - convert to absolutes
            left = detected_object.bounding_box.left * w 
            top = detected_object.bounding_box.top * h 
            height = detected_object.bounding_box.height * h
            width =  detected_object.bounding_box.width * w
            # Draw the box
            points = ((left,top), (left+width,top), (left+width,top+height), (left,top+height),(left,top))
            draw.line(points, fill=color, width=lineWidth)
            # Add the tag name and probability
            plt.annotate(detected_object.tag_name + ": {0:.2f}%".format(detected_object.probability * 100),(left,top), backgroundcolor=color)
    plt.imshow(image)
    outputfile = 'output.jpg'
    fig.savefig(outputfile)
    print('Results saved in', outputfile)    


if __name__ == "__main__":
    main()