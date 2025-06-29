'''
Main entry point for the application.
'''
from app import App
import sys
if __name__ == "__main__":
    # Redirect standard input to read from command line
    input_data = sys.stdin.read().strip().splitlines()
    # Simulate the input for the application
    if input_data:
        root = App(input_data)
        root.run()