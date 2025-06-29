'''
Main application file for the Travel Cost Calculator.
'''
from travel_cost import minimum_travel_cost
from validators import validate_coordinates
def main():
    input_text = input("Enter city coordinates (x, y, z) separated by semicolons: ")
    try:
        coordinates = []
        for coord in input_text.split(';'):
            coord = coord.strip()  # Trim whitespace
            values = coord.split(',')
            if len(values) != 3:
                raise ValueError("Each coordinate must have exactly three values.")
            coordinates.append(tuple(map(int, values)))
        # New validation check for minimum cities
        if len(coordinates) < 2:
            raise ValueError("At least two cities are required.")
        if not validate_coordinates(coordinates):
            raise ValueError("Invalid coordinates: Ensure all coordinates are unique and within bounds.")
        N = len(coordinates)
        min_cost = minimum_travel_cost(N, coordinates)
        print(f"Minimum Travel Cost: {min_cost}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()