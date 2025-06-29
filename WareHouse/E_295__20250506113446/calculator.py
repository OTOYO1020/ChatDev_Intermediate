'''
Module to perform calculations for the expected value.
'''
class Calculator:
    MOD = 998244353
    def compute_expected_value(self, N, K, A):
        expected_value_numerator = 0
        expected_value_denominator = 1  # Start with 1 for the denominator
        M = 100  # Assuming M is defined as 100 for the random integer range
        zero_count = 0  # Count the number of zeros in A
        # Calculate the expected value contribution from non-zero elements
        for i in range(N):
            if A[i] == 0:
                zero_count += 1  # Increment zero count
            else:
                expected_value_numerator += A[i] * expected_value_denominator
        # Calculate expected value contribution from zeros
        if zero_count > 0:
            # Correctly calculate the average value for zeros
            expected_value_per_zero_numerator = (M + 1) * expected_value_denominator
            expected_value_per_zero_denominator = 2
            # Update expected value for zeros
            expected_value_numerator += zero_count * expected_value_per_zero_numerator // expected_value_per_zero_denominator
        # Create a new list to hold the modified values for sorting
        modified_A = A[:]
        for i in range(N):
            if modified_A[i] == 0:
                modified_A[i] = expected_value_per_zero_numerator // expected_value_per_zero_denominator  # Replace zero with expected value
        # Sort the modified sequence A
        modified_A.sort()
        # Calculate the K-th element after sorting
        Kth_element = modified_A[K - 1]
        # Calculate the total expected value as a fraction
        if zero_count > 0:
            P = expected_value_numerator  # Numerator
            Q = zero_count * M  # Denominator should be the total possible outcomes for zeros
        else:
            P = expected_value_numerator  # If no zeros, just the sum of non-zero elements
            Q = 1  # Denominator should be 1 if there are no zeros
        # Calculate modular inverse of Q
        Q_inverse = pow(Q, self.MOD - 2, self.MOD)
        result = (P * Q_inverse) % self.MOD
        return result