'''
Module to handle query logic for the application.
'''
class QueryHandler:
    def __init__(self):
        self.queries = []  # Initialize an empty list to store queries
    def add(self, x):
        self.queries.append(x)  # Append the value to the list
    def get_kth_from_end(self, k):
        if not self.queries:
            return "Error: No elements in the list"  # Handle empty list case
        if k > len(self.queries):
            return "Error: k is greater than the number of elements in the list."  # Return a user-friendly message
        return self.queries[-k]  # Return the k-th value from the end