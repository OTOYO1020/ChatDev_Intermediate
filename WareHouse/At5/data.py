'''
This file contains the Data class.
'''
from utils import function1, function2
class Data:
    def __init__(self):
        self.A = []
        self.B = []
        self.matches = 0  # New instance variable to store the number of matches
    def load_data(self, filename):
        """
        Load the data from a file.
        Args:
            filename (str): The name of the file to load the data from.
        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.A = list(map(int, lines[0].split()))
                self.B = list(map(int, lines[1].split()))
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
    def process_data(self):
        """
        Process the loaded data and find the number of matches.
        Returns:
            int: The number of matches found.
        """
        counter = 0
        for i in range(len(self.A) - len(self.B) + 1):
            if self.A[i:i+len(self.B)] == self.B:
                counter += 1
        self.matches = counter  # Store the result in the instance variable
        return counter
    def save_data(self, filename):
        """
        Save the result to a file.
        Args:
            filename (str): The name of the file to save the result to.
        """
        with open(filename, 'w') as file:
            file.write(f"Number of matches: {self.matches}")  # Use the instance variable instead of calling process_data again