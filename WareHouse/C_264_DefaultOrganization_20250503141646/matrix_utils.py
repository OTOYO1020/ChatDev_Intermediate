'''
Utility file containing the function to check matrix transformation.
'''
def can_transform(A, B):
    '''
    Determines if matrix A can be transformed into matrix B.
    This is done by checking if A has at least as many rows and columns as B,
    and if all elements of B can be found in A, allowing for duplicates.
    '''
    # Check if either matrix is empty
    if not A:  # If A is empty
        return False if B else True  # Return False if B is not empty, True if both are empty
    if not B:  # If B is empty
        return True  # A can be transformed into an empty B
    # Ensure A has enough rows and columns
    if len(A) < len(B) or len(A[0]) < len(B[0]):  
        return False
    from collections import Counter
    count_a = Counter()
    count_b = Counter()
    # Count occurrences of each element in A
    for row in A:
        count_a.update(row)
    # Count occurrences of each element in B
    for row in B:
        count_b.update(row)
    # Check if A has enough of each element to match B
    for key in count_b:
        if count_b[key] > count_a.get(key, 0):
            return False
    return True