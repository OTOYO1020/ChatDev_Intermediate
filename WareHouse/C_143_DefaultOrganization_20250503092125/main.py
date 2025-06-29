'''
Main file to run the Slime Counter application.
'''
from slime_counter import count_slimes
def main():
    try:
        n = int(input())
        if n < 1:
            raise ValueError("N must be a positive integer.")
        s = input()
        if len(s) != n:
            raise ValueError("Length of S must be equal to N.")
        if not s:
            raise ValueError("S cannot be an empty string.")
        slime_count = count_slimes(s)
        print(slime_count)
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()