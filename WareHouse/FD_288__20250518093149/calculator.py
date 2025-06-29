'''
Contains the logic for calculating the sum of products.
'''
from itertools import combinations
def calculate_sum_of_products(X: str, N: int) -> int:
    MOD = 998244353
    total_sum = 0
    indices = list(range(1, N))  # Indices for splitting
    # Generate all subsets of indices
    for r in range(len(indices) + 1):
        for subset in combinations(indices, r):
            # Split the string based on the subset
            parts = []
            last_index = 0
            if not subset:  # Handle the empty subset case
                parts.append(int(X))  # Treat the whole string as one part
            else:
                for index in subset:
                    part = X[last_index:index]
                    if part:  # Ensure part is not empty
                        parts.append(int(part))
                    last_index = index
                part = X[last_index:]  # Add the last part
                if part:  # Ensure part is not empty
                    parts.append(int(part))
            # Calculate the product of the parts only if parts are not empty
            if parts:
                product = 1
                for part in parts:
                    product *= part
                total_sum = (total_sum + product) % MOD
    return total_sum