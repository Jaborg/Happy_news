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
    Text text NOT NULL
)
'''

def insert_sql(table,columns,values):
    con = db_connect()  # connect to the database
    cur = con.cursor() # instantiate a cursor obj
    sql = '''INSERT or IGNORE into {table}({columns}) VALUES {values};
                            '''.format(table=table,columns=columns,values=values)
    print(sql)
    cur.execute(sql)
    con.commit()

    return
sql = 'select text from texts;'
