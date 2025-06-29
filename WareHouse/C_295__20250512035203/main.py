'''
This module is the main entry point for the Sock Pair Calculator application.
It handles user input and displays the result in the console.
'''
from sock_pair_calculator import SockPairCalculator
def main():
    calculator = SockPairCalculator()
    # Get user input
    try:
        N = int(input("Enter number of socks (N): "))
        colors_input = input("Enter sock colors (comma-separated): ")
        A = list(map(int, colors_input.split(',')))
        # Validate input before processing
        if not calculator.validate_input(N, A):
            print("Invalid input. Please ensure that N is between 1 and 500,000 and matches the number of sock colors provided.")
            return  # Early exit on invalid input
        pairs = calculator.max_pairs(N, A)
        print(f"Maximum pairs: {pairs}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()