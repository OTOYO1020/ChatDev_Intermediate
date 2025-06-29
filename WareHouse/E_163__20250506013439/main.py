'''
Main application file for the Happiness Points Calculator.
'''
import sys
from happiness_calculator import calculate_max_happiness
def main():
    try:
        # Read the number of children
        num_children = int(input("Enter number of children: "))
        # Read the activeness values
        values = list(map(int, input("Enter activeness values (comma separated): ").split(',')))
        if len(values) != num_children:
            raise ValueError("Number of values must match the number of children.")
        max_happiness = calculate_max_happiness(values)
        print(f"Max Happiness Points: {max_happiness}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()