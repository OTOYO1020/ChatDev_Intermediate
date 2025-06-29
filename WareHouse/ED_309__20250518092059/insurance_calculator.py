'''
Module for calculating the number of insured individuals based on family relationships and insurance purchases.
'''
from typing import List, Tuple
def count_insured_people(N: int, M: int, parents: List[int], insurances: List[Tuple[int, int]]) -> int:
    # Validate the length of parents list
    if len(parents) != N:
        raise ValueError(f"The length of parents list must be {N}.")
    # Validate parent indices
    for parent in parents:
        if parent != -1 and (parent < 0 or parent >= N):
            raise ValueError(f"Invalid parent index: {parent}. Must be -1 or between 0 and {N-1}.")
    # Construct the family tree
    tree = [[] for _ in range(N)]
    for child in range(N):
        if parents[child] != -1:  # -1 indicates no parent
            tree[parents[child]].append(child)  # Add child to the parent's list
    # Set to track insured individuals
    insured_set = set()
    def dfs(person: int, generations_left: int):
        """
        Depth-first search to traverse descendants of a person.
        :param person: The index of the person whose descendants are being counted.
        :param generations_left: The number of generations to traverse down the tree.
        """
        if generations_left < 0 or person < 0 or person >= N:  # Check for valid person index
            return
        if person not in insured_set:  # Only add if not already counted
            insured_set.add(person)
            # Traverse through children
            for child in tree[person]:
                dfs(child, generations_left - 1)
    # Process each insurance
    for person, generations in insurances:
        if person < N:  # Ensure the person index is valid
            dfs(person, generations)  # Directly use generations without max depth check
    return len(insured_set)