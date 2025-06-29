'''
Main application file for the Jewels Management System.
'''
from jewels_handler import JewelsHandler
def main():
    # Read integers N and K from standard input
    n = int(input("Enter number of jewels (N): "))
    k = int(input("Enter maximum operations (K): "))
    # Read jewel values from standard input
    values = list(map(int, input("Enter jewel values (comma-separated): ").split(',')))
    if len(values) != n:
        raise ValueError("Number of jewel values must match N.")
    jewels_handler = JewelsHandler(values, k)
    max_sum = jewels_handler.perform_operations()
    # Output the maximum sum
    print(max_sum)
if __name__ == "__main__":
    main()