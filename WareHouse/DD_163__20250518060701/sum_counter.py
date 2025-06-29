'''
Module to calculate the number of unique sums from a generated list of integers.
'''
def count_possible_sums(N: int, K: int) -> int:
    MOD = 10**9 + 7
    start = 10**100
    # Handle edge cases
    if K > N or N < 0 or K < 0:
        return 0  # If K is greater than N or either is negative, no combinations are possible
    # The number of unique sums can be calculated as follows:
    # The smallest sum is K * start and the largest sum is K * start + (0 + 1 + ... + (N - K))
    # The number of unique sums is the range of sums from K * start to K * start + (N - K) * (N - K + 1) / 2
    min_sum = K * start
    max_sum = min_sum + (N - K) * (N - K + 1) // 2
    # The number of unique sums is the difference between max_sum and min_sum + 1
    unique_sum_count = (max_sum - min_sum + 1) % MOD
    return unique_sum_count