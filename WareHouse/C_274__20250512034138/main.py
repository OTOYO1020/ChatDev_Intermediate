'''
Main application file for the Amoeba Generation Calculator.
'''
from amoeba_calculator import calculate_generations
def main():
    try:
        N = int(input("Enter number of amoebae: "))
        records = list(map(int, input("Enter amoebae records (comma-separated): ").split(',')))
        if len(records) != N:
            raise ValueError("Number of records must match N.")
        result = calculate_generations(N, records)
        print(f"Generations: {result}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()