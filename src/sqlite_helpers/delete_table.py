from logging_functions.class_logging import Logger
from sqlite3 import Error
import sqlite3

class DeleteTable:
    logger = Logger("DeleteTable").logger
    def __init__(self, db_full, drop_table):
        self.db_full = db_full
        self.drop_table = drop_table
        self.query = f'DROP TABLE {self.drop_table}'
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = sqlite3.connect(self.db_full)
            self.cursor = self.conn.cursor()
        except Error as E:
            raise E

    def delete_table(self):
        self.logger.info(f'dropping table in {self.db_full} called {self.drop_table}')
        try:
            self.cursor.execute(self.query)
        except Exception as E:
            self.logger.info(f'Error dropping Table {E}')
