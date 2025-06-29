'''
Main entry point for the Card Flipper application.
'''
from card import Card
from input_validator import InputValidator
def read_card_values(num_cards):
    cards = []
    for i in range(num_cards):
        while True:
            try:
                # Read both front and back values in one line
                values = input(f"Enter front and back values for card {i + 1} (separated by space): ").split()
                if len(values) != 2:
                    raise ValueError("Please enter exactly two integers.")
                front, back = map(int, values)
                cards.append(Card(front, back))
                break  # Break the loop if input is valid
            except ValueError as e:
                print(f"Invalid input. {e}")
    return cards
def main():
    input_validator = InputValidator()
    try:
        num_cards = input_validator.validate_integer(input("Enter number of cards: "))
        if num_cards <= 0:
            print("Number of cards must be a positive integer.")
            return  # Exit the program if the input is invalid
        cards = read_card_values(num_cards)  # Use the new method for reading card values
        count = 1
        MOD = 998244353
        for i in range(num_cards - 1):
            a1, b1 = cards[i].front, cards[i].back
            a2, b2 = cards[i + 1].front, cards[i + 1].back
            # Correctly calculate the number of valid configurations
            valid_configurations = 0
            if a1 == a2:
                valid_configurations += 1
            if a1 == b2:
                valid_configurations += 1
            if b1 == a2:
                valid_configurations += 1
            if b1 == b2:
                valid_configurations += 1
            # If no valid configurations, set count to 0
            if valid_configurations == 0:
                count = 0
                break  # No need to check further if there are no valid configurations
            count = (count * valid_configurations) % MOD
        print(f"Total valid flips: {count}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()