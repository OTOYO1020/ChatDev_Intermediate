'''
Main application file for the ball operations calculator.
'''
def calculate_operations(A, B, C, D):
    operations = 0
    # Calculate the minimum R needed
    R = (A + D - 1) // D  
    # Check if the initial condition is already satisfied
    if A <= D * R:
        return operations
    # Loop until the condition A ≤ D * R is satisfied
    while A > D * R:
        operations += 1  # Increment the operation count
        A += B  # Update the number of cyan balls
        R = (A + D - 1) // D  # Recalculate R based on the updated A
        R += C  # Increment R by C to account for the new red balls
    return operations
if __name__ == "__main__":
    # Read integers A, B, C, and D from standard input
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    C = int(input("Enter C: "))
    D = int(input("Enter D: "))
    # Calculate the number of operations needed
    operations = calculate_operations(A, B, C, D)
    # Print the total number of operations
    print(f"Operations: {operations}")