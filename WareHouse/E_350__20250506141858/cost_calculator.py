'''
Module for calculating the minimum expected cost based on given parameters.
'''
def calculate_cost(N, A, X, Y, memo=None):
    '''
    Recursive function to calculate the minimum expected cost with memoization.
    '''
    if memo is None:
        memo = {}
    if N in memo:
        return memo[N]
    if N == 0:
        return 0  # Base case
    # Initialize min_cost to infinity
    min_cost = float('inf')
    # Calculate cost for the first operation
    if A > N:
        cost_A = X  # If A is greater than N, we cannot divide further
    else:
        cost_A = X + calculate_cost(N // A, A, X, Y, memo)
    min_cost = min(min_cost, cost_A)  # Update min_cost with cost_A
    # Initialize cost_dice to store the total cost from die rolls
    cost_dice = 0
    # Calculate the average cost of the second operation
    for b in range(1, 7):
        cost_b = Y + calculate_cost(N // b, A, X, Y, memo)
        cost_dice += cost_b
    # Only average if N is greater than 0
    if N > 0:
        cost_dice /= 6  # Average of the costs from the die rolls
    # Update min_cost with the average cost from die rolls
    min_cost = min(min_cost, cost_dice)
    memo[N] = min_cost
    return min_cost  # Return the minimum cost directly