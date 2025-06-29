'''
Main entry point of the Distance Calculator application.
'''
from distance_calculator import calculate_distance
def main():
    # Read integers N and Q from standard input
    try:
        N, Q = map(int, input("Enter two positive integers N (number of A coordinates) and Q (number of B coordinates): ").strip().split())
        if N <= 0 or Q <= 0:
            print("Error: Both N and Q must be positive integers.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter two integers.")
        return
    # Read N integers representing coordinates A
    A = list(map(int, input(f"Enter {N} coordinates for A (space-separated): ").strip().split()))
    if len(A) != N:
        print(f"Error: You must enter exactly {N} coordinates for A.")
        return
    # Read Q integers representing coordinates B
    B = list(map(int, input(f"Enter {Q} coordinates for B (space-separated): ").strip().split()))
    if len(B) != Q:
        print(f"Error: You must enter exactly {Q} coordinates for B.")
        return
    # Read k_j values
    print(f"Note: k_j values must be between 1 and {N} (inclusive). Please enter them as space-separated integers.")
    k_j = list(map(int, input(f"Enter {Q} k_j values (1-based index, space-separated): ").strip().split()))
    # Validate k_j values
    if len(k_j) != Q or any(k <= 0 for k in k_j) or any(k > N for k in k_j):
        print(f"Error: All k_j values must be positive integers, match the number of B values ({Q}), and be less than or equal to N ({N}).")
        return
    distances = []
    for j, b in enumerate(B):
        d = [calculate_distance(a, b) for a in A]  # Calculate distances
        d.sort()  # Sort distances
        k_index = k_j[j] - 1  # Convert to zero-based index
        # Check if k_index is within bounds before accessing
        if k_index < 0 or k_index >= len(d):
            print(f"Error: k_j value {k_j[j]} out of bounds for B[{j}]. It should be between 1 and {len(d)}.")
            continue  # Skip to the next B_j if out of bounds
        distances.append(d[k_index])  # Retrieve the k_j-th closest distance
    # Print results
    for distance in distances:
        print(distance)  # Print only the distance value
if __name__ == "__main__":
    main()