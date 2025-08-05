# Travel Chat Bot Evaluation Flow

This evaluation flow is designed to comprehensively assess the quality of responses from the travel chat bot. It evaluates multiple dimensions of response quality to ensure the bot provides helpful, accurate, and professional travel advice.

## Evaluation Dimensions

### 1. Relevance (relevance_eval.jinja2)
- **Purpose**: Measures how well the response addresses the user's travel question
- **Scale**: 1-5 (1 = Not relevant, 5 = Perfectly relevant)
- **Criteria**: On-topic content, direct addressing of the question, focus on travel-related information

### 2. Helpfulness (helpfulness_eval.jinja2)
- **Purpose**: Evaluates the practical value and actionability of the response
- **Scale**: 1-5 (1 = Not helpful, 5 = Extremely helpful)
- **Criteria**: Actionable advice, practical recommendations, usefulness for travel planning

### 3. Accuracy (accuracy_eval.jinja2)
- **Purpose**: Assesses factual correctness and reliability of travel information
- **Scale**: 1-5 (1 = Inaccurate, 5 = Completely accurate)
- **Criteria**: Factual correctness, up-to-date information, absence of misleading statements

### 4. Travel Expertise (travel_expertise_eval.jinja2)
- **Purpose**: Measures professional travel agent knowledge and expertise demonstrated
- **Scale**: 1-5 (1 = Novice level, 5 = Expert level)
- **Criteria**: Industry knowledge, professional approach, consideration of travel factors

### 5. Overall Summary (overall_summary.jinja2)
- **Purpose**: Provides comprehensive assessment and improvement recommendations
- **Output**: Overall score, rating, strengths, areas for improvement, and summary

## Files Structure

```
evaluation-flow/
├── flow.dag.yaml                 # Main evaluation flow configuration
├── relevance_eval.jinja2         # Relevance evaluation prompt
├── helpfulness_eval.jinja2       # Helpfulness evaluation prompt
├── accuracy_eval.jinja2          # Accuracy evaluation prompt
├── travel_expertise_eval.jinja2  # Travel expertise evaluation prompt
├── overall_summary.jinja2        # Overall summary prompt
├── requirements.txt              # Python dependencies
├── test_data.jsonl              # Sample test data
├── run_evaluation.py            # Script to run evaluation with test data
├── run_chat_and_evaluate.py     # End-to-end chat and evaluation script
└── README.md                    # This documentation
```

## Usage

### Option 1: Run Evaluation with Pre-defined Test Data
```bash
cd evaluation-flow
python run_evaluation.py
```

### Option 2: Run Chat Flow and Then Evaluate
```bash
cd evaluation-flow
python run_chat_and_evaluate.py
```

### Option 3: Use PromptFlow CLI
```bash
cd evaluation-flow
pf run create --flow . --data test_data.jsonl
```

## Test Data Format

The evaluation expects JSONL format with the following fields:

```json
{
  "question": "User's travel question",
  "answer": "Chat bot's response to evaluate",
  "ground_truth": "Expected answer or key points (optional)"
}
```

## Customization

### Adding New Evaluation Criteria
1. Create a new Jinja2 template file (e.g., `new_criteria_eval.jinja2`)
2. Add the evaluation node to `flow.dag.yaml`
3. Update the overall summary to include the new score

### Modifying Scoring Criteria
Edit the respective Jinja2 template files to adjust the evaluation criteria and scoring guidelines.

### Using Different Models
Update the `deployment_name` in `flow.dag.yaml` to use a different Azure OpenAI model.

## Integration with Chat Flow

This evaluation flow is designed to work with the travel chat bot located in `../chat-flow/`. The evaluation can be run independently or as part of an automated testing pipeline.

## Best Practices

1. **Regular Evaluation**: Run evaluations regularly during development to track improvement
2. **Diverse Test Data**: Use varied travel questions covering different scenarios and complexities
3. **Ground Truth**: Provide ground truth answers when possible for more accurate evaluation
4. **Iterative Improvement**: Use evaluation feedback to improve the chat flow prompts and logic

## Sample Output

```
Test Case 1:
Question: What are the best places to visit in Japan during cherry blossom season?
Relevance: Score: 5, Reasoning: Directly answers the cherry blossom question...
Helpfulness: Score: 4, Reasoning: Provides specific locations and practical advice...
Accuracy: Score: 5, Reasoning: All locations and timing information is correct...
Travel Expertise: Score: 4, Reasoning: Shows good travel knowledge and planning advice...
```

## Troubleshooting

- **Connection Issues**: Ensure your Azure OpenAI connection `ai-foundry-resource_aoai` is properly configured
- **Missing Dependencies**: Run `pip install -r requirements.txt` to install required packages
- **Path Issues**: Make sure you're running scripts from the correct directory
