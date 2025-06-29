'''
Module containing the simulation logic to determine the maximum number of satisfied conditions.
'''
from itertools import product
def simulate(conditions, actions, K, N):
    max_satisfied = 0
    num_dishes = max(max(cond.dish_a, cond.dish_b) for cond in conditions) + 1
    # Validate that the number of dishes is sufficient
    if num_dishes > N:
        raise ValueError(f"The number of dishes (N) is {N}, but conditions and actions reference up to dish {num_dishes - 1}.")
    # Generate all combinations of actions for K people
    for action_combination in product(actions, repeat=K):
        dishes = [0] * num_dishes
        for action in action_combination:
            action.perform(dishes)
        satisfied_count = sum(cond.is_satisfied(dishes) for cond in conditions)
        max_satisfied = max(max_satisfied, satisfied_count)
    return max_satisfied