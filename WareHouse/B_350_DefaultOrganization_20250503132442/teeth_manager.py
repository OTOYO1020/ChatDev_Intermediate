'''
TeethManager class to manage the state of teeth and handle treatments.
'''
class TeethManager:
    def __init__(self, n):
        self.teeth = [True] * n  # Initialize all teeth as present
    def treat(self, index):
        '''
        Treat the specified tooth by toggling its state.
        If a tooth is present, it will be removed; if absent, it will grow.
        '''
        if self.teeth[index]:
            self.teeth[index] = False  # Remove the tooth
        else:
            self.teeth[index] = True  # Grow a tooth
    def count_teeth(self):
        '''
        Count the number of teeth present (True values).
        Returns the count of True values in the teeth list.
        '''
        return sum(self.teeth)  # Count the number of True values