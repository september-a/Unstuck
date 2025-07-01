import sys
import os

# Add the parent directory to the Python path so we can import from agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.chunker import parse_task
from agents.listener import parse_user_input
from tests import load_test_inputs

def test_chunker():
    """Test the chunker agent with various user inputs"""
    
    # Read test inputs from file
    test_inputs = load_test_inputs()
    if not test_inputs:
        print("No test inputs found. Please check the test_inputs.txt file.")
        return

    print("Testing Chunker Agent\n")
    print("=" * 50)
    
    for i, user_input in enumerate(test_inputs, 1):
        print(f"\nTest {i}:")
        print(f"User Input: {user_input}")
        print("-" * 30)
        
        try:
            # Parse the user input
            result = parse_user_input(user_input)
            result = parse_task(result)
            
            # Display the structured output
            print("Actions:")
            actions = result.get('actions', [])
            if actions:
                for j, action in enumerate(actions, 1):
                    print(f"    {j}. {action.get('action', 'N/A')}")
                    print(f"       Description: {action.get('description', 'N/A')}")
                    print(f"       Priority: {action.get('priority', 'N/A')}")
                    print(f"       Estimated Time: {action.get('estimated_time', 'N/A')}")
                    print()
            else:
                print("    No actions generated")
            
        except Exception as e:
            print(f"Error processing input: {e}")

def interactive_test():
    """Interactive test where you can input your own messages"""
    print("\nInteractive Test Mode")
    print("Enter your message (or 'quit' to exit):")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        try:
            result = parse_user_input(user_input)
            result = parse_task(result)
            
            # Display the structured output
            print("Actions:")
            actions = result.get('actions', [])
            if actions:
                for j, action in enumerate(actions, 1):
                    print(f"    {j}. {action.get('action', 'N/A')}")
                    print(f"       Description: {action.get('description', 'N/A')}")
                    print(f"       Priority: {action.get('priority', 'N/A')}")
                    print(f"       Estimated Time: {action.get('estimated_time', 'N/A')}")
                    print()
            
        except Exception as e:
            print(f"Error: {e}")
            
            
if __name__ == "__main__":
    print("Chunker Agent Test Suite")
    print("=" * 50)
    test_chunker()
    interactive_test()