'''
Utility functions for the probability calculator.
'''
def num_twice(A, K):
    '''
    Given two natural numbers A and K, return how many times A must be doubled until it exceeds K.
    '''
    count = 0
    while A < K:
        A *= 2
        count += 1
    print(count)
    return count