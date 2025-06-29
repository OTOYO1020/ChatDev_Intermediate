'''
Contains the game logic functions for the Takahashi game.
'''
def can_play(word, words):
    last_three_chars = word[-3:]
    valid_words = [w for w in words if w.startswith(last_three_chars) and w != word]
    return valid_words
def play_game(current_word, words, visited):
    visited.add(current_word)
    next_words = can_play(current_word, words)
    # If no next words, the current player loses
    if not next_words:
        return "Aoki"  # If no next words, Takahashi cannot play, so Aoki wins
    for next_word in next_words:
        if next_word not in visited:
            result = play_game(next_word, words, visited)
            if result == "Aoki":
                return "Takahashi"  # If Aoki wins, then Takahashi loses this round
    return "Aoki"  # If all paths lead to Aoki winning, then Aoki wins