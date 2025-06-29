'''
Contains the Player class that represents a player in the game.
'''
class Player:
    def __init__(self, name, symbol):
        """Initialize a player with a name and symbol.
        Parameters:
        name (str): The name of the player.
        symbol (str): The symbol used by the player.
        """
        self.name = name
        self.symbol = symbol