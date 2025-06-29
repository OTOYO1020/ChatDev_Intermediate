'''
Module for computation functions related to truncated product calculation.
'''
def compute_truncated_product(A: int, B: float) -> int:
    """
    Computes the truncated product of an integer A and a floating-point number B.
    Parameters:
    A (int): The integer value.
    B (float): The floating-point value to be converted.
    Returns:
    int: The truncated product of A and B.
    """
    B_int = int(B * 100)  # Convert B to an integer representation
    product = A * B_int   # Compute the product
    truncated_result = product // 100  # Truncate the fractional part
    return truncated_result