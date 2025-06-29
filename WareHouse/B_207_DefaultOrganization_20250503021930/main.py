'''
Main application file for the Ball Operations application.
'''
import math  # Import math for ceiling function
from utils import validate_input  # Import the utility function
def calculate_operations(A, B, C, D):
    '''
    Performs the calculations based on input values A, B, C, and D.
    Returns the total number of operations performed.
    '''
    if A <= D * 0:  # Check if the initial condition is satisfied
        return 0
    operations = 0
    R = 0  # Initialize R to 0
    while A > D * R:  # Continue until the condition is satisfied
        R = math.ceil(A / D)  # Calculate R based on current A and D
        A += B  # Update the number of cyan balls after calculating R
        operations += 1
        R += C  # Increment R by C after each operation
        # Recalculate R based on the updated A
        R = math.ceil(A / D)  # This line ensures R is recalculated correctly
    return operations
if __name__ == "__main__":
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    C = int(input("Enter C: "))
    D = int(input("Enter D: "))
    # Validate input before proceeding
    if validate_input(A, D):
        print("Invalid input: A must be greater than D * 0.")
    else:
        operations = calculate_operations(A, B, C, D)
        print(f"Total operations: {operations}")