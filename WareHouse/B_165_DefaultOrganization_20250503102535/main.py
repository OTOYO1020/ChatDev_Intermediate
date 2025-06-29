'''
Main file to run the Takahashi balance application.
'''
from takahashi import calculate_years  # Import the function
if __name__ == "__main__":
    try:
        target_balance = int(input("Enter the target balance: "))  # Prompt for clarity
        if target_balance < 100:
            raise ValueError("Target balance must be at least 100, as the initial balance is 100.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        exit(1)  # Exit the program if input is invalid
    years = calculate_years(target_balance)  # Use the function to calculate years
    print(years)  # Output the number of years required without additional text