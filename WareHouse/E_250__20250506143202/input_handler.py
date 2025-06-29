'''
Handles user input for sequences and queries.
'''
import sys
class InputHandler:
    def __init__(self, main_app):
        self.main_app = main_app
        self.sequence_a = []
        self.sequence_b = []
        self.prefix_sets_a = []
        self.prefix_sets_b = []
        self.queries = []
    def process_input(self):
        # Read integers N and Q from standard input
        N, Q = map(int, sys.stdin.readline().split())
        # Read the integer sequence A of length N
        self.sequence_a = list(map(int, sys.stdin.readline().split()))
        # Read the integer sequence B of length N
        self.sequence_b = list(map(int, sys.stdin.readline().split()))
        # Precompute sets for all prefixes of A and B
        current_set_a = set()
        current_set_b = set()
        for i in range(N):
            current_set_a.add(self.sequence_a[i])
            current_set_b.add(self.sequence_b[i])
            # Store a copy of the current set instead of the reference
            self.prefix_sets_a.append(current_set_a.copy())
            self.prefix_sets_b.append(current_set_b.copy())
        # Read each query
        for _ in range(Q):
            x_i, y_i = map(int, sys.stdin.readline().split())
            self.queries.append((x_i, y_i))
        results = self.main_app.set_comparison.compare_sets(self.prefix_sets_a, self.prefix_sets_b, self.queries)
        self.main_app.output_handler.display_results(results)