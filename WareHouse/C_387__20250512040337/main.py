'''
Main application file for counting Snake numbers using standard input/output.
'''
from snake_number_logic import count_snake_numbers
def main():
    # Input handling
    L, R = map(int, input("Enter two integers L and R (10 <= L <= R <= 10^18): ").split())
    if 10 <= L <= R <= 10**18:
        snake_count = count_snake_numbers(L, R)
        print(f"Snake Numbers Count: {snake_count}")
    else:
        print("Input Error: Please ensure 10 <= L <= R <= 10^18.")
if __name__ == "__main__":
    main()