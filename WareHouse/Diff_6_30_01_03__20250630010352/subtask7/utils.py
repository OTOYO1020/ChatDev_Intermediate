'''
Utility functions for finding the smallest integer X.
'''
def find_smallest_x(n):
    """
    Finds the smallest integer X such that X = a^3 + a^2b + ab^2 + b^3 for non-negative integers a and b.
    Args:
        n (int): The starting integer to find X.
    Returns:
        int: The smallest integer X that satisfies the condition, or None if not found.
    """
    x = n
    max_attempts = 10000  # Set a maximum limit to avoid infinite loops
    attempts = 0
    while attempts < max_attempts:
        found = False
        for a in range(int(x**(1/3)) + 1):
            a_cubed = a**3
            if a_cubed > x:
                break
            for b in range(int((x - a_cubed)**(1/3)) + 1):
                b_cubed = b**3
                if a_cubed + b_cubed > x:
                    break
                remaining = x - (a_cubed + b_cubed)
                if remaining >= 0:
                    # Check if remaining can be expressed as a^2 * b + a * b^2
                    if a == 0 and b == 0:
                        continue  # Skip the case where both a and b are zero
                    if a + b > 0 and remaining % (a + b) == 0:  # Check if remaining can be divided evenly
                        b_calculated = remaining // (a + b)
                        if b_calculated >= 0:
                            found = True
                            break
                if found:
                    break  # Break out of the b loop if found
            if found:
                break  # Break out of the a loop if found
        if found:
            return x
        x += 1
        attempts += 1
    return None  # Return None if no valid X is found within the attempts