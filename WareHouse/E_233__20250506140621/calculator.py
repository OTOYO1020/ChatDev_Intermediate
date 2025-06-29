'''
Calculator class that contains the logic for calculating the cumulative sum of floor values.
'''
class Calculator:
    def calculate_total_sum(self, x_str):
        '''
        Calculate the cumulative sum of floor values based on the powers of 10.
        '''
        total_sum = 0
        k = 0
        x_int = int(x_str)  # Convert to integer once for efficiency
        while 10 ** k <= x_int:  # Ensure we are still within bounds
            floor_value = x_int // (10 ** k)  # Calculate floor value directly
            total_sum += floor_value
            k += 1
        return total_sum