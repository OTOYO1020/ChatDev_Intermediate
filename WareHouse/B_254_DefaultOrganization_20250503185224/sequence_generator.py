'''
Module for generating integer sequences based on the input integer N.
'''
class SequenceGenerator:
    def __init__(self, N):
        self.N = N
        self.sequences = []  # Start with an empty list
    def generate(self):
        for i in range(self.N):  # Loop from 0 to N-1
            row = [0] * (i + 1)  # Initialize the row with zeros
            for j in range(i + 1):
                if j == 0 or j == i:
                    row[j] = 1  # Set the first and last elements to 1
                else:
                    # Ensure that we only access previous rows when i > 0
                    if i > 0:
                        row[j] = self.sequences[i - 1][j - 1] + self.sequences[i - 1][j]  # Calculate the value based on previous row
            self.sequences.append(row)  # Append the constructed row to sequences
        return self.sequences