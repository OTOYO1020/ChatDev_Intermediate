'''
Module for processing queries.
'''
from typing import List, Tuple, Union
class QueryProcessor:
    def __init__(self):
        self.A = []
    def append(self, x: int):
        """Append an integer x to the list A."""
        self.A.append(x)
    def pop_first(self) -> Union[int, None]:
        """Remove and return the first element of the list A, or None if A is empty."""
        if self.A:
            return self.A.pop(0)
        return None
    def sort(self):
        """Sort the list A in ascending order."""
        self.A.sort()
    def process_queries(self, Q: int, queries: List[Tuple[int, Union[int, None]]]) -> List[str]:
        """Process a list of queries and return the results as a list of strings."""
        results = []
        for query in queries:
            if query[0] == 1:
                self.append(query[1])
            elif query[0] == 2:
                if not self.A:  # Check if A is empty
                    raise ValueError("Cannot perform operation: List is empty")
                first_element = self.pop_first()
                results.append(str(first_element))  # Append the first element to results
            elif query[0] == 3:
                self.sort()
        return results  # Return the results list