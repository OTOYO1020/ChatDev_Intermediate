'''
Main entry point for the graph query application.
'''
from graph import Graph
from query_processor import QueryProcessor
from typing import List, Tuple, Union
def main():
    N = int(input("Enter number of vertices: "))
    Q = int(input("Enter number of queries: "))
    queries = []
    for _ in range(Q):
        query = list(map(int, input("Enter query: ").split()))
        if query[0] == 1 and len(query) == 3:  # Type 1 query
            queries.append((1, (query[1], query[2])))
        elif query[0] == 2 and len(query) == 3:  # Type 2 query
            queries.append((2, (query[1], query[2])))
        else:
            print("Invalid query format. Type 1 should have 3 integers and Type 2 should have 3 integers.")
    graph = Graph(N)
    query_processor = QueryProcessor(graph)
    results = query_processor.process_queries(queries)
    if not results:
        print("No results to display.")
    else:
        for result in results:
            print(result)
if __name__ == "__main__":
    main()