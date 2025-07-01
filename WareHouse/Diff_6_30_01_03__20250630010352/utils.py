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
    while True:
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
                    # Check if remaining can be expressed as a^2b + ab^2
                    if a == 0:
                        # When a is zero, check if remaining can be expressed as b^3
                        if remaining == 0 or (remaining > 0 and (remaining ** (1/3)).is_integer()):
                            found = True
                            break
                    else:
                        # Check for non-zero a
                        for b_check in range(remaining + 1):  # Iterate through all possible b values
                            if remaining == a**2 * b_check + a * b_check**2:
                                found = True
                                break  # Found a valid pair (a, b)
                if found:
                    break  # Exit the inner loop if a valid pair is found
            if found:
                break  # Exit the outer loop if a valid pair is found
        if found:
            return x
        x += 1  # Increment X if no valid pair is found