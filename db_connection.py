from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj



links_sql = '''
CREATE TABLE IF NOT EXISTS links(
    Id integer PRIMARY KEY,
    Title varchar NOT NULL,
    Link varchar NOT NULL
)
'''

cur.execute(links_sql)
