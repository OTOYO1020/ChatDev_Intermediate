'''
Contains the Query class to represent a query with its type and associated values.
'''
class Query:
    def __init__(self, query_type, x, y=None):
        self.query_type = query_type
        self.x = x
        self.y = y