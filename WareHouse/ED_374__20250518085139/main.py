'''
Main application file for the Production Capacity Calculator.
'''
from production_capacity import max_production_capacity
def main():
    '''
    Main function to parse input and calculate maximum production capacity.
    '''
    # Read input values
    N = int(input("Enter the number of processes (N): "))
    A = list(map(int, input("Enter processing rates A (comma-separated): ").split(',')))
    B = list(map(int, input("Enter processing rates B (comma-separated): ").split(',')))
    P = list(map(int, input("Enter prices of machines S (comma-separated): ").split(',')))
    Q = list(map(int, input("Enter prices of machines T (comma-separated): ").split(',')))
    X = int(input("Enter budget (X): "))
    # Calculate maximum production capacity
    max_capacity = max_production_capacity(N, A, B, P, Q, X)
    # Output the result
    print(f"Maximum Production Capacity: {max_capacity}")
if __name__ == "__main__":
    main()