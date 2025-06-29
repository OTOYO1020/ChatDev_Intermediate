'''
Main entry point of the application that handles user input and calculates the factorial.
'''
from factorial_calculator import calculate_factorial
def main():
    user_input = input("Enter an integer (>= 2): ")
    if validate_input(user_input):
        x = int(user_input)
        n = calculate_factorial(x)
        if n is not None:
            print(f"The smallest N such that N! = {x} is: {n}")
        else:
            print(f"There is no integer N such that N! = {x}.")
    else:
        print("Input Error: Please enter an integer greater than or equal to 2.")
def validate_input(user_input):
    """
    Validate the user input to ensure it is an integer and >= 2.
    """
    try:
        value = int(user_input)
        return value >= 2
    except ValueError:
        return False
if __name__ == "__main__":
    main()