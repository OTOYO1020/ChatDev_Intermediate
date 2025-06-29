'''
Module for managing a bag of integers with add, remove, and count functionalities.
'''
class Bag:
    def __init__(self):
        self.data = {}
    def add(self, x):
        if x in self.data:
            self.data[x] += 1
        else:
            self.data[x] = 1
    def remove(self, x):
        if x in self.data:
            self.data[x] -= 1
            if self.data[x] == 0:
                del self.data[x]
            return True
        else:
            raise ValueError(f"{x} not found in the bag, cannot remove.")  # Raise an exception for better feedback
    def count(self):
        return len(self.data)