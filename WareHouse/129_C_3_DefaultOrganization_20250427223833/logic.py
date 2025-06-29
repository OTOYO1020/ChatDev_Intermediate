'''
Logic file for calculating the number of ways to climb steps.
'''
def countWaysToClimb(N, M, broken_steps):
    MOD = 1000000007
    broken_set = set(broken_steps)  # Convert to set for O(1) checks
    ways = [0] * (N + 1)
    ways[0] = 1  # There's one way to be on the 0-th step
    for i in range(1, N + 1):
        if i in broken_set:
            continue  # Skip broken steps
        if i - 1 >= 0 and (i - 1) not in broken_set:
            ways[i] += ways[i - 1]
        if i - 2 >= 0 and (i - 2) not in broken_set:
            ways[i] += ways[i - 2]
        ways[i] %= MOD  # Take modulo for each update
    return ways[N]