'''
Main application file for the Good String Calculator.
'''
from good_string import min_cost_to_good_string
def main():
    S = input("Enter binary string (0s and 1s): ")
    costs_str = input("Enter costs (comma-separated): ")
    try:
        C = list(map(int, costs_str.split(',')))
        min_cost = min_cost_to_good_string(S, C)
        print(f"Minimum Cost: {min_cost}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()