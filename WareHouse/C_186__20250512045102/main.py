'''
Main application file that handles user input and output.
'''
from counter import count_integers_without_7
if __name__ == "__main__":
    while True:
        try:
            N = int(input("Enter an integer N (1 ≤ N ≤ 100000): "))
            if 1 <= N <= 100000:
                count = count_integers_without_7(N)
                print(f"Count: {count}")
                break  # Exit the loop after valid input
            else:
                print("Input Error: Please enter a number between 1 and 100000.")
        except ValueError:
            print("Input Error: Please enter a valid integer.")