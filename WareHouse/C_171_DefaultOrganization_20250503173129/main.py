'''
Main entry point for the Dog Name Generator application.
'''
import sys
from dog_name_generator import DogNameGenerator
def main():
    try:
        n = int(input("Enter a number (1 to 1000000000000001): "))
        dog_name_generator = DogNameGenerator()
        dog_name = dog_name_generator.generate_name(n)
        print(f"Dog Name: {dog_name}")
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()