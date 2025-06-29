'''
Main application file for the Product Printer application.
'''
from product import Product  # Importing the Product class
def read_input():
    while True:
        try:
            N = int(input("Enter the number of products to print: "))  # Clearer user prompt
            if N <= 0:
                raise ValueError("The number of products must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    products = []  # Initialize products list here
    for _ in range(N):
        while True:
            try:
                T_i, D_i = map(int, input("Enter entry time and duration for product (T_i D_i): ").split())
                if T_i < 0 or D_i < 0:
                    raise ValueError("Entry time and duration must be non-negative integers.")
                products.append(Product(T_i, D_i))  # Create Product instances
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter two integers separated by a space.")
    return products  # Return the list of products
def calculate_max_printed(products):
    products.sort(key=lambda x: x.entry_time)  # Sort by entry time T_i
    last_print_time = 0
    max_printed = 0
    for product in products:
        if product.entry_time >= last_print_time + 1:
            last_print_time += product.duration  # Update to last_print_time + D_i
            max_printed += 1
    return max_printed
if __name__ == "__main__":
    products = read_input()  # Capture the returned products list
    max_printed = calculate_max_printed(products)
    print(f"Maximum products printed: {max_printed}")