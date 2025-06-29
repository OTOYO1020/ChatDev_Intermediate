'''
Module for managing player scores in the game.
'''
class ScoreManager:
    '''
    Class to manage scores of players.
    '''
    def __init__(self, num_players, initial_points):
        '''
        Initializes the scores based on the number of players and initial points.
        '''
        self.scores = [initial_points] * num_players
    def update_scores(self, correct_answers):
        '''
        Updates the scores based on the correct answers.
        '''
        # Create a set of players who answered correctly
        correct_players = set(answer - 1 for answer in correct_answers)
        # Decrement scores for all players who did not answer correctly
        for i in range(len(self.scores)):
            if i not in correct_players:  # If the player did not answer correctly
                self.scores[i] -= 1  # Decrement score by 1 for each incorrect player
    def get_survival_status(self):
        '''
        Returns the survival status of each player.
        '''
        return [1 if score > 0 else 0 for score in self.scores]