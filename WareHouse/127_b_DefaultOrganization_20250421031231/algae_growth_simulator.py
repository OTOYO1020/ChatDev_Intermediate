'''
Module for simulating algae growth over a period of 10 years.
'''
class AlgaeGrowthSimulator:
    '''
    Class to simulate algae growth based on given parameters.
    '''
    def __init__(self, r, D, x_2000):
        self.r = r
        self.D = D
        self.x = x_2000
    def simulate_growth(self):
        '''
        Simulates the growth of algae over a period of 10 years.
        Calculates the weight of algae for each year using the formula:
        x_{i+1} = r * x_i - D
        Returns a list of results for each year from 2001 to 2010.
        '''
        results = []
        for year in range(1, 11):  # Simulate from 2001 to 2010
            # Calculate the weight of algae for the next year
            self.x = self.r * self.x - self.D
            # Check if the weight of algae has gone below zero
            if self.x < 0:
                print(f"Warning: Algae weight dropped below zero in year {2000 + year}.")
                break  # Stop further calculations
            results.append(int(self.x))  # Store the result as an integer
        return results