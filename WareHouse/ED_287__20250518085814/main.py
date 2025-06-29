'''
Main application file for the LCP calculator.
'''
from lcp_calculator import max_lcp
def main():
    try:
        # Read the number of strings
        n = int(input("Enter number of strings (N): "))
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        strings = []
        total_length = 0
        for _ in range(n):
            string = input("Enter string (lowercase letters only): ")
            if not string.isalpha() or not string.islower():
                raise ValueError("All strings must consist of lowercase English letters.")
            strings.append(string)
            total_length += len(string)
        # Check total length constraint
        if total_length > 500000:
            raise ValueError("Total length of strings must not exceed 500,000.")
        # Calculate LCP values
        lcp_values = max_lcp(strings)
        print(f"Max LCP values: {lcp_values}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()