'''
Main entry point of the application that handles user input and output.
'''
from addition import check_addition
def main():
    try:
        a = int(input("Enter first positive integer (A): "))
        b = int(input("Enter second positive integer (B): "))
        if a <= 0 or b <= 0:
            raise ValueError("Both numbers must be positive integers.")
        result = check_addition(a, b)
        print(result)
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()