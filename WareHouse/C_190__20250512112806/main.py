'''
Main application file that handles user interactions and simulates condition satisfaction.
'''
from condition import Condition
from action import Action
from simulation import simulate
def main():
    try:
        # Read input values
        N, M, K = map(int, input("Enter N (number of dishes), M (number of conditions), K (number of people): ").strip().split())
        conditions_input = input("Enter conditions (A,B) separated by commas: ").strip()
        actions_input = input("Enter actions (C,D) separated by commas: ").strip()
        # Validate conditions input
        conditions = []
        if not conditions_input.strip():
            raise ValueError("Conditions cannot be empty.")
        for cond in conditions_input.split(','):
            cond = cond.strip()  # Remove any extra spaces
            if ',' not in cond:
                raise ValueError(f"Invalid condition format: '{cond}'. Expected format A,B.")
            try:
                a, b = map(int, cond.split(','))
            except ValueError:
                raise ValueError(f"Condition values must be integers: '{cond}'.")
            if a < 0 or b < 0:
                raise ValueError(f"Dish indices must be non-negative: {a}, {b}.")
            conditions.append(Condition(a, b))
        # Validate actions input
        actions = []
        if not actions_input.strip():
            raise ValueError("Actions cannot be empty.")
        for act in actions_input.split(','):
            act = act.strip()  # Remove any extra spaces
            if ',' not in act:
                raise ValueError(f"Invalid action format: '{act}'. Expected format C,D.")
            try:
                c, d = map(int, act.split(','))
            except ValueError:
                raise ValueError(f"Action values must be integers: '{act}'.")
            if c < 0 or d < 0:
                raise ValueError(f"Dish indices must be non-negative: {c}, {d}.")
            actions.append(Action(c, d))
        # Pass N to the simulate function
        max_satisfied = simulate(conditions, actions, K, N)
        print(f"Max Conditions Satisfied: {max_satisfied}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
if __name__ == "__main__":
    main()