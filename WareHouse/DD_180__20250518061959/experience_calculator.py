'''
Module to calculate the maximum experience based on training parameters.
'''
def max_experience(X: int, Y: int, A: int, B: int) -> int:
    max_exp = 0
    # Check immediate evolution
    if X >= Y:
        return 0  # No training needed, already evolved
    # Train at Kakomon Gym
    current_STR = X
    exp_kakomon = 0
    while current_STR < Y:
        current_STR *= A
        exp_kakomon += 1
        if current_STR >= Y:
            max_exp = max(max_exp, exp_kakomon)
            break  # Exit if evolved
    # Train at AtCoder Gym
    current_STR = X
    exp_atcoder = 0
    while current_STR < Y:
        current_STR += B
        exp_atcoder += 1
        if current_STR >= Y:
            max_exp = max(max_exp, exp_atcoder)
            break  # Exit if evolved
    # Return the maximum experience obtained from both training gyms
    return max_exp