'''
Main entry point for the chess application.
'''
from collections import deque
from chessboard import Chessboard
def main():
    size = int(input("Enter Chessboard Size (N): "))
    if size <= 0:
        print("Invalid size. Please enter a positive integer.")
        return
    rows = []
    for i in range(size):
        row = input(f"Enter Row {i+1} (must be {size} characters long): ")
        if len(row) != size:
            print(f"Invalid row length. Each row must contain exactly {size} characters.")
            return
        rows.append(row.strip())
    start = input("Enter Starting Position (Ax, Ay) in zero-based format (e.g., 0,0 for top-left): ").strip().split(',')
    if len(start) != 2 or not all(s.strip().isdigit() for s in start):
        print("Invalid input format. Please enter two integers separated by a comma.")
        return
    start = tuple(map(int, start))
    target = input("Enter Target Position (Bx, By) in zero-based format (e.g., 1,1 for second square): ").strip().split(',')
    if len(target) != 2 or not all(t.strip().isdigit() for t in target):
        print("Invalid input format. Please enter two integers separated by a comma.")
        return
    target = tuple(map(int, target))
    if not (0 <= start[0] < size and 0 <= start[1] < size):
        print("Invalid starting position. Please enter valid coordinates.")
        return
    if not (0 <= target[0] < size and 0 <= target[1] < size):
        print("Invalid target position. Please enter valid coordinates.")
        return
    chessboard = Chessboard(size, rows)
    moves = chessboard.bfs(start, target)
    print(f"Minimum Moves: {moves}")
if __name__ == "__main__":
    main()