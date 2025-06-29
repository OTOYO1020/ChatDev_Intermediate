'''
Module containing the logic to find the previous permutation.
'''
from itertools import permutations
def find_previous_permutation(N: int, P: list, K: int) -> list:
    '''
    Find the (K-1)-th permutation in lexicographical order.
    Parameters:
    N (int): Size of the permutation.
    P (list): The permutation list.
    K (int): The index of the permutation.
    Returns:
    list: The (K-1)-th permutation or an empty list if K is out of bounds.
    '''
    if not (2 <= N <= 100):
        raise ValueError("N must be between 2 and 100.")
    # Check if P is a valid permutation
    if len(P) != N or len(set(P)) != N or any(x < 1 or x > N for x in P):
        raise ValueError("P must contain unique integers in the range 1 to N.")
    # Check if P is the identity permutation
    identity_permutation = list(range(1, N + 1))
    if P == identity_permutation:
        raise ValueError("The permutation P cannot be the identity permutation.")
    all_perms = sorted(permutations(range(1, N + 1)))
    # Check if K is out of bounds for the number of permutations.
    if K < 1 or K > len(all_perms):
        return []  # Return an empty list if K is out of bounds.
    # Check if P is a valid permutation
    if tuple(P) not in all_perms:
        raise ValueError("The permutation P is not valid.")
    # Retrieve the (K-1)-th permutation from the sorted list
    return list(all_perms[K - 1])