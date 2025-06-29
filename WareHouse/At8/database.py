'''
This file handles the database operations.
'''
import sqlite3
class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        # Create necessary tables and initialize database here
    def close(self):
        self.conn.close()