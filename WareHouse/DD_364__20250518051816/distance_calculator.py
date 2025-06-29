'''
Module for calculating the K-th closest distances between two sets of points.
'''
def find_kth_closest_distance(N, Q, A, B, K):
    # Check for empty input cases
    if N == 0 or Q == 0:
        return []  # Return an empty list if there are no points to compare
    results = []
    for j in range(Q):
        # Calculate distances from each point in A to the current point in B
        distances = [abs(a - B[j]) for a in A]
        distances.sort()  # Sort the distances to find the k-th closest
        k_j = K[j]
        # Check if k_j is within the valid range
        if 1 <= k_j <= N:
            results.append(distances[k_j - 1])  # Append the k_j-th closest distance
        else:
            raise ValueError(f"K value {k_j} for query {j+1} is out of range. It must be between 1 and {N}.")
    return results