'''
Main application file for the Safe Squares application.
'''
from safe_squares import count_safe_squares
def main():
    try:
        N = int(input("Enter Grid Size (N): "))
        pieces_input = input("Enter Pieces (format: x1,y1 x2,y2 ...): ").strip()
        pieces = [tuple(map(int, piece.split(','))) for piece in pieces_input.split() if piece]
        safe_squares_count = count_safe_squares(N, len(pieces), pieces)
        print(f"Safe Squares: {safe_squares_count}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()