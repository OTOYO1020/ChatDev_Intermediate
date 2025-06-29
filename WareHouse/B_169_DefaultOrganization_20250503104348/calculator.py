'''
Module to handle product calculation logic.
'''
class ProductCalculator:
    '''
    Class to calculate the product of a list of integers.
    '''
    def calculate_product(self, integers):
        '''
        Method to calculate the product of the given integers.
        Returns -1 if the product exceeds 10^18 during calculation.
        '''
        product = 1
        for number in integers:
            # If any number is zero, print 0 and terminate the program
            if number == 0:
                print(0)
                return 0  # Terminate the calculation
            # Check for overflow before multiplication
            if product > 10**18 // number:
                return -1  # Return -1 if overflow occurs
            product *= number
        return product