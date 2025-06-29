'''
Main application file for the insurance calculator.
'''
from insurance_calculator import count_insured_people
def main():
    try:
        N = int(input("Enter number of people (N): "))
        M = int(input("Enter number of insurances (M): "))
        # Validate parents input
        parents_input = input("Enter parents list (comma-separated): ")
        if not parents_input.strip():  # Check for empty input
            raise ValueError("Parents list cannot be empty.")
        parents = list(map(int, parents_input.split(',')))
        # Validate insurances input
        insurances_input = input("Enter insurances (format: person, generations; comma-separated): ")
        if not insurances_input.strip():  # Check for empty input
            raise ValueError("Insurances list cannot be empty.")
        insurances = [tuple(map(int, item.split(','))) for item in insurances_input.split(';')]
        # Validate insurances
        for person, generations in insurances:
            if person >= N:  # Ensure the person index is valid
                raise ValueError(f"Insurance entry references invalid person index: {person}. Must be less than {N}.")
            if generations < 0:  # Validate generations
                raise ValueError(f"Invalid generations value: {generations}. Must be non-negative.")
        total_insured = count_insured_people(N, M, parents, insurances)
        print(f"Total Insured: {total_insured}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()