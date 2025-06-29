'''
Main file to run the Median Calculator application.
'''
from median_calculator import count_median_values
def main():
    try:
        N = int(input("Enter N: "))
        A = list(map(int, input("Enter list A (comma-separated): ").split(',')))
        B = list(map(int, input("Enter list B (comma-separated): ").split(',')))
        if len(A) != N or len(B) != N:
            raise ValueError("Length of A and B must be equal to N.")
        result = count_median_values(N, A, B)
        print(f"Distinct Median Values Count: {result}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()