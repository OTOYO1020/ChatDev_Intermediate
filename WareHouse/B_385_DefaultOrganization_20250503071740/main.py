'''
Main entry point for the Santa simulation application.
'''
from grid import Grid
def is_valid_position(X, Y, grid_data):
    # Check if the position is within bounds and not an impassable cell
    return 0 <= X < len(grid_data) and 0 <= Y < len(grid_data[0]) and grid_data[X][Y] != '#'
def get_valid_starting_position(H, W):
    max_retries = 3  # Set a maximum number of retries
    retries = 0
    while retries < max_retries:
        try:
            X, Y = map(int, input("Enter new starting position (X Y): ").split())
            if 1 <= X <= H and 1 <= Y <= W:  # Adjusted for 1-based input
                return X - 1, Y - 1  # Return 0-based indexing
            else:
                print("Position out of bounds. Please choose a valid starting position.")
        except ValueError:
            print("Invalid input format. Please enter two integers for the starting position.")
        retries += 1
    print("Exceeded maximum attempts for valid starting position. Exiting program.")
    return None  # Return None instead of exiting
def main():
    # Read input values
    H, W, X, Y = map(int, input().split())
    grid_data = [input().strip() for _ in range(H)]
    # Adjust starting position to 0-based indexing
    current_x, current_y = X - 1, Y - 1
    # Initialize the grid and check the starting position
    while not is_valid_position(current_x, current_y, grid_data):
        print("Starting position is impassable or out of bounds.")
        new_position = get_valid_starting_position(H, W)  # Ensure user can retry
        if new_position is None:
            print("Exiting program due to invalid starting position.")
            return  # Exit gracefully
        current_x, current_y = new_position
    commands = input().strip()  # Read movement commands after confirming the starting position
    grid = Grid(H, W, current_x, current_y, grid_data)
    final_position, houses_count = grid.move_santa(commands)
    # Print the output
    print(f"Final Position: {final_position}")
    print(f"Distinct Houses Visited: {houses_count}")
if __name__ == "__main__":
    main()