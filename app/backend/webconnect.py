from fastapi import FastAPI

app = FastAPI()


import sqlite3

con = sqlite3.connect(r'/Users/jacob/workspace/data_eng/database.sqlite3')
cur = con.cursor() # instantiate a cursor obj

sql = '''select * from links'''
x = cur.execute(sql).fetchall()
print(x)



@app.get("/")
async def root():
    return {"Hello": "World"}

#
# @app.get("/positive_new")
# def get_news():
#     return 'yo'
#
# @app.post("/articles")
# def post_news(db: list):
#     return db
