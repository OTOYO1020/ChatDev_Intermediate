'''
Main application file for the SumModApp using standard input and output.
'''
from calculator import calculate_sum_mod
def main():
    try:
        n = int(input("Enter N (size of list): "))
        a = list(map(int, input("Enter list A (space-separated): ").split()))
        m = int(input("Enter M (modulus): "))
        if not (1 <= n <= 200000) or not (1 <= m <= 200000):
            raise ValueError("N and M must be within the specified constraints.")
        if len(a) != n:
            raise ValueError("The size of list A must be equal to N.")
        result = calculate_sum_mod(a, m)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()