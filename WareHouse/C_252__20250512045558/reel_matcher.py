'''
Contains the logic for calculating the minimum time required for all reels to show the same character.
'''
from typing import List
def minimum_seconds_to_match_reels(N: int, S: List[str]) -> int:
    positions = {str(i): [] for i in range(10)}
    # Store positions of each character in the reels
    for reel_index, reel in enumerate(S):
        for char_index, char in enumerate(reel):
            positions[char].append((reel_index, char_index))
    min_time = float('inf')
    # Calculate minimum time for each character
    for char in positions:
        times = []
        for reel_index in range(N):
            # Check if the character exists in the current reel
            min_reel_time = float('inf')
            for (r_index, char_index) in positions[char]:
                if r_index == reel_index:
                    # Calculate the time based on the position and k
                    for k in range(10):  # Limit k to a reasonable range
                        time = (char_index) + k * 10  # Correctly using 0-based index
                        if time >= 0:  # Ensure we only consider non-negative times
                            min_reel_time = min(min_reel_time, time)
            if min_reel_time == float('inf'):
                # If the character is not present in this reel, break and skip to the next character
                break
            times.append(min_reel_time)
        else:  # This else corresponds to the for loop, it executes if the loop is not broken
            # The time for all reels to show this character is the max of the times calculated
            total_time = max(times)
            min_time = min(min_time, total_time)
    return min_time if min_time != float('inf') else -1  # Return -1 if no valid time found