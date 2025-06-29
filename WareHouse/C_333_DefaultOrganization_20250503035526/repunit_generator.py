'''
Module for generating repunit numbers and calculating unique sums.
'''
from itertools import combinations_with_replacement  # Updated import
class RepunitGenerator:
    def generate_repunits(self, limit=333):  # Set limit to 333 for repunits
        """
        Generate repunit numbers up to the specified limit.
        A repunit is a number consisting entirely of the digit '1'.
        This method creates repunits from 1 to the specified limit.
        """
        repunits = []
        for i in range(1, limit + 1):
            repunits.append(int('1' * i))
        return repunits
    def calculate_unique_sums(self, n, limit=333):  # Ensure the limit is consistent
        """
        Calculate unique sums of three repunits.
        This method generates repunit numbers up to the specified limit,
        computes all unique sums of combinations of three repunits,
        and returns the N-th smallest sum.
        """
        repunits = self.generate_repunits(limit)  # Pass the limit explicitly
        sums = set()
        for combo in combinations_with_replacement(repunits, 3):  # Use combinations_with_replacement
            sums.add(sum(combo))
        sorted_sums = sorted(sums)
        # Check if there are enough unique sums
        if len(sorted_sums) < n:
            raise ValueError(f"There are only {len(sorted_sums)} unique sums available, but you requested the {n}-th smallest. Please try a smaller N or increase the limit.")
        return sorted_sums[n - 1]  # Return the N-th smallest sum