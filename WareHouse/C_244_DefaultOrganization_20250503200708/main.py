'''
Main module to run the Takahashi vs Aoki game.
'''
from game import Game
def main():
    N = int(input())
    game = Game(N)
    while True:
        takahashi_declaration = game.declare_number()
        print(takahashi_declaration, flush=True)
        aoki_declaration = int(input())
        if game.is_game_over(aoki_declaration):
            break
        game.add_declared_number(takahashi_declaration)
        game.add_declared_number(aoki_declaration)
if __name__ == "__main__":
    main()