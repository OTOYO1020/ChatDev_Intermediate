'''
Game class to manage the game logic.
'''
class Game:
    def __init__(self, n):
        self.n = n
        self.declared_integers = set()
        self.game_over = False
        self.next_integer = 1  # Track the next integer to declare
    def declare_integer(self):
        '''
        Declare the next integer that has not been declared yet.
        If all integers have been declared, return None.
        '''
        if self.next_integer <= 2 * self.n + 1:
            declared = self.next_integer
            self.declared_integers.add(declared)
            self.next_integer += 1  # Increment to the next integer
            return declared
        return None  # No more integers to declare
    def check_aoki_declaration(self, aoki_declaration):
        '''
        Check Aoki's declaration and update game state.
        '''
        if aoki_declaration == 0:
            self.game_over = True
            return True
        self.declared_integers.add(aoki_declaration)
        return False