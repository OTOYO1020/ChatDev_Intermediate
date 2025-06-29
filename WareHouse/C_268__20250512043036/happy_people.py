'''
Module containing the logic to calculate the maximum number of happy people.
'''
from typing import List
def is_person_happy(dish: int, index: int) -> bool:
    """Check if a person at index is happy with the dish value after rotation."""
    return dish == index
def max_happy_people(N: int, dishes: List[int]) -> int:
    # Initialize the maximum number of happy people
    max_happy_count = 0
    # Iterate through all possible rotations of the dishes
    for rotation in range(N):
        # Count happy people for the current rotation
        happy_count = sum(1 for i in range(N) if dishes[(i + rotation) % N] == i)
        # Update the maximum number of happy people found
        max_happy_count = max(max_happy_count, happy_count)
    return max_happy_count