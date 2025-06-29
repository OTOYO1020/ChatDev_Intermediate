'''
Module for handling friendship and blockship logic.
'''
from typing import List, Tuple
def count_friend_candidates(N: int, friendships: List[Tuple[int, int]], blockships: List[Tuple[int, int]]) -> List[int]:
    '''
    Counts the number of friend candidates for each user based on friendships and blockships.
    '''
    # Initialize friendship and blockship data structures
    friends = {i: set() for i in range(1, N + 1)}
    blockers = {i: set() for i in range(1, N + 1)}
    # Populate friendships with validation
    for a, b in set(friendships):  # Convert to set to remove duplicates
        if 1 <= a <= N and 1 <= b <= N:
            friends[a].add(b)  # Set automatically handles duplicates
            friends[b].add(a)  # Set automatically handles duplicates
        else:
            raise ValueError(f"Friendship contains invalid user(s): {a}, {b}")
    # Populate blockships with validation
    for a, b in set(blockships):  # Convert to set to remove duplicates
        if 1 <= a <= N and 1 <= b <= N:
            blockers[a].add(b)  # Set automatically handles duplicates
            blockers[b].add(a)  # Set automatically handles duplicates
        else:
            raise ValueError(f"Blockship contains invalid user(s): {a}, {b}")
    # Count friend candidates
    result = []
    for user in range(1, N + 1):
        candidate_count = 0
        for potential_friend in range(1, N + 1):
            if (potential_friend != user and 
                potential_friend not in friends[user] and 
                potential_friend not in blockers[user]):
                # Count mutual friends
                mutual_friends_count = sum(1 for friend in friends[user] if friend in friends[potential_friend])
                # Check for the four conditions that define a friend candidate
                if (mutual_friends_count >= 2 and  # At least two mutual friends
                    user not in blockers[potential_friend] and  # User is not blocked by potential friend
                    len(friends[potential_friend]) > 0):  # Potential friend has at least one friend
                    candidate_count += 1
        result.append(candidate_count)
    return result