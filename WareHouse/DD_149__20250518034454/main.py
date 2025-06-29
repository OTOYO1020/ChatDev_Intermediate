'''
Main application file for the Max Score Calculator.
'''
from score_calculator import max_score
def main():
    try:
        N = int(input("Number of Rounds (N): "))
        K = int(input("Last K Hands (K): "))
        R = int(input("Score for Rock (R): "))
        S = int(input("Score for Scissors (S): "))
        P = int(input("Score for Paper (P): "))
        T = input("Machine's Hands (T): ")
        score = max_score(N, K, R, S, P, T)
        print(f"Maximum Score: {score}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()