'''
Main application file for the conditions and actions evaluator.
'''
import sys
from conditions_actions import count_satisfied_conditions
def main():
    try:
        # Read integer N, M, and K from standard input
        N = int(input("Enter N (number of dishes): "))  # Number of dishes
        M = int(input("Enter M (number of conditions): "))  # Number of conditions
        K = int(input("Enter K (number of actions): "))      # Number of actions
        # Handle edge case where M or K is zero
        if M == 0:
            print("No conditions to evaluate. Satisfied Conditions: 0")
            return
        if K == 0:
            print("No actions to evaluate. Satisfied Conditions: 0")
            return
        # Validate and parse conditions
        conditions = set()  # Use a set to avoid duplicates
        max_attempts = 5  # Set a maximum number of attempts for input
        attempts = 0
        while len(conditions) < M and attempts < max_attempts:
            print("Enter conditions (A_i, B_i) as comma-separated pairs (e.g., '1,2' for condition A_1 and B_1). Please ensure to separate the integers with a comma:")
            cond = input().strip()
            try:
                parts = list(map(int, cond.split(',')))
                if len(parts) != 2:
                    raise ValueError("Each condition must have exactly two integers.")
                if not (1 <= parts[0] <= N) or not (1 <= parts[1] <= N):
                    raise ValueError(f"Condition values must be between 1 and {N}.")
                if tuple(parts) in conditions:
                    print("This condition is already entered. Please enter a unique condition.")
                    attempts += 1
                    continue
                conditions.add(tuple(parts))  # Add to set to avoid duplicates
                attempts = 0  # Reset attempts on successful input
            except ValueError as e:
                print(f"Invalid input: {str(e)}. Please enter two integers separated by a comma.")
                attempts += 1
        if attempts >= max_attempts:
            print("Too many invalid attempts for conditions. Exiting.")
            return  # or handle exit appropriately
        # Convert set back to list for further processing
        conditions = list(conditions)
        # Validate and parse actions
        actions = set()  # Use a set to avoid duplicates
        attempts = 0
        while len(actions) < K and attempts < max_attempts:
            print("Enter actions (C_i, D_i) as comma-separated pairs (e.g., '1,2' for action C_1 and D_1). Please ensure to separate the integers with a comma:")
            act = input().strip()
            try:
                parts = list(map(int, act.split(',')))
                if len(parts) != 2:
                    raise ValueError("Each action must have exactly two integers.")
                if not (1 <= parts[0] <= N) or not (1 <= parts[1] <= N):
                    raise ValueError(f"Action values must be between 1 and {N}.")
                if tuple(parts) in actions:
                    print("This action is already entered. Please enter a unique action.")
                    attempts += 1
                    continue
                actions.add(tuple(parts))  # Add to set to avoid duplicates
                attempts = 0  # Reset attempts on successful input
            except ValueError as e:
                print(f"Invalid input: {str(e)}. Please enter two integers separated by a comma.")
                attempts += 1
        if attempts >= max_attempts:
            print("Too many invalid attempts for actions. Exiting.")
            return  # or handle exit appropriately
        satisfied_count = count_satisfied_conditions(conditions, actions)
        print(f"Satisfied Conditions: {satisfied_count}")
    except Exception as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()