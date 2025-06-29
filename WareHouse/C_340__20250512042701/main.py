'''
Main application file for the Total Payment Calculator.
'''
from payment_calculator import calculate_total_payment
def main():
    try:
        N = int(input("Enter an integer N: "))
        total_payment = calculate_total_payment(N)
        print(f"Total Payment: {total_payment}")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()