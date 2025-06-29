'''
Utility functions for the Potato Packing application.
'''
from typing import List
def count_potatoes_in_boxes(N: int, W: List[int], X: int, Q: int, K: List[int]) -> List[int]:
    '''
    Counts the number of potatoes packed in boxes based on the given weights and limits.
    '''
    current_weight = 0
    potatoes_in_current_box = 0
    potatoes_in_boxes = []
    for weight in W:
        # If the weight of the potato exceeds the box limit, skip this potato
        if weight > X:
            continue  # Move to the next potato
        # Add the weight to the current box
        current_weight += weight
        potatoes_in_current_box += 1  # Increment the count of potatoes in the current box
        # If adding the current weight meets or exceeds the box limit, seal the current box
        if current_weight >= X:
            potatoes_in_boxes.append(potatoes_in_current_box)  # Store the number of potatoes in the box
            current_weight = 0  # Reset for the next box
            potatoes_in_current_box = 0  # Reset the count for the next box
    # Check if there are any remaining potatoes in the last box
    if potatoes_in_current_box > 0:
        potatoes_in_boxes.append(potatoes_in_current_box)
    # Handle queries
    results = []
    for query in K:
        if query - 1 < len(potatoes_in_boxes):
            results.append(potatoes_in_boxes[query - 1])
        else:
            results.append(0)  # If the query is out of bounds
    # If no boxes were sealed, ensure all queries return 0
    if not potatoes_in_boxes:
        results = [0] * len(K)
    return results