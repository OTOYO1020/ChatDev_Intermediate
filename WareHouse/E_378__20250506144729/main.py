'''
Main application file for the sum calculation application.
'''
def get_inputs():
    while True:
        try:
            n = int(input("Enter N (number of elements, must be positive): "))
            m = int(input("Enter M (positive modulo value): "))
            a = list(map(int, input("Enter the sequence of non-negative integers (space-separated): ").split()))
            if validate_input(n, m, a):
                return n, m, a
            else:
                print("Input Error: Please ensure N is positive, M is positive, and the number of elements matches N.")
        except ValueError:
            print("Input Error: Please enter valid integers.")
def main():
    n, m, a = get_inputs()
    total_sum = calculate_total_sum(a, m)
    print(f"Total Sum: {total_sum}")
if __name__ == "__main__":
    from utils import validate_input, calculate_total_sum
    main()