from fastapi import FastAPI

app = FastAPI()

from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj




db = 'SELECT * FROM LINKS;'

db = cur.execute(db).fetchall()


@app.get("/")
async def root():
    return {"message": "Abdullah is happy"}


@app.get("/positive_new")
def get_news():
    return db

@app.post("/articles")
def post_news(db: list):
    return 'Hello'
