'''
Module to generate dog names based on a base-26-like naming system.
'''
class DogNameGenerator:
    '''
    Class to generate dog names from a given integer.
    '''
    def get_dog_name(self, N: int) -> str:
        '''
        Convert the integer N into a base-26-like naming system where 'a' corresponds to 1 and 'z' corresponds to 26.
        The length of the name is determined by the value of N, with larger values resulting in longer names.
        Parameters:
        N (int): The number to convert into a dog name.
        Returns:
        str: The corresponding dog name.
        Raises:
        ValueError: If N is not in the range [1, 1000000000000001].
        '''
        if N < 1 or N > 1000000000000001:
            raise ValueError("N must be between 1 and 1000000000000001.")
        # Determine the length of the name based on N
        length = 1
        cumulative_count = 0  # Start with 0 for the first length
        while cumulative_count < N:
            cumulative_count += 26 ** length  # Update cumulative count for the current length
            length += 1
        # Adjust N to be the index within the current length
        cumulative_count -= 26 ** (length - 1)  # Get the cumulative count of the previous length
        N -= cumulative_count  # Adjust N to be the index within the current length
        # Now generate the name
        name = []
        while length > 0:
            length -= 1
            N -= 1  # Adjust for 0-indexing
            remainder = N % 26
            name.append(chr(remainder + ord('a')))  # Correctly map to 'a' to 'z'
            N //= 26
        return ''.join(reversed(name))