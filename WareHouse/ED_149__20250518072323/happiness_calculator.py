'''
Module to calculate maximum happiness based on guests' powers and handshakes.
'''
from typing import List
def max_happiness(N: int, M: int, A: List[int]) -> int:
    happiness = 0
    handshake_set = set()  # To track unique handshakes
    handshake_count = 0
    # Iterate through all possible pairs of guests
    for x in range(N):
        for y in range(x + 1, N):
            if handshake_count < M:  # Check if we can still perform handshakes
                handshake = (min(x, y), max(x, y))  # Ensure the handshake is unique by ordering
                if handshake not in handshake_set:  # Ensure the handshake is unique
                    happiness += A[x] + A[y]  # Add happiness from this handshake
                    handshake_set.add(handshake)  # Add to the set of handshakes
                    handshake_count += 1  # Increment the count of handshakes
            else:
                break  # Exit if we have reached the maximum handshakes
        if handshake_count >= M:
            break  # Exit outer loop if maximum handshakes reached
    return happiness