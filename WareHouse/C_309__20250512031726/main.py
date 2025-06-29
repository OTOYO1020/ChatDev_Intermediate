'''
Main entry point of the application that manages the application flow.
'''
from input_handler import InputHandler
from pills_calculator import PillsCalculator
from typing import List, Tuple
def parse_days_input(days_input: str) -> List[Tuple[int, int]]:
    days = []
    for day in days_input.strip().split(','):
        try:
            a, b = map(int, day.strip().split())
            if a < 1 or b < 1:  # Ensure a_i and b_i are positive integers
                raise ValueError(f"Both a_i and b_i must be positive integers for day: '{day}'.")
            days.append((a, b))
        except ValueError:
            raise ValueError(f"Invalid format for day: '{day}'. Please enter as 'a_i b_i' pairs separated by commas.")
    return days
def main():
    # Read input values
    n = int(input("Enter the number of medicine types (N): "))
    k = int(input("Enter the threshold (K): "))
    days_input = input("Enter the days (a_i, b_i) - comma separated: ")
    # Validate days_input
    if not days_input.strip():
        print("Days input cannot be empty.")
        return
    # Parse the input into a list of tuples
    try:
        days = parse_days_input(days_input)
    except ValueError as e:
        print(e)
        return
    # Validate input
    input_handler = InputHandler(n, k, days)
    if not input_handler.validate_input():
        print("Invalid input values.")
        return
    # Calculate the first day with K or fewer pills
    calculator = PillsCalculator(n, k, days)
    result = calculator.first_day_with_k_or_less_pills()
    print(f"First day with K or less pills: {result if result != -1 else 'No such day'}")
if __name__ == "__main__":
    main()