'''
Main file to run the Product Calculator application.
'''
from calculator import ProductCalculator
def main():
    '''
    Main function to read input and calculate the product.
    '''
    try:
        n = int(input())
        integers = list(map(int, input().split()))
        if len(integers) != n:
            raise ValueError("Number of integers does not match N.")
        calculator = ProductCalculator()
        product = calculator.calculate_product(integers)
        if product != -1:  # Only print if product is not -1
            print(product)
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()