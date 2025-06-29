'''
Main entry point of the Cookie Finder application.
'''
from typing import List
from grid_manager import GridManager
def main():
    '''
    Main function to handle standard input and output for the Cookie Finder application.
    '''
    grid_data = []
    try:
        # Read grid input from standard input
        while True:
            try:
                line = input().strip()
                if line:
                    grid_data.append(line)
                else:
                    break
            except EOFError:
                break
        # Convert grid_data from list of strings to list of lists of characters
        grid_data = [list(line) for line in grid_data]  # Ensure correct conversion
        grid_manager = GridManager()
        result = grid_manager.process_grid(grid_data)
        if result == (-1, -1):
            print("No missing cookie found.")
        else:
            print(f"Missing cookie at: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()