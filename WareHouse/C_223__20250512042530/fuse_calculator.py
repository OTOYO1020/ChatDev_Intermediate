'''
Contains the logic to calculate the meeting point of the flames.
'''
from typing import List
def find_meeting_point(N: int, A: List[float], B: List[float]) -> float:
    left_position = 0.0
    right_position = sum(A)
    left_index = 0
    right_index = N - 1
    left_time = 0.0
    right_time = 0.0
    while left_index <= right_index:
        time_to_next_left = (A[left_index] - left_position) / B[left_index] if left_index < N else float('inf')
        time_to_next_right = (right_position - (sum(A) - A[right_index])) / B[right_index] if right_index >= 0 else float('inf')
        if left_time + time_to_next_left < right_time + time_to_next_right:
            left_time += time_to_next_left
            left_position = A[left_index]
            left_index += 1
            right_position -= time_to_next_left * B[right_index]
        else:
            right_time += time_to_next_right
            right_position = sum(A) - A[right_index]
            right_index -= 1
            left_position += time_to_next_right * B[left_index]
    # Calculate the meeting point based on the final positions of both flames
    return (left_position + right_position) / 2