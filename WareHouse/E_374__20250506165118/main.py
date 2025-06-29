'''
Main application file for the Production Capacity Calculator.
'''
from capacity_calculator import calculate_max_capacity
def main():
    N = int(input("Enter the number of processes: "))
    A = []
    B = []
    P = []
    Q = []
    for i in range(N):
        a_i, b_i, p_i, q_i = map(int, input(f"Enter A_{i+1}, B_{i+1}, P_{i+1}, Q_{i+1} (space-separated): ").split())
        A.append(a_i)
        B.append(b_i)
        P.append(p_i)
        Q.append(q_i)
    X = int(input("Enter the total budget X: "))
    max_capacity = calculate_max_capacity(A, B, P, Q, X)
    print(f"The maximum achievable production capacity is: {max_capacity}")
if __name__ == "__main__":
    main()