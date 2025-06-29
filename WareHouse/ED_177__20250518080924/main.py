'''
Main application file for the Coprime Checker.
'''
from utils import is_pairwise_coprime, gcd_of_list
def main():
    try:
        N = int(input("Enter the number of integers (N): "))
        if N < 2:
            raise ValueError("N must be at least 2.")
        A = list(map(int, input(f"Enter {N} integers (space-separated): ").split()))
        if len(A) != N:
            raise ValueError(f"Expected {N} integers, but got {len(A)}.")
        if any(not (1 <= x <= 10**6) for x in A):
            raise ValueError("All integers must be in the range 1 to 10^6.")
        pairwise_result = is_pairwise_coprime(A)
        if pairwise_result:
            print("pairwise coprime")
        else:
            overall_gcd = gcd_of_list(A)
            if overall_gcd == 1:
                print("setwise coprime")
            else:
                print("neither")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()