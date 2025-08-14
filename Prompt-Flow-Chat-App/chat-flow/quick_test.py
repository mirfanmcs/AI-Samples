#!/usr/bin/env python3
"""
Quick test script for the travel chat bot.
Simple script to run a few questions and see responses.
"""

from promptflow import PFClient
import json

def quick_test():
    """Run a quick test of the chat flow."""
    
    print("🚀 Quick Chat Flow Test")
    print("=" * 30)
    
    # Initialize PromptFlow client
    pf = PFClient()
    
    # Test with basic data
    try:
        run = pf.run(
            flow=".",
            data="test_data.jsonl",
            stream=True,
        )
        
        print(f"✅ Test completed: {run.name}")
        
        # Get and display first few results
        details = pf.get_details(run)
        
        print("\n📊 Sample Results:")
        print("-" * 40)
        
        # Show first 3 results
        for index, row in details.head(3).iterrows():
            question = row.get('inputs.question', 'N/A')
            answer = row.get('outputs.answer', 'No response')
            
            print(f"\n❓ {question}")
            print(f"🤖 {answer}")
            print("-" * 40)
        
        total_tests = len(details)
        print(f"\n📈 Total tests run: {total_tests}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you're in the chat-flow directory")
        print("2. Check that your Azure OpenAI connection is working")
        print("3. Verify test_data.jsonl exists")
        return False

if __name__ == "__main__":
    quick_test()
