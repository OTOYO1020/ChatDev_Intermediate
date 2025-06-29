'''
Main application file for calculating integer averages of subsets.
'''
from average_calculator import count_integer_averages
def main():
    '''
    Main function to handle input and output for the integer average calculation.
    '''
    while True:
        try:
            # Read input from standard input
            N = int(input("Enter the length of the list (must be a positive integer): "))
            if N <= 0:
                raise ValueError("The length of the list must be a positive integer.")
            # Read and validate the list of integers
            A = []
            print(f"Please enter exactly {N} positive integers (space-separated):")
            while len(A) < N:
                A = list(map(int, input().split()))
                if len(A) != N:
                    print(f"Expected {N} integers, but received {len(A)}. Please try again.")
                    A = []  # Reset the list to prompt for input again
                elif any(value <= 0 for value in A):
                    print("All elements in the list must be positive integers. Please try again.")
                    A = []  # Reset the list to prompt for input again
            result = count_integer_averages(N, A)
            print(f"Count of subsets with integer averages: {result}")
            break  # Exit the loop if everything is correct
        except ValueError as e:
            print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()