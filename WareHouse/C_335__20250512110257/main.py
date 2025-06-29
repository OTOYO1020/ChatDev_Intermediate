'''
Main application file for the query processing software.
'''
from typing import List, Tuple
from query_handler import QueryHandler
def process_queries(N: int, Q: int, queries: List[Tuple[int, str]]) -> List[Tuple[int, int]]:
    # Validate input parameters
    if N <= 0 or Q <= 0:
        raise ValueError("N and Q must be positive integers.")
    if len(queries) != Q:
        raise ValueError(f"Expected {Q} queries, but got {len(queries)}.")
    handler = QueryHandler(N)  # Initialize the QueryHandler with N parts
    results = []  # List to store results of type 2 queries
    for query in queries:
        query_type = int(query[0])  # Convert the first element to an integer
        if query_type == 1:  # Type 1 query: Update position
            direction = query[1]
            handler.update_position(direction)  # Update the head's position based on direction
        elif query_type == 2:  # Type 2 query: Retrieve position
            p = int(query[1])  # Convert back to integer for processing
            if p < 1 or p > N:
                raise ValueError("Part index out of range for type 2 query.")
            results.append(handler.get_position(p))  # Append the position of part p to results
        else:
            raise ValueError("Invalid query type")  # Raise error for invalid query type
    return results  # Return the results list containing coordinates for type 2 queries
if __name__ == "__main__":
    N = int(input("Enter the number of parts (N): "))
    Q = int(input("Enter the number of queries (Q): "))
    queries = []
    for _ in range(Q):
        query_input = input("Enter query (format: '1 C' or '2 p'): ").strip()
        parts = query_input.split()
        if len(parts) != 2:
            raise ValueError("Each query must have exactly two parts.")
        query_type = int(parts[0])  # Convert to integer
        if query_type == 1:
            query_value = parts[1].strip()  # Trim whitespace
            if query_value not in ['R', 'L', 'U', 'D']:
                raise ValueError("Invalid direction for type 1 query.")
        elif query_type == 2:
            query_value = str(int(parts[1].strip()))  # Convert to string
            if int(query_value) < 1 or int(query_value) > N:
                raise ValueError("Part index out of range for type 2 query.")
        else:
            raise ValueError("Query type must be 1 or 2.")
        queries.append((query_type, query_value))
    results = process_queries(N, Q, queries)
    for i, pos in enumerate(results):
        print(f"Part {i + 1}: {pos}")