'''
Main entry point for the die throwing game application.
'''
from game_logic import simulate_die_throw, expected_score
def main():
    '''
    Main function to run the die throwing game.
    Prompts the user for the number of turns and displays the expected score.
    '''
    try:
        N = int(input("Enter number of turns: "))
        if N < 1:
            raise ValueError("Number of turns must be at least 1.")
        score = expected_score(N)
        print(f"Expected Score: {score:.2f}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()