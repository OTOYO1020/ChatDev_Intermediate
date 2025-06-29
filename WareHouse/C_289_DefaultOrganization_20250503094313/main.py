'''
Main entry point of the application that handles user interactions via standard input and output.
'''
from set_manager import SetManager  # Ensure this import is present
def main():
    # Read integers M and N from standard input
    while True:
        try:
            M = int(input("Enter number of sets (M): "))
            N = int(input("Enter the maximum integer (N): "))
            if M <= 0 or N <= 0:
                print("M and N must be positive integers.")
                continue
            break
        except ValueError:
            print("Please enter valid integers for M and N.")
    set_manager = SetManager(M)  # Pass M to SetManager
    # Initialize a list of sets 'S' to store the integer sets
    for i in range(M):
        while True:
            try:
                C_i = int(input(f"Enter the size of set {i + 1} (must be unique integers): "))
                if C_i <= 0:
                    print("Size of the set must be a positive integer.")
                    continue
                numbers = list(map(int, input(f"Enter exactly {C_i} unique integers separated by space: ").split()))
                if len(numbers) != C_i or len(set(numbers)) != C_i:
                    print(f"Please enter exactly {C_i} unique integers.")
                else:
                    set_manager.add_set(i + 1, numbers)  # Pass the index as i + 1 for 1-based indexing
                    break  # Exit the loop if the correct number of unique integers is entered
            except ValueError:
                print(f"Please enter valid integers for the set {i + 1}.")
    # Calculate valid combinations
    valid_count = set_manager.get_valid_count(N)
    print(f"Valid combinations: {valid_count}")
if __name__ == "__main__":
    main()