'''
Main application file for the Lattice Point Checker.
'''
from lattice_logic import find_lattice_points
def main():
    '''
    Main function to read input coordinates and check for lattice points.
    '''
    try:
        # Read coordinates from standard input
        x1, y1 = map(int, input("Enter coordinates x1, y1 (format: x1,y1, e.g., 1,2): ").strip().split(','))
        x2, y2 = map(int, input("Enter coordinates x2, y2 (format: x2,y2, e.g., 3,4): ").strip().split(','))
        # Check for lattice points
        if find_lattice_points(x1, y1, x2, y2):
            print("YES")
        else:
            print("NO")
    except ValueError:
        print("Input Error: Please enter valid integer coordinates in the format x,y.")
if __name__ == "__main__":
    main()