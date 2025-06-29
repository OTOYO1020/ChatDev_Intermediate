'''
Module for counting valid subsets with integer-valued averages.
'''
class SubsetCounter:
    '''
    Class to count valid subsets.
    '''
    def count_integer_averages(self, N, A):
        '''
        Counts the number of valid subsets with integer-valued averages.
        '''
        count = 0
        MOD = 998244353
        # Iterate over all possible non-empty subsets
        for i in range(1, 1 << N):
            subset_sum = 0
            num_elements = 0
            for j in range(N):
                if i & (1 << j):
                    subset_sum += A[j]
                    num_elements += 1
            # Check if the average is an integer
            if subset_sum % num_elements == 0:
                count += 1
        return count % MOD