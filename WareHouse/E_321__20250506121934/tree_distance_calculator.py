'''
Module for calculating the number of vertices at a specific distance in a conceptual tree.
'''
class TreeDistanceCalculator:
    def __init__(self, N, X, K):
        self.N = N
        self.X = X
        self.K = K
    def count_vertices_at_distance(self):
        if self.K < 0:
            return 0  # No valid distance if K is negative
        max_depth = self.calculate_depth(self.N)
        distance_to_root = self.calculate_distance_to_root(self.X)
        effective_depth = max_depth - distance_to_root
        if self.K > effective_depth:
            return 0  # No vertices at this distance if K exceeds effective depth
        if self.K == 0:
            return 1  # The node itself is at distance 0
        count = 0
        # Count vertices from the current node
        count += self.count_vertices_at_distance_from_node(self.X, self.K)
        # Count vertices from the ancestors of X
        for i in range(1, self.K + 1):
            ancestor = self.X // (2 ** i)
            if ancestor < 1:
                break  # Stop if the ancestor is out of bounds
            remaining_distance = self.K - i
            if remaining_distance >= 0:
                count += self.count_vertices_at_distance_from_node(ancestor, remaining_distance)
        return count
    def count_vertices_at_distance_from_node(self, node, distance):
        # Check if the node is out of bounds
        if node > self.N:
            return 0
        if distance == 0:
            return 1 if node <= self.N else 0  # Count the node itself if it's within bounds
        # Calculate the range of nodes at the given distance
        leftmost = node * (1 << distance)  # node * 2^distance
        rightmost = leftmost + (1 << distance) - 1  # leftmost + (2^distance - 1)
        # Ensure the range is within [1, N]
        valid_leftmost = max(leftmost, 1)
        valid_rightmost = min(rightmost, self.N)
        # Return the count of valid nodes within the range
        if valid_leftmost > valid_rightmost:
            return 0  # No valid nodes in range
        return valid_rightmost - valid_leftmost + 1
    def calculate_depth(self, N):
        depth = 0
        while (1 << depth) <= N:
            depth += 1
        return depth - 1  # Return the maximum depth of the tree
    def calculate_distance_to_root(self, X):
        distance = 0
        while X > 1:
            X //= 2
            distance += 1
        return distance  # Return the distance from the node to the root