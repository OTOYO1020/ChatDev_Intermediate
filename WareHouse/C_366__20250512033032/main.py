'''
Main application file for the integer bag management system.
'''
from bag import Bag  # Ensure this line is present to import the Bag class
from typing import List, Tuple
def process_queries(Q: int, queries: List[Tuple[int, int]]) -> List[int]:
    bag = Bag()
    results = []
    for query in queries:
        # Validate the query format
        if (len(query) != 2 and query[0] != 3) or (query[0] in [1, 2] and not isinstance(query[1], int)):
            print(f"Warning: Invalid query format {query}. Expected format is (type, value) or (3).")
            continue  # Skip invalid queries
        query_type = query[0]
        if query_type == 1:
            # Add integer to the bag
            bag.add(query[1])
        elif query_type == 2:
            # Remove integer from the bag
            try:
                bag.remove(query[1])
            except ValueError as e:
                print(f"Warning: {e}")
        elif query_type == 3:
            # Count unique integers
            results.append(bag.count())
    return results
if __name__ == "__main__":
    # Example usage
    Q = int(input("Enter number of queries: "))
    queries = []
    for _ in range(Q):
        try:
            query = tuple(map(int, input("Enter query (type and value): ").split()))
            queries.append(query)
        except ValueError:
            print("Warning: Invalid input. Please enter integers only.")
    results = process_queries(Q, queries)
    print("Results of type 3 queries:", results)