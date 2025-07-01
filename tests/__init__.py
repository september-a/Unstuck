# Tests package 

import os

def load_test_inputs():
    """Load test inputs from the test_inputs.txt file"""
    test_inputs_file = os.path.join(os.path.dirname(__file__), 'test_inputs.txt')
    try:
        with open(test_inputs_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Warning: Could not find test inputs file at {test_inputs_file}")
        return []
    except Exception as e:
        print(f"Error reading test inputs file: {e}")
        return [] 