'''
Module containing the function to generate the final sequence based on input parameters.
'''
def final_sequence(N, S):
    '''
    Generates a final sequence based on the input parameters.
    Parameters:
    N (int): The number of elements to process.
    S (str): A string consisting of 'L' and 'R' indicating the direction for each element.
    Returns:
    list: A list containing the final sequence starting with 0.
    '''
    if len(S) != N:
        raise ValueError("The length of S must be equal to N.")
    A = [0]
    for i in range(1, N + 1):
        s_i = S[i - 1]  # Adjust for 0-based index
        if s_i == 'L':
            A.insert(0, i)  # Insert at index 0 to keep 0 at the start
        elif s_i == 'R':
            A.append(i)  # Append to the end of the list
    return A