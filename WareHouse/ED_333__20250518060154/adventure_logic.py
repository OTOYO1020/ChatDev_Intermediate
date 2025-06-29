'''
Contains the adventure logic for managing potions and events.
'''
from typing import List, Tuple
def adventure(N: int, events: List[Tuple[int, int]]) -> Tuple[int, List[str]]:
    potions = {}
    actions = []
    current_potions = 0
    required_potions = {}
    K_min = float('inf')  # Initialize K_min to infinity
    # First pass to determine potion needs for monsters
    for event in events:
        t_i, x_i = event
        if t_i == 2:  # Defeat monster
            required_potions[x_i] = required_potions.get(x_i, 0) + 1
    # Second pass to handle events
    for event in events:
        t_i, x_i = event
        if t_i == 1:  # Collect potion
            potions[x_i] = potions.get(x_i, 0) + 1
            current_potions += 1
            actions.append(f"Collected potion {x_i}")
        elif t_i == 2:  # Defeat monster
            if potions.get(x_i, 0) > 0:
                potions[x_i] -= 1
                current_potions -= 1
                actions.append(f"Defeated monster with potion {x_i}")
                K_min = min(K_min, current_potions)  # Update K_min after defeating a monster
            else:
                actions.append(f"Failed to defeat monster with potion {x_i}")
                return -1, []  # Cannot defeat all monsters
    # Check if all required potions were collected
    for potion_type, needed in required_potions.items():
        if potions.get(potion_type, 0) < needed:
            return -1, []  # Cannot defeat all monsters
    # If K_min was never updated, it means no monsters were defeated
    if K_min == float('inf'):
        K_min = 0  # If no monsters were defeated, K_min should be 0
    return K_min, actions