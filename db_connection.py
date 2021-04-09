from db_utils import db_connect




links_sql = '''
CREATE TABLE IF NOT EXISTS links(
    Id text PRIMARY KEY,
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

def insert_sql(cur,table,values):
    sql = 'INSERT or IGNORE into {table}(Id,Date,Title,Link) VALUES {values};'.format(table=table,values=values)
    cur.execute(sql)

    return

query = '''SELECT * FROM links'''
