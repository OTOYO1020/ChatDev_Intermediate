'''
Module containing the sorting logic for the LexicoSorter application.
'''
class LexicoSorter:
    def sort(self, input_string):
        # Convert the input string into a list of characters
        char_list = list(input_string)
        # Sort the list of characters in lexicographical order
        char_list.sort()
        # Join the sorted list back into a string and return it
        return ''.join(char_list)