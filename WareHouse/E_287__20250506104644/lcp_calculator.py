'''
Module containing the logic for calculating the longest common prefix.
'''
def lcp(x, y):
    '''
    Compute the longest common prefix between two strings x and y.
    '''
    min_length = min(len(x), len(y))
    for i in range(min_length):
        if x[i] != y[i]:
            return i
    return min_length
def find_max_lcp(strings):
    '''
    Find the maximum LCP value among all pairs of strings.
    '''
    max_lcp = 0
    n = len(strings)
    for i in range(n):
        for j in range(n):
            if i != j:
                current_lcp = lcp(strings[i], strings[j])
                max_lcp = max(max_lcp, current_lcp)
    return max_lcp