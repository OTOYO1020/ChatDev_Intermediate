'''
Main application file for the Sum Greater Elements application.
'''
from sum_greater import sum_greater_elements
def main():
    '''
    Main function to handle input and output for the sum of greater elements.
    '''
    try:
        # Read input from standard input
        user_input = input("Enter N followed by the list of integers (space-separated): ")
        parts = list(map(int, user_input.split()))
        # Ensure there is at least one integer for N and at least one integer in the list
        if len(parts) < 2:
            raise ValueError("Please provide at least one integer for N and one integer in the list.")
        N = parts[0]
        A = parts[1:]
        # Ensure the length of A matches N
        if len(A) != N:
            raise ValueError("The length of the list must match N.")
        # Calculate results
        results = sum_greater_elements(A)
        # Print each result on a new line
        for result in results:
            print(result)
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()