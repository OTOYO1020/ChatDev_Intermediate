'''
Module for processing tastiness data.
'''
class DataProcessor:
    def __init__(self, tastiness_values, disliked_indices):
        self.tastiness_values = tastiness_values
        self.disliked_indices = disliked_indices
    def find_max_tastiness(self):
        if not self.tastiness_values:  # Check if the list is empty
            return []  # Return an empty list if no tastiness values are present
        max_tastiness = max(self.tastiness_values)
        max_indices = [index for index, value in enumerate(self.tastiness_values) if value == max_tastiness]
        return max_indices
    def check_disliked_food(self):
        max_indices = self.find_max_tastiness()
        disliked_set = set(self.disliked_indices)  # Convert to set to handle duplicates
        has_disliked_food = any(index in disliked_set for index in max_indices)
        return has_disliked_food