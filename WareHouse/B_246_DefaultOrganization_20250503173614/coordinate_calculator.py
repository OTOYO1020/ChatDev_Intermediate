'''
Module for calculating coordinates based on input values A and B.
'''
import math
def calculate_distance(A, B):
    return math.sqrt(A ** 2 + B ** 2)
def normalize_vector(A, B):
    distance = calculate_distance(A, B)
    if distance == 0:  # Check for zero distance
        raise ValueError("Cannot normalize a zero vector.")
    unit_vector_x = A / distance
    unit_vector_y = B / distance
    return (unit_vector_x, unit_vector_y)
def get_new_coordinates(A, B):
    # Check for the zero vector case
    if A == 0 and B == 0:
        print("The coordinates (0, 0) do not represent a valid direction. Returning (0, 0) as default.")
        return (0, 0)  # Return a default value instead of raising an error
    distance = calculate_distance(A, B)
    unit_vector_x, unit_vector_y = normalize_vector(A, B)  # This will not raise an error now
    new_x = unit_vector_x * 1
    new_y = unit_vector_y * 1
    final_x = round(new_x)
    final_y = round(new_y)
    return (final_x, final_y)