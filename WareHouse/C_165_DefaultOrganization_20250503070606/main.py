'''
Main application file for the score calculation.
'''
import sys
from sequence_generator import SequenceGenerator
from query_handler import QueryHandler
def main():
    # Read integers N, M, Q from standard input
    N, M, Q = map(int, sys.stdin.readline().strip().split())
    # Initialize an empty list 'queries' to store the quadruples (a_i, b_i, c_i, d_i)
    queries = []
    # For each of the Q queries, read the quadruple and append it to 'queries' list
    for _ in range(Q):
        a, b, c, d = map(int, sys.stdin.readline().strip().split())
        # Convert from one-based to zero-based indexing
        queries.append((a - 1, b - 1, c, d))
    # Generate all possible non-decreasing sequences 'A' of length N with values between 1 and M
    generator = SequenceGenerator(N, M)
    sequences = generator.generate_sequences()
    # Initialize QueryHandler with the queries
    handler = QueryHandler(queries)
    # Calculate the maximum score
    max_score = handler.calculate_max_score(sequences, N)
    # Print the maximum score as the output
    print(max_score)
if __name__ == "__main__":
    main()