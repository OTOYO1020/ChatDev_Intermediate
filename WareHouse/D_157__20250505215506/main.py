'''
Main application file for the friendship candidate calculator.
'''
import sys
from graph import Graph
def main():
    # Read integers N, M, K from standard input with validation
    while True:
        try:
            N, M, K = map(int, sys.stdin.readline().strip().split())
            if N <= 0 or M < 0 or K < 0 or M > (N * (N - 1)) // 2 or K > (N * (N - 1)) // 2:
                raise ValueError("N must be positive and M, K must be non-negative and within valid limits.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter three integers N, M, K.")
    graph = Graph(N)
    # Read friendships with validation
    for _ in range(M):
        while True:
            try:
                A, B = map(int, sys.stdin.readline().strip().split())
                if A < 1 or A > N or B < 1 or B > N:
                    raise ValueError("Friendship indices must be between 1 and N.")
                graph.add_friendship(A, B)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid friendship pair.")
    # Read blockships with validation
    for _ in range(K):
        while True:
            try:
                C, D = map(int, sys.stdin.readline().strip().split())
                if C < 1 or C > N or D < 1 or D > N:
                    raise ValueError("Blockship indices must be between 1 and N.")
                graph.add_blockship(C, D)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid blockship pair.")
    friend_candidate_counts = []
    # Calculate friend candidates for each user
    for b in range(1, N + 1):
        count = 0
        for a in range(1, N + 1):
            # Check if 'a' is not equal to 'b', and if there is no friendship and no blockship
            if a != b and not graph.is_friendship(a, b) and not graph.is_blockship(a, b):
                if graph.bfs(a, b):  # Check if a path exists through friendships
                    count += 1
        friend_candidate_counts.append(count)
    # Print the result as a space-separated list of integers
    print(" ".join(map(str, friend_candidate_counts)))
if __name__ == "__main__":
    main()