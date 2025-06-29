'''
Main entry point for the Key Combination application.
'''
from key_combination import count_valid_key_combinations
def main():
    input_data = input("Enter N, M, K and test cases (each test case on a new line):\n").strip().splitlines()
    try:
        N, M, K = map(int, input_data[0].split())
        if M != len(input_data) - 1:
            raise ValueError("The number of test cases does not match M.")
        tests = []
        for line in input_data[1:]:
            parts = line.split()
            if len(parts) < 2 or parts[-1] not in ['o', 'x']:
                raise ValueError("Each test case must end with 'o' or 'x'.")
            keys = list(map(int, parts[:-1]))
            if any(key < 1 or key > N for key in keys):
                raise ValueError("Key indices must be between 1 and N.")
            tests.append((keys, parts[-1]))
        valid_count = count_valid_key_combinations(N, M, K, tests)
        print(f"Valid combinations: {valid_count}")
    except ValueError as e:
        print(f"Input error: {e}")
if __name__ == "__main__":
    main()