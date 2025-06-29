'''
Module to manage string operations and unique character counting.
'''
class StringManager:
    def __init__(self, initial_string):
        self.string = list(initial_string)
        self.char_count = {}
        self.unique_chars = set(initial_string)
        for char in initial_string:
            self.char_count[char] = self.char_count.get(char, 0) + 1
    def update_character(self, index, new_char):
        # Check if the new character is different from the old character
        if self.string[index] == new_char:
            return  # No change needed, exit the method
        old_char = self.string[index]
        self.string[index] = new_char
        # Update character counts for old_char
        self.char_count[old_char] -= 1
        if self.char_count[old_char] == 0:
            del self.char_count[old_char]
            self.unique_chars.discard(old_char)
        # Update character counts for new_char
        self.char_count[new_char] = self.char_count.get(new_char, 0) + 1
        self.unique_chars.add(new_char)
    def get_unique_count(self, start, end):
        '''
        Returns the number of unique characters in the substring from start to end.
        This method should utilize the existing character count to determine uniqueness.
        '''
        seen_chars = set(self.string[start:end])  # Get unique characters in the substring
        unique_count = sum(1 for char in seen_chars if char in self.char_count)
        return unique_count