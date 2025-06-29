'''
Contains the logic for generating dog names based on input integer N.
'''
from utils import validate_input, index_to_name
class DogNameGenerator:
    def generate_name(self, n):
        if not validate_input(n):
            raise ValueError("Input must be in the range 1 to 1000000000000001.")
        length = 1
        cumulative_count = 0
        # Calculate the length of the name based on cumulative counts
        while True:
            count_of_length = 26 ** length
            if cumulative_count + count_of_length >= n:  # Corrected condition
                break
            cumulative_count += count_of_length
            length += 1
        # Calculate the index relative to the starting point of that length category
        index = n - cumulative_count - 1  # Zero-based index
        return index_to_name(index)