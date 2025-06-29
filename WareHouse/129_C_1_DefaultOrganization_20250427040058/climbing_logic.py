'''
Logic module to calculate the number of ways to climb steps avoiding broken steps.
'''
def countWaysToClimb(N, M, broken_steps):
    MOD = 1000000007
    ways = [0] * (N + 1)
    ways[0] = 1  # There's one way to be on the 0-th step
    broken_set = set(broken_steps)  # For O(1) average-time complexity checks
    for i in range(1, N + 1):
        if i in broken_set:
            continue  # Skip broken steps
        if i - 1 >= 0 and (i - 1) not in broken_set:
            ways[i] = (ways[i] + ways[i - 1]) % MOD
        if i - 2 >= 0 and (i - 2) not in broken_set:
            ways[i] = (ways[i] + ways[i - 2]) % MOD
    return ways[N]