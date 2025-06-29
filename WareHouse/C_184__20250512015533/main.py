'''
Main entry point of the application that handles user interactions through standard input and output.
'''
from move_calculator import MoveCalculator
def main():
    r1, c1, r2, c2 = map(int, input("Enter starting position (r1, c1) and target position (r2, c2) separated by spaces: ").split())
    calculator = MoveCalculator()
    moves = calculator.min_moves(r1, c1, r2, c2)
    print(f"Minimum Moves: {moves}")
if __name__ == "__main__":
    main()