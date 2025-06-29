'''
Main application file to run the maze solver from standard input.
'''
from maze_solver import MazeSolver
if __name__ == "__main__":
    # Read dimensions of the maze
    H, W = map(int, input().strip().split())
    # Read the maze grid
    S = [input().strip() for _ in range(H)]
    solver = MazeSolver(W, H, S)
    max_moves = solver.calculate_max_moves()
    print(max_moves)