'''
Main application file for the bitwise AND and popcount calculator.
This program reads two non-negative integers N and M from standard input,
calculates the total number of 1s in the binary representation of the 
results of the bitwise AND operation between each integer from 0 to N 
and M, and prints the final result modulo 998244353.
'''
from utils import popcount
def main():
    N, M = None, None
    while N is None or M is None:
        try:
            user_input = input("Enter two non-negative integers N and M (separated by space) or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                return
            N, M = map(int, user_input.split())
            if N < 0 or M < 0:
                raise ValueError("N and M must be non-negative integers.")
        except ValueError as e:
            print(f"Input Error: {e}. Please enter valid non-negative integers for N and M.")
            N, M = None, None  # Reset N and M to prompt again
    total_sum = 0
    for k in range(N + 1):
        and_result = k & M
        popcount_result = popcount(and_result)
        total_sum += popcount_result
    final_result = total_sum % 998244353
    print(f"Final Result: {final_result}")
if __name__ == "__main__":
    main()