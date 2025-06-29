'''
Module for distributing bottles among friends.
'''
from friend import Friend
class BottleDistribution:
    def __init__(self, total_bottles):
        self.total_bottles = total_bottles
    def distribute_bottles(self, num_friends):
        # Ensure num_friends does not exceed total_bottles
        if num_friends > self.total_bottles:
            num_friends = self.total_bottles
        friends_bottles = {}
        for friend_id in range(1, num_friends + 1):
            friend = Friend(friend_id)
            bottles = []
            # Assign bottles based on the binary representation of the friend's ID
            for bottle_id in range(1, self.total_bottles + 1):  # Limit to total bottles
                if (bottle_id - 1) & (1 << (friend_id - 1)):
                    bottles.append(bottle_id)
            friends_bottles[friend_id] = bottles  # Bottles are already in ascending order
        return friends_bottles