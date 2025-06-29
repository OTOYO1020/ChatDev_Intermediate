'''
Main file to run the Takahashi vs Aoki game application.
'''
import sys
from game_logic import determine_winner
def validate_input(A: int, B: int, C: int, D: int) -> bool:
    """Validate the input constraints."""
    if not (1 <= A <= 100):
        print("Input Error: A must be between 1 and 100.")
        return False
    if not (A <= B <= 100):
        print("Input Error: B must be greater than or equal to A and less than or equal to 100.")
        return False
    if not (1 <= C <= 100):
        print("Input Error: C must be between 1 and 100.")
        return False
    if not (C <= D <= 100):
        print("Input Error: D must be greater than or equal to C and less than or equal to 100.")
        return False
    return True
def main():
    try:
        # Check if input is from a file or standard input
        if len(sys.argv) > 1:
            with open(sys.argv[1], 'r') as file:
                A, B, C, D = map(int, file.readline().strip().split())
        else:
            A, B, C, D = map(int, input("Enter A, B, C, D (space-separated): ").split())
        # Validate input constraints
        if not validate_input(A, B, C, D):
            return
        winner = determine_winner(A, B, C, D)
        print(f"The winner is: {winner}")
    except ValueError:
        print("Input Error: Please enter valid integers.")
    except FileNotFoundError:
        print("Input Error: The specified file was not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()