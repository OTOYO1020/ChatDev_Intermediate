'''
Main entry point for the application.
'''
from grid import Grid
def main():
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    grid_obj = Grid(H, W, grid)
    result = grid_obj.find_shortest_time()
    print(result)
if __name__ == "__main__":
    main()