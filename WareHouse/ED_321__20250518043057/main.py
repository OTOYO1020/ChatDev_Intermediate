'''
Main application file for the Tree Distance Calculator.
'''
from distance_calculator import find_distance_count
def main():
    T = int(input("Enter number of test cases: "))
    results = []
    for _ in range(T):
        N, X, K = map(int, input("Enter N, X, K: ").split())
        result = find_distance_count(N, X, K)
        results.append(result)
    for res in results:
        print(res)
if __name__ == "__main__":
    main()