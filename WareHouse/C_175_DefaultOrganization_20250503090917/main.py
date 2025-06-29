'''
Main application file for the Takahashi movement calculator.
'''
def main():
    max_attempts = 5  # Limit the number of attempts
    attempts = 0
    while attempts < max_attempts:
        try:
            user_input = input("Please enter three integers separated by spaces (X K D, where X can be negative): ")
            inputs = user_input.split()
            if len(inputs) != 3:
                attempts += 1
                print(f"Invalid input. Please enter exactly three integers. Attempts left: {max_attempts - attempts}")
                continue
            x, k, d = map(int, inputs)
            if k < 0 or d < 0:
                attempts += 1
                print(f"Invalid input. K and D must be non-negative integers. Attempts left: {max_attempts - attempts}")
                continue
            break
        except ValueError:
            attempts += 1
            print(f"Invalid input. Please enter three integers. Attempts left: {max_attempts - attempts}")
    if attempts == max_attempts:
        print("Maximum attempts reached. Exiting the program.")
        return  # Exit the program after maximum attempts
    initial_abs = abs(x)
    max_move = k * d
    if initial_abs <= max_move:
        if (max_move - initial_abs) % 2 == 0:
            min_abs_value = 0
        else:
            min_abs_value = 1
    else:
        min_abs_value = initial_abs - max_move
    print(min_abs_value)
if __name__ == "__main__":
    main()