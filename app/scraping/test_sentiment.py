from db_utils import db_connect


con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj


def word_image_gen(cur : object, id ; str):
    sql = "select text from texts where id =  {}".format()
    text = cur.execute(sql).fetchall()


    print(text)

word_image_gen(cur,'c2c7e0952032421c9adc37b3567e1ebb')
