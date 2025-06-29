'''
Module for counting valid combinations of switch states for bulbs.
'''
def count_valid_combinations(N, bulb_conditions):
    valid_count = 0
    total_combinations = 1 << N  # 2^N combinations
    for combination in range(total_combinations):
        if all(is_bulb_lit(combination, bulb) for bulb in bulb_conditions):
            valid_count += 1
    return valid_count
def is_bulb_lit(combination, bulb):
    switches = bulb[:-1]  # All but the last element are switch numbers
    p_i = bulb[-1]  # The last element is the required parity
    # Adjusted for 1-based indexing by subtracting 1 from each switch number
    on_switches_count = sum((combination >> (s - 1)) & 1 for s in switches)  
    return (on_switches_count % 2) == p_i