'''
Main application file for the blackout counting program.
'''
from grid import Grid
def main():
    try:
        H = int(input("Enter Height (H): "))
        W = int(input("Enter Width (W): "))
        N = int(input("Enter Number of Integers (N): "))
        h = int(input("Enter Blackout Height (h): "))
        w = int(input("Enter Blackout Width (w): "))
        # Check for valid blackout dimensions
        if h > H or w > W:
            print("Error: Blackout dimensions exceed grid dimensions.")
            return
        grid = Grid(H, W)
        grid.populate_grid()  # Updated to read from input
        distinct_counts = grid.count_distinct_numbers(h, w)
        print("Distinct Counts: " + ', '.join(map(str, distinct_counts)))
    except ValueError:
        print("Input Error: Please enter valid integers.")
if __name__ == "__main__":
    main()