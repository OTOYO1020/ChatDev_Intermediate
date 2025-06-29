'''
Main application file for the binary string value calculator.
'''
from logic import greatest_value_less_than_or_equal
def main():
    try:
        n = int(input("Enter N (integer): "))
        if not (0 <= n <= 1000000):
            raise ValueError("N must be between 0 and 1,000,000.")
        s = input("Enter S (binary string with '?'): ")
        if not s or any(c not in '01?' for c in s):
            raise ValueError("S must contain only '0', '1', or '?'.")
        result = greatest_value_less_than_or_equal(n, s)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()