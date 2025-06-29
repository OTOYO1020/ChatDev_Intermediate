'''
Main application file for the minimum actions console application.
'''
from actions import minimum_actions
def main():
    # Input parsing
    N = int(input("Number of cells (N): "))
    L = list(map(int, input("Lower bounds (L): ").split()))
    U = list(map(int, input("Upper bounds (U): ").split()))
    Q = int(input("Number of queries (Q): "))
    queries = [tuple(map(int, input("Query (format: s_x s_y t_x t_y): ").split())) for _ in range(Q)]
    # Process queries
    results = minimum_actions(N, L, U, Q, queries)
    # Output results
    print("Results:", ', '.join(map(str, results)))
if __name__ == "__main__":
    main()