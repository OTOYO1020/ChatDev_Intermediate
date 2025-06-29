'''
Logic for calculating the maximum village Taro can reach based on friends' data.
'''
from typing import List, Tuple
def max_village_reached(N: int, K: int, friends: List[Tuple[int, int]]) -> int:
    current_village = 0
    friends.sort(key=lambda x: x[0])  # Sort friends based on village A_i
    # Check if Taro can reach the first friend's village
    if friends and K < friends[0][0]:  # If there are friends and K is less than the first A_i
        return current_village  # Taro cannot reach any village
    for A_i, B_i in friends:
        # Calculate cost to reach A_i from current_village
        cost_to_reach = A_i - current_village  # Calculate cost based on last visited village
        if K >= cost_to_reach:
            K -= cost_to_reach  # Update yen after reaching A_i
            K += B_i  # Add yen received from friend
            current_village = A_i  # Update current village
        else:
            break  # Taro cannot reach any more villages
    return current_village  # Return the maximum village reached