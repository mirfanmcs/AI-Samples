

from dotenv import load_dotenv
import os
import time
import sys
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures


def main():
    
    global cv_client

    # Load environment variables from .env file
    load_dotenv()

    cv_endpoint = os.getenv("CV_SERVICE_ENDPOINT", "")            
    cv_key = os.getenv("CV_SERVICE_KEY", "")       
    

    # Create client using endpoint and key
    credential = AzureKeyCredential(cv_key)
    cv_client = ImageAnalysisClient(endpoint=cv_endpoint, credential=credential)

    # Get image
    image_file = 'images/Lincoln.jpg'
    #input image file name from command line
    if len(sys.argv) > 1:
        image_file = sys.argv[1]

    result = read_image_text(image_file)

    # Print the text
    if result.read is not None:
        print("\nText:")
        
        for line in result.read.blocks[0].lines:
            print(f" {line.text}")        
        # Annotate the text in the image
        annotate_lines(image_file, result.read)

        # Find individual words in each line
        print ("\nIndividual words:")
        for line in result.read.blocks[0].lines:
            for word in line.words:
                print(f"  {word.text} (Confidence: {word.confidence:.2f}%)")
        # Annotate the words in the image
        annotate_words(image_file, result.read)                




def read_image_text(image_file):
    # Read text in image
    with open(image_file, "rb") as f:
        image_data = f.read()
    print (f"\nReading text in {image_file}")

    result = cv_client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.READ])
    
    return result

    


def annotate_lines(image_file, detected_text):
    print(f'\nAnnotating lines of text in image...')

     # Prepare image for drawing
    image = Image.open(image_file)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'red'

    for line in detected_text.blocks[0].lines:
        # Draw line bounding polygon
        r = line.bounding_polygon
        rectangle = ((r[0].x, r[0].y),(r[1].x, r[1].y),(r[2].x, r[2].y),(r[3].x, r[3].y))
        draw.polygon(rectangle, outline=color, width=3)

    # Save image
    plt.imshow(image)
    plt.tight_layout(pad=0)
    textfile = 'lines.jpg'
    fig.savefig(textfile)
    print('  Results saved in', textfile)
    

def annotate_words(image_file, detected_text):
    print(f'\nAnnotating individual words in image...')

     # Prepare image for drawing
    image = Image.open(image_file)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'red'

    for line in detected_text.blocks[0].lines:
        for word in line.words:
            # Draw word bounding polygon
            r = word.bounding_polygon
            rectangle = ((r[0].x, r[0].y),(r[1].x, r[1].y),(r[2].x, r[2].y),(r[3].x, r[3].y))
            draw.polygon(rectangle, outline=color, width=3)

    # Save image
    plt.imshow(image)
    plt.tight_layout(pad=0)
    textfile = 'words.jpg'
    fig.savefig(textfile)
    print('  Results saved in', textfile)
    

if __name__ == "__main__":
    main()