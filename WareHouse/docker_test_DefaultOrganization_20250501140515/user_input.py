'''
Class to manage user input fields.
'''
class UserInput:
    @staticmethod
    def get_input():
        attempt_count = 0
        max_attempts = 5  # Limit the number of attempts
        while attempt_count < max_attempts:
            try:
                user_input = input("Enter your input (type 'exit' to quit): ")
                if user_input.strip().lower() == "exit":  # Check for exit command
                    print("You have chosen to exit the input prompt. Thank you for using the program!")
                    return None  # Indicate that the input process should stop
                if user_input.strip():  # Check if input is not empty or whitespace
                    return user_input
                else:
                    attempt_count += 1
                    remaining_attempts = max_attempts - attempt_count
                    print(f"Invalid input. Please enter a non-empty value (not just spaces). You have {remaining_attempts} attempts left.")
            except KeyboardInterrupt:
                print("\nInput interrupted. Exiting the program gracefully. Thank you!")
                return None  # Indicate that the input process should stop
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
                attempt_count += 1  # Increment attempt count only for unexpected errors
        print("Maximum attempts reached. Exiting the program.")
        return None  # Indicate that the input process should stop