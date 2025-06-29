'''
Main entry point for the maze application.
'''
from maze import max_moves
if __name__ == "__main__":
    # Read input dimensions
    try:
        H, W = map(int, input("Enter maze dimensions (H W): ").split())
        if H <= 0 or W <= 0:
            raise ValueError("Dimensions must be positive integers.")
    except ValueError as ve:
        print(f"Error: {str(ve)}")
        exit(1)  # Exit the program if input is invalid
    # Read maze representation
    S = [input().strip() for _ in range(H)]
    # Validate maze representation
    if len(S) != H:
        print(f"Error: Expected {H} rows, but got {len(S)}.")
        exit(1)  # Exit the program if input is invalid
    for row in S:
        if len(row) != W or any(char not in ('.', '#') for char in row):
            print("Error: Each row must have exactly W characters and can only contain '.' and '#' characters.")
            exit(1)  # Exit the program if input is invalid
    try:
        result = max_moves(H, W, S)
        print(f"Max Moves: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")