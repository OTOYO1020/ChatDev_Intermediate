'''
Module defining the PotionTracker class for managing potion counts.
'''
class PotionTracker:
    def __init__(self):
        '''
        Initializes the PotionTracker instance with an empty potion dictionary and count.
        '''
        self.potions = {}
        self.current_count = 0
    def add_potion(self, x):
        '''
        Adds a potion of type x to the tracker.
        Parameters:
        x (int): The type of potion to add.
        '''
        if x in self.potions:
            self.potions[x] += 1
        else:
            self.potions[x] = 1
        self.current_count += 1
    def remove_potion(self, x):
        '''
        Removes a potion of type x from the tracker.
        Parameters:
        x (int): The type of potion to remove.
        Returns:
        bool: True if the potion was successfully removed, False otherwise.
        '''
        if x in self.potions and self.potions[x] > 0:
            self.potions[x] -= 1
            self.current_count -= 1
            return True
        return False
    def get_current_potions(self):
        '''
        Returns the current count of potions.
        Returns:
        int: The current number of potions.
        '''
        return self.current_count