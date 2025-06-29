'''
Module for counting valid sequences in a graph.
'''
from typing import List, Tuple
def count_sequences(N: int, M: int, K: int, S: int, T: int, X: int, edges: List[Tuple[int, int]]) -> int:
    MOD = 998244353
    # Handle edge cases
    if K == 0:
        return 1 if S == T else 0  # Return 1 only if S equals T
    if S == T and K % 2 == 1:
        return 0
    # Construct the adjacency list
    graph = [[] for _ in range(N + 1)]
    edges_set = set()  # Use a set to avoid duplicate edges
    x_present = False  # Flag to check if X is in the graph
    for u, v in edges:
        if u < 1 or u > N or v < 1 or v > N:
            raise ValueError(f"Vertices must be in the range [1, {N}]. Invalid edge: ({u}, {v})")
        if (u, v) not in edges_set and (v, u) not in edges_set:  # Check for duplicates
            graph[u].append(v)
            graph[v].append(u)
            edges_set.add((u, v))  # Add the edge to the set
            edges_set.add((v, u))  # Add the reverse edge to the set
            if u == X or v == X:
                x_present = True  # Mark if X is present in the edges
    if not x_present:
        return 0  # If X is not present, return 0
    # Dynamic programming table
    dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
    dp[0][S] = 1  # Starting at S with 0 occurrences of X
    for length in range(K):
        for node in range(1, N + 1):
            if dp[length][node] > 0:
                for neighbor in graph[node]:
                    if neighbor == X:
                        # Increment the count of X
                        dp[length + 1][neighbor] = (dp[length + 1][neighbor] + dp[length][node]) % MOD
                    else:
                        dp[length + 1][neighbor] = (dp[length + 1][neighbor] + dp[length][node]) % MOD
    # Return count of sequences ending at T with even occurrences of X
    return (dp[K][T] if K % 2 == 0 else 0) % MOD