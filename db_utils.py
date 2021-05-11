import sqlite3
from sqlite3 import Error
import os



DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
print(DEFAULT_PATH)
def db_connect(db_path=DEFAULT_PATH ) ->  sqlite3.Connection:
    con = sqlite3.connect(db_path)
    return con
