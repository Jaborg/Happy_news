from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj



def insert_sql(table : str ,columns : tuple ,values: tuple) -> None:
    con = db_connect()  # connect to the database
    cur = con.cursor() # instantiate a cursor obj
    sql = '''INSERT or IGNORE into {table}({columns}) VALUES {values};
                            '''.format(table=table,columns=columns,values=values)
    cur.execute(sql)
    con.commit()

    return
