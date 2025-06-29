'''
QueryProcessor class to handle the processing of queries.
'''
from typing import List, Tuple
class QueryProcessor:
    def __init__(self):
        self.queue = []
    def process_queries(self, Q: int, queries: List[Tuple[int, int]]) -> List[int]:
        results = []
        head_position = 1  # Initial head position
        cumulative_adjustment = 0  # To track the total adjustment for head positions
        for query in queries:
            query_type = query[0]
            if query_type == 1:
                l = query[1]
                self.queue.append((head_position, l))
                head_position += l  # Update head position for the next snake
            elif query_type == 2:
                if not self.queue:
                    raise ValueError("Cannot remove snake: The queue is empty.")
                head_position, m = self.queue.pop(0)
                cumulative_adjustment += m  # Update the cumulative adjustment
            elif query_type == 3:
                k = query[1]
                if k < 1 or k > len(self.queue):
                    raise IndexError(f"Index out of bounds: There are only {len(self.queue)} snakes in the queue.")
                # Append the adjusted head position of the k-th snake
                results.append(self.queue[k - 1][0] - cumulative_adjustment)
            else:
                raise ValueError("Invalid query type: Must be 1, 2, or 3.")
        return results