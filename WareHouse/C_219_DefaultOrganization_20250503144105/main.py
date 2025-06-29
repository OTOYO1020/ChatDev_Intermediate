'''
Main application file for the Name Sorter.
'''
from name_sorter import sort_names  # Updated import to reflect the new function name
def main():
    # Read the permutation string 'X' from standard input
    while True:
        order = input("Enter the custom alphabetical order (26 unique lowercase letters, e.g., 'zyxwvutsrqponmlkjihgfedcba'): ")
        if len(order) == 26 and len(set(order)) == 26 and all(c.islower() for c in order):
            break
        print("Error: The custom order must contain 26 unique lowercase letters. Ensure there are no duplicates and all are lowercase.")
    # Read the integer 'N' from standard input
    while True:
        try:
            N = int(input("Enter the number of citizens (positive integer): "))
            if N > 0:
                break
            else:
                print("Error: Please enter a positive integer for the number of citizens.")
        except ValueError:
            print("Error: Please enter a valid integer for the number of citizens.")
    # Initialize an empty list 'names' to store the names of the citizens
    names = []
    # For each citizen from 1 to N, read the name 'S_i' from standard input
    for _ in range(N):
        while True:
            name = input("Enter the name of the citizen (must contain only lowercase letters and cannot be empty): ").strip()
            if all(c.islower() for c in name) and name != "":
                names.append(name)
                break
            print("Error: Names must contain only lowercase alphabetic characters and cannot be empty. Please try again.")
    # Sort the names using the custom order
    sorted_names = sort_names(order, names)  # Updated function name
    # Output the sorted names
    for name in sorted_names:
        print(name)
if __name__ == "__main__":
    main()