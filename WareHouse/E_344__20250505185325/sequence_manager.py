'''
Manages the sequence of integers, allowing insertion and removal of elements.
'''
class SequenceManager:
    def __init__(self, sequence):
        self.sequence = sequence
    def insert_after(self, x, y):
        '''
        Inserts element y immediately after element x in the sequence.
        Raises ValueError if x is not found or if y already exists in the sequence.
        '''
        if x not in self.sequence:
            raise ValueError(f"Element {x} not found in the sequence.")
        if y in self.sequence:
            print(f"Element {y} already exists in the sequence; insertion skipped.")
            return
        index = self.sequence.index(x)
        self.sequence.insert(index + 1, y)
        # Check for duplicates after insertion
        if len(set(self.sequence)) != len(self.sequence):
            self.sequence.remove(y)  # Revert the insertion
            raise ValueError(f"Insertion of {y} would create duplicates.")
    def remove(self, x):
        '''
        Removes element x from the sequence.
        Raises ValueError if x is not found or if removing x would leave the sequence empty.
        '''
        if x not in self.sequence:
            raise ValueError(f"Element {x} not found in the sequence.")
        if len(self.sequence) <= 1:
            raise ValueError("Cannot remove element; sequence would become empty.")
        self.sequence.remove(x)
        # Ensure the sequence remains distinct after removal
        if len(self.sequence) != len(set(self.sequence)):
            self.sequence.append(x)  # Revert the removal
            raise ValueError(f"Removal of {x} would create duplicates.")
    def get_sequence(self):
        '''
        Returns the current state of the sequence.
        '''
        return self.sequence