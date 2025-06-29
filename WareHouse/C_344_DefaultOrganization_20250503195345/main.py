'''
Main entry point for the application that computes possible sums from sequences A, B, and C.
'''
def main():
    # Read integers N, M, L, and Q from standard input
    N, M, L, Q = map(int, input().split())
    # Read sequences A, B, and C
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # Read the sequence of queries
    queries = list(map(int, input().split()))
    # Initialize a set to store all possible sums of one element from A, B, and C
    possible_sums = set()
    # Precompute sums of A and B
    ab_sums = {a + b for a in A for b in B}
    # Compute all possible sums with elements from C
    for c in C:
        for ab_sum in ab_sums:
            possible_sums.add(ab_sum + c)  # Add the computed sum of A, B, and C to the set
    results = []
    # Check each query against the possible sums
    for query in queries:
        results.append("YES" if query in possible_sums else "NO")
    # Print the results for all queries in order
    print("\n".join(results))
if __name__ == "__main__":
    main()