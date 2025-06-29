'''
Module for calculating the minimum cost of egg packs.
'''
class EggCostCalculator:
    '''
    Class to calculate the minimum cost for purchasing eggs.
    '''
    def __init__(self, n, s, m, l):
        self.n = n  # Number of eggs needed
        self.s = s  # Cost of 6-egg pack
        self.m = m  # Cost of 8-egg pack
        self.l = l  # Cost of 12-egg pack
    def calculate_min_cost(self):
        '''
        Calculate the minimum cost to purchase at least N eggs.
        '''
        min_cost = float('inf')
        for num_6_packs in range(self.n // 6 + 1):
            for num_8_packs in range((self.n - 6 * num_6_packs) // 8 + 1):
                remaining_eggs = self.n - (6 * num_6_packs + 8 * num_8_packs)
                if remaining_eggs >= 0:
                    # Calculate total cost for the current combination of packs
                    total_cost = (num_6_packs * self.s) + (num_8_packs * self.m)
                    # Calculate the number of 12-egg packs needed for the remaining eggs
                    num_12_packs = remaining_eggs // 12
                    total_cost += num_12_packs * self.l
                    remaining_after_12 = remaining_eggs % 12
                    # Handle remaining eggs after using 12-egg packs
                    if remaining_after_12 > 0:
                        if remaining_after_12 <= 6:
                            total_cost += self.s  # Add cost of one 6-egg pack
                        elif remaining_after_12 <= 8:
                            total_cost += self.m  # Add cost of one 8-egg pack
                        else:
                            # If remaining eggs are more than 8 but less than 12, check combinations
                            additional_cost = float('inf')
                            for extra_6_packs in range(0, (remaining_after_12 // 6) + 1):
                                for extra_8_packs in range(0, (remaining_after_12 // 8) + 1):
                                    total_remaining = extra_6_packs * 6 + extra_8_packs * 8
                                    if total_remaining >= remaining_after_12:
                                        additional_cost = min(additional_cost, extra_6_packs * self.s + extra_8_packs * self.m)
                            total_cost += additional_cost if additional_cost != float('inf') else 0
                    min_cost = min(min_cost, total_cost)
        return min_cost