'''
Contains functions for populating the transformation matrix and calculating the final element.
'''
def populate_transformation_matrix(n, matrix_values):
    """
    Populates a 2D list with transformation values based on user input.
    Parameters:
    n (int): The number of element types.
    matrix_values (list): A list of lists containing transformation values.
    Returns:
    list: A 2D list representing the transformation matrix.
    """
    matrix = []
    for i in range(n):
        row = matrix_values[i]  # Directly use the row from matrix_values
        if len(row) != n:
            raise ValueError("Each row must contain exactly N values.")
        matrix.append(row)
    # Validate the entire matrix after population
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 1 or matrix[i][j] > n:
                raise ValueError(f"Invalid transformation value at A[{i+1}][{j+1}]: {matrix[i][j]}. It must be between 1 and {n}.")
    return matrix
def calculate_final_element(transformation_matrix, n):
    """
    Calculates the final element after performing transformations.
    Parameters:
    transformation_matrix (list): The 2D list of transformation values.
    n (int): The number of element types.
    Returns:
    int: The final element obtained after transformations.
    """
    current_element = 1
    for k in range(1, n + 1):
        if current_element >= k:
            new_element = transformation_matrix[current_element - 1][k - 1]
        else:
            new_element = transformation_matrix[k - 1][current_element - 1]
        # Validate the new element before assigning
        if new_element < 1 or new_element > n:
            raise ValueError(f"Invalid transformation value: {new_element}. It must be between 1 and {n}.")
        current_element = new_element
        # Additional check to ensure current_element remains valid
        if current_element < 1 or current_element > n:
            raise ValueError(f"Current element out of bounds: {current_element}. It must be between 1 and {n}.")
    return current_element