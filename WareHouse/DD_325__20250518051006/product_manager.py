'''
Module for managing product data and calculations.
'''
from typing import List, Tuple
class ProductManager:
    def max_printable_products(self, N: int, products: List[Tuple[int, int]]) -> int:
        '''
        Calculate the maximum number of products that can be printed based on their timing.
        '''
        if N == 0:
            return 0
        # Sort products based on entry time T_i
        products.sort(key=lambda x: x[0])
        last_printed_time = -1  # Start from a negative time
        count = 0
        for T_i, D_i in products:
            # Check if the product can be printed considering the charge time
            if last_printed_time <= T_i:  # Allow printing at T_i
                last_printed_time = T_i + 1  # Increment by 1 microsecond after printing
                count += 1
            elif last_printed_time <= D_i:  # Allow printing at D_i
                last_printed_time = D_i + 1  # Increment by 1 microsecond after printing
                count += 1
        return count