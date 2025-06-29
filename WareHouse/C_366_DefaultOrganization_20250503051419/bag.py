'''
Bag class to manage integers and track unique integers.
'''
class Bag:
    def __init__(self):
        """Initialize an empty bag and a counter for unique integers."""
        self.bag = {}
        self.unique_count = 0
    def add(self, x):
        """Add an integer x to the bag. If x is already present, increment its count."""
        if x in self.bag:
            self.bag[x] += 1
        else:
            self.bag[x] = 1
            self.unique_count += 1
    def remove(self, x):
        """Remove an integer x from the bag. Raise KeyError if x is not found."""
        if x in self.bag:
            self.bag[x] -= 1
            if self.bag[x] == 0:
                del self.bag[x]
                self.unique_count -= 1
        else:
            raise KeyError(f"{x} not found in the bag.")
    def count_unique(self):
        """Return the count of unique integers in the bag."""
        return self.unique_count