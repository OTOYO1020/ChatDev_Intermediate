'''
Main application file for the Lunch Break application.
'''
from lunch_break import min_max_lunch_break
def main():
    try:
        n = int(input("Enter number of departments (positive integer): "))
        if n <= 0:
            raise ValueError("Number of departments must be a positive integer.")
        k_values = input("Enter number of people in each department (comma-separated non-negative integers): ")
        k_values = [value.strip() for value in k_values.split(',')]  # Strip whitespace from each value
        # Validate that we have exactly N integers
        if len(k_values) != n:
            raise ValueError("Number of departments does not match the input values.")
        # Convert to integers and validate
        people_counts = []
        for value in k_values:
            try:
                num = int(value.strip())
                if num < 0:
                    raise ValueError("Number of people in each department must be a non-negative integer.")
                people_counts.append(num)
            except ValueError:
                raise ValueError(f"Invalid input '{value.strip()}': must be a non-negative integer.")
        result = min_max_lunch_break(people_counts)
        print(f"Minimum maximum lunch break: {result}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
if __name__ == "__main__":
    main()