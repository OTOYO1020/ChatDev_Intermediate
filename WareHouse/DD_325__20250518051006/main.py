'''
Main application file for the product printing application.
'''
from product_manager import ProductManager
from typing import List, Tuple
def get_products_input() -> List[Tuple[int, int]]:
    while True:
        products_input = input("Enter products (T_i, D_i) separated by semicolons: ").strip()
        if not products_input:  # Check for empty input
            print("Input cannot be empty. Please enter valid products.")
            continue
        products = []
        try:
            for p in products_input.split(';'):
                T_i, D_i = map(int, p.split(','))
                products.append((T_i, D_i))
            return products
        except ValueError:
            print("Invalid product format. Ensure you enter (T_i, D_i) pairs separated by semicolons. Please try again.")
def main():
    while True:
        try:
            n = input("Enter number of products: ")
            if not n.isdigit() or int(n) < 0:
                raise ValueError("Number of products must be a non-negative integer.")
            n = int(n)
            products = get_products_input()
            if len(products) != n:
                print("Number of products does not match the input count. Please try again.")
                continue
            product_manager = ProductManager()
            max_printable = product_manager.max_printable_products(n, products)
            print(f"Max Printable Products: {max_printable}")
            break  # Exit the loop after successful processing
        except Exception as e:
            print(f"Input Error: {str(e)}. Please try again.")
if __name__ == "__main__":
    main()