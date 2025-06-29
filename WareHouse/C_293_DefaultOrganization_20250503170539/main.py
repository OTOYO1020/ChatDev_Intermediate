'''
Main application file for counting paths in a grid using standard input and output.
'''
from path_counter import PathCounter
def main():
    # Read dimensions H and W
    H, W = map(int, input().strip().split())
    # Check for valid dimensions
    if H <= 0 or W <= 0:
        print("Invalid grid dimensions. H and W must be greater than 0.")
        return
    grid = []
    # Populate the grid with H rows of W integers
    for _ in range(H):
        row = list(map(int, input().strip().split()))
        if len(row) != W:
            print("Invalid input. Each row must contain exactly W integers.")
            return
        grid.append(row)
    # Check if the grid is empty after population
    if not grid or len(grid) != H or any(len(row) != W for row in grid):
        print("Invalid grid. Ensure all rows have exactly W integers.")
        return
    # Create a PathCounter instance and count paths
    path_counter = PathCounter(grid)
    visited = set()  # Initialize visited set
    total_paths = path_counter.count_paths(0, 0, visited)
    # Print the total number of paths
    print(f"Total Paths: {total_paths}")
if __name__ == "__main__":
    main()