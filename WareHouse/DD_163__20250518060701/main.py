'''
Main application file to run the Sum Counter.
'''
from sum_counter import count_possible_sums
def main():
    try:
        N = int(input("Enter N: "))
        K = int(input("Enter K: "))
        result = count_possible_sums(N, K)
        print(f"Unique sums count: {result}")
    except ValueError:
        print("Please enter valid integers for N and K.")
if __name__ == "__main__":
    main()