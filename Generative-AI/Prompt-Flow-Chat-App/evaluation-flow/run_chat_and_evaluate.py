#!/usr/bin/env python3
"""
Script to run the chat flow and then evaluate its outputs.
This demonstrates end-to-end evaluation of the travel chat bot.
"""

from promptflow import PFClient
import json
import os

def run_chat_and_evaluate():
    """Run the chat flow and then evaluate the results."""
    
    # Initialize the PromptFlow client
    pf = PFClient()
    
    # Paths
    chat_flow_path = "../chat-flow"
    evaluation_flow_path = "."
    
    # Test questions for the chat bot
    test_questions = [
        {"question": "What are the best places to visit in Japan during cherry blossom season?"},
        {"question": "How much should I budget for a week in Thailand?"},
        {"question": "What documents do I need to travel to Europe?"},
        {"question": "When is the best time to visit Australia?"},
        {"question": "What should I pack for a safari in Kenya?"}
    ]
    
    # Create test data file for chat flow
    chat_test_file = "chat_test_data.jsonl"
    with open(chat_test_file, 'w') as f:
        for question in test_questions:
            f.write(json.dumps(question) + '\n')
    
    print("Step 1: Running chat flow to generate responses...")
    
    try:
        # Run the chat flow
        chat_run = pf.run(
            flow=chat_flow_path,
            data=chat_test_file,
            stream=True,
        )
        
        print(f"Chat flow run completed: {chat_run.name}")
        
        # Get chat flow results
        chat_details = pf.get_details(chat_run)
        
        # Prepare evaluation data by combining questions and answers
        evaluation_data = []
        for index, row in chat_details.iterrows():
            eval_item = {
                "question": row.get('inputs.question', ''),
                "answer": row.get('outputs.answer', ''),
                "ground_truth": ""  # Add ground truth if available
            }
            evaluation_data.append(eval_item)
        
        # Create evaluation test data file
        eval_test_file = "generated_eval_data.jsonl"
        with open(eval_test_file, 'w') as f:
            for item in evaluation_data:
                f.write(json.dumps(item) + '\n')
        
        print("\nStep 2: Running evaluation flow on chat responses...")
        
        # Run the evaluation flow
        evaluation_run = pf.run(
            flow=evaluation_flow_path,
            data=eval_test_file,
            stream=True,
        )
        
        print(f"Evaluation run completed: {evaluation_run.name}")
        
        # Get evaluation results
        eval_details = pf.get_details(evaluation_run)
        
        print("\nEvaluation Results:")
        print("=" * 70)
        
        # Print detailed results
        for index, row in eval_details.iterrows():
            print(f"\nTest Case {index + 1}:")
            print(f"Question: {row.get('inputs.question', 'N/A')}")
            print(f"Answer: {row.get('inputs.answer', 'N/A')[:150]}...")
            print(f"Relevance: {row.get('outputs.relevance_score', 'N/A')}")
            print(f"Helpfulness: {row.get('outputs.helpfulness_score', 'N/A')}")
            print(f"Accuracy: {row.get('outputs.accuracy_score', 'N/A')}")
            print(f"Travel Expertise: {row.get('outputs.travel_expertise_score', 'N/A')}")
            print(f"Overall Evaluation: {row.get('outputs.overall_evaluation', 'N/A')}")
            print("-" * 70)
        
        # Clean up temporary files
        if os.path.exists(chat_test_file):
            os.remove(chat_test_file)
        
        return evaluation_run
        
    except Exception as e:
        print(f"Error in chat and evaluation process: {e}")
        return None

if __name__ == "__main__":
    run_chat_and_evaluate()
