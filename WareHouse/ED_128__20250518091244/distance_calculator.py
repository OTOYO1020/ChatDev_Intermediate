'''
Module for calculating distances based on roadworks and people's data.
'''
from typing import List, Tuple
import bisect
def calculate_distances(N: int, Q: int, roadworks: List[Tuple[int, int, int]], people: List[Tuple[int, int]]) -> List[int]:
    # Sort roadworks based on the coordinate X_i
    roadworks.sort(key=lambda x: x[0])
    # Prepare lists for binary search
    X = [rw[0] for rw in roadworks]
    S = [rw[1] for rw in roadworks]
    T = [rw[2] for rw in roadworks]
    results = [0] * Q
    for D_i, index in people:
        # Find the position of the nearest roadwork that starts after D_i
        pos = bisect.bisect_right(X, D_i)
        distance_walked = D_i  # Start with the distance equal to D_i
        blocked = False  # Flag to check if the person is blocked
        # Check the roadworks before the position found
        for i in range(pos):
            if S[i] <= D_i < T[i]:  # Blocked
                distance_walked = X[i] - D_i  # Stop at the blocked point
                blocked = True
                break
            elif D_i < S[i]:  # Can walk to the next roadwork
                distance_walked = D_i  # No blockage, can walk to D_i
                break
        # If not blocked, check if can walk past all roadworks
        if not blocked:
            if pos == 0:  # No roadworks before D_i
                distance_walked = D_i  # Can walk past all roadworks
            elif pos == len(roadworks):  # D_i is greater than the last roadwork's end
                distance_walked = D_i  # Can walk past all roadworks
            else:
                # Check if D_i is between the last roadwork's end and the next roadwork
                if D_i < X[pos]:  # Can walk past the last roadwork
                    distance_walked = D_i
                else:
                    # Adjusted condition to ensure correct distance calculation
                    distance_walked = max(D_i, T[pos - 1])  # Walk past the last roadwork
        results[index] = distance_walked
    return results