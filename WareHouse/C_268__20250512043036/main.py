'''
Main application file for the Happy People application.
'''
from happy_people import max_happy_people
def main():
    while True:
        try:
            # Parse input for the number of dishes
            N = int(input("Enter number of dishes (N): "))
            # Validate that N is within the acceptable range
            if N < 3 or N > 200000:
                raise ValueError("N must be between 3 and 200,000.")
            # Parse input for the dish values
            dishes = list(map(int, input("Enter the dish values separated by commas: ").strip().split(',')))
            # Validate that the number of dishes matches N
            if len(dishes) != N:
                raise ValueError("Number of dishes must match N.")
            # Check if all dish values are unique
            if len(set(dishes)) != N:
                raise ValueError("All dish values must be unique.")
            # Validate that all dish values are within the acceptable range
            if any(d < 0 or d >= N for d in dishes):
                raise ValueError("Dish values must be in the range 0 to N-1.")
            break  # Exit the loop if all inputs are valid
        except Exception as e:
            print(f"Input Error: {str(e)}. Please try again.")
    # Calculate maximum happy people
    max_happy = max_happy_people(N, dishes)
    print(f"Maximum Happy People: {max_happy}")
if __name__ == "__main__":
    main()