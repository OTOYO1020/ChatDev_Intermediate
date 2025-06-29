'''
Main file to run the Happy Sets application.
'''
from happy_sets import count_happy_sets
def main():
    # Read input values for A and B
    A, B = map(int, input("Enter two integers A and B (space-separated): ").split())
    # Call the count_happy_sets function and print the result
    result = count_happy_sets(A, B)
    print(f"Number of Happy Sets: {result}")
if __name__ == "__main__":
    main()