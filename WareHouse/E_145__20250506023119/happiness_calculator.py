'''
Module defining the HappinessCalculator class to calculate maximum happiness.
'''
from dish import Dish
class HappinessCalculator:
    def __init__(self):
        pass
    def calculate_max_happiness(self, dishes, total_time):
        '''
        Calculate the maximum happiness based on the dishes and available time.
        Parameters:
        dishes (list): A list of Dish objects.
        total_time (int): The total time available to eat dishes.
        Returns:
        int: The maximum happiness achievable.
        '''
        # Sort dishes based on deliciousness in descending order
        dishes.sort(key=lambda x: x.deliciousness, reverse=True)
        max_happiness = 0
        remaining_time = total_time
        # Iterate through sorted dishes to calculate maximum happiness
        for dish in dishes:
            # Check if there is enough time to eat the dish
            if remaining_time >= dish.eating_time:  
                max_happiness += dish.deliciousness  # Add deliciousness to max_happiness
                remaining_time -= dish.eating_time  # Subtract eating time
                remaining_time -= 0.5  # Subtract the additional 0.5 time unit after eating
            else:
                break  # Exit the loop if not enough time remains
        return max_happiness