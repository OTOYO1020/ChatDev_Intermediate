'''
Contains the logic for performing digit-wise addition and determining if the result is "Easy" or "Hard".
'''
def check_addition(a, b):
    """
    Perform digit-wise addition of two integers and determine if the result is "Easy" or "Hard".
    Parameters:
    a (int): The first positive integer.
    b (int): The second positive integer.
    Returns:
    str: "Easy" if the addition does not produce a carry, "Hard" otherwise.
    """
    carry = 0
    str_a = str(a)
    str_b = str(b)
    max_length = max(len(str_a), len(str_b))
    for i in range(max_length):
        digit_a = int(str_a[-(i + 1)]) if i < len(str_a) else 0
        digit_b = int(str_b[-(i + 1)]) if i < len(str_b) else 0
        total = digit_a + digit_b + carry
        if total > 9:  # If the total is greater than 9, we have a carry
            carry = 1
        # No need to reset carry here, it should retain its value for the next iteration
    return "Hard" if carry > 0 else "Easy"