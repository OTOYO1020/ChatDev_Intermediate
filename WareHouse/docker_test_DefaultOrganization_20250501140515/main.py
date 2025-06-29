'''
Main entry point of the application that manages the application flow using standard input and output.
'''
from user_input import UserInput
from output_display import OutputDisplay
def main():
    user_input_value = UserInput.get_input()
    if user_input_value is None:
        print("Program terminated by user.")
        return  # Exit the main function gracefully
    if user_input_value.strip():  # Check if the input is not empty
        output = f"You entered: {user_input_value}"
        OutputDisplay.show_output(output)
    else:
        print("No valid input was provided.")
if __name__ == "__main__":
    main()