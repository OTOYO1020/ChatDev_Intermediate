'''
Main application file for the medicine pill calculator.
'''
import sys
from medicine import Medicine
from input_validation import InputValidation
def main():
    # Read the number of medicines
    while True:
        N = input("Enter the number of different kinds of medicine prescribed: ")
        if InputValidation.validate_integer(N) and int(N) > 0:  # Ensure N is positive
            N = int(N)
            break
        print("Please enter a valid positive integer.")
    medicines = []
    # Read each medicine's days and pills
    for i in range(N):
        while True:
            try:
                a_i, b_i = input(f"Enter days and pills for medicine {i + 1} (space-separated): ").split()
                if InputValidation.validate_integer(a_i) and InputValidation.validate_integer(b_i):
                    if int(b_i) >= 0:  # Ensure b_i is non-negative
                        medicines.append(Medicine(int(a_i), int(b_i)))
                        break
                    else:
                        print("Please enter a valid non-negative integer for pills (b_i). Negative values are not allowed.")
                else:
                    print("Please enter valid non-negative integers for days and pills.")
            except ValueError:
                print("Invalid input. Please enter two space-separated integers.")
    # Read the maximum number of pills (K)
    while True:
        K = input("Enter the maximum number of pills (K): ")
        if InputValidation.validate_integer(K) and int(K) >= 0:
            K = int(K)
            break
        print("Please enter a valid non-negative integer for K.")
    max_days = max(medicine.days for medicine in medicines)
    # Loop through each day
    found_valid_day = False  # Flag to track if a valid day is found
    for day in range(1, max_days + 1):
        total_pills = 0  # Reset total_pills for each day
        for medicine in medicines:
            if day <= medicine.days:
                total_pills += medicine.pills  # Add pills for the current day
        if total_pills <= K:
            print(f"Valid day found: {day} with total pills = {total_pills} (<= {K})")
            found_valid_day = True
            break  # Break the loop after finding the first valid day
    if not found_valid_day:
        print("No day found where total pills are K or less.")
if __name__ == "__main__":
    main()