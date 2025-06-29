'''
Utility functions for counting valid integers based on specific criteria.
'''
def count_valid_integers(N):
    if N < 1:
        return 0  # Return 0 if N is less than 1
    count = 0
    for x in range(1, N + 1):
        str_x = str(x)
        if len(str_x) % 2 == 0:  # Check if the length is even
            mid = len(str_x) // 2
            first_half = str_x[:mid]
            second_half = str_x[mid:]
            if first_half == second_half:  # Compare halves
                count += 1
    return count