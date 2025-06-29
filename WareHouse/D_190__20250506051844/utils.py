'''
Utility functions for the Arithmetic Progression Calculator.
'''
def calculate_arithmetic_progressions(N):
    '''
    Calculates the number of valid arithmetic progressions that sum to N.
    '''
    count = 0
    for a in range(1, N + 1):
        discriminant = (2 * a - 1) ** 2 + 8 * N
        if discriminant >= 0:
            sqrt_discriminant = int(discriminant ** 0.5)
            if sqrt_discriminant * sqrt_discriminant == discriminant:  # Check if perfect square
                # Calculate both potential k values
                k1 = (- (2 * a - 1) + sqrt_discriminant) // 2
                k2 = (- (2 * a - 1) - sqrt_discriminant) // 2
                # Function to check if k is a valid positive integer
                def is_valid_k(k):
                    return k > 0 and (2 * a + k - 1) * k == 2 * N
                # Check both k1 and k2
                if k1 > 0 and is_valid_k(k1):
                    count += 1
                if k2 > 0 and k2 != k1 and is_valid_k(k2):  # Ensure k2 is counted only if it's different from k1
                    count += 1
    return count