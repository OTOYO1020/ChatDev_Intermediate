'''
This file contains utility functions.
'''
def validate_input(input_data):
    """
    Validates the input data.
    Args:
        input_data: The input data to be validated.
    Returns:
        True if the input data is valid, False otherwise.
    """
    if len(input_data) > 0:
        return True
    else:
        return False
def process_data(data):
    """
    Processes the data.
    Args:
        data: The data to be processed.
    Returns:
        The processed data.
    """
    processed_data = [x * 2 for x in data]
    return processed_data