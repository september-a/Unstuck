import sys
import os

# Add the parent directory to the Python path so we can import from agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.listener import parse_user_input
from tests import load_test_inputs

def test_listener():
    """Test the listener agent with various user inputs"""
    
    # Read test inputs from file
    test_inputs = load_test_inputs()
    if not test_inputs:
        print("No test inputs found. Please check the test_inputs.txt file.")
        return
    
    print("Testing Listener Agent\n")
    print("=" * 50)
    
    for i, user_input in enumerate(test_inputs, 1):
        print(f"\nTest {i}:")
        print(f"User Input: {user_input}")
        print("-" * 30)
        
        try:
            # Parse the user input
            result = parse_user_input(user_input)
            
            # Display the structured output
            print("Analysis Results:")
            print(f"  Mood: {result.get('mood', 'N/A')}")
            print(f"  Energy: {result.get('energy', 'N/A')}")
            print(f"  Task: {result.get('task', 'N/A')}")
            print(f"  Blockers: {result.get('blockers', [])}")
            print(f"  Urgency: {result.get('urgency', 'N/A')}")
            
        except Exception as e:
            print(f"Error processing input: {e}")
        
        print()

def interactive_test():
    """Interactive test where you can input your own messages"""
    print("\nInteractive Test Mode")
    print("Enter your message (or 'quit' to exit):")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
            
        try:
            result = parse_user_input(user_input)
            
            print("\nListener Analysis:")
            print(f"  Mood: {result.get('mood', 'N/A')}")
            print(f"  Energy: {result.get('energy', 'N/A')}")
            print(f"  Task: {result.get('task', 'N/A')}")
            print(f"  Blockers: {result.get('blockers', [])}")
            print(f"  Urgency: {result.get('urgency', 'N/A')}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Listener Agent Test Suite")
    print("=" * 50)
    
    # Run automated tests
    test_listener()
    
    # Run interactive test
    interactive_test()