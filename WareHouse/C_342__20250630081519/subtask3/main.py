'''
Main entry point for the character replacement application.
'''
from input_handler import InputHandler  # Importing InputHandler class
from output_display import OutputDisplay  # Importing OutputDisplay class
def main():
    input_handler = InputHandler()
    output_display = OutputDisplay()
    # Read integer values N and Q
    N, Q = map(int, input().split())
    # Read the string S of length N
    S = input_handler.get_string(input())
    # Read all operation lines into a list
    input_lines = [input() for _ in range(Q)]
    # Initialize a list to store Q pairs of characters (c_i, d_i)
    operations = input_handler.get_operations(Q, input_lines)
    # Replace all occurrences of character c_i in string S with character d_i
    for c_i, d_i in operations:
        S = S.replace(c_i, d_i)
    # Print the modified string S as the output
    output_display.show_output(S)
if __name__ == "__main__":
    main()