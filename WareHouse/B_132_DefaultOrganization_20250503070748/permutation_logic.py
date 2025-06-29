'''
Contains the logic for counting valid elements in a permutation.
'''
class PermutationLogic:
    def __init__(self, n, p):
        self.n = n
        self.p = p
    def count_valid_elements(self):
        count = 0
        # Iterate from index 2 to n-2 to evaluate valid elements
        for i in range(2, self.n - 1):  # Corrected to avoid IndexError
            neighbors = [self.p[i - 1], self.p[i], self.p[i + 1]]
            neighbors.sort()
            second_smallest = neighbors[1]
            if self.p[i] == second_smallest:
                count += 1
        return count