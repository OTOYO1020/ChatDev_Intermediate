'''
Main application file for processing matrix queries.
'''
from typing import List, Tuple
from matrix import Matrix
def process_queries(N: int, M: int, Q: int, queries: List[Tuple[int, ...]]) -> List[int]:
    matrix = Matrix(N, M)
    outputs = []
    for query in queries:
        if query[0] == 1:
            l, r, x = query[1], query[2], query[3]
            matrix.update_columns(l - 1, r - 1, x)  # Adjust for 0-based indexing
        elif query[0] == 2:
            i, x = query[1], query[2]
            matrix.replace_row(i - 1, x)  # Adjust for 0-based indexing
        elif query[0] == 3:
            i, j = query[1], query[2]
            value = matrix.get_value(i - 1, j - 1)  # Adjust for 0-based indexing
            outputs.append(value)  # Append value (None if out of bounds)
    return outputs
if __name__ == "__main__":
    # Example usage
    N = 3  # Number of rows
    M = 4  # Number of columns
    Q = 5  # Number of queries
    queries = [
        (1, 1, 2, 5),  # Update columns 1 to 2 by adding 5
        (2, 1, 10),    # Replace row 1 with 10
        (3, 1, 1),     # Get value at (1, 1)
        (1, 2, 4, 3),  # Update columns 2 to 4 by adding 3
        (3, 2, 3)      # Get value at (2, 3)
    ]
    results = process_queries(N, M, Q, queries)
    print(results)  # Output the results of type '3' queries