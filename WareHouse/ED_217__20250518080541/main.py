'''
Main application file for processing queries without GUI.
'''
from typing import List, Tuple, Union
from query_processor import QueryProcessor  # Ensure to import the class
def process_queries(Q: int, queries: List[Tuple[int, Union[int, None]]]) -> List[str]:
    """Process the queries using the QueryProcessor class."""
    processor = QueryProcessor()
    return processor.process_queries(Q, queries)
if __name__ == "__main__":
    # Example usage
    Q = int(input())
    queries = []
    for _ in range(Q):
        query = tuple(map(int, input().split()))
        queries.append(query)
    results = process_queries(Q, queries)
    for result in results:
        print(result)  # Print the results collected from the queries