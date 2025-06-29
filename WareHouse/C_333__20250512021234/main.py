'''
Main application file for the Repunits Sum Finder.
'''
from repunits import find_nth_repunits_sum
def main():
    while True:
        try:
            n = int(input("Enter N (1-333): "))
            if 1 <= n <= 333:
                result = find_nth_repunits_sum(n)
                if result == -1:
                    print("Not enough unique sums to find the N-th smallest sum.")
                else:
                    print(f"The {n}-th smallest sum is: {result}")
                break
            else:
                print("Please enter a number between 1 and 333.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()