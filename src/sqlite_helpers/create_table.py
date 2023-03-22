from logging_functions.class_logging import Logger
from sqlite3 import Error
import sqlite3

class CreateNewTable:
    logger = Logger("CreateNewTable").logger
    def __init__(self, db_full, new_data, new_table):
        self.db_full = db_full
        self.new_data = new_data
        self.new_table = new_table
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = sqlite3.connect(self.db_full)
        except Error as E:
            raise E

    def create_table(self):
        self.logger.info(f'Creating new table in {self.db_full} called {self.new_table}')
        try:
            self.new_data.to_sql(name=self.new_table, con=self.conn)
        except Exception as E:
            self.logger.info(f'Error Creating Table {E}')
