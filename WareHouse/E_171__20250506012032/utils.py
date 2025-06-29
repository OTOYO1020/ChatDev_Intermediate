'''
Utility functions for the Snuke Cat application.
'''
def restore_scarves(N, a):
    '''
    Calculate the scarves for each Snuke Cat based on the total XOR of the input array.
    Parameters:
    N (int): The number of Snuke Cats (must be even).
    a (list): The list of integers representing the XOR values from each Snuke Cat.
    Returns:
    list: A list of integers representing the scarves for each Snuke Cat, where each
          scarf value is calculated as total_xor XOR a[i].
    '''
    if len(a) != N:
        raise ValueError("The length of the array must match N.")
    total_xor = 0
    for value in a:
        total_xor ^= value
    scarves = [total_xor ^ value for value in a]
    return scarves