'''
Main application file for the Triangle Right Check application.
'''
from triangle_utils import validate_input, is_right_triangle
def main():
    input_data = input("Enter coordinates in the format xA, yA, xB, yB, xC, yC (e.g., 0,0,3,0,0,4): ")
    try:
        # Strip whitespace from each coordinate after splitting and ensure they are integers
        coordinates = list(map(int, (coord.strip() for coord in input_data.split(','))))
        if validate_input(coordinates):
            result = is_right_triangle(coordinates)
            print("YES" if result else "NO")
        else:
            print("Input Error: Please enter exactly six integers that can form a triangle (non-collinear).")
    except ValueError:
        print("Input Error: Invalid input. Please enter integers.")
if __name__ == "__main__":
    main()