#!/usr/bin/env python3
"""
Evaluation script for the travel chat bot.
This script runs the evaluation flow against test data.
"""

from promptflow import PFClient
import json

def run_evaluation():
    """Run the evaluation flow with test data."""
    
    # Initialize the PromptFlow client
    pf = PFClient()
    
    # Set the flow path (current directory)
    flow = "."
    
    # Set the test data file
    data = "test_data.jsonl"
    
    print("Starting evaluation of travel chat bot...")
    print(f"Flow: {flow}")
    print(f"Data: {data}")
    
    try:
        # Run the evaluation flow
        evaluation_run = pf.run(
            flow=flow,
            data=data,
            stream=True,
        )
        
        print(f"Evaluation run completed successfully!")
        print(f"Run name: {evaluation_run.name}")
        
        # Get the evaluation results
        details = pf.get_details(evaluation_run)
        print("\nEvaluation Results:")
        print("=" * 50)
        
        # Print summary of results
        for index, row in details.iterrows():
            print(f"\nTest Case {index + 1}:")
            print(f"Question: {row.get('inputs.question', 'N/A')[:100]}...")
            print(f"Relevance: {row.get('outputs.relevance_score', 'N/A')}")
            print(f"Helpfulness: {row.get('outputs.helpfulness_score', 'N/A')}")
            print(f"Accuracy: {row.get('outputs.accuracy_score', 'N/A')}")
            print(f"Travel Expertise: {row.get('outputs.travel_expertise_score', 'N/A')}")
            print("-" * 30)
        
        return evaluation_run
        
    except Exception as e:
        print(f"Error running evaluation: {e}")
        return None

if __name__ == "__main__":
    run_evaluation()
