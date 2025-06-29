'''
This file contains database-related operations.
'''
import sqlite3
class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    def connect(self):
        '''
        Connects to the database.
        '''
        self.connection = sqlite3.connect(self.db_name)
    def disconnect(self):
        '''
        Disconnects from the database.
        '''
        if self.connection:
            self.connection.close()
            self.connection = None
    def execute_query(self, query):
        '''
        Executes a SQL query on the database.
        Parameters:
            query (str): SQL query string
        Returns:
            list: Result of the query
        '''
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        else:
            return []