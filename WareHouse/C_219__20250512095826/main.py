'''
Main application file for the Name Sorter.
'''
import sys
from sorter import sort_names
def main():
    '''
    Main function to handle input and output for sorting names.
    '''
    if len(sys.argv) < 3:
        print("Usage: python main.py <new_order> <name1,name2,...>")
        return
    new_order = sys.argv[1]
    names_input = sys.argv[2]
    names = [name.strip() for name in names_input.split(',')]
    try:
        sorted_names = sort_names(new_order, names)
        print("Sorted Names:")
        for name in sorted_names:
            print(name)
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()