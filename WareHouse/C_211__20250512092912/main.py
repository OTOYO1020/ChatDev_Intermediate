'''
Main application file for counting character combinations.
'''
from counting import count_ways
def main():
    input_string = input("Enter a string: ")
    if not input_string:
        print("Input Error: Please enter a string.")
        return
    result = count_ways(input_string)
    print(f"Number of ways: {result}")
if __name__ == "__main__":
    main()