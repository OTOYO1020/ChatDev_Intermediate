'''
Module containing functions for reducing integers and calculating operations.
'''
def reduce_value(value):
    if value < 1:
        raise ValueError("Value must be a positive integer.")
    if value == 1:
        return 0  # No operations needed for the value 1
    operations = 0
    # Reduce the value until it is not divisible by 2 or 3
    while value % 2 == 0 or value % 3 == 0:
        if value % 2 == 0:
            value //= 2
        elif value % 3 == 0:
            value //= 3
        operations += 1
    # If the reduced value is greater than 1, find the next valid number
    if value > 1:
        while value % 2 == 0 or value % 3 == 0:
            value += 1  # Increment to find the next valid number
            operations += 1
            if operations > 100:  # Safety check to prevent infinite loop
                raise RuntimeError("Exceeded maximum operations to find a valid number.")
    return operations  # Return only the operations count
def calculate_operations(numbers):
    total_operations = 0
    reduced_values = []
    # Validate input numbers to ensure they are positive integers
    for number in numbers:
        if number <= 0:
            return -1  # Invalid input, must be positive integers
    for number in numbers:
        operations = reduce_value(number)
        total_operations += operations
        # Store the reduced value instead of the original number
        reduced_value = number
        while reduced_value % 2 == 0 or reduced_value % 3 == 0:
            if reduced_value % 2 == 0:
                reduced_value //= 2
            elif reduced_value % 3 == 0:
                reduced_value //= 3
        reduced_values.append(reduced_value)  # Store the reduced value for comparison
    # Check if all reduced values can be the same
    if len(set(reduced_values)) > 1:
        return -1  # Cannot reduce to a common value
    return total_operations