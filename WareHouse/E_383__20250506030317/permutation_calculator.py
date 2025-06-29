'''
Class to calculate permutations and minimum sums.
'''
from itertools import permutations
class PermutationCalculator:
    @staticmethod
    def calculate_min_sum(A, B, graph):
        min_sum = float('inf')
        for perm in permutations(B):
            current_sum = 0
            valid_path = True
            for i in range(len(A)):
                path_weight = graph.f(A[i], perm[i])
                if path_weight == float('inf'):
                    valid_path = False
                    print(f"No valid path exists for permutation: {perm}")
                    break
                current_sum += path_weight
            if valid_path:
                min_sum = min(min_sum, current_sum)
        if min_sum == float('inf'):
            return None  # Return None if no valid paths were found
        return min_sum  # Return the minimum sum found