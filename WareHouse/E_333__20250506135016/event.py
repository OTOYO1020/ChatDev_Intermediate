'''
Module defining the Event class for tracking events in the potion adventure.
'''
class Event:
    def __init__(self, t, x):
        '''
        Initializes an Event instance.
        Parameters:
        t (int): Event type (1 for adding potion, 2 for removing potion).
        x (int): Potion type.
        '''
        self.t = t  # Event type (1 or 2)
        self.x = x  # Potion type