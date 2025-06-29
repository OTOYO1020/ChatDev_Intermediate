'''
Module for calculating the minimum expected cost.
'''
def min_expected_cost(N: int, A: int, X: int, Y: int) -> float:
    memo = {}
    def calculate(n):
        # Base case: if n is 0, no cost is incurred
        if n == 0:
            return 0
        # Check if the result is already computed
        if n in memo:
            return memo[n]
        # Cost for operation with A: replace N with floor(N / A)
        cost_a = Y + calculate(n // A)
        # Cost for die operation: Calculate the expected cost by averaging over all die outcomes (1 to 6)
        expected_cost_die = 0
        valid_outcomes = 0  # Count of valid outcomes for averaging
        for b in range(1, 7):
            next_n = n // b
            if next_n >= 0:  # Only consider valid next_n
                expected_cost_die += (1/6) * (X + calculate(next_n))
                valid_outcomes += 1
        # If there are valid outcomes, average the expected cost
        if valid_outcomes > 0:
            expected_cost_die /= valid_outcomes
        else:
            expected_cost_die = float('inf')  # Set to infinity if no valid outcomes
        # Determine the minimum cost between the two operations
        min_cost = min(cost_a, expected_cost_die)
        memo[n] = min_cost  # Store the computed cost for memoization
        return min_cost
    return calculate(N)