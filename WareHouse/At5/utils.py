'''
This file contains utility functions that can be used throughout the software.
'''
import numpy as np
def function1(seq):
    """
    Update all elements of the sequence that are 0 with any positive real number.
    """
    return [x if x != 0 else np.random.rand() for x in seq]
def function2(seq, t):
    """
    Multiply all elements of the sequence by t.
    """
    return [x * t for x in seq]