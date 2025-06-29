'''
Main application file for the coordinate calculator using standard input and output.
'''
from coordinate_calculator import calculate_distance, normalize_vector, get_new_coordinates  # Importing necessary functions
def main():
    try:
        A = int(input("Enter an integer value for A (x-coordinate): "))
        B = int(input("Enter an integer value for B (y-coordinate): "))
        final_x, final_y = get_new_coordinates(A, B)
        print(f"Final Coordinates: ({final_x}, {final_y})")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid integer coordinates.")
if __name__ == "__main__":
    main()