'''
Main entry point for the character replacement application.
'''
from input_handler import InputHandler  # Importing InputHandler class
from output_display import OutputDisplay  # Importing OutputDisplay class
def main():
    input_handler = InputHandler()
    output_display = OutputDisplay()
    # Read integer values N and Q with validation
    try:
        N, Q = map(int, input().split())
        if N <= 0 or Q < 0:
            raise ValueError("N must be a positive integer and Q must be a non-negative integer.")
    except ValueError as e:
        print(f"Invalid input for N and Q: {e}")
        return
    # Read the string S of length N directly from input
    S = input().strip()  # Directly read and strip the input
    # Validate that the length of S matches N
    if len(S) != N:
        print(f"The length of the string S ({len(S)}) does not match N ({N}).")
        return
    if len(S) == 0:
        print("The string S cannot be empty.")
        return
    # Read all operation lines into a list only if Q > 0
    operations = []
    if Q > 0:
        input_lines = [input() for _ in range(Q)]
        # Initialize a list to store Q pairs of characters (c_i, d_i)
        operations = input_handler.get_operations(Q, input_lines)
    # Replace all occurrences of characters in S based on the operations
    for c_i, d_i in operations:
        S = S.replace(c_i, d_i)  # Apply each replacement in order
    # Print the modified string S as the output
    output_display.show_output(S)
if __name__ == "__main__":
    main()