'''
Main application file for the product calculator.
'''
from product_calculator import ProductCalculator  # Import the ProductCalculator class
def main():
    """Main function to read input, calculate products, and print the K-th smallest product."""
    try:
        n = input("Enter N (length of array): ")
        if not n.isdigit() or int(n) < 2:
            raise ValueError("N must be a positive integer of at least 2 to form pairs.")
        n = int(n)
        k = input("Enter K (position of smallest product): ")
        if not k.isdigit() or int(k) <= 0:
            raise ValueError("K must be a positive integer.")
        k = int(k)
        array_input = input("Enter array elements (space-separated, non-negative integers only): ").split()
        if len(array_input) != n:
            raise ValueError("Array length does not match N.")
        array = []
        for item in array_input:
            try:
                num = int(item)
                if num < 0:
                    raise ValueError(f"Invalid input '{item}'. Please enter only non-negative integers.")
                array.append(num)
            except ValueError:
                raise ValueError(f"Invalid input '{item}'. Please enter only non-negative integers.")
        calculator = ProductCalculator(array, k)
        result = calculator.get_kth_smallest_product()
        print(f"K-th smallest product: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()