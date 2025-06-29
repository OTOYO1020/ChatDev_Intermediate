'''
Main entry point of the application that handles user interactions for calculating valid strings.
'''
import sys
from string_calculator import StringCalculator
def main():
    try:
        k = int(input("Enter maximum length (K): "))
        c = list(map(int, input("Enter occurrences (26 space-separated integers): ").split()))
        if len(c) != 26:
            raise ValueError("There must be exactly 26 integers for occurrences.")
        calculator = StringCalculator(k, c)
        total_count = calculator.count_valid_strings()
        print(f"Total valid strings: {total_count}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()