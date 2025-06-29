'''
Contains the Game class that manages the game logic.
'''
class Game:
    def __init__(self, dictionary):
        self.dictionary = dictionary
    def can_follow(self, word1, word2):
        # Check if word2 can follow word1 based on the last three characters of word1
        return word2.lower().startswith(word1[-3:].lower())
    def determine_winner(self, start_word):
        if start_word not in self.dictionary:
            return "Player 2"  # If the starting word is not in the dictionary, Player 1 loses immediately
        current_word = start_word
        used_words = set()
        used_words.add(current_word)  # Mark the starting word as used
        turn = 0  # 0 for Player 1, 1 for Player 2
        total_words = len(self.dictionary)
        while True:
            found_next_word = False
            for word in self.dictionary:
                if word not in used_words and self.can_follow(current_word, word):
                    used_words.add(word)
                    current_word = word
                    found_next_word = True
                    break
            if not found_next_word:
                # If no word can be said, the current player loses
                return "Player 2" if turn == 0 else "Player 1"
            # Check if all words have been used
            if len(used_words) == total_words:
                return "Draw"  # All words used, declare a draw
            # Switch players
            turn = 1 - turn  # Toggle between 0 and 1