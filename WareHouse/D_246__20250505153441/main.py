'''
Main application file for finding the smallest integer X that satisfies the given conditions.
'''
def can_express_as_polynomial(remaining, a):
    '''
    Checks if the remaining value can be expressed as a^2b + ab^2 for any non-negative integer b.
    '''
    for b in range(int(remaining**(1/3)) + 1):
        if remaining == a**2 * b + a * b**2:
            return True
    return False
def find_smallest_x(n):
    '''
    Finds the smallest integer X that satisfies the conditions.
    '''
    x = n
    while True:
        found = False
        for a in range(int(x**(1/3)) + 1):
            a_cubed = a**3
            if a_cubed > x:
                break
            for b in range(int((x - a_cubed)**(1/3)) + 1):
                b_cubed = b**3
                if a_cubed + b_cubed > x:
                    break
                remaining = x - (a_cubed + b_cubed)
                if remaining >= 0 and can_express_as_polynomial(remaining, a):
                    found = True
                    break
            if found:
                break
        if found:
            return x
        x += 1
def validate_input(input_value):
    '''
    Validates if the input is a valid non-negative integer.
    '''
    try:
        value = int(input_value)
        return value >= 0
    except ValueError:
        return False
def main():
    '''
    Main function to run the application.
    '''
    n = input("Please enter a non-negative integer N: ")
    if not validate_input(n):
        print("Invalid input. Please enter a valid non-negative integer.")
        return
    n = int(n)
    result = find_smallest_x(n)
    print(f"The smallest integer X is: {result}")
if __name__ == "__main__":
    main()