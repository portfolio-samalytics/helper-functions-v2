import sqlite3
from sqlite3 import Error
from src.logging_functions.class_logging import Logger

class CreateNewDBFile:
    logger = Logger("CreateNewDBFile").logger
    def __init__(self, db_full):
        self.db_full = db_full
    def create_db(self):
        self.logger.info(f'Creating new DB file {self.db_full}')
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.db_full)
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()


if __name__ == '__main__':
    CreateNewDBFile(r'C:\Users\samad\OneDrive\Documents\proper trading admin\db_v1').create_db()
