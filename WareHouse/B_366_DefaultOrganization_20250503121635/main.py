'''
Main application file for the string processing application.
'''
import sys
from string_processor import StringProcessor
def main():
    try:
        num_strings = int(input("Enter the number of strings: "))
        strings = [input(f"Enter string {i + 1}: ") for i in range(num_strings)]
        processor = StringProcessor(strings)
        results = processor.process_strings()
        print("Results:")
        for line in results:
            print(line)
    except ValueError:
        print("Error: Please enter a valid integer for the number of strings.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()