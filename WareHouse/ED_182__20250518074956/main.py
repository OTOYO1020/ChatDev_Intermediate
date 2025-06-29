'''
Main entry point of the Illumination application.
'''
from typing import List, Tuple
from grid import Grid
def main():
    try:
        height = int(input("Enter Height: "))
        width = int(input("Enter Width: "))
        # Handle input for bulbs and blocks
        bulbs_input = input("Enter Bulbs (x,y) separated by semicolon: ").strip()
        blocks_input = input("Enter Blocks (x,y) separated by semicolon: ").strip()
        # Validate bulbs input
        bulbs = []
        if bulbs_input:
            for bulb in bulbs_input.split(';'):
                try:
                    x, y = map(int, bulb.split(','))
                    bulbs.append((x - 1, y - 1))  # Adjust for 1-based to 0-based indexing
                except ValueError:
                    print("Error: Invalid bulb format. Use (x,y) format.")
                    return
        # Validate blocks input
        blocks = []
        if blocks_input:
            for block in blocks_input.split(';'):
                try:
                    x, y = map(int, block.split(','))
                    blocks.append((x - 1, y - 1))  # Adjust for 1-based to 0-based indexing
                except ValueError:
                    print("Error: Invalid block format. Use (x,y) format.")
                    return
        # Validate positions
        for x, y in bulbs + blocks:
            if not (0 <= x < height and 0 <= y < width):
                print("Error: Bulb or Block position out of bounds.")
                return
        # Check for overlapping bulbs and blocks
        if any(bulb in blocks for bulb in bulbs):
            print("Error: Bulb and Block positions cannot overlap.")
            return
        grid = Grid(height, width, bulbs, blocks)
        illuminated_count = grid.count_illuminated_squares()
        print(f"Illuminated Squares: {illuminated_count}")
    except ValueError:
        print("Error: Please enter valid integers for height and width.")
if __name__ == "__main__":
    main()