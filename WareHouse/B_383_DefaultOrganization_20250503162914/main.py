'''
Main application file for the humidification calculator.
'''
from grid_processor import GridProcessor
def get_grid_input(H, W):
    '''
    Retrieve the grid input from the user, ensuring it meets the specified requirements.
    '''
    grid_input = []
    total_attempts = 0
    max_attempts = 3  # Set a limit for attempts for the entire grid input
    while len(grid_input) < H and total_attempts < max_attempts:
        row = input().strip()
        if len(row) == W and all(c in ['.', '#'] for c in row):
            grid_input.append(row)
        else:
            total_attempts += 1
            print(f"Invalid input. Each row must be exactly {W} characters long and contain only '.' or '#'. Please try again.")
    if len(grid_input) < H:
        print(f"Maximum attempts reached for grid input. You have entered {len(grid_input)} valid rows. Please provide {H - len(grid_input)} more rows.")
        return None  # Indicate failure to get valid input
    return grid_input
def main():
    while True:  # Loop until valid grid is entered
        try:
            H = int(input("Enter Height (H): "))
            W = int(input("Enter Width (W): "))
            D = int(input("Enter Distance (D): "))
        except ValueError:
            print("Please enter valid integers for Height, Width, and Distance.")
            continue
        # Validate H and W
        if H <= 0 or W <= 0:
            print("Height and Width must be positive integers. Please try again.")
            continue
        print("Enter Grid (row by row, use '.' for floor and '#' for wall):")
        grid_input = get_grid_input(H, W)
        if grid_input is not None:
            grid_processor = GridProcessor(grid_input, D)
            try:
                max_humidified = grid_processor.max_humidified()
                print(f"Maximum Humidified Cells: {max_humidified}")
                break  # Exit the loop if a valid grid is processed
            except ValueError as e:
                print(e)
        else:
            print("Please restart the input process.")
if __name__ == "__main__":
    main()