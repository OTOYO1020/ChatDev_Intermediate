'''
Main entry point of the application that handles user input and displays output.
'''
from input_handler import InputHandler
def main():
    input_handler = InputHandler()
    input_handler.get_input()
if __name__ == "__main__":
    main()