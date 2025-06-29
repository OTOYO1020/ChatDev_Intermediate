'''
Module to evaluate conditions based on actions.
'''
def count_satisfied_conditions(conditions, actions):
    """
    Count how many conditions can be satisfied based on the actions taken.
    Parameters:
    conditions (list of tuples): List of conditions (A_i, B_i).
    actions (list of tuples): List of actions (C_i, D_i).
    Returns:
    int: Number of satisfied conditions.
    """
    dishes_with_balls = set()
    # Add balls to the respective dishes based on actions
    for C_i, D_i in actions:
        dishes_with_balls.add(C_i)
        dishes_with_balls.add(D_i)
    # Count satisfied conditions
    satisfied_count = 0
    for A_i, B_i in conditions:
        if A_i in dishes_with_balls and B_i in dishes_with_balls:
            satisfied_count += 1
    return satisfied_count