'''
Module to calculate the generations of amoebae based on their records.
'''
from typing import List
def calculate_generations(N: int, records: List[int]) -> List[int]:
    generations = [-1] * (2 * N + 2)
    generations[1] = 0  # Amoeba 1 is the root
    # Input validation for records
    for A_i in records:
        if A_i < 1 or A_i > 2 * N + 1:
            raise ValueError(f"Amoeba index {A_i} is out of bounds. It must be between 1 and {2 * N + 1}.")
    for i in range(N):
        A_i = records[i]
        # Ensure A_i is a valid parent amoeba and has been initialized
        if A_i < 1 or A_i > 2 * N + 1 or generations[A_i] == -1:
            print(f"Skipping record for parent amoeba {A_i} as it is not valid or has not been initialized.")
            continue  # Skip this record if the parent amoeba is invalid
        # Correctly assign the generation for the new amoebae
        new_amoeba_1 = 2 * i + 2
        new_amoeba_2 = 2 * i + 3
        # Check if the new amoebae indices are within bounds
        if new_amoeba_1 < len(generations) and new_amoeba_2 < len(generations):
            generations[new_amoeba_1] = generations[A_i] + 1  # 2*i + 2
            generations[new_amoeba_2] = generations[A_i] + 1  # 2*i + 3
        else:
            raise ValueError("New amoeba indices are out of bounds.")
    result = generations[1:2 * N + 2]
    return result