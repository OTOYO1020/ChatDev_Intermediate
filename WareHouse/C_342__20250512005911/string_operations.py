'''
Module for performing string operations based on user-defined replacements.
'''
from typing import List, Tuple
class StringOperations:
    def __init__(self, S: str, operations: List[Tuple[str, str]]):
        '''
        Initialize the StringOperations class with a string and a list of operations.
        '''
        self.S = S
        self.operations = operations
    def perform_operations(self) -> str:
        '''
        Perform the string operations by replacing characters in S based on the operations list.
        This method ensures that replacements do not interfere with each other by applying all operations sequentially.
        '''
        modified_string = self.S  # Start with the original string
        for original_char, replacement_char in self.operations:
            modified_string = modified_string.replace(original_char, replacement_char)  # Replace in the current modified string
        return modified_string