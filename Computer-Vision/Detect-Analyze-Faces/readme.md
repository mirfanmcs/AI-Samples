# Detect and Analyze Faces

A sample application that uses Azure AI Foundry Face Service to detect and analyze faces in images. It provides information about dedected faces.


## Overview

This application performs the following tasks:
- Initializes the Azure Face Service client.
- Accepts an image file for analysis (either a default image or one provided via the command line).
- Analyse face from the image.
- Prints information about the face analysis to the console.
- Annotates the image with detected face in the image.
- Saves the annotated image to file.


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- An Azure AI Face Service

## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry Face Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/). 


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Face Service Endpoint
FACE_SERVICE_ENDPOINT=your-face-service-endpoint
FACE_SERVICE_KEY=your-face-service-key
```

**How to find these values:**

- **FACE_SERVICE_ENDPOINT**: In Azure portal, go to your face service you created → Keys and Endpoints → find the "Endpoint"
- **FACE_SERVICE_KEY**: In Azure portal, go to your face service you created → Keys and Endpoints → find the "KEY 1"

## Running the Application

1. Run the application:
   ```bash
   python app.py images/face1.jpg
   ```
   
   Notice the detected_faces.jpg file created annotating face in the image. 
   Repeat this step for each image in the images folder. 


## Dependencies

- `azure-ai-vision-face`: Azure AI Vision Face
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file
- `matplotlib`: Data visualization library for Python.

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Check that your FACE_SERVICE_ENDPOINT is correct
2. Check that your FACE_SERVICE_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade azure-identity azure-ai-vision-face==1.0.0b2 matplotlib`

## Project Structure

```
Detect-Analyze-Faces/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── images/              # Images for text read
├── readme.md            # This file
└── install.sh           # Installation script
```


## License

These samples are provided for educational and demonstration purposes.