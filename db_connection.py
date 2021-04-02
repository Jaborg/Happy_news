from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj

links_sql = '''
CREATE TABLE IF NOT EXISTS links(
    id integer PRIMARY KEY,
    title varchar NOT NULL,
    link varchar NOT NULL
)
'''

cur.execute(links_sql)


link_sql = "INSERT INTO links (id,title, link) VALUES ({},{}, {})"
