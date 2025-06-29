'''
Main application file for the cumulative product sum calculator.
'''
from calculator import calculate_total_sum
def get_input(N):
    max_attempts = 3  # Set a limit for attempts
    attempts = 0
    while attempts < max_attempts:
        try:
            # Read the array A of size N containing integers
            A = list(map(int, input(f"Please enter exactly {N} integers (separated by spaces): ").split()))
            if len(A) == N:
                return A
            else:
                print(f"Expected {N} integers, but got {len(A)}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter only integers.")
        attempts += 1
        print(f"You have {max_attempts - attempts} attempts left.")
    print("Maximum attempts reached. Please restart the program and try again.")
    return None  # Return None if maximum attempts are reached
def main():
    try:
        # Read the integer N from standard input
        N = int(input("Enter the number of integers: "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        # Get the array A from user input
        A = get_input(N)
        if A is None:
            return  # Exit if input was not successful
        # Calculate the total sum of products
        total_sum = calculate_total_sum(A)
        # Print the final value of total_sum
        print(total_sum)
    except ValueError as e:
        print(f"Input error: {e}")
if __name__ == "__main__":
    main()