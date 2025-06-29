'''
Main entry point for the Snuke Cat application.
'''
from utils import restore_scarves
def main():
    # Prompt for an even integer N within the specified range
    while True:
        try:
            N = int(input("Enter an even integer N (2-200000): "))
            if N % 2 != 0 or N < 2 or N > 200000:
                raise ValueError("Invalid input. Ensure N is even and within the range [2, 200000].")
            break  # Exit the loop if input is valid
        except ValueError as ve:
            print("Error:", str(ve))
            continue  # Prompt the user again for valid input
    # Prompt for the array of integers
    while True:
        try:
            input_values = input("Enter the array of integers (space-separated): ").split()
            a = []
            for value in input_values:
                a.append(int(value))  # This will raise ValueError if conversion fails
            if len(a) != N:
                raise ValueError("Invalid input. Ensure the length of the array matches N.")
            if any(value < 0 or value > 10**9 for value in a):
                raise ValueError("Invalid input. Each element of the array must be in the range [0, 10^9].")
            break  # Exit the loop if input is valid
        except ValueError as ve:
            print("Error:", str(ve))
            print("Please enter valid integers for the array.")
            continue  # Prompt the user again for valid input
    scarves = restore_scarves(N, a)
    for scarf in scarves:
        print(scarf)
if __name__ == "__main__":
    main()