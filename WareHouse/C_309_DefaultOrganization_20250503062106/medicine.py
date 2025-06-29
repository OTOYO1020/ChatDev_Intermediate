'''
Module containing the Medicine class.
'''
class Medicine:
    def __init__(self, days, pills):
        '''
        Initializes a Medicine instance with the number of days and pills.
        Parameters:
        days (int): The number of days the medicine is prescribed.
        pills (int): The number of pills taken each day.
        '''
        self.days = days
        self.pills = pills