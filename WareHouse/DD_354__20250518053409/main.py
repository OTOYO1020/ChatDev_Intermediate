'''
Main module to execute the black area calculation based on user input.
'''
from calculator import calculate_black_area
def test_calculate_black_area():
    assert calculate_black_area(0, 0, 2, 2) == 8  # Simple case
    assert calculate_black_area(1, 1, 3, 3) == 8  # Overlapping area
    assert calculate_black_area(-1, -1, 1, 1) == 8  # Negative coordinates
    assert calculate_black_area(0, 0, 0, 0) == 0  # Single point
    assert calculate_black_area(5, 5, 5, 5) == 0  # Invalid rectangle
    assert calculate_black_area(0, 0, 1000, 1000) == 4000000  # Large rectangle
if __name__ == "__main__":
    A, B, C, D = map(int, input("Enter A, B, C, D: ").split())
    result = calculate_black_area(A, B, C, D)
    print(f"The final black area is: {result}")