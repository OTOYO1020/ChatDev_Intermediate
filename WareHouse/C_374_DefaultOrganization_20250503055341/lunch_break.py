'''
Module containing functions to calculate the minimum maximum lunch break.
'''
def min_max_lunch_break(K):
    '''
    Calculate the minimum maximum lunch break counts across all divisions of departments.
    Args:
        K (list): List of integers representing the number of people in each department.
    Returns:
        int: Minimum value of the maximum lunch break counts across all divisions.
    '''
    n = len(K)
    total_people = sum(K)
    min_max_break = float('inf')
    # Iterate through all possible combinations using bitmasking
    for mask in range(1 << n):  # 2^n combinations
        group_a = 0
        for i in range(n):
            if mask & (1 << i):  # Check if the i-th department is included in Group A
                group_a += K[i]
        group_b = total_people - group_a
        max_lunch_break = max(group_a, group_b)
        min_max_break = min(min_max_break, max_lunch_break)
    return min_max_break