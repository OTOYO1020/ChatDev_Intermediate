'''
Handles the logic for querying and processing user inputs.
'''
import sys
import random
class QueryHandler:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.query_count = 0
        self.A = [None] * n  # Initialize A with None
        self.parity_info = [0] * n  # To track parity information
    def make_query(self):
        # Ensure distinct integers are selected
        x = random.sample(range(1, self.n + 1), self.k)
        print(f"? {' '.join(map(str, x))}")
        sys.stdout.flush()  # Ensure the output is flushed
        return x
    def process_response(self, response, queried_indices):
        if response == -1:
            print("Terminating due to invalid query.")
            sys.exit()  # Terminate the program immediately
        elif response not in (0, 1):
            print("Received an invalid response.")
            return  # Handle invalid response gracefully
        # Update the parity information based on the response
        if response == 0:
            # Even number of odd numbers in queried indices
            for index in queried_indices:
                self.parity_info[index - 1] = (self.parity_info[index - 1] + 0) % 2  # No change needed
        elif response == 1:
            # Odd number of odd numbers in queried indices
            for index in queried_indices:
                self.parity_info[index - 1] = (self.parity_info[index - 1] + 1) % 2  # Change parity to odd
    def deduce_values(self):
        # Deduce the values of A based on parity information
        for i in range(self.n):
            # Determine the value of A[i] based on the parity information
            if self.parity_info[i] % 2 == 0:
                self.A[i] = 0  # Even parity
            else:
                self.A[i] = 1  # Odd parity
    def execute_queries(self):
        while self.query_count < self.n:  # Continue until maximum queries are reached
            queried_indices = self.make_query()
            # Read the response from standard input
            response = int(sys.stdin.readline().strip())
            self.process_response(response, queried_indices)
            self.query_count += 1  # Increment query count after processing the response
            if None not in self.A:  # Check if all values in A are determined
                break
        self.deduce_values()  # Deduce final values of A
        return self.A