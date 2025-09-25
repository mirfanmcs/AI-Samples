# Detect Objects in Image

A sample application that uses Azure AI Foundry Custom Vision Service to detect and identify objects within images. It can locate multiple objects and provide bounding boxes with confidence scores.


## Overview

This application performs the following tasks:
- Train Model 
  - Connects to an Azure Custom Vision project using the provided credentials.
  - Uploads images from the training-images folder, tagging them based on subfolder names.
  - Trains the Custom Vision model using the uploaded images.
  - Monitors the training process until completion.
- Test Model 
  - Connects to an Azure Custom Vision project using the provided credentials.
  - Read input image 
  - Detect object in image by connecting to the Custom Vision model for object detection.
  - Prints detected objects names to the console.
  - Annotates the image with detected objects
  - Saves annotated images to files.  
- Generate `tagged-images.json` 
  - Batch processes all JPG images in the training-images folder
  - Uses Azure Computer Vision API to detect objects in each image
  - Extracts bounding boxes and object labels with confidence filtering (>0.5)
  - Generates tagged-images.json with structured object detection data
  

## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- An Azure AI Custom Vision Service

## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry Custom Vision Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/). Two services will be created one the the name you give and other with the yourservicename-Prediction.
- Open Custom Vision Portal [https://www.customvision.ai/](https://www.customvision.ai/) and create a custom vision project with following values:
  - Project type: `Object Detection`
  - Domain: `General`
- Open the the project and add following tags: `apple`,`banana`,`orange`
- Generate tagged-images.json by running `python tgenerate-image-bounding-boxes.py`
- Train the model by running `python training-app.py`
- Publish the model in Custom Vision Portal under Performance → Publish. Select the resource with `-Prediction` suffix under Prediction resource. Name the model and note down its name. 
- Test the model by running `python prediction-app.py`
- You can also upload and tag images, as well as train the model, using the Computer Vision Portal.


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Face Service Endpoint
CUSTOM_VISION_TRAINING_ENDPOINT=your-custom-vision-training-endpoint
CUSTOM_VISION_TRAINING_KEY=your-custom-vision-training-key
CUSTOM_VISION_PREDICTION_ENDPOINT=your-custom-vision-prediction-endpoint
CUSTOM_VISION_PREDICTION_KEY=your-custom-vision-prediction-key
CUSTOM_VISION_PROJECT_ID="your-custom-vision-project-id"
CUSTOM_VISION_MODEL_NAME="your-custom-vision-model-name"
CV_SERVICE_ENDPOINT=your-computer-vision-service-endpoint
CV_SERVICE_KEY=your-computer-vision-service-key
```


**How to find these values:**

- **CUSTOM_VISION_TRAINING_ENDPOINT**: In Azure portal, go to your custom vision service you created → Keys and Endpoints → find the "Endpoint"
- **CUSTOM_VISION_TRAINING_KEY**: In Azure portal, go to your custom vision service you created → Keys and Endpoints → find the "KEY 1"
- **CUSTOM_VISION_PREDICTION_ENDPOINT**: In Azure portal, go to your custom vision prediction service (with -Prediction suffix) you created → Keys and Endpoints → find the "Endpoint"
- **CUSTOM_VISION_PREDICTION_KEY**: In Azure portal, go to your custom vision prediction service (with -Prediction suffix) you created → Keys and Endpoints → find the "KEY 1"
- **CUSTOM_VISION_PROJECT_ID**: In Custom Vision portal, go to your project settings → find the "Project Id"
- **CUSTOM_VISION_MODEL_NAME**: In Custom Vision portal name of model you deployed"
- **CV_SERVICE_ENDPOINT**: In Azure portal, go to your computer vision service you created → Overview → find the "Endpoint"
- **CV_SERVICE_KEY**: In Azure portal, go to your computer vision service you created → Overview → find the "KEY 1"


## Running the Application

1. Generate tagged-images.json:
   ```bash
   python tgenerate-image-bounding-boxes.py 
   ```

1. Run the application to train the model:
   ```bash
   python training-app.py 
   ```
2. Run the application to test the model:
   ```bash
   python prediction-app.py test-images/image1.jpg
   ```

Notice the output.jpg file created annotating objects in the original image. 
  

## Dependencies

- `azure-cognitiveservices-vision-customvision`: Azure AI Custom Vision Service
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file
- `matplotlib`: Data visualization library for Python.

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Check that your CUSTOM_VISION_TRAINING_ENDPOINT is correct
2. Check that your CUSTOM_VISION_TRAINING_KEY is correct
3. Check that your CUSTOM_VISION_PREDICTION_ENDPOINT is correct
4. Check that your CUSTOM_VISION_PREDICTION_KEY is correct
5. Check that your CUSTOM_VISION_PROJECT_ID is correct
6. Check that your CUSTOM_VISION_MODEL_NAME is correct
7. Check that your CV_SERVICE_ENDPOINT is correct
8. Check that your CV_SERVICE_KEY is correct

### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade azure-identity matplotlib azure-cognitiveservices-vision-customvision`

## Project Structure

```
Detect-Object-In-Image/
├── training-app.py      # Code for training the model
├── prediction-app.py    # Code for testing the model
├── requirements.txt     # Python dependencies
├── training-images/     # Images for training the model
├── test-images/         # Images for testing the model
├── readme.md            # This file
└── install.sh           # Installation script
```


## License

These samples are provided for educational and demonstration purposes.