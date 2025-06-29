'''
Main application file for the Takahashi cost calculation program.
'''
from calculator import calculate_total_cost
def main():
    while True:
        try:
            n = int(input("Enter a positive integer N (greater than or equal to 2): "))
            if n < 2:
                raise ValueError("N must be greater than or equal to 2.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(e)  # Print the error message and prompt again
    total_cost = calculate_total_cost(n)
    print(f"Total Cost: {total_cost}")
if __name__ == "__main__":
    main()