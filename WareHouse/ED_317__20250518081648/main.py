'''
Main application file for the grid navigation program.
'''
from grid_processor import GridProcessor
from typing import List
def main():
    '''
    Main function to handle input and output for the grid navigation.
    '''
    grid_input = []
    print("Enter Grid (use S for Start, G for Goal, >, <, v, ^ for persons, # for obstacles):")
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            grid_input.append(list(line.strip()))  # Convert each line to a list of characters
        except EOFError:
            break
    if not grid_input:
        print("Input Error: Please enter a valid grid.")
        return
    try:
        grid_processor = GridProcessor(grid_input)
        reachable, moves = grid_processor.can_reach_goal(grid_processor.H, grid_processor.W, grid_processor.grid)
        if reachable:
            print(f"Goal is reachable in {moves} moves.")
        else:
            print("Goal is not reachable.")
    except Exception as e:
        print(f"Processing Error: {str(e)}")
if __name__ == "__main__":
    main()