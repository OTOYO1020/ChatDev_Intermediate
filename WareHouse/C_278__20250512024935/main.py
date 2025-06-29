'''
Main entry point for the Twidai application.
'''
from typing import List, Tuple
from user_manager import UserManager
def process_twidai_operations(N: int, Q: int, operations: List[Tuple[int, int, int]]) -> List[str]:
    user_manager = UserManager(N)  # Create an instance of UserManager with N users
    results = []
    for operation in operations:
        T_i, A_i, B_i = operation
        if T_i == 1:
            user_manager.follow(A_i, B_i)  # Use UserManager's follow method
        elif T_i == 2:
            user_manager.unfollow(A_i, B_i)  # Use UserManager's unfollow method
        elif T_i == 3:
            if user_manager.check_mutual(A_i, B_i):  # Use UserManager's check_mutual method
                results.append("Yes")
            else:
                results.append("No")
    return results
if __name__ == "__main__":
    # Example usage
    N = 5  # Number of users
    Q = 5  # Number of operations
    operations = [
        (1, 1, 2),  # User 1 follows User 2
        (1, 2, 1),  # User 2 follows User 1
        (3, 1, 2),  # Check mutual following between User 1 and User 2
        (2, 1, 2),  # User 1 unfollows User 2
        (3, 1, 2)   # Check mutual following between User 1 and User 2
    ]
    results = process_twidai_operations(N, Q, operations)
    for result in results:
        print(result)