'''
Main entry point for the card game application.
'''
from card_game import CardGame
def main():
    try:
        N = int(input("Enter the number of cards: "))
        if N < 1 or N > 18:
            raise ValueError("N must be between 1 and 18.")
        A = []
        B = []
        print("Enter the card pairs (A_i B_i):")
        for _ in range(N):
            a, b = map(int, input().split())
            A.append(a)
            B.append(b)
        game = CardGame(A, B)
        winner = game.play_game(0)
        print(f"The winner is: {winner}")
    except ValueError as e:
        print(f"Invalid input: {e}")
if __name__ == "__main__":
    main()