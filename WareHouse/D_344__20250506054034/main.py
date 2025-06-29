'''
Main application file for the String Formation application.
'''
from string_utils import calculate_min_cost
def main():
    try:
        N = int(input("Enter the number of bags: "))
        if N <= 0:
            raise ValueError("Number of bags must be a positive integer.")
        bags = []
        for i in range(N):
            while True:
                try:
                    A_i = int(input(f"How many strings would you like to add to bag {i + 1}? "))
                    if A_i < 0:
                        raise ValueError("Number of strings in a bag cannot be negative.")
                    break  # Exit the loop if input is valid
                except ValueError:
                    print("Please enter a valid integer for the number of strings.")
            bag_input = input(f"Enter {A_i} strings for bag {i + 1} (space separated): ")
            bags.append(bag_input.split())
        target_string = input("Enter the target string: ")
        min_cost = calculate_min_cost(target_string, bags)
        print(f"Minimum Cost: {min_cost}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()