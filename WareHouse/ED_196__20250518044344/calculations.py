'''
Contains the calculation logic for the application.
'''
from typing import List
def calculate_f(N: int, A: List[int], T: List[int], X: List[int]) -> List[int]:
    results = []
    for x_i in X:
        result = x_i
        error_occurred = False
        for i in range(1, N + 1):
            try:
                result = f_i(result, A[i - 1], T[i - 1])
            except ValueError as e:
                print(f"Error processing x_i={x_i} with f_{i}: {e}")
                error_occurred = True
                break  # Stop processing this x_i on error
        if not error_occurred:
            results.append(result)
        else:
            print(f"Skipping x_i={x_i} due to errors.")  # Log the error instead of appending None
    return results
def f_i(x: int, a_i: int, t_i: int) -> int:
    '''
    Computes the value based on the conditions provided for t_i.
    - If t_i == 1: Add a_i to x
    - If t_i == 2: Subtract a_i from x
    - If t_i == 3: Multiply x by a_i
    - If t_i == 4: Integer divide x by a_i (if a_i is not zero)
    - For any other t_i: Raise an error indicating invalid operation
    '''
    if t_i < 1 or t_i > 4:
        raise ValueError(f"Invalid operation code t_i: {t_i}. Must be between 1 and 4.")
    if t_i == 1:
        return x + a_i
    elif t_i == 2:
        return x - a_i
    elif t_i == 3:
        return x * a_i
    elif t_i == 4:
        if a_i == 0:
            raise ValueError("Division by zero is not allowed.")
        return x // a_i