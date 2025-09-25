# Knowledge Mining Using AI Search

A sample application that uses Azure AI Search to perform knowledge mining operations on large datasets. It demonstrates how to create search indexes, extract insights from unstructured data, and build intelligent search experiences.

## Overview

This application:
- Connects to Azure AI Search using provided credentials.
- Prompts user for search queries in a loop.
- Searches the specified index for documents matching the query.
- Retrieves and displays document name, locations, people, and key phrases.


## Prerequisites

- Python 3.8 or higher
- Azure subscription with access to Azure AI Foundry
- Azure AI Search


## Setup Instructions

### 1. Clone or Download the Project

Download or clone this project to your local machine.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt --user
```

### 3. Azure Setup 
- Create Azure AI Foundry AI Search Service in Azure Portal [https://portal.azure.com/](https://portal.azure.com/). Enable system managed identity when you create service. 
- Create the storage account in the same region where you created AI Search service
- Open storage account you created. Under Access Control (IAM), give `Storage Blob Data Contributor` role to the managed identity of your AI Search resource. 
- Create the blob container in your storage account and upload all files from `sample-docs` folder. This data will be used to create indexes for knowledge mining. 
- Open the AI Search resource and click Import data under Overview. 
  - Select `Azure Blob Storage` under Data Source. 
  - Select your storage account and blob container 
  - Select system-assigned managed identity 
  - Click Add congnitive skills tab
    - Under Attach AI Services, select AI Service resource
    - Under Add enrichments
      - Select `Enable OCR`
      - Text Cognitive Skills → select `Extract people names`, `Extract location names`, `Extract key phrases`
      - Image Cognitive Skills → select `Generate tags from images`, `Generate captions from images`
    - Under Save enrichments to a knowledge store
      - Select connection string of storage account with container name `knowledge-store`. Create this container if doens't exists. 
      - Select system-assigned managed identity in the connection string.
      - Azure file projects → select `Image projections`
      - Azure table proejcts → select `Documents` → `Key phrases`
      - Add blob projections → select `Documents
      - Enter `knowledge-store` in the Container name
   - Click Customize target index tab 
     - Select `analyzingInfixMatching` in search mode 
     - Select `Retrievable`, `Filterable`, `Sortable` for metadata_storage_size, metadata_storage_last_modified
     - Select `Retrievable`, `Filterable`, `Sortable`, `Searchable` for metadata_storage_name
     - Select `Retrievable`, `Filterable`, `Searchable` for locations, people, keyphrases
- Test the index by running following queries in Search explorer
```code
 {
   "search": "*",
   "count": true
 }
```

```code
 {
   "search": "*",
   "count": true,
   "select": "metadata_storage_name,locations"
 }
```

```code
 {
   "search": "New York",
   "count": true,
   "select": "metadata_storage_name,keyphrases"
 }
```

```code
 {
     "search": "New York",
     "count": true,
     "select": "metadata_storage_name,keyphrases",
     "filter": "metadata_storage_size lt 380000"
 }
```



### 4. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:



```env
# AI Search Endpoint
AI_SEARCH_ENDPOINT=https://your-ai-search-resource-name.search.windows.net/
QUERY_KEY=your-ai-search-query-key
INDEX_NAME=your-your-index-name
```

**How to find these values:**

- **AI_SEARCH_ENDPOINT**: In Azure portal, go to your AI Search service you created → Overview → find the "Url"
- **QUERY_KEY**: In Azure portal, go to your AI Search service you created → Keys → find the "Manage query keys"
- **INDEX_NAME**: Name of your Index in AI Search


## Running the Application

1. Run the application:
   ```bash
   python app.py
   ```
2 Enter query such as `London`, `Flights`. 


## Dependencies

- `python-dotenv`: For loading environment variables from .env file
- `azure-search-documents==11.5.1`: AI Search 
- `azure-identity`: Azure authentication library

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Verify your account has access to the Azure AI Foundry project
2. Check that your AI_SEARCH_ENDPOINT and QUERY_KEY is correct


### Package Issues

If you encounter package import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt --user`
2. Try upgrading packages: `pip install --upgrade python-dotenv azure-identity azure-search-documents==11.5.1`

## Project Structure

```
Knowledge-Mining-Using-AI-Search/
├── app.py              # Main application file
├── requirements.txt     # Python dependencies
├── readme.md            # This file
├── install.sh           # Installation script (if applicable)
├── sample-docs/         # Sample docs for knowledge mining
└── .env                 # Environment variables (create this file)
```

## License

These samples are provided for educational and demonstration purposes.