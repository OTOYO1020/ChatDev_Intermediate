'''
Main entry point for the word game application.
'''
def main():
    # Load words from the dictionary file
    file_path = input("Please enter the path to the dictionary file: ")  # Accept user input for the file path
    words = DictionaryLoader.load_dictionary(file_path)
    if not words:
        print("The dictionary is empty or the file does not exist. Please provide a valid dictionary file.")
        return
    # Create a Game instance
    game = Game(words)
    # Determine winners for each starting word
    results = []
    for word in words:
        winner = game.determine_winner(word)
        results.append(f"The winner starting with '{word}' is: {winner}")
    # Output results
    for result in results:
        print(result)
if __name__ == "__main__":
    from game import Game
    from dictionary_loader import DictionaryLoader  # Ensure to import the DictionaryLoader
    main()