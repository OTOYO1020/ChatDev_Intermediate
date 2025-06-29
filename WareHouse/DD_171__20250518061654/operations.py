'''
Module to perform operations on the list of integers based on user-defined operations.
'''
from typing import List, Tuple
def perform_operations(N: int, Q: int, A: List[int], operations: List[Tuple[int, int]]) -> List[int]:
    '''
    Perform operations on the list A based on the provided operations.
    Each operation replaces occurrences of B_i with C_i and calculates the sum of the modified list.
    '''
    results = []
    for B_i, C_i in operations:
        if B_i != C_i:  # Ensure B_i is not equal to C_i
            if B_i in A:  # Check if B_i exists in A
                # Create a copy of A to perform the replacement
                modified_A = [C_i if x == B_i else x for x in A]
                # Calculate the sum of the modified A after each operation
                current_sum = sum(modified_A)
            else:
                # If B_i does not exist in A, sum the original A
                current_sum = sum(A)
        else:
            # If B_i is equal to C_i, just sum the original A
            current_sum = sum(A)
        results.append(current_sum)
    return results