'''
Main entry point for the String Swap application.
'''
from string_logic import can_swap_to_equal
def main():
    S = input()
    T = input()
    if can_swap_to_equal(S, T):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()