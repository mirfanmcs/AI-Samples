#!/usr/bin/env python3
"""
Test script for the travel chat bot flow.
This script runs the chat flow with various test scenarios and displays results.
"""

from promptflow import PFClient
import json
import os
from datetime import datetime

class ChatFlowTester:
    def __init__(self):
        self.pf = PFClient()
        self.flow_path = "."
        
    def run_basic_tests(self):
        """Run basic tests without chat history."""
        print("🚀 Running Basic Chat Flow Tests")
        print("=" * 50)
        
        data_file = "test_data.jsonl"
        
        try:
            # Run the chat flow
            run = self.pf.run(
                flow=self.flow_path,
                data=data_file,
                stream=True,
            )
            
            print(f"✅ Basic test run completed: {run.name}")
            
            # Get and display results
            details = self.pf.get_details(run)
            self._display_results(details, "Basic Tests")
            
            return run
            
        except Exception as e:
            print(f"❌ Error in basic tests: {e}")
            return None
    
    def run_conversation_tests(self):
        """Run tests with chat history to test conversation flow."""
        print("\n💬 Running Conversation Flow Tests")
        print("=" * 50)
        
        data_file = "test_data_with_history.jsonl"
        
        try:
            # Run the chat flow with conversation history
            run = self.pf.run(
                flow=self.flow_path,
                data=data_file,
                stream=True,
            )
            
            print(f"✅ Conversation test run completed: {run.name}")
            
            # Get and display results
            details = self.pf.get_details(run)
            self._display_conversation_results(details)
            
            return run
            
        except Exception as e:
            print(f"❌ Error in conversation tests: {e}")
            return None
    
    def run_single_question_test(self, question, chat_history=None):
        """Run a single question test interactively."""
        print(f"\n🔍 Testing Single Question")
        print("=" * 50)
        print(f"Question: {question}")
        
        # Create temporary test data
        test_data = {
            "question": question,
            "chat_history": chat_history or []
        }
        
        temp_file = "temp_single_test.jsonl"
        with open(temp_file, 'w') as f:
            f.write(json.dumps(test_data) + '\n')
        
        try:
            # Run the test
            run = self.pf.run(
                flow=self.flow_path,
                data=temp_file,
                stream=True,
            )
            
            # Get results
            details = self.pf.get_details(run)
            
            for index, row in details.iterrows():
                print(f"\n💡 Response:")
                print(f"{row.get('outputs.answer', 'No response')}")
            
            # Clean up
            if os.path.exists(temp_file):
                os.remove(temp_file)
                
            return run
            
        except Exception as e:
            print(f"❌ Error in single question test: {e}")
            # Clean up on error
            if os.path.exists(temp_file):
                os.remove(temp_file)
            return None
    
    def run_performance_test(self):
        """Run performance tests to measure response times."""
        print("\n⚡ Running Performance Tests")
        print("=" * 50)
        
        # Create a smaller dataset for performance testing
        perf_questions = [
            {"question": "What's the weather like in Bali?", "chat_history": []},
            {"question": "Best budget hotels in Bangkok?", "chat_history": []},
            {"question": "How to get a visa for India?", "chat_history": []}
        ]
        
        perf_file = "performance_test.jsonl"
        with open(perf_file, 'w') as f:
            for item in perf_questions:
                f.write(json.dumps(item) + '\n')
        
        try:
            start_time = datetime.now()
            
            run = self.pf.run(
                flow=self.flow_path,
                data=perf_file,
                stream=True,
            )
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            print(f"✅ Performance test completed in {duration:.2f} seconds")
            print(f"⏱️ Average time per question: {duration/len(perf_questions):.2f} seconds")
            
            # Clean up
            if os.path.exists(perf_file):
                os.remove(perf_file)
                
            return run
            
        except Exception as e:
            print(f"❌ Error in performance tests: {e}")
            if os.path.exists(perf_file):
                os.remove(perf_file)
            return None
    
    def _display_results(self, details, test_name):
        """Display test results in a formatted way."""
        print(f"\n📊 {test_name} Results:")
        print("-" * 30)
        
        for index, row in details.iterrows():
            question = row.get('inputs.question', 'N/A')
            answer = row.get('outputs.answer', 'No response')
            
            print(f"\n🗣️ Q{index + 1}: {question}")
            print(f"🤖 A{index + 1}: {answer[:200]}{'...' if len(answer) > 200 else ''}")
            print("-" * 30)
    
    def _display_conversation_results(self, details):
        """Display conversation test results showing the flow."""
        print(f"\n💬 Conversation Flow Results:")
        print("-" * 40)
        
        for index, row in details.iterrows():
            question = row.get('inputs.question', 'N/A')
            answer = row.get('outputs.answer', 'No response')
            chat_history = row.get('inputs.chat_history', [])
            
            print(f"\n📍 Turn {index + 1}:")
            if chat_history:
                print(f"📚 Context: {len(chat_history)} previous exchanges")
            print(f"🗣️ User: {question}")
            print(f"🤖 Assistant: {answer[:250]}{'...' if len(answer) > 250 else ''}")
            print("-" * 40)
    
    def interactive_test(self):
        """Allow user to test questions interactively."""
        print("\n🎯 Interactive Testing Mode")
        print("Enter 'quit' to exit, 'help' for commands")
        print("=" * 50)
        
        chat_history = []
        
        while True:
            question = input("\n💭 Enter your travel question: ").strip()
            
            if question.lower() == 'quit':
                print("👋 Goodbye!")
                break
            elif question.lower() == 'help':
                print("\nCommands:")
                print("- Type any travel question to get a response")
                print("- 'clear' - Clear chat history")
                print("- 'history' - Show current chat history")
                print("- 'quit' - Exit interactive mode")
                continue
            elif question.lower() == 'clear':
                chat_history = []
                print("🧹 Chat history cleared!")
                continue
            elif question.lower() == 'history':
                if chat_history:
                    print(f"📚 Chat history ({len(chat_history)} exchanges):")
                    for i, exchange in enumerate(chat_history, 1):
                        print(f"  {i}. Q: {exchange['inputs']['question'][:50]}...")
                else:
                    print("📭 No chat history")
                continue
            elif not question:
                continue
            
            # Run the test
            run = self.run_single_question_test(question, chat_history)
            
            if run:
                # Get the response and add to history
                details = self.pf.get_details(run)
                for index, row in details.iterrows():
                    response = row.get('outputs.answer', '')
                    chat_history.append({
                        "inputs": {"question": question},
                        "outputs": {"answer": response}
                    })
                    break

def main():
    """Main function to run all tests."""
    print("🌍 Travel Chat Bot - Test Suite")
    print("=" * 50)
    
    tester = ChatFlowTester()
    
    try:
        # Run all test suites
        basic_run = tester.run_basic_tests()
        conv_run = tester.run_conversation_tests()
        perf_run = tester.run_performance_test()
        
        # Summary
        print(f"\n📋 Test Summary:")
        print(f"✅ Basic Tests: {'Passed' if basic_run else 'Failed'}")
        print(f"✅ Conversation Tests: {'Passed' if conv_run else 'Failed'}")
        print(f"✅ Performance Tests: {'Passed' if perf_run else 'Failed'}")
        
        # Ask if user wants interactive testing
        if input("\n🎯 Start interactive testing? (y/n): ").lower().startswith('y'):
            tester.interactive_test()
            
    except KeyboardInterrupt:
        print("\n\n⏹️ Tests interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
