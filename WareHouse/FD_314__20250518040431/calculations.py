'''
Module for calculating expected wins based on matches.
'''
from typing import List, Tuple
from math import gcd
def modular_inverse(a: int, mod: int) -> int:
    """Compute the modular inverse of a under modulo mod."""
    return pow(a, mod - 2, mod)
def calculate_expected_wins(N: int, matches: List[Tuple[int, int]]) -> List[int]:
    """Calculate expected wins for each player based on matches."""
    MOD = 998244353
    expected_wins = [(0, 1)] * N  # Store as (numerator, denominator)
    team_sizes = [1] * N  # Each player starts in their own team
    parent = list(range(N))  # Union-Find structure to track team leaders
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    for p_i, q_i in matches:
        p_i -= 1  # Adjusting for 0-based index
        q_i -= 1  # Adjusting for 0-based index
        root_p = find(p_i)
        root_q = find(q_i)
        if root_p == root_q:
            continue  # They are already in the same team
        a = team_sizes[root_p]
        b = team_sizes[root_q]
        total_size = a + b
        # Calculate winning probabilities
        prob_first = (a, total_size)  # (numerator, denominator)
        prob_second = (b, total_size)  # (numerator, denominator)
        # Update expected wins for both players before merging teams
        expected_wins[root_p] = (
            (expected_wins[root_p][0] * prob_first[1] + expected_wins[root_q][0] * prob_second[1]) % MOD,
            (expected_wins[root_p][1] * prob_first[1] * expected_wins[root_q][1] * prob_second[1]) % MOD
        )
        # Normalize the expected wins for player p
        gcd_value_p = gcd(expected_wins[root_p][0], expected_wins[root_p][1])
        expected_wins[root_p] = (
            expected_wins[root_p][0] // gcd_value_p,
            expected_wins[root_p][1] // gcd_value_p
        )
        # Merge teams
        parent[root_q] = root_p  # Merge team of q into team of p
        team_sizes[root_p] = total_size  # Update size of the new team
    # Convert expected wins to the required format
    results = []
    for num, denom in expected_wins:
        if denom == 0:  # Prevent division by zero
            results.append(0)
        else:
            results.append((num * modular_inverse(denom, MOD)) % MOD)
    return results