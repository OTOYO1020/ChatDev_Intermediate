'''
This file contains the database class.
'''
import sqlite3
class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value REAL)")
        self.conn.commit()
    def insert_data(self, data):
        """
        Inserts the given data into the database.
        Args:
            data: The data to be inserted into the database.
        """
        for value in data:
            self.cursor.execute("INSERT INTO data (value) VALUES (?)", (value,))
        self.conn.commit()
    def get_data(self):
        """
        Retrieves data from the database.
        Returns:
            The retrieved data from the database.
        """
        self.cursor.execute("SELECT value FROM data")
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]
    def close(self):
        """
        Closes the database connection.
        """
        self.cursor.close()
        self.conn.close()