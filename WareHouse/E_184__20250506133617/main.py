'''
Main application file for the grid pathfinding application using BFS.
'''
from collections import deque
from bfs import find_shortest_time
def main():
    # Read grid dimensions from standard input
    H, W = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    S = None
    G = None
    # Identify positions of 'S' and 'G'
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                S = (i, j)
            elif grid[i][j] == 'G':
                G = (i, j)
    if S is not None and G is not None:
        time_taken = find_shortest_time(S, G, grid)
        print(time_taken)  # Print only the time taken
    else:
        print("Start or Goal not found!")
if __name__ == "__main__":
    main()