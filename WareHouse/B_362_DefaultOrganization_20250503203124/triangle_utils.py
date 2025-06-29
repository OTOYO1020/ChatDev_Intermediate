'''
Utility functions for triangle calculations and input validation.
'''
def validate_input(coordinates):
    '''
    Validates that the input coordinates are exactly six integers and can form a triangle.
    '''
    if len(coordinates) != 6:
        return False
    # Check if all coordinates are integers
    if not all(isinstance(coord, int) for coord in coordinates):
        return False
    # Check if the coordinates can form a triangle
    x_A, y_A, x_B, y_B, x_C, y_C = coordinates
    # Calculate the area using the determinant method
    area = abs(x_A*(y_B - y_C) + x_B*(y_C - y_A) + x_C*(y_A - y_B))
    if area <= 0:  # Ensure area is greater than zero to confirm triangle formation
        return False
    return True  # Valid input for triangle formation
def is_right_triangle(coordinates):
    '''
    Determines if the triangle formed by the given coordinates is a right triangle.
    '''
    x_A, y_A, x_B, y_B, x_C, y_C = coordinates
    AB_squared = (x_B - x_A) ** 2 + (y_B - y_A) ** 2
    BC_squared = (x_C - x_B) ** 2 + (y_C - y_B) ** 2
    CA_squared = (x_A - x_C) ** 2 + (y_A - y_C) ** 2
    return (AB_squared + BC_squared == CA_squared or
            AB_squared + CA_squared == BC_squared or
            BC_squared + CA_squared == AB_squared)