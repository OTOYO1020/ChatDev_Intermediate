'''
This module contains the Database class.
It provides methods to connect to a database, execute queries, and disconnect from the database.
'''
import sqlite3
class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
    def disconnect(self):
        self.connection.close()
    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result