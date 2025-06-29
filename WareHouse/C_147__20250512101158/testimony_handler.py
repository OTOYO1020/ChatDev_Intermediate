'''
Module to handle testimonies and evaluate the maximum number of honest people.
'''
from typing import List, Tuple
class TestimonyHandler:
    def __init__(self, N: int, testimonies: List[List[Tuple[int, int]]]):
        '''
        Initialize the TestimonyHandler with the number of people and their testimonies.
        Parameters:
        N (int): The number of people.
        testimonies (List[List[Tuple[int, int]]]): The testimonies for each person.
        '''
        self.N = N
        self.testimonies = testimonies
    def max_honest_people(self) -> int:
        '''
        Evaluate the maximum number of honest people based on the testimonies.
        Returns:
        int: The maximum count of honest people found.
        '''
        max_count = 0
        # Iterate through all combinations of honesty using bitmasking
        for i in range(1 << self.N):
            honest_set = [j for j in range(self.N) if (i & (1 << j)) > 0]
            if self.is_valid_combination(honest_set):
                max_count = max(max_count, len(honest_set))
        return max_count
    def is_valid_combination(self, honest_set: List[int]) -> bool:
        '''
        Check if the current combination of honest people is valid.
        Parameters:
        honest_set (List[int]): The list of honest people in the current combination.
        Returns:
        bool: True if the combination is valid, False otherwise.
        '''
        for person in range(self.N):
            if person in honest_set:  # If the person is honest
                for testimony in self.testimonies[person]:
                    # Check if the receiver of the testimony is honest
                    if testimony[1] not in honest_set:  # Testimony contradicts
                        return False
            else:  # If the person is not honest
                for testimony in self.testimonies[person]:
                    # Check if the receiver of the testimony is honest
                    if testimony[1] in honest_set:  # Honest person contradicts
                        return False
        return True