'''
Logic for calculating the minimum cost to determine card values based on conditions.
'''
from typing import List, Tuple
def minimum_cost_to_determine_cards(N: int, M: int, conditions: List[Tuple[int, int, int]]) -> int:
    if N <= 0 or M < 0:
        return -1  # Handle edge cases
    if M == 0:
        return 0  # No conditions means no magic uses required
    if len(conditions) > M:
        return -1  # More conditions than allowed
    parent = list(range(N))
    rank = [0] * N
    parity = [0] * N  # To store parity information
    def find(x):
        if parent[x] != x:
            orig_parent = parent[x]
            parent[x] = find(parent[x])
            parity[x] ^= parity[orig_parent]  # Update parity based on path compression
        return parent[x]
    def union(x, y, p):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            # Union logic
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
                parity[root_y] = parity[x] ^ parity[y] ^ p  # Update parity for root_y
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
                parity[root_x] = parity[x] ^ parity[y] ^ p  # Update parity for root_x
            else:
                parent[root_y] = root_x
                parity[root_y] = parity[x] ^ parity[y] ^ p  # Update parity for root_y
                rank[root_x] += 1
        else:
            # Check if the current parity matches
            if (parity[x] ^ parity[y]) != p:
                return False  # Conditions cannot be satisfied
        return True
    # Process each condition
    for x, y, required_parity in conditions:
        if not union(x, y, required_parity % 2):
            return -1  # Return -1 if conditions cannot be satisfied
    # Count distinct groups based on the union-find structure
    distinct_groups = set()
    for i in range(N):
        root = find(i)
        distinct_groups.add((root, parity[i]))  # Store the root and its parity
    # The number of magic uses required is equal to the number of distinct groups
    magic_uses = len(distinct_groups)
    return magic_uses  # Return the total number of magic uses required