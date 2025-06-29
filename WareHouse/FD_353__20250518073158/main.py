'''
Main application file for the Toll Calculator.
'''
from toll_calculator import minimum_toll
def main():
    K = int(input("Enter K: "))
    S_x, S_y = map(int, input("Enter Start (S_x, S_y): ").split())
    T_x, T_y = map(int, input("Enter Target (T_x, T_y): ").split())
    toll = minimum_toll(K, S_x, S_y, T_x, T_y)
    print(f"Minimum Toll: {toll}")
if __name__ == "__main__":
    main()