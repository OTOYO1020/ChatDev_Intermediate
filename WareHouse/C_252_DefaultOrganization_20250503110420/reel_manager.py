'''
Module for managing reels and calculating minimum time for matching symbols.
'''
class ReelManager:
    '''
    Class to manage the reels and their symbols.
    '''
    def __init__(self, num_reels):
        self.num_reels = num_reels
        self.reel_symbols = [[] for _ in range(num_reels)]
    def add_symbols(self, symbols):
        '''
        Adds symbols for each reel.
        '''
        for i in range(self.num_reels):
            symbol = symbols[i].strip()
            if not all(char.isdigit() for char in symbol):
                raise ValueError(f"Invalid characters found in reel {i}. Only digits are allowed.")
            self.reel_symbols[i] = list(symbol)
    def calculate_min_time(self):
        '''
        Calculates the minimum time for all reels to display the same character.
        '''
        symbol_count = [{} for _ in range(10)]  # Initialize a list of dictionaries for each time t
        for t in range(10):
            for i in range(self.num_reels):
                char = self.reel_symbols[i][t]
                if char.isdigit():  # Ensure we only consider characters '0' to '9'
                    if char not in symbol_count[t]:
                        symbol_count[t][char] = 0
                    symbol_count[t][char] += 1
            # Check if any character appears on all reels
            found = False
            for char in symbol_count[t]:
                if symbol_count[t][char] == self.num_reels:
                    return t
                    found = True
            if not found and t == 9:  # If we reach the last time without finding a match
                return None  # Indicate impossibility after checking all times
        return None