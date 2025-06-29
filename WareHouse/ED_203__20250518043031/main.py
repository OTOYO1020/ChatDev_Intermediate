'''
Main entry point for the Pawn Game application.
'''
from pawn_logic import count_possible_Y
def main():
    try:
        N = int(input("Enter the maximum row number (N): "))
        M = int(input("Enter the number of black pawns (M): "))
        if N <= 0 or M < 0:
            raise ValueError("N must be a positive integer and M must be a non-negative integer.")
        positions_input = input("Enter black pawn positions (X,Y) separated by commas: ")
        positions = [tuple(map(int, pos.split(','))) for pos in positions_input.split(',')]
        if len(positions) != M:
            raise ValueError(f"Expected {M} black pawn positions, but got {len(positions)}.")
        # Validate that black pawn positions are within bounds and do not overlap
        if any(x < 0 or x > 2 * N or y < 0 or y > N for x, y in positions):
            raise ValueError("Black pawn positions must be within the grid bounds.")
        if len(set(positions)) != len(positions):
            raise ValueError("Black pawn positions must not overlap.")
        valid_count = count_possible_Y(N, M, positions)
        print(f"Valid Y positions: {valid_count}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()