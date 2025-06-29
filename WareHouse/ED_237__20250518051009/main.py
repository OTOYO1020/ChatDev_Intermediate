'''
Main entry point for the happiness calculation application.
'''
from input_parser import parse_input
from happiness import max_happiness  # Importing the max_happiness function
def main():
    input_data = input("Enter the input data:\n")
    try:
        N, M, H, slopes = parse_input(input_data)
        max_hap = max_happiness(N, M, H, slopes)  # Call the function from happiness.py
        print(f"Maximum Happiness: {max_hap}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()