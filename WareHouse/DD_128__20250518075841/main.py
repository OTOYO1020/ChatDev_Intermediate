'''
Main entry point for the Jewel Collector application.
'''
from jewel_collector import max_jewel_sum
if __name__ == "__main__":
    # Read input values from standard input
    N = int(input("Enter the number of jewels (N): "))
    K = int(input("Enter the maximum number of operations (K): "))
    V = list(map(int, input("Enter the jewel values (space-separated): ").split()))
    # Read operations from standard input
    operations = input(f"Enter {K} operations (A/B/C/D) separated by spaces: ").strip().upper().split()
    # Validate the number of operations
    if len(operations) > K:
        print(f"Warning: Only the first {K} operations will be considered.")
        operations = operations[:K]
    # Calculate and print the maximum jewel sum
    result = max_jewel_sum(N, K, V, operations)
    print(f"Max Jewel Sum: {result}")