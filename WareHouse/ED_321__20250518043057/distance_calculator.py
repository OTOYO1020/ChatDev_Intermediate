'''
Module for calculating the number of vertices at distance K from vertex X in a binary tree.
'''
def find_distance_count(N, X, K):
    if K == 0:
        return 1 if 1 <= X <= N else 0
    # Check if K is too large to find an ancestor
    height = 0
    current = X
    while current > 1:
        current //= 2
        height += 1
    if K > height:
        return 0  # K is greater than the height of the tree from X
    # Upward traversal to find the ancestor at distance K from X
    current = X
    for i in range(K):
        current //= 2
    # Now current is the ancestor at distance K from X
    count = 0
    # Count the ancestor itself if it's within bounds
    if 1 <= current <= N:
        count += 1  # Count the ancestor itself
        # Calculate the leftmost and rightmost nodes at distance K from the ancestor
        leftmost_node = current * (2 ** K)
        rightmost_node = current * (2 ** (K + 1)) - 1  # Corrected calculation
        # Ensure the nodes are within bounds
        if leftmost_node <= N:
            count += max(0, min(N, rightmost_node) - leftmost_node + 1)
    return count