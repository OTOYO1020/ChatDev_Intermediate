'''
Main application file for calculating the minimum time to visit towns and return to the origin.
'''
import itertools
import math
from helpers import euclidean_distance, get_permutations, is_chest_on_path
def calculate_min_time(N, M, towns, chests):
    '''
    Calculate the minimum time required to visit all towns and return to the origin.
    '''
    min_time = float('inf')
    for perm in get_permutations(towns):
        current_speed = 1
        current_time = 0
        current_position = (0, 0)
        for town in perm:
            # Calculate distance to the next town
            distance_to_town = euclidean_distance(current_position[0], current_position[1], town[0], town[1])
            # Check for chests along the way to the next town
            encountered_chests = False
            for chest in chests:
                if is_chest_on_path(current_position, town, chest, threshold=1.0):  # Using threshold parameter
                    encountered_chests = True  # Mark that we encountered a chest
                    break  # No need to check further chests
            if encountered_chests:
                current_speed *= 2  # Double speed if a chest is encountered
            # Update time and position after checking for chests
            current_time += distance_to_town / current_speed
            current_position = town
        # Return to origin
        distance_to_origin = euclidean_distance(current_position[0], current_position[1], 0, 0)
        current_time += distance_to_origin / current_speed
        min_time = min(min_time, current_time)
    return min_time
if __name__ == "__main__":
    '''
    Main entry point for the program. Reads input, validates it, and calculates the minimum time.
    '''
    try:
        N = int(input("Enter the number of towns (N): "))
        M = int(input("Enter the number of chests (M): "))
        towns_input = input("Enter towns (X1,Y1;X2,Y2;...): ").split(';')
        chests_input = input("Enter chests (P1,Q1;P2,Q2;...): ").split(';')
        # Validate towns input
        towns = []
        for town in towns_input:
            try:
                x, y = map(int, town.split(','))
                towns.append((x, y))
            except ValueError:
                raise ValueError(f"Invalid town coordinate format: {town}")
        # Validate chests input
        chests = []
        for chest in chests_input:
            try:
                p, q = map(int, chest.split(','))
                chests.append((p, q))
            except ValueError:
                raise ValueError(f"Invalid chest coordinate format: {chest}")
        # Validate input lengths
        if len(towns) != N or len(chests) != M:
            raise ValueError("Number of towns and chests do not match the provided coordinates.")
        min_time = calculate_min_time(N, M, towns, chests)
        print(f"Minimum time required: {min_time:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")