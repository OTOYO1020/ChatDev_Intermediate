'''
Main application file for the Takoyaki machine payment system.
'''
from banknote_calculator import min_banknotes
def main():
    '''
    Main function to execute the Takoyaki payment calculation.
    '''
    try:
        N = int(input("Enter the amount (N): "))
        if N < 1:
            raise ValueError("Amount must be at least 1.")
        total_banknotes = min_banknotes(N)
        print(f"Total banknotes used: {total_banknotes}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()