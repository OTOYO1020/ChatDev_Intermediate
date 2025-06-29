'''
Main application file for the honesty evaluation program.
'''
from testimony_handler import TestimonyHandler
from typing import List, Tuple
def main():
    try:
        n = int(input("Enter number of people: "))
        testimonies = [[] for _ in range(n)]  # Initialize testimonies for each person
        print("Enter testimonies (format: giver receiver, each on a new line, end with an empty line):")
        while True:
            testimonies_input = input("Enter testimony (format: giver receiver, or press Enter to finish): ").strip()
            if not testimonies_input:  # Break on empty line
                break
            try:
                testimony_giver, testimony_receiver = map(int, testimonies_input.split())
                # Validate indices and ensure giver and receiver are not the same
                if testimony_giver < 0 or testimony_giver >= n or testimony_receiver < 0 or testimony_receiver >= n or testimony_giver == testimony_receiver:
                    raise ValueError(f"Testimony indices must be between 0 and {n-1}, and cannot be the same.")
                # Store the testimony as a tuple (giver, receiver)
                testimonies[testimony_giver].append((testimony_giver, testimony_receiver))  # Store the testimony as (giver, receiver)
            except ValueError as ve:
                print(f"Input Error: {ve}")
        handler = TestimonyHandler(n, testimonies)
        max_honest = handler.max_honest_people()
        print(f"Max Honest People: {max_honest}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()