'''
Handles user input and processes it for output.
'''
import re  # Importing the re module for input validation
from output_display import OutputDisplay  # Importing the OutputDisplay module for output handling
class InputHandler:
    def __init__(self):
        pass
    def get_input(self):
        while True:
            try:
                user_input = input("Enter your input (type 'exit' to quit): ")
                if user_input.strip().lower() == 'exit':
                    self.handle_exit()
                    break
                if not user_input.strip():  # Check if the input is empty or consists only of whitespace
                    output = "Input cannot be empty or consist only of whitespace. Please enter a valid input."
                else:
                    output = self.process_input(user_input)
                OutputDisplay.display_message(output)  # Using OutputDisplay for output
            except Exception as e:
                OutputDisplay.display_message(f"An error occurred: {e}. Please try again.")
    def process_input(self, user_input):
        '''
        Processes the user input and applies necessary transformations or validations.
        Args:
            user_input (str): The input string provided by the user.
        Returns:
            str: A message indicating the result of the processing.
        '''
        if not re.match("^[A-Za-z0-9 ]*$", user_input):  # Allow spaces in input
            return "Processed Input (Invalid): Your input contains invalid characters. Please use only letters and numbers."
        if user_input.isdigit():
            return f"Processed Input (Number): {user_input}"
        elif user_input.isalpha():
            return f"Processed Input (Text): {user_input}"
        elif any(char.isdigit() for char in user_input) and any(char.isalpha() for char in user_input):
            return f"Processed Input (Mixed): {user_input} - contains both letters and numbers. Ensure no special characters are included."
        else:
            return "Processed Input (Invalid): Please enter a valid input. Ensure it contains only letters and numbers."
    def handle_exit(self):
        '''
        Method to handle exit from the application.
        '''
        OutputDisplay.display_message("Exiting the application. Goodbye!")