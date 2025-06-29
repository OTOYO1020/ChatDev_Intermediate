'''
Main application file for the visibility checker.
'''
from visibility_checker import VisibilityChecker
def main():
    num_sevens = int(input("Enter the number of 7's: "))
    coordinates = []
    for _ in range(num_sevens):
        while True:
            coord_input = input("Enter coordinates in the format x,y (e.g., 3,4): ")
            try:
                x, y = map(int, coord_input.split(','))
                if x < 0 or y < 0:
                    raise ValueError("Coordinates must be non-negative integers.")
                coordinates.append((x, y))
                break  # Exit the loop if input is valid
            except ValueError as e:
                print(f"Invalid input. {e} Please enter coordinates in the format x,y.")
    origin = (0, 0)  # Origin point
    checker = VisibilityChecker(coordinates)  # Pass coordinates to the checker
    visible_count = 0
    for coord in coordinates:
        if checker.is_visible(origin, coord):
            visible_count += 1
    print(f"Visible 7's: {visible_count}")
if __name__ == "__main__":
    main()