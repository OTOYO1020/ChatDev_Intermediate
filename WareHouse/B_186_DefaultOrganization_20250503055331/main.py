'''
Main entry point for the block grid application.
'''
from grid import Grid
def main():
    try:
        H = int(input("Enter number of rows (H): "))
        W = int(input("Enter number of columns (W): "))
        grid = Grid(H, W)
        grid.get_input()
        blocks_to_remove = grid.calculate_blocks_to_remove()
        print(f"Minimum blocks to remove: {blocks_to_remove}")
    except ValueError:
        print("Input Error: Please enter valid integers for H and W.")
if __name__ == "__main__":
    main()