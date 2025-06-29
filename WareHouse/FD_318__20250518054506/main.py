'''
Main application file for the Treasure Grabber application.
'''
from typing import List
from treasure_logic import count_grabbable_treasures
def main():
    '''
    Main function to handle input and output for the Treasure Grabber application.
    '''
    try:
        N = int(input("Enter the number of treasures (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        X_input = input("Enter the treasure coordinates (comma-separated, e.g., 1,2,3): ")
        if not X_input.strip():
            raise ValueError("Treasure coordinates cannot be empty.")
        try:
            X = list(map(int, X_input.split(',')))
        except ValueError:
            raise ValueError("All treasure coordinates must be integers.")
        L_input = input("Enter the leg lengths (comma-separated, e.g., 1,2,3): ")
        if not L_input.strip():
            raise ValueError("Leg lengths cannot be empty.")
        try:
            L = list(map(int, L_input.split(',')))
        except ValueError:
            raise ValueError("All leg lengths must be integers.")
        # Check if the lengths of X and L match N
        if len(X) != N or len(L) != N:
            raise ValueError(f"Expected {N} coordinates and {N} leg lengths, but got {len(X)} coordinates and {len(L)} leg lengths.")
        if any(l < 0 for l in L):
            raise ValueError("Leg lengths must be non-negative.")
        valid_positions = count_grabbable_treasures(N, X, L)
        print(f"Valid Positions: {valid_positions}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()