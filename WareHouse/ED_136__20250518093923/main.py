'''
Main entry point of the application that handles user interactions.
'''
from max_divisor import max_divisor
from utils import validate_input
def main():
    try:
        N = int(input("Enter N (size of list): "))
        A = list(map(int, input("Enter A (comma-separated integers): ").split(',')))
        K = int(input("Enter K (number of operations): "))
        # Validate inputs
        validate_input(N, A, K)
        result = max_divisor(N, A, K)
        print(f"Max Divisor: {result}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()