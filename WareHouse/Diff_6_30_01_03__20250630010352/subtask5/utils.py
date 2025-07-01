'''
Utility functions for finding the smallest integer X.
'''
def find_smallest_x(n):
    """
    Finds the smallest integer X such that X = a^3 + a^2b + ab^2 + b^3 for non-negative integers a and b.
    Args:
        n (int): The starting integer to find X.
    Returns:
        int: The smallest integer X that satisfies the condition.
    """
    x = n
    while True:
        found = False
        for a in range(int(x**(1/3)) + 1):
            a_cubed = a**3
            if a_cubed > x:
                break
            for b in range(int(x**(1/3)) + 1):
                b_cubed = b**3
                if a_cubed + b_cubed > x:
                    break
                remaining = x - (a_cubed + b_cubed)
                # Check if remaining can be expressed as a^2 * b + a * b^2
                if remaining >= 0 and remaining == a**2 * b + a * b**2:
                    found = True
                    break  # Break out of the b loop if found
            if found:
                break  # Break out of the a loop if found
        if found:
            return x
        x += 1