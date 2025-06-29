'''
Module containing functions to calculate f(A, B) and sum of f(S_i, S_j).
'''
def merge_and_sort(A, B):
    '''
    Merges two sets A and B, maintaining the order of elements, and returns a sorted list.
    '''
    merged = list(A.union(B))  # Use union to merge sets and ensure uniqueness
    return sorted(merged)  # Sort the merged list before returning
def calculate_f(A, B):
    '''
    Calculates the sum of indices of elements of set A in the sorted merged list of A and B.
    '''
    C = merge_and_sort(A, B)
    index_map = {value: idx for idx, value in enumerate(C)}  # Create a mapping of value to index
    indices_sum = sum(index_map[a] for a in A if a in index_map)  # Check if a is in index_map
    return indices_sum
def sum_of_f(N, sets):
    '''
    Computes the total sum of f(S_i, S_j) for all pairs (i, j) with 1 ≤ i < j ≤ N.
    '''
    total_sum = 0
    for i in range(N):
        for j in range(i + 1, N):
            total_sum += calculate_f(sets[i], sets[j])
    return total_sum