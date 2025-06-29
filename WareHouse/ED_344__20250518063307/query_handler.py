'''
Module to handle query processing for the list of distinct integers.
'''
from typing import List, Tuple, Optional
def process_queries(N: int, A: List[int], Q: int, queries: List[Tuple[int, int, Optional[int]]]) -> str:
    for query in queries:
        query_type, x = query[0], query[1]
        y = query[2] if len(query) > 2 else None  # Safely handle optional y
        if query_type == 1:  # Insert y after x
            index = find_index(A, x)
            if index != -1:  # Ensure x is found
                if y is not None and y not in A:  # Check for distinctness and that y is provided
                    A.insert(index + 1, y)
                elif y is None:
                    print("No value provided for y in insertion query.")
                else:
                    print(f"Cannot insert {y} as it already exists in the list.")
            else:
                print(f"Element {x} not found for insertion. Skipping this query.")
                continue  # Skip this query if x is not found
        elif query_type == 2:  # Remove x
            index = find_index(A, x)
            if index != -1:  # Ensure x is found
                if len(A) > 1:  # Ensure A remains non-empty after removal
                    A.pop(index)
                else:
                    print(f"Cannot remove {x} as it would leave the list empty.")
                    continue  # Skip this query if it would leave the list empty
            else:
                print(f"Element {x} not found for removal.")
    return ', '.join(map(str, A))  # Convert final list to string format
def find_index(A: List[int], x: int) -> int:
    try:
        return A.index(x)
    except ValueError:
        return -1