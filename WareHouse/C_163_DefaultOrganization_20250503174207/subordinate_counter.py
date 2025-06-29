'''
Module for counting immediate subordinates based on boss relationships.
'''
class SubordinateCounter:
    def __init__(self, n):
        '''
        Initializes the SubordinateCounter with the number of members.
        Parameters:
        n (int): The total number of members in the company.
        '''
        self.n = n
        self.subordinates_count = [0] * (n + 1)  # 1-based indexing
    def count_subordinates(self, bosses):
        '''
        Counts the immediate subordinates for each member based on the boss relationships.
        Parameters:
        bosses (list): A list of integers representing the bosses of members 2 to N.
        Returns:
        list: A list containing the count of immediate subordinates for each member from 1 to N.
        '''
        for i in range(len(bosses)):
            boss = bosses[i]
            self.subordinates_count[boss] += 1  # Increment the count for the boss of member i+2
        return self.subordinates_count[1:]  # Return counts for members 1 to N only