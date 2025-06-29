'''
Main application file for the Max Area Calculator.
'''
from area_calculator import max_area_cut
def main():
    try:
        # Read input values for Width (W), Height (H), and cut point (x, y)
        W, H, x, y = map(int, input("Enter Width (W), Height (H), x, y: ").split())
        # Validate input values
        if W <= 0 or H <= 0 or not (0 <= x <= W) or not (0 <= y <= H):
            raise ValueError("Invalid input values.")
    except ValueError as e:
        print(f"Error: {e}")
        return
    # Calculate the maximum area and whether there are multiple ways
    max_area, multiple_ways = max_area_cut(W, H, x, y)
    # Output handling
    print(f"max_area is {max_area} and multiple ways: {multiple_ways}")
if __name__ == "__main__":
    main()