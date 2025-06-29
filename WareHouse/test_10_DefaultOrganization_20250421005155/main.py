'''
Main file for the Number Guessing Game application using standard input and output.
This game allows users to guess a randomly generated number between 1 and 100.
'''
import random
def start_game():
    '''Starts a new game by generating a target number and initializing guess count.'''
    target_number = random.randint(1, 100)
    guess_count = 0
    max_attempts = 10  # Set a maximum number of attempts
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100:")
    while guess_count < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            guess_count += 1
            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {guess_count} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")
    if guess_count == max_attempts:
        print(f"Sorry, you've used all your attempts. The correct number was {target_number}.")
def main():
    '''Main function to run the game.'''
    while True:
        start_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    main()