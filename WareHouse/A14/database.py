'''
This file handles database operations.
'''
import sqlite3
class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
    def connect(self):
        '''
        Connects to the database.
        '''
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
    def disconnect(self):
        '''
        Disconnects from the database.
        '''
        self.cursor.close()
        self.connection.close()
    def create_table(self, table_name, columns):
        '''
        Creates a table in the database.
        Parameters:
            table_name (str): Name of the table
            columns (list): List of column names and their data types
        '''
        self.cursor.execute(f"CREATE TABLE {table_name} ({', '.join(columns)})")
        self.connection.commit()
    def insert_data(self, table_name, data):
        '''
        Inserts data into a table.
        Parameters:
            table_name (str): Name of the table
            data (list): List of data to be inserted
        '''
        placeholders = ', '.join(['?' for _ in range(len(data))])
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
        self.connection.commit()