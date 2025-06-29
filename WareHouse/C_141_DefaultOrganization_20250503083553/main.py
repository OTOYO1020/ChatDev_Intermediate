'''
Main application file for the game.
'''
from score_manager import ScoreManager
def main():
    '''
    Starts the game by reading input values and processing scores.
    '''
    try:
        # Read input values
        n, k, q = map(int, input("Enter number of players (N), initial points (K), and number of correct answers (Q): ").split())
        # Initialize ScoreManager with initial scores
        score_manager = ScoreManager(n, k)
        if q > 0:
            answers = list(map(int, input("Enter correct answers (space-separated): ").split()))
            # Validate answers
            if len(answers) != q:
                raise ValueError("Number of answers must match Q.")
            if any(answer < 1 or answer > n for answer in answers):
                raise ValueError("All answers must be between 1 and N (inclusive).")
            score_manager.update_scores(answers)
        # Get survival status
        survival_status = score_manager.get_survival_status()
        # Display results
        print(' '.join(map(str, survival_status)))
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()