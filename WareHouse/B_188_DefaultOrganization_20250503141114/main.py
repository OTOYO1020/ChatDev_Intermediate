'''
Main application file to run the Vector Inner Product application.
'''
from vector_inner_product import calculate_inner_product
def main():
    while True:
        try:
            n = int(input("Enter the dimension of vectors (N): "))
            if not (1 <= n <= 100000):
                raise ValueError("N must be between 1 and 100000.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Input Error: {e}. Please try again.")
    while True:
        try:
            a = list(map(int, input("Enter vector A (space-separated integers): ").split()))
            if len(a) != n:
                raise ValueError("Vectors must have exactly N elements.")
            if not all(-100 <= x <= 100 for x in a):
                raise ValueError("All elements in vector A must be between -100 and 100.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Input Error: {e}. Please try again.")
        except Exception:
            print("Input Error: Please enter valid integers for vector A.")
    while True:
        try:
            b = list(map(int, input("Enter vector B (space-separated integers): ").split()))
            if len(b) != n:
                raise ValueError("Vectors must have exactly N elements.")
            if not all(-100 <= x <= 100 for x in b):
                raise ValueError("All elements in vector B must be between -100 and 100.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Input Error: {e}. Please try again.")
        except Exception:
            print("Input Error: Please enter valid integers for vector B.")
    result = calculate_inner_product(a, b, n)
    print(result)  # This will now print "YES" or "NO" directly.
if __name__ == "__main__":
    main()