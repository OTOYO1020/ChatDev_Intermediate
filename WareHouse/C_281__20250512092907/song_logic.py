'''
Module containing the logic to find the current song and elapsed time.
'''
from typing import List, Tuple
def find_current_song_and_time(N: int, A: List[int], T: int) -> Tuple[int, int]:
    '''
    Calculates the current song index and elapsed time based on the playlist and total time.
    Parameters:
    N (int): Number of songs.
    A (List[int]): List of song durations.
    T (int): Total time elapsed.
    Returns:
    Tuple[int, int]: A tuple containing the current song index (1-based) and elapsed time since it started.
    '''
    if N <= 0 or not A:
        raise ValueError("Invalid input: No songs available.")
    if T < 0:
        raise ValueError("Invalid input: Total time cannot be negative.")
    # Check for zero or negative durations in the list
    if any(duration <= 0 for duration in A):
        raise ValueError("Invalid input: All song durations must be positive.")
    total_duration = sum(A)
    if total_duration == 0:
        raise ValueError("Invalid input: Total duration of songs cannot be zero.")
    # Handle case where T is less than total_duration
    if T < total_duration:
        if T == 0:
            return 1, 0  # Explicitly handle the case where T is zero
        elapsed_time = 0
        for index, duration in enumerate(A):
            if T < elapsed_time + duration:
                return index + 1, T - elapsed_time
            elapsed_time += duration
        return 1, 0  # This line can be removed as it should not be reached if inputs are valid
    complete_cycles = T // total_duration
    remaining_time = T % total_duration
    # Check if remaining_time is zero
    if complete_cycles > 0 and remaining_time == 0:
        return N, A[-1]  # Return the last song and its duration if T is a multiple of total_duration
    elapsed_time = 0
    for index, duration in enumerate(A):
        if remaining_time < elapsed_time + duration:
            return index + 1, remaining_time - elapsed_time
        elapsed_time += duration
    return 1, 0  # Default case, should not reach here if inputs are valid