# Read Image Text

A sample application that uses Azure AI Foundry Computer Vision Service to extract text from images using OCR (Optical Character Recognition). It can read printed and handwritten text from images and return the extracted content.


## Overview

This application performs the following tasks:
- Initializes the Azure Computer Vision client.
- Accepts an image file for analysis (either a default image or one provided via the command line).
- Reads text from the image.
- Prints the extracted text and individual words to the console.
- Annotates the image with detected lines and words.
- Saves the annotated images to files.


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- An Azure AI Computer Vision Service

## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry Computer Vision Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/). 


### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
# AI Foundry Computer Vision Service Endpoint
CV_SERVICE_ENDPOINT=your-computer-vision-service-endpoint
CV_SERVICE_KEY=your-computer-vision-service-key
```

**How to find these values:**

- **CV_SERVICE_ENDPOINT**: In Azure portal, go to your computer vision service you created → Overview → find the "Endpoint"
- **CV_SERVICE_KEY**: In Azure portal, go to your computer vision service you created → Overview → find the "KEY 1"

## Running the Application

1. Run the application:
   ```bash
   python app.py images/Lincoln.jpg
   ```
   
   Notice the words.jpg file created annotating lines and words in the original image. 
   Repeat this step for each image in the images folder. 


## Dependencies

- `azure-ai-vision-imageanalysis`: Azure AI Vision Image Analysis
- `azure-identity`: Azure authentication library
- `python-dotenv`: For loading environment variables from .env file
- `matplotlib`: Data visualization library for Python.

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Check that your CV_SERVICE_ENDPOINT is correct
2. Check that your CV_SERVICE_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade azure-identity azure-ai-vision-imageanalysis==1.0.0 matplotlib`

## Project Structure

```
Text-Analysis/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── images/              # Images for text read
├── readme.md            # This file
└── install.sh           # Installation script
```


## License

These samples are provided for educational and demonstration purposes.