'''
Module for processing strings into vertical format.
'''
class StringProcessor:
    def __init__(self, strings):
        self.strings = strings
    def process_strings(self):
        max_length = max(len(s) for s in self.strings)
        result = ['' for _ in range(max_length)]
        # Fill the result list with characters in vertical alignment
        for i in range(len(self.strings)):  # Iterate over the index of strings
            s = self.strings[i]  # Use the original order of strings
            for j in range(len(s)):
                result[max_length - 1 - j] += s[j]  # Place character in the correct vertical position
        # Fill remaining positions with '*' if the string is shorter
        for i in range(max_length):
            if len(result[i]) < len(self.strings):
                result[i] += '*' * (len(self.strings) - len(result[i]))  # Fill with '*' to match N
        # Ensure no trailing '*' characters
        for i in range(len(result)):
            result[i] = result[i].rstrip('*')  # Trim trailing '*' characters
        return result