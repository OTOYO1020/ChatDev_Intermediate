'''
Function to calculate the number of inspectors needed based on the number of trees and inspection range.
'''
def calculate_inspectors(n, d):
    if n <= 0 or d < 0:
        raise ValueError("N must be positive and D must be non-negative.")
    inspectors = 0
    i = 1
    while i <= n:
        inspectors += 1
        i += 2 * d + 1  # Move to the next tree not covered by the current inspector
    return inspectors