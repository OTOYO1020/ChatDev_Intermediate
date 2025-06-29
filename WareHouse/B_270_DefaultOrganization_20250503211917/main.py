'''
Main application file for calculating minimum distance based on user input.
'''
from utils import validate_input  # Importing the validate_input function
def calculate_distance(x, y, z):
    min_distance = float('inf')  # Initialize to infinity to find the minimum distance
    # Check if Takahashi can reach the goal directly
    if x < y:
        min_distance = abs(x - 0)  # Distance from start (0) to X when X < Y
    elif x == y:
        min_distance = 0  # If X is equal to Y, no distance is needed
    # Check if Takahashi can reach the goal after picking up the hammer
    if z < y and x > y:
        distance_with_hammer = abs(z - 0) + abs(y - z) + abs(x - y)  # Total distance with hammer
        min_distance = min(min_distance, distance_with_hammer)  # Update min_distance if this path is shorter
    # If neither condition allows reaching the goal
    if min_distance == float('inf'):
        min_distance = -1  # Set to -1 if no valid path exists
    return min_distance
if __name__ == "__main__":
    while True:
        x_input = input("Enter the integer value for X (Takahashi's starting point): ")
        y_input = input("Enter the integer value for Y (Goal position): ")
        z_input = input("Enter the integer value for Z (Hammer position): ")
        if validate_input(x_input) and validate_input(y_input) and validate_input(z_input):
            x = int(x_input)
            y = int(y_input)
            z = int(z_input)
            break  # Exit the loop if inputs are valid
        else:
            print("Please enter valid integers.")
    result = calculate_distance(x, y, z)
    print(f"Minimum Distance: {result}")