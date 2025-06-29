'''
Main application file for the user following system without GUI.
'''
from user_manager import UserManager  # Import the UserManager class
def process_operations(N, Q, operations):
    if N <= 0 or Q <= 0:
        raise ValueError("N and Q must be positive integers.")
    users = set()  # Use a set to handle arbitrary user IDs
    for operation in operations:
        if len(operation) != 3:
            raise ValueError("Each operation must contain exactly three integers.")
        users.add(str(operation[1]))  # Convert user A_i to string
        users.add(str(operation[2]))  # Convert user B_i to string
    user_manager = UserManager(users)  # Create an instance of UserManager with all users initialized
    results = []
    for operation in operations:
        T_i, A_i, B_i = map(str, operation)  # Convert A_i and B_i to strings
        if T_i not in ['1', '2', '3']:  # Check as strings
            raise ValueError(f"Invalid operation type {T_i}. Must be 1, 2, or 3.")
        # Check if A_i and B_i are valid users before proceeding
        if A_i not in users or B_i not in users:
            raise ValueError(f"User ID {A_i} or {B_i} is not valid.")
        if T_i == '1':  # Follow operation
            user_manager.follow(A_i, B_i)
        elif T_i == '2':  # Unfollow operation
            user_manager.unfollow(A_i, B_i)
        elif T_i == '3':  # Check status operation
            result = user_manager.check_status(A_i, B_i)
            results.append(result)  # Append the result directly
    for result in results:
        print(result)
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    N, Q = map(int, input_data[0].split())
    operations = [list(map(int, line.split())) for line in input_data[1:]]
    process_operations(N, Q, operations)