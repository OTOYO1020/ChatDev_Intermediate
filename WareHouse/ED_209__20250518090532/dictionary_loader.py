'''
Handles loading the Takahashi Dictionary from a file.
'''
import os
class DictionaryLoader:
    @staticmethod
    def load_dictionary(file_path):
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return []
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]