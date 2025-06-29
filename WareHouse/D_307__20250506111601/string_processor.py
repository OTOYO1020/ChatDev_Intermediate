'''
Utility module for processing strings to remove unmatched parentheses.
'''
class StringProcessor:
    def remove_unmatched_parentheses(self, s):
        '''
        Removes unmatched parentheses from the input string.
        Parameters:
        s (str): The input string to process.
        Returns:
        str: A string containing only the matched lowercase letters and unmatched closing parentheses.
        '''
        result = []
        open_parentheses = 0
        for char in s:
            if char == '(':
                open_parentheses += 1
            elif char == ')':
                if open_parentheses > 0:
                    open_parentheses -= 1
                else:
                    result.append(char)
            elif char.islower():  # Add lowercase letters to result
                result.append(char)
        return ''.join(result)