'''
Utility functions for mathematical operations.
'''
MOD = 10**9 + 7
def mod_inverse(a, p):
    return pow(a, p - 2, p)
def comb(n, k, fact, inv_fact):
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD