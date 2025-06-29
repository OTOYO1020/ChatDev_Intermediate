'''
Main application file for the Jewel Collector game.
'''
import sys
from simulation import simulate_operations
def main():
    # Input Handling
    try:
        N = int(input("Enter the number of jewels (N): "))
        K = int(input("Enter the number of operations (K): "))
        V_input = input("Enter jewel values (comma-separated integers): ").strip()
        # Validate and parse jewel values
        V = []
        for value in V_input.split(','):
            try:
                V.append(int(value))
            except ValueError:
                raise ValueError(f"Invalid jewel value '{value}'. Please enter integers only.")
        if len(V) != N:
            raise ValueError("Number of jewel values must match N.")
        # Simulate Operations
        max_sum = simulate_operations(V, N, K)
        # Output Result
        print(f"Maximum Sum: {max_sum}")
    except ValueError as ve:
        print(f"Input Error: {ve}. Please ensure you enter integers and that the number of values matches N.")
    except Exception as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()