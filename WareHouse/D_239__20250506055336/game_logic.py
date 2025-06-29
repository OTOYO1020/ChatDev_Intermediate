'''
Contains the game logic and prime checking function.
'''
def is_prime(n):
    '''
    Check if a number n is prime.
    '''
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
class GameLogic:
    '''
    Class to handle the game logic.
    '''
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.winning_moves = []
    def calculate_winning_moves(self):
        '''
        Calculate all possible sums of integers chosen by Takahashi and Aoki.
        '''
        for t in range(self.A, self.B + 1):
            for a in range(self.C, self.D + 1):
                self.winning_moves.append(t + a)
    def determine_winner(self):
        '''
        Determine the winner based on the winning moves.
        '''
        aoki_wins = sum(1 for s in self.winning_moves if is_prime(s))
        takahashi_wins = len(self.winning_moves) - aoki_wins
        if aoki_wins > takahashi_wins:  # Aoki wins if he has more wins
            return "Aoki"
        else:  # Takahashi wins if he has more or equal wins
            return "Takahashi"