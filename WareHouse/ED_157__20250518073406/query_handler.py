'''
Module for handling string queries.
'''
from typing import List, Tuple
import re  # Importing regex for validation
class QueryHandler:
    def __init__(self, S: str):
        if not S:  # Check if S is empty
            raise ValueError("Input string cannot be empty.")
        if not re.match("^[a-z]+$", S):  # Check if S contains only lowercase letters
            raise ValueError("Input string must consist only of lowercase English letters.")
        self.S = list(S)  # Convert string to list for mutability
        self.N = len(S)  # This remains constant as the length of S does not change
    def execute_query(self, query: Tuple[int, ...]) -> str:
        """
        Execute a query based on its type.
        For type 1 queries, update the character at the specified index.
        For type 2 queries, count distinct characters in the specified range.
        Returns:
            str: The updated string for type 1 queries, or the number of distinct characters for type 2 queries.
        Raises:
            ValueError: If the query type is not recognized.
        """
        query_type = query[0]
        if query_type == 1:
            self.update_string(query[1], query[2])
            return ''.join(self.S)  # Return the updated string
        elif query_type == 2:
            return self.count_distinct_characters(query[1], query[2])
        else:
            raise ValueError("Invalid query type. Must be 1 or 2.")
    def update_string(self, i_q: int, c_q: str) -> None:
        if 0 <= i_q < self.N:
            if self.S[i_q] != c_q:
                self.S[i_q] = c_q
                # No need to update N since the length of S does not change
        else:
            raise IndexError("Index for update is out of bounds.")
    def count_distinct_characters(self, l_q: int, r_q: int) -> int:
        if 0 <= l_q <= r_q < self.N:
            distinct_chars = set(self.S[l_q:r_q + 1])
            return len(distinct_chars)
        else:
            raise IndexError("Query indices are out of bounds.")