'''
Module containing the Friend class for managing individual friends.
'''
class Friend:
    def __init__(self, friend_id):
        self.friend_id = friend_id
        self.bottles = []
    def serve_bottles(self, bottles):
        self.bottles = bottles