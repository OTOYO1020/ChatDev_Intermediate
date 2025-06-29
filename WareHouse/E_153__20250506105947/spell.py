'''
Defines the Spell class representing a spell's damage and cost.
'''
class Spell:
    '''
    Class representing a spell with damage and cost.
    '''
    def __init__(self, damage, cost):
        '''
        Initializes the spell with damage and cost.
        '''
        self.damage = damage
        self.cost = cost