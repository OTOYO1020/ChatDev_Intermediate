'''
This file contains utility functions.
'''
def update_sequence(sequence):
    '''
    Update all elements of the sequence that are 0 with any positive real number.
    '''
    updated_sequence = []
    for element in sequence:
        if element == 0:
            updated_sequence.append(1)  # Replace 0 with 1, you can choose any positive real number
        else:
            updated_sequence.append(element)
    return updated_sequence
def multiply_sequence(sequence, multiplier):
    '''
    Multiply all elements of the sequence by a given multiplier.
    '''
    multiplied_sequence = []
    for element in sequence:
        multiplied_sequence.append(element * multiplier)
    return multiplied_sequence
def find_matching_subsequences(A, B):
    '''
    Find the number of integers i that satisfy 1 ≤ i ≤ N - M + 1 and meet the condition.
    '''
    count = 0
    sum_B = sum(update_sequence(B))
    for i in range(len(A) - len(B) + 1):
        subsequence = A[i:i+len(B)]
        sum_subsequence = sum(subsequence)
        if sum_subsequence % sum_B == 0:
            multiplier = sum_subsequence / sum_B
            updated_subsequence = multiply_sequence(subsequence, multiplier)
            if all(x == y for x, y in zip(updated_subsequence, update_sequence(B))):
                count += 1
    return count