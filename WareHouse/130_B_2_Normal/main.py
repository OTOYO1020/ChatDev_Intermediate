'''
Main application file for the Bounce Calculator.
'''
import sys
from bounce_calculator import BounceCalculator
def parse_input():
    """Parse the input from standard input."""
    try:
        n = int(input("Enter N: "))
        l = list(map(int, [x.strip() for x in input("Enter list of integers (comma-separated): ").split(',')]))
        if len(l) != n:
            print(f"Input Error: The length of the list must be equal to N ({n}).")
            sys.exit(1)
        x = int(input("Enter X: "))
        return n, l, x
    except ValueError:
        print("Input Error: Please enter valid integers.")
        sys.exit(1)
def main():
    """Main function to execute the bounce calculation."""
    n, l, x = parse_input()
    calculator = BounceCalculator(n, l, x)
    result = calculator.get_result()
    print(f"Valid Bounces: {result}")
if __name__ == "__main__":
    main()