'''
Main application file for the sum calculation.
'''
def main():
    while True:
        try:
            # Prompt the user for input with clearer instructions
            x = int(input("Enter an integer (X) that is a product of two numbers between 1 and 9 (valid range: 1 to 81, e.g., 6 for 2*3): "))
            # Check if the input is within the valid range of multiplication results
            if x < 1 or x > 81:
                print("Invalid input! Please enter a product of two numbers between 1 and 9 (valid range: 1 to 81).")
                continue  # Prompt again for input
            # Check if the input is a valid product of two numbers from 1 to 9
            valid_products = {i * j for i in range(1, 10) for j in range(1, 10)}
            if x not in valid_products:
                print("Invalid input! Please enter a product of two numbers between 1 and 9 (valid range: 1 to 81).")
                continue  # Prompt again for input
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    total_sum = 0
    # Loop through each row index from 1 to 9
    for i in range(1, 10):
        # Loop through each column index from 1 to 9
        for j in range(1, 10):
            # Calculate the product of the current row and column indices
            value = i * j
            # If the product is not equal to the input X, add it to the total sum
            if value != x:
                total_sum += value
    print(f"Total Sum: {total_sum}")
if __name__ == "__main__":
    main()