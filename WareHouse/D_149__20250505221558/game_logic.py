'''
Contains the logic for calculating the maximum score in the game.
'''
class GameLogic:
    def __init__(self, R, S, P):
        self.R = R  # Score for Rock
        self.S = S  # Score for Scissors
        self.P = P  # Score for Paper
    def calculate_max_score(self, N, K, T):
        max_score = 0
        last_moves = []
        for i in range(N):
            machine_move = T[i]
            player_move = None
            # Determine the optimal move based on the machine's move
            if machine_move == 'R':
                player_move = 'P'  # Paper beats Rock
            elif machine_move == 'P':
                player_move = 'S'  # Scissors beats Paper
            elif machine_move == 'S':
                player_move = 'R'  # Rock beats Scissors
            # Check if the player move is valid
            if i >= K and last_moves[i - K] == player_move:
                # If the same move as (i-K)-th round, choose a different one
                alternatives = {'R', 'P', 'S'} - {last_moves[i - K]}  # Exclude the last K move
                if alternatives:
                    # Prioritize the best move against the machine's current move
                    if machine_move == 'R':
                        player_move = 'P' if 'P' in alternatives else ('S' if 'S' in alternatives else 'R')
                    elif machine_move == 'P':
                        player_move = 'S' if 'S' in alternatives else ('R' if 'R' in alternatives else 'P')
                    elif machine_move == 'S':
                        player_move = 'R' if 'R' in alternatives else ('P' if 'P' in alternatives else 'S')
                else:
                    # If no alternatives are available, revert to the last move (if K is not yet reached)
                    player_move = last_moves[-1] if last_moves else 'R'  # Default to 'R' if no moves exist
            # Update max_score based on the chosen move
            if player_move == 'R' and machine_move == 'S':
                max_score += self.R
            elif player_move == 'S' and machine_move == 'P':
                max_score += self.S
            elif player_move == 'P' and machine_move == 'R':
                max_score += self.P
            last_moves.append(player_move)
            if len(last_moves) > K:
                last_moves.pop(0)  # Keep only the last K moves
        return max_score