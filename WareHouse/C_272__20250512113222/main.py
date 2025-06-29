'''
Main application file for the Max Even Sum Calculator.
'''
from max_even_sum import find_max_even_sum
def main():
    '''
    Main function to handle input and output for the Max Even Sum Calculator.
    '''
    # Read input from standard input
    while True:
        try:
            N = int(input("Enter the number of distinct non-negative integers (must be at least 2): "))
            if N < 2:
                print("Error: You must enter at least 2 distinct non-negative integers.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")
    while True:
        try:
            A = list(map(int, input(f"Enter exactly {N} distinct non-negative integers (space-separated): ").split()))
            if len(A) == N:
                # Check for distinct and non-negative integers
                if len(A) == len(set(A)) and all(x >= 0 for x in A):
                    break
                else:
                    print("Error: All integers must be distinct and non-negative. Please try again.")
            else:
                print(f"Error: Expected {N} distinct non-negative integers, but got {len(A)}. Please try again.")
        except ValueError:
            print("Error: Please enter valid non-negative integers.")
    # Calculate the maximum even sum
    max_even_sum = find_max_even_sum(A)
    # Output the result
    print(max_even_sum)
if __name__ == "__main__":
    main()