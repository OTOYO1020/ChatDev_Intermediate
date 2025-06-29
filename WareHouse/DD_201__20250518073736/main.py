'''
Main entry point for the game application.
'''
from game import Game
from typing import List
def run():
    H = int(input("Enter number of rows (H): "))
    W = int(input("Enter number of columns (W): "))
    A = []
    print("Enter grid (each row separated by spaces):")
    for _ in range(H):
        row = input().strip().split()  # Changed from split(',') to split()
        if len(row) != W:
            print(f"Error: Each row must have exactly {W} columns.")
            return
        if any(cell not in ('B', 'R') for cell in row):
            print("Error: Grid can only contain 'B' for blue and 'R' for red.")
            return
        A.append(row)
    game = Game(H, W, A)
    game.play_game()
    winner = game.get_winner()
    print(f"The winner is: {winner}")
if __name__ == "__main__":
    run()