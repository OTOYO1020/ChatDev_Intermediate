'''
Main entry point of the application that handles user interactions and calculates happiness based on handshakes.
'''
import random
from guest import Guest
def main():
    try:
        n = int(input("Number of Guests (N): "))
        m = int(input("Number of Handshakes (M): "))
        powers = list(map(int, input("Enter Powers (space-separated): ").split()))
        if len(powers) != n:
            raise ValueError("Number of powers must match the number of guests.")
        guests = [Guest(power) for power in powers]
        happiness = 0
        handshake_set = set()
        # Check if M exceeds the maximum number of unique handshakes possible
        max_handshakes = n * (n - 1) // 2
        if m > max_handshakes:
            raise ValueError(f"Number of handshakes M cannot exceed the maximum unique pairs: {max_handshakes}.")
        # Generate unique pairs randomly
        while len(handshake_set) < m:
            x = random.randint(1, n)
            y = random.randint(1, n)
            if x != y:  # Ensure x and y are not the same
                pair = (min(x, y), max(x, y))  # Store pairs in a consistent order
                if pair not in handshake_set:
                    handshake_set.add(pair)
                    happiness += guests[x - 1].power + guests[y - 1].power
        print(f"Total Happiness: {happiness}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()