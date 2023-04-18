from logging_functions.class_logging import Logger
import sqlite3
from sqlite3 import Error
import pandas as pd

class SQLiteActions:
    logger = Logger("SQLiteActions").logger
    def __init__(self, db_full):
        self.db_full = db_full
        self.connect_to_db()
    def connect_to_db(self):
        try:
            self.conn = sqlite3.connect(self.db_full)
            self.cursor = self.conn.cursor()
        except Error as E:
            raise E
    def list_all_tables(self):
        query = """SELECT name FROM sqlite_master WHERE type='table'"""
        self.cursor.execute(query)
        all_tables = self.cursor.fetchall()
        all_tables = [table[0] for table in all_tables]
        return all_tables

    def load_table_data(self, table_name):
        if table_name in self.list_all_tables():
            query = """  SELECT * FROM {table} """.format(table=table_name)
            table_data = pd.read_sql_query(query, con=self.conn)
        else:
            self.logger.info(f'{table_name} is not in {self.db_full},'
                             f' available tables are the following {self.list_all_tables()}')
            table_data = None

        return table_data

    def drop_table(self, table):
        self.logger.info(f'dropping table in {self.db_full} called {table}')
        query = f'DROP TABLE {table}'
        try:
            self.cursor.execute(query)
        except Exception as E:
            self.logger.info(f'Error dropping Table {E}')

    def create_table(self, table, data):
        self.logger.info(f'Creating new table in {self.db_full} called {table}')
        try:
            data.to_sql(name=table, con=self.conn)
        except Exception as E:
            self.logger.info(f'Error Creating Table {E}')

