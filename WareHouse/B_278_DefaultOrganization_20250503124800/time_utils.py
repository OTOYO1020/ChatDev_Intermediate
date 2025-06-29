'''
Utility functions for time manipulation and checking confusing times.
'''
def is_confusing_time(h, m):
    # Extract digits A, B, C, D
    A = h // 10
    B = h % 10
    C = m // 10
    D = m % 10
    # Swap B and C
    new_h = A * 10 + C
    new_m = B * 10 + D
    # Check if the new time is valid and different from the original time
    return (0 <= new_h < 24 and 0 <= new_m < 60) and (new_h != h or new_m != m)
def increment_time(h, m):
    # Increment the time by one minute
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
    return h, m