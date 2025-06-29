'''
Main application file for the number processing application.
'''
def calculate_output(n):
    result = []
    # Collect valid divisors of N in the range 1 to 9
    valid_divisors = [j for j in range(1, 10) if n % j == 0]
    for i in range(n + 1):
        found = False
        for j in valid_divisors:
            # Check if i is a multiple of N/j
            if i % (n // j) == 0:
                result.append(str(j))  # Append the corresponding character
                found = True
                break
        if not found:
            result.append('-')  # Append '-' if no divisor was found
    output_string = ''.join(result)
    print(output_string)
if __name__ == "__main__":
    try:
        n = int(input("Please enter a positive integer N to process: "))
        if n > 0:
            calculate_output(n)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")