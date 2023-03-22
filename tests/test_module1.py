from sqlite_helpers.create_db_file import CreateNewDBFile
from sqlite_helpers.create_table import CreateNewTable
from sqlite_helpers.simple_actions import SQLiteBasicActions
import pandas as pd

if __name__ == '__main__':
    db_full = r'C:\Users\samad\OneDrive\Documents\proper trading admin\db_v1'
    db = CreateNewDBFile(db_full=db_full).create_db()
    df = [('sam', 27), ('cat', 28)]
    df = pd.DataFrame(df, columns=['name', 'age'])
    CreateNewTable(db_full=db_full, new_data=df, new_table='test_table_2').create_table()
    basic_actions = SQLiteBasicActions(db_full=db_full)
    tables = basic_actions.list_all_tables()
    table_data = basic_actions.load_table_data(table_name='test_table_1')
    a=1
    a=1


