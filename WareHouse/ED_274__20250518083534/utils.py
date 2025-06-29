'''
Utility functions for the Takahashi Travel application.
'''
import itertools
import math
from typing import List, Tuple
def get_input(N: int, M: int) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    '''
    Function to get the coordinates of towns and chests from user input.
    '''
    towns = []
    for i in range(N):
        x, y = map(int, input(f"Enter coordinates for town {i + 1} (x y): ").split())
        towns.append((x, y))
    chests = []
    for i in range(M):
        x, y = map(int, input(f"Enter coordinates for chest {i + 1} (x y): ").split())
        chests.append((x, y))
    return towns, chests
def euclidean_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    '''
    Calculate the Euclidean distance between two points.
    '''
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def generate_permutations(towns: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
    '''
    Generate all permutations of the towns.
    '''
    return list(itertools.permutations(towns))
def evaluate_chests(current_position: Tuple[int, int], current_speed: int, chests: List[Tuple[int, int]], next_town: Tuple[int, int], current_time: float) -> Tuple[float, set]:
    '''
    Evaluate which chests to visit based on current position and speed.
    Return updated current_time and visited chests.
    '''
    if not chests:  # Handle case when there are no chests
        return current_time, set()
    visited_chests = set()
    for chest in chests:
        chest_distance = euclidean_distance(current_position, chest)
        time_to_chest = chest_distance / current_speed
        time_from_chest_to_next = euclidean_distance(chest, next_town) / (current_speed + 1)  # Speed boost from chest
        total_time_if_visited = current_time + time_to_chest + time_from_chest_to_next
        # Only visit the chest if it saves time
        if total_time_if_visited < current_time + (euclidean_distance(current_position, next_town) / current_speed):
            current_time = total_time_if_visited
            current_speed += 1  # Speed boost from chest
            current_position = chest
            visited_chests.add(chest)  # Mark chest as visited
    return current_time, visited_chests
def calculate_shortest_time(N: int, M: int, towns: List[Tuple[int, int]], chests: List[Tuple[int, int]]) -> float:
    '''
    Calculate the shortest time for Takahashi to travel through towns and collect chests.
    '''
    min_time = float('inf')
    # Generate all permutations of towns
    for perm in generate_permutations(towns):
        current_time = 0
        current_position = (0, 0)  # Starting from the origin
        current_speed = 1  # Initial speed
        # Visit towns in the current permutation
        for i, town in enumerate(perm):
            distance = euclidean_distance(current_position, town)
            current_time += distance / current_speed
            current_position = town
            # Evaluate chests after visiting each town, passing the next town
            next_town = perm[i + 1] if i + 1 < len(perm) else (0, 0)  # Next town or return to origin
            current_time, visited_chests = evaluate_chests(current_position, current_speed, chests, next_town, current_time)
        # Return to origin
        current_time += euclidean_distance(current_position, (0, 0)) / current_speed
        min_time = min(min_time, current_time)
    return min_time if min_time != float('inf') else 0.0