from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj


links_sql = '''
CREATE TABLE IF NOT EXISTS links(
    Id text PRIMARY KEY,
    Date text NOT NULL,
    Title text NOT NULL,
    Link text NOT NULL
)
'''

text_sql = '''
CREATE TABLE IF NOT EXISTS texts(
    Id text PRIMARY KEY,
    Link text NOT NULL,
    Text text NOT NULL
)
'''

def insert_sql(curd,table,values):
    sql = 'INSERT or IGNORE into {table}(Id,Date,Title,Link) VALUES {values};'.format(table=table,values=values)
    curd.execute(sql)

    return
