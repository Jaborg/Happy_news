from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj



links_sql = '''
CREATE TABLE IF NOT EXISTS links(
    Id text PRIMARY KEY,
    Title text NOT NULL,
    Link text NOT NULL
)
'''


query = '''SELECT * FROM links'''
print(cur.execute(query).fetchall())
