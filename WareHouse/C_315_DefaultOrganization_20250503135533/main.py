'''
Main file to run the Ice Cream Satisfaction application.
This program reads the number of ice cream cups, their flavors, and deliciousness values,
calculates the maximum satisfaction based on the given criteria, and outputs the result.
'''
def main():
    N = int(input("Enter the number of ice cream cups: "))
    if N < 2:
        print("At least two ice cream cups are required to calculate satisfaction.")
        return  # Exit the program early if N is less than 2
    flavors = []
    deliciousness = []
    for i in range(N):
        flavor = input(f"Enter flavor for cup {i + 1}: ")
        while not flavor.strip():  # Check for empty input
            print("Flavor cannot be empty. Please enter a valid flavor.")
            flavor = input(f"Enter flavor for cup {i + 1}: ")
        while True:
            try:
                deliciousness_value = int(input(f"Enter deliciousness for cup {i + 1}: "))
                if deliciousness_value < 0:
                    print("Deliciousness cannot be negative. Please enter a valid value.")
                    continue
                break  # Exit the loop if input is valid
            except ValueError:
                print("Please enter a valid integer for deliciousness.")
        flavors.append(flavor)
        deliciousness.append(deliciousness_value)
    max_satisfaction = float('-inf')  # Initialize to negative infinity
    valid_pair_found = False  # Flag to track if any valid pair is found
    # Evaluate all pairs of cups (i, j) where i < j
    for i in range(N):
        for j in range(i + 1, N):
            valid_pair_found = True  # A valid pair is being evaluated
            if flavors[i] != flavors[j]:
                satisfaction = deliciousness[i] + deliciousness[j]
            else:
                satisfaction = deliciousness[i] + (deliciousness[j] / 2)
            # Update max_satisfaction if the calculated satisfaction is greater
            if satisfaction > max_satisfaction:
                max_satisfaction = satisfaction
    if not valid_pair_found or max_satisfaction < 0:
        print("No valid satisfaction could be calculated.")
    else:
        print(f"Max Satisfaction: {max_satisfaction}")
if __name__ == "__main__":
    main()