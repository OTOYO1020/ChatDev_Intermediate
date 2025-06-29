'''
Module for calculating the cumulative sum of products of integer pairs.
'''
def calculate_total_sum(numbers):
    total_sum = 0
    n = len(numbers)
    MOD = 10**9 + 7
    for i in range(n):
        for j in range(i + 1, n):
            product = numbers[i] * numbers[j]
            total_sum = (total_sum + product) % MOD
    return total_sum