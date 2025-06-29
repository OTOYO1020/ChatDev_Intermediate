'''
Main application file for the hand movement operations.
'''
from operations import calculate_operations
def main():
    # Read integers N and Q from standard input
    N, Q = map(int, input().split())
    left_hand = 1
    right_hand = 2 if N > 1 else 1  # Ensure right_hand is valid
    total_operations = 0
    for _ in range(Q):
        instruction = input().strip().split()
        h_i = instruction[0]
        t_i = int(instruction[1])
        if h_i == 'L' and left_hand != t_i:  # Check to avoid unnecessary operations
            operations = calculate_operations(left_hand, t_i, N)
            total_operations += operations
            left_hand = t_i
        elif h_i == 'R' and right_hand != t_i:  # Check to avoid unnecessary operations
            operations = calculate_operations(right_hand, t_i, N)
            total_operations += operations
            right_hand = t_i
    print(total_operations)
if __name__ == "__main__":
    main()