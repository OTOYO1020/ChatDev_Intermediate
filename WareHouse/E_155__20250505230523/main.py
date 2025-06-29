'''
Main application file for the Takoyaki Machine software.
'''
from banknote_calculator import calculate_min_banknotes
def main():
    try:
        N_str = input("Enter the amount (N): ")
        if len(N_str) < 1 or len(N_str) > 1000000 or not N_str.isdigit() or N_str[0] == '0':
            raise ValueError("N must be a positive integer between 1 and 10^1,000,000.")
        total_banknotes = calculate_min_banknotes(N_str)
        print(f"Total Banknotes: {total_banknotes}")
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()