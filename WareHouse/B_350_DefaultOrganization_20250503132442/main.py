'''
Main application file to run the Teeth Treatment application using standard input and output.
'''
from teeth_manager import TeethManager
def main():
    # Read integers N and Q from standard input
    N = int(input())
    Q = int(input())
    # Initialize TeethManager with N teeth
    teeth_manager = TeethManager(N)
    # Initialize counters for successful, attempted, and skipped treatments
    successful_treatments = 0
    attempted_treatments = 0
    skipped_treatments = 0
    # Process each treatment
    for treatment_number in range(Q):
        attempts = 3  # Allow up to 3 attempts for valid input
        treatment_attempted = False  # Flag to check if treatment was attempted
        while attempts > 0:
            try:
                T_i = int(input()) - 1  # Convert to zero-based index
                if 0 <= T_i < N:
                    teeth_manager.treat(T_i)
                    successful_treatments += 1  # Increment successful treatments
                    treatment_attempted = True  # Mark treatment as attempted
                    break  # Exit the loop if the index is valid
                else:
                    attempts -= 1
                    print(f"Index must be between 1 and {N}. You have {attempts} attempts left.")
            except ValueError:
                attempts -= 1
                print(f"Invalid input. You have {attempts} attempts left.")
        if not treatment_attempted:
            print(f"Maximum attempts reached for treatment {treatment_number + 1}. This treatment was skipped.")
            skipped_treatments += 1  # Increment skipped treatments
            print("You can continue to the next treatment.")
        else:
            attempted_treatments += 1  # Count this treatment as attempted
    # Count and print the remaining teeth
    remaining_teeth = teeth_manager.count_teeth()
    print(remaining_teeth)
    # Print the number of successfully completed and skipped treatments
    print(f"Successfully completed {successful_treatments} treatments.")
    print(f"Attempted {attempted_treatments} treatments in total.")
    print(f"Skipped {skipped_treatments} treatments due to invalid input.")
if __name__ == "__main__":
    main()