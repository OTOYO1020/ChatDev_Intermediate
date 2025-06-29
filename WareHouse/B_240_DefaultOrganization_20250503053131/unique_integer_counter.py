'''
This module contains the UniqueIntegerCounter class which implements
the logic for counting unique integers from user input.
'''
class UniqueIntegerCounter:
    def run(self):
        while True:
            try:
                N = int(input("Enter the number of integers in the sequence: "))
                if N <= 0:
                    raise ValueError("The number of integers must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
        while True:
            try:
                a = list(map(int, input(f"Enter {N} positive integers separated by spaces: ").split()))
                if len(a) != N or any(x <= 0 for x in a):
                    raise ValueError("Please enter exactly N positive integers.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please enter valid integers.")
        count_unique = self.count_unique_integers(a)
        print(f"Count of unique integers: {count_unique}")
    def count_unique_integers(self, integers):
        '''
        Count the number of unique integers in a list.
        '''
        unique_integers = set(integers)
        return len(unique_integers)