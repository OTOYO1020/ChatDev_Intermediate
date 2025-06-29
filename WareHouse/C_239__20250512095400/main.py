'''
This is the main application file that handles input and output
for checking lattice points at a distance of sqrt(5) from two given points.
'''
from lattice_checker import is_lattice_point_distance_sqrt5  # Import the function
def main():
    import sys
    try:
        input_data = sys.stdin.read().strip()
        x1, y1, x2, y2 = map(int, input_data.split())
        result = is_lattice_point_distance_sqrt5(x1, y1, x2, y2)
        print("Yes" if result else "No")
    except ValueError:
        print("Invalid input. Please enter four integers.")
if __name__ == "__main__":
    main()