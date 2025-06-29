def max_happiness(N: int, A: List[int]) -> int:
    max_hap = 0
    # Generate all permutations of the list A
    for perm in permutations(A):
        total_happiness = 0
        # Calculate happiness for the current permutation
        for x in range(N):
            total_happiness += perm[x] * abs(x - A.index(perm[x]))  # Corrected logic
        max_hap = max(max_hap, total_happiness)
    return max_hap