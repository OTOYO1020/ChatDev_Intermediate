'''
Module to define the QueryProcessor class for processing graph queries.
'''
from typing import List, Tuple, Union
class QueryProcessor:
    def __init__(self, graph):
        self.graph = graph
    def process_queries(self, queries: List[Tuple[int, Union[Tuple[int, int], Tuple[int, int]]]]) -> List[int]:
        results = []
        if not queries:  # Check if the queries list is empty
            return results  # Return an empty list instead of a message
        for query in queries:
            if query[0] == 1:  # Type 1 query
                u, v = query[1]
                try:
                    self.graph.add_edge(u, v)
                except ValueError as e:
                    results.append(str(e))  # Append error message to results
            elif query[0] == 2:  # Type 2 query
                v, k = query[1]
                try:
                    connected_vertices = self.graph.get_connected_vertices(v)
                    connected_vertices.sort(reverse=True)
                    if len(connected_vertices) < k:
                        results.append(-1)
                    else:
                        results.append(connected_vertices[k - 1])
                except ValueError as e:
                    results.append(str(e))  # Append error message to results
        return results