'''
Handles input operations for the Takahashi game.
'''
def load_words(N):
    words = []
    print(f"Please enter {N} words (each between 3 and 8 characters):")
    for _ in range(N):
        word = input().strip()
        while not (3 <= len(word) <= 8):
            print("Invalid word length. Please enter a word between 3 and 8 characters:")
            word = input().strip()
        words.append(word)
    return words