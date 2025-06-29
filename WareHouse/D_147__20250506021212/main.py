'''
Main file to run the XOR Calculator application.
'''
from xor_calculator import calculate_xor_sum
def main():
    while True:
        try:
            # Read the integer N from standard input
            N = int(input("Please enter the total number of integers you wish to input: "))
            # Read the N integers into an array A
            A = list(map(int, input(f"Please enter {N} integers separated by spaces: ").split()))
            # Check if the number of integers entered matches N
            if len(A) != N:
                print(f"Error: You entered {len(A)} integers, but expected {N}. Please try again.")
                continue  # Prompt the user again
            # Calculate the total XOR sum
            total_xor_sum = calculate_xor_sum(N, A)
            # Print the result
            print(total_xor_sum)
            break  # Exit the loop if everything is correct
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid integers.")
if __name__ == "__main__":
    main()