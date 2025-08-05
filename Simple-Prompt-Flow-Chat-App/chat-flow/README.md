# Travel Chat Bot - PromptFlow Application

A sophisticated travel assistant chat bot built with Microsoft PromptFlow, powered by Azure OpenAI GPT-4o. This intelligent assistant provides expert travel advice, recommendations, and planning assistance with conversation memory.

## 🌟 Overview

The Travel Chat Bot is designed to act as a knowledgeable travel agent, offering:
- **Personalized Travel Recommendations** - Tailored suggestions based on preferences and budget
- **Expert Travel Advice** - Professional insights on destinations, timing, and logistics
- **Conversation Memory** - Maintains context across multiple interactions
- **Real-time Responses** - Fast, accurate travel information and planning assistance

## 🏗️ Architecture

### PromptFlow Configuration (`flow.dag.yaml`)

```yaml
environment:
  python_requirements_txt: requirements.txt

inputs:
  chat_history:
    type: list
    default: []
    is_chat_input: false
    is_chat_history: true
  question:
    type: string
    default: What is the capital of France?
    is_chat_input: true
    is_chat_history: false

outputs:
  answer:
    type: string
    reference: ${chat.output}
    is_chat_output: true

nodes:
- name: chat
  type: llm
  source:
    type: code
    path: chat.jinja2
  inputs:
    deployment_name: gpt-4o
    temperature: 0.7
    max_tokens: 256
    top_p: 1
    response_format:
      type: text
    chat_history: ${inputs.chat_history}
    question: ${inputs.question}
  provider: AzureOpenAI
  connection: ai-foundry-resource_aoai
  api: chat
  module: promptflow.tools.aoai
```

### Key Components

1. **Input Schema**
   - `question`: User's travel query (string, chat input)
   - `chat_history`: Previous conversation context (list, maintains session state)

2. **LLM Node Configuration**
   - **Model**: GPT-4o via Azure OpenAI
   - **Temperature**: 0.7 (balanced creativity and consistency)
   - **Max Tokens**: 256 (concise but comprehensive responses)
   - **Provider**: Azure OpenAI with enterprise security

3. **Output Schema**
   - `answer`: Generated travel advice and recommendations

## 🎯 Travel Agent Capabilities

### Conversation Flow

The bot maintains conversation context through the `chat_history` parameter:

```json
{
  "question": "Follow-up question about Japan",
  "chat_history": [
    {
      "inputs": {"question": "When is the best time to visit Japan?"},
      "outputs": {"answer": "The best time to visit Japan depends on your preferences..."}
    }
  ]
}
```

## 📁 Project Structure

```
chat-flow/
├── flow.dag.yaml              # PromptFlow configuration
├── chat.jinja2               # Travel agent prompt template
├── requirements.txt          # Python dependencies
├── test_data.jsonl          # Basic test scenarios
├── test_data_with_history.jsonl # Conversation tests
├── quick_test.py            # Simple validation script
├── test_chat_flow.py        # Comprehensive test suite
└── README.md                # This documentation
```

## 🚀 Quick Start

### Prerequisites

1. **Python Environment** - Python 3.11+ with PromptFlow
2. **Azure OpenAI** - Deployed GPT-4o model
3. **Azure AI Connection** - Configured `ai-foundry-resource_aoai`

### Installation

```pwsh
# Install dependencies
pip install -r requirements.txt

# Verify PromptFlow installation
pf --version
```

### Basic Testing

#### Single Question Test
```pwsh
cd chat-flow
pf flow test --flow . --inputs question="What are the best places to visit in Japan during cherry blossom season?"
```

#### Interactive Testing
```pwsh
pf flow test --flow . --interactive
```

#### Batch Testing
```pwsh
pf run create --flow . --data test_data.jsonl
```

### Advanced Testing

#### Comprehensive Test Suite
```pwsh
python test_chat_flow.py
```

#### Quick Validation
```pwsh
python quick_test.py
```

## 🎨 Prompt Engineering

### Travel Agent Persona (`chat.jinja2`)

The prompt is engineered to create a professional travel agent experience:

```jinja
# system:
**Objective**: Assist users with travel-related inquiries, offering tips, advice, and recommendations as a knowledgeable travel agent.

**Capabilities**:
- Provide up-to-date travel information, including destinations, accommodations, transportation, and local attractions.
- Offer personalized travel suggestions based on user preferences, budget, and travel dates.
- Share tips on packing, safety, and navigating travel disruptions.
- Help with itinerary planning, including optimal routes and must-see landmarks.
- Answer common travel questions and provide solutions to potential travel issues.

**Instructions**:
1. Engage with the user in a friendly and professional manner, as a travel agent would.
2. Use available resources to provide accurate and relevant travel information.
3. Tailor responses to the user's specific travel needs and interests.
4. Ensure recommendations are practical and consider the user's safety and comfort.
5. Encourage the user to ask follow-up questions for further assistance.

{% for item in chat_history %}
# user:
{{item.inputs.question}}
# assistant:
{{item.outputs.answer}}
{% endfor %}

# user:
{{question}}
```

### Key Design Principles

1. **Professional Tone** - Maintains travel agent expertise
2. **Context Awareness** - Uses chat history for personalized responses
3. **Safety First** - Prioritizes user safety and comfort
4. **Actionable Advice** - Provides specific, implementable recommendations
5. **Engagement** - Encourages follow-up questions and deeper planning

## 🧪 Testing & Validation

## 🧪 Testing & Validation

### Test Data Scenarios

#### Basic Travel Queries (`test_data.jsonl`)
- **Destination Planning**: Japan cherry blossoms, Australia timing
- **Budget Planning**: Thailand cost estimates, accommodation pricing
- **Documentation**: Europe visa requirements, travel documents
- **Specialized Travel**: Kenya safari packing, solo female travel safety
- **Transportation**: Tokyo to Mount Fuji routes, Amsterdam layovers

#### Conversation Tests (`test_data_with_history.jsonl`)
Progressive multi-turn conversation simulating real travel planning:
1. **Initial Query**: "I'm planning a trip to Japan. What's the best time to visit?"
2. **Follow-up**: "That sounds great! What are the must-see places in Tokyo?"
3. **Detailed Planning**: "How should I get around Tokyo? Is public transport good?"
4. **Budget Inquiry**: "What's the typical cost for accommodation in central Tokyo?"

### Test Scripts

#### Quick Validation (`quick_test.py`)
```python
# Simple validation of core functionality
pf = PFClient()
run = pf.run(flow=".", data="test_data.jsonl", stream=True)
details = pf.get_details(run)
# Displays first 3 results for quick verification
```

#### Comprehensive Testing (`test_chat_flow.py`)
Advanced test suite with multiple modes:
- **Basic Tests**: Individual questions without context
- **Conversation Tests**: Multi-turn dialogues with history
- **Performance Tests**: Response time measurement
- **Interactive Mode**: Real-time testing interface

### Test Execution

```pwsh
# Quick validation
python quick_test.py

# Full test suite
python test_chat_flow.py

# PromptFlow CLI testing
pf flow test --flow . --inputs question="What should I pack for a safari in Kenya?"
pf flow test --flow . --interactive --verbose
```

## 🔧 Configuration & Customization

### Model Configuration

The flow uses GPT-4o with optimized parameters:

```yaml
deployment_name: gpt-4o       # Azure OpenAI model deployment
temperature: 0.7              # Balanced creativity (0.0-1.0)
max_tokens: 256              # Response length limit
top_p: 1                     # Token sampling diversity
response_format:
  type: text                 # Plain text responses
```

### Connection Configuration

Azure OpenAI connection setup:
```pwsh
# Verify connection
pf connection show --name ai-foundry-resource_aoai

# Test connection
pf connection test --name ai-foundry-resource_aoai
```

### Customization Options

#### Modify Travel Expertise
Edit `chat.jinja2` to specialize in:
- **Business Travel** - Corporate travel policies, expense management
- **Adventure Travel** - Extreme sports, outdoor activities
- **Luxury Travel** - Premium experiences, concierge services
- **Budget Travel** - Backpacking, hostels, cost optimization

#### Adjust Response Style
Modify prompt instructions for:
- **Formal**: Professional business tone
- **Casual**: Friendly, conversational approach
- **Detailed**: Comprehensive planning assistance
- **Concise**: Quick, essential information only

#### Regional Specialization
Customize for specific regions:
```jinja
**Regional Expertise**: Focus on {{region}} travel including local customs, 
currency, language tips, and region-specific safety considerations.
```

## 🚀 Deployment Options

### Local Development
```pwsh
# Run locally for development
pf flow serve --flow . --port 8080
curl -X POST http://localhost:8080/score -H "Content-Type: application/json" -d '{"question": "Best time to visit Italy?", "chat_history": []}'
```

### Azure AI Studio Deployment

#### 1. Upload Flow
```pwsh
# Upload to Azure AI Studio
pf flow create --flow . --cloud
```

#### 2. Deploy Endpoint
```pwsh
# Create real-time endpoint
pf deployment create --flow . --name travel-bot-endpoint --cloud
```

#### 3. Test Deployment
```pwsh
# Test deployed endpoint
pf deployment test --name travel-bot-endpoint --cloud --inputs question="Travel advice for Japan"
```

### Integration Examples

#### REST API Usage
```python
import requests

endpoint = "https://your-endpoint.inference.ml.azure.com/score"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your-api-key"
}

data = {
    "question": "What are the best places to visit in Japan during cherry blossom season?",
    "chat_history": []
}

response = requests.post(endpoint, headers=headers, json=data)
print(response.json()["answer"])
```

#### Chat Interface Integration
```python
class TravelChatSession:
    def __init__(self, endpoint_url, api_key):
        self.endpoint = endpoint_url
        self.api_key = api_key
        self.chat_history = []
    
    def ask_question(self, question):
        payload = {
            "question": question,
            "chat_history": self.chat_history
        }
        
        response = requests.post(
            self.endpoint,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload
        )
        
        answer = response.json()["answer"]
        
        # Update chat history
        self.chat_history.append({
            "inputs": {"question": question},
            "outputs": {"answer": answer}
        })
        
        return answer
```

## 📊 Performance & Monitoring

### Expected Performance
- **Response Time**: 2-5 seconds per query
- **Throughput**: 10-15 requests per minute (single instance)
- **Context Length**: Supports 5+ turn conversations
- **Accuracy**: High-quality travel advice with factual information

### Monitoring Metrics
```pwsh
# View deployment metrics
pf deployment show --name travel-bot-endpoint --cloud

# Check logs
pf deployment get-logs --name travel-bot-endpoint --cloud

# Monitor performance
az monitor metrics list --resource [endpoint-resource-id] --metric-names RequestLatency,RequestsPerSecond
```

## 🔍 Troubleshooting

### Common Issues

#### Connection Problems
```pwsh
# Verify Azure OpenAI connection
pf connection show --name ai-foundry-resource_aoai

# Test connection
pf connection test --name ai-foundry-resource_aoai
```

#### Model Deployment Issues
- Ensure GPT-4o is deployed in your Azure OpenAI service
- Verify deployment name matches `flow.dag.yaml` configuration
- Check quota availability in your subscription

#### Flow Execution Errors
```pwsh
# Test flow locally
pf flow test --flow . --inputs question="Test question"

# Validate flow definition
pf flow validate --flow .

# Check detailed logs
pf run show-details --name [run-name]
```

### Debug Steps

1. **Validate Dependencies**
   ```pwsh
   pip install -r requirements.txt
   pf --version
   ```

2. **Test Connection**
   ```pwsh
   pf connection list
   pf connection show --name ai-foundry-resource_aoai
   ```

3. **Validate Flow**
   ```pwsh
   pf flow validate --flow .
   pf flow test --flow . --inputs question="Hello"
   ```

4. **Check Azure Resources**
   ```pwsh
   az cognitiveservices account list
   az cognitiveservices account deployment list --name [openai-service-name] --resource-group [rg-name]
   ```

## 🔗 Integration with Evaluation Flow

This chat-flow integrates seamlessly with the evaluation system:

```pwsh
# Run chat flow and generate responses
cd chat-flow
python test_chat_flow.py

# Evaluate responses for quality
cd ../evaluation-flow
python run_chat_and_evaluate.py
```

The evaluation flow assesses:
- **Relevance**: How well responses address travel questions
- **Helpfulness**: Practical value for travelers
- **Accuracy**: Factual correctness of travel information
- **Expertise**: Professional travel agent knowledge demonstrated

## 🎯 Use Cases

### Individual Travelers
- Trip planning and itinerary suggestions
- Budget estimation and cost optimization
- Safety advice and travel tips
- Cultural guidance and etiquette

### Travel Agencies
- Customer service automation
- Initial consultation assistance
- FAQ handling and information delivery
- Lead qualification and routing

### Corporate Travel
- Policy compliance guidance
- Expense management advice
- Business travel optimization
- Emergency travel assistance

## 🛡️ Security & Best Practices

### Production Deployment
- Use managed identity for Azure authentication
- Store sensitive configuration in Azure Key Vault
- Enable endpoint authentication and authorization
- Implement rate limiting and usage monitoring

### Data Privacy
- No personal data storage in chat history
- Stateless conversation design
- Compliance with travel industry regulations
- Secure API communication with HTTPS

### Performance Optimization
- Monitor token usage and costs
- Implement caching for common queries
- Use auto-scaling for variable demand
- Optimize prompt for efficient token usage

## 📚 Additional Resources

- [PromptFlow Documentation](https://microsoft.github.io/promptflow/)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/)
- [Azure AI Studio](https://azure.microsoft.com/en-us/products/ai-studio/)
- [Travel Industry Best Practices](https://docs.microsoft.com/en-us/azure/architecture/industries/travel/)
