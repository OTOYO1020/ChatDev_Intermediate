'''
Main application file for the query processing.
'''
import sys
from typing import List, Tuple
import re  # Importing regex for validation
from query_handler import QueryHandler  # Importing the QueryHandler class
def process_queries(S: str, queries: List[Tuple[int, ...]]) -> List[int]:
    # Validate the input string S
    if not S:  # Check if S is empty
        raise ValueError("Input string cannot be empty.")
    if not re.match("^[a-z]+$", S):  # Check if S contains only lowercase letters
        raise ValueError("Input string must consist only of lowercase English letters.")
    query_handler = QueryHandler(S)
    results = []
    for query in queries:
        try:
            # Validate the query length based on its type
            if query[0] == 1 and len(query) == 3:  # Type 1 query should have 3 elements
                if not (0 <= query[1] < len(S)):
                    raise IndexError(f"Index {query[1]} for update query is out of bounds.")
                updated_string = query_handler.execute_query(query)
                S = updated_string  # Update S with the modified string
                query_handler.S = list(S)  # Update the QueryHandler's string to reflect the change
            elif query[0] == 2 and len(query) == 3:  # Type 2 query should have 3 elements
                if not (0 <= query[1] <= query[2] < len(S)):
                    raise IndexError(f"Query indices {query[1]} to {query[2]} are out of bounds.")
                result = query_handler.execute_query(query)
                if result is not None:
                    results.append(result)
            else:
                raise ValueError("Invalid query format. Type 1 should have 3 elements and Type 2 should have 3 elements.")
        except (ValueError, IndexError) as e:
            print(f"Error processing query {query}: {e}")  # User-friendly error message
    return results
if __name__ == "__main__":
    S = input("Enter a string consisting of lowercase letters: ").strip()
    queries_input = input("Enter queries (e.g., '1 0 a' for update or '2 0 5' for distinct count, separated by ';'): ").strip().split(';')
    queries = []
    for query in queries_input:
        parts = list(map(str, query.split()))
        if parts:
            try:
                queries.append(tuple(map(int, parts)))
            except ValueError:
                print(f"Invalid query input: {query}. Please ensure all elements are integers.")
    results = process_queries(S, queries)
    print("Results:", results)