'''
Main entry point for the application that handles user interactions.
'''
from calculator import Calculator
def main():
    x_value_str = input("Enter an integer X (1 ≤ X < 10^500000): ")
    try:
        # Validate input based on numeric content and string length
        if not x_value_str.isdigit():
            raise ValueError("X must be a positive integer.")
        if len(x_value_str) > 500000:
            raise ValueError("X must be less than 10^500000.")
        if int(x_value_str) < 1:
            raise ValueError("X must be in the range 1 ≤ X.")
        calculator = Calculator()
        total_sum = calculator.calculate_total_sum(x_value_str)
        print(total_sum)  # Print the total sum directly as per the task requirement
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()