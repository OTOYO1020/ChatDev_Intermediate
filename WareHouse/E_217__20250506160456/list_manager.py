'''
Module for managing a list of integers with various operations.
'''
from collections import deque
class ListManager:
    def __init__(self):
        self.A = deque()  # Use deque for efficient pop from the front
    def add_to_list(self, x):
        '''
        Append an integer x to the end of the list A.
        '''
        self.A.append(x)
    def remove_first(self):
        '''
        Remove and return the first element from the list A.
        Raises IndexError if the list is empty.
        '''
        if not self.is_empty():
            return self.A.popleft()  # Use popleft for O(1) complexity
        raise IndexError("remove_first from empty list")
    def sort_list(self):
        '''
        Sort the list A in ascending order.
        '''
        self.A = deque(sorted(self.A))  # Sort and convert back to deque
    def get_first(self):
        '''
        Return the first element of the list A.
        Raises IndexError if the list is empty.
        '''
        if not self.is_empty():
            return self.A[0]
        raise IndexError("get_first from empty list")
    def is_empty(self):
        '''
        Check if the list A is empty.
        Returns True if empty, False otherwise.
        '''
        return len(self.A) == 0