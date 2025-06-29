'''
Computation module for calculating the popcount sum.
'''
def popcount(x: int) -> int:
    '''
    Calculate the number of 1s in the binary representation of x.
    '''
    return bin(x).count('1')
def compute_popcount_sum(N: int, M: int) -> int:
    '''
    Compute the sum of popcounts for k & M for k in range 0 to N.
    '''
    total_sum = 0
    MODULO = 998244353
    for k in range(N + 1):
        total_sum += popcount(k & M)
        total_sum %= MODULO
    return total_sum