'''
Main application file for calculating minimum moves in a grid.
'''
import sys
from moves import min_moves
def main():
    # Read input from standard input
    input_start = input("Enter Start Position (r1, c1): ")
    input_target = input("Enter Target Position (r2, c2): ")
    if validate_input(input_start) and validate_input(input_target):
        r1, c1 = map(int, input_start[1:-1].split(','))
        r2, c2 = map(int, input_target[1:-1].split(','))
        moves = min_moves(r1, c1, r2, c2)
        if moves == -1:
            print("Target position is unreachable.")
        else:
            print(f"Minimum Moves: {moves}")
    else:
        print("Input Error: Please enter valid positions in the format (r, c).")
def validate_input(input_str):
    input_str = input_str.strip()
    if input_str.startswith('(') and input_str.endswith(')'):
        input_str = input_str[1:-1]  # Remove parentheses
        try:
            r, c = map(int, input_str.split(','))
            return True
        except ValueError:
            return False
    return False
if __name__ == "__main__":
    main()