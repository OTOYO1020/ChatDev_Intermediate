'''
Graph class to represent superiority relations among programmers.
'''
class Graph:
    def __init__(self, num_programmers):
        self.num_programmers = num_programmers
        self.adjacency_list = [[] for _ in range(num_programmers)]
    def add_relation(self, A, B):
        self.adjacency_list[A].append(B)
    def find_strongest_programmer(self):
        count_reachable = [0] * self.num_programmers
        for programmer in range(self.num_programmers):
            visited = [False] * self.num_programmers  # Reset visited for each programmer
            self.dfs_count(programmer, visited)  # Perform DFS to mark reachable programmers
            count_reachable[programmer] = sum(visited)  # Count how many programmers are reachable
        max_reachable = max(count_reachable)
        strongest_candidates = [i for i, count in enumerate(count_reachable) if count == max_reachable]
        # Ensure that there is exactly one strongest programmer
        if len(strongest_candidates) == 1:
            return strongest_candidates[0]  # Return the index of the strongest programmer
        return -1  # More than one strongest programmer found or none found
    def dfs_count(self, programmer, visited):
        visited[programmer] = True  # Mark the programmer as visited
        for neighbor in self.adjacency_list[programmer]:  # Traverse the adjacency list of the current programmer
            if not visited[neighbor]:
                self.dfs_count(neighbor, visited)  # Recursively visit the neighbor