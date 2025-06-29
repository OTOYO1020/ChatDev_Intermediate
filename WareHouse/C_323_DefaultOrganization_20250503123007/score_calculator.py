'''
Utility class to handle score calculations for players based on their solved problems.
'''
class ScoreCalculator:
    def __init__(self, N, M, scores, solutions):
        self.N = N
        self.M = M
        self.scores = scores
        self.solutions = solutions
        # Validate scores
        for score in scores:
            if score < 500 or score > 2500 or score % 100 != 0:
                raise ValueError("Scores must be multiples of 100 and in the range of 500 to 2500.")
    def calculate_min_problems_to_solve(self):
        total_scores = [0] * self.N
        # Calculate total scores for each player
        for i in range(self.N):
            # Calculate the total score for player i
            total_scores[i] = self.calculate_player_score(i)
        results = []
        for i in range(self.N):
            # Determine the maximum score among all other players
            max_other_score = max(total_scores[j] for j in range(self.N) if j != i)
            # Check if the current player's score is already greater than the maximum score of others
            if total_scores[i] > max_other_score:
                results.append(0)  # No additional problems needed
                continue  # Skip to the next player
            # Create a list of unsolved problems for player i
            unsolved_scores = [self.scores[j] for j in range(self.M) if self.solutions[i][j] == 'x']
            unsolved_scores.sort(reverse=True)  # Sort unsolved scores in descending order
            cumulative_score = total_scores[i]
            problems_solved = 0
            # Iterate through the sorted list of unsolved problems
            for score in unsolved_scores:
                cumulative_score += score
                problems_solved += 1
                # Check if the cumulative score exceeds the maximum score of other players
                if cumulative_score > max_other_score:
                    break
            results.append(problems_solved)  # Store the result for player i
        return results
    def calculate_player_score(self, player_index):
        '''
        Calculate the total score for a specific player based on solved problems and bonus.
        The bonus is equal to the player's index (1-based), hence we add (player_index + 1).
        Note: player_index is 0-based in the array context but treated as 1-based for scoring.
        This means for player 0 (1st player), the bonus is 1, for player 1 (2nd player), the bonus is 2, and so on.
        '''
        return sum(self.scores[j] for j in range(self.M) if self.solutions[player_index][j] == 'o') + (player_index + 1)