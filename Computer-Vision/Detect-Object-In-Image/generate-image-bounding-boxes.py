
import os
import json
import glob
from dotenv import load_dotenv
from PIL import Image, ImageDraw
import sys
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

    # Process all images in training-images folder
    training_images_path = "training-images"
    
    # Get all image files from training-images folder
    image_files = glob.glob(os.path.join(training_images_path, "*.jpg"))
    
    if not image_files:
        print("No images found in training-images folder")
        return
    
    print(f"Found {len(image_files)} images to process")
    
    # Process all images and generate tagged-images.json
    generate_tagged_images_json(image_files)


def generate_tagged_images_json(image_files):
    """Process all images and generate tagged-images.json file"""
    tagged_data = {"files": []}
    
    for i, image_file in enumerate(image_files, 1):
        print(f"Processing image {i}/{len(image_files)}: {os.path.basename(image_file)}")
        
        try:
            # Analyze the image
            result = analyse_image(image_file)
            
            # Get image dimensions for normalization
            with Image.open(image_file) as img:
                image_width, image_height = img.size
            
            # Process objects and create tags
            filename = os.path.basename(image_file)
            image_data = {
                "filename": filename,
                "tags": []
            }
            
            if result.objects is not None:
                for detected_object in result.objects.list:
                    # Get the highest confidence tag
                    if detected_object.tags:
                        tag_name = detected_object.tags[0].name
                        confidence = detected_object.tags[0].confidence
                        
                        # Only include objects with reasonable confidence
                        if confidence > 0.5:
                            # Get bounding box and normalize coordinates
                            bbox = detected_object.bounding_box
                            normalized_tag = {
                                "tag": tag_name,
                                "left": bbox.x / image_width,
                                "top": bbox.y / image_height,
                                "width": bbox.width / image_width,
                                "height": bbox.height / image_height
                            }
                            image_data["tags"].append(normalized_tag)
            
            tagged_data["files"].append(image_data)
            
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")
            continue
    
    # Save to tagged-images.json
    output_file = "tagged-images.json"
    with open(output_file, 'w') as f:
        json.dump(tagged_data, f, indent=4)
    
    print(f"\nCompleted! Results saved to {output_file}")
    print(f"Processed {len(tagged_data['files'])} images successfully")

def analyse_image(image_file):
    """Analyze image using Azure Computer Vision API"""
    with open(image_file, "rb") as f:
        image_data = f.read()

    result = cv_client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.OBJECTS],
    )
    return result


if __name__ == "__main__":
    main()