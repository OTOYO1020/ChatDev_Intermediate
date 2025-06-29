'''
Main application file to run the Dog Name Generator.
'''
from dog_name_generator import DogNameGenerator
def main():
    '''
    Main function to read input and generate the dog name.
    '''
    generator = DogNameGenerator()
    try:
        number = int(input("Enter a number: "))
        dog_name = generator.get_dog_name(number)
        print(f"Dog Name: {dog_name}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()