from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()
con = sqlite3.connect(r'/Users/jacob/workspace/data_eng/database.sqlite3')
con.row_factory = sqlite3.Row
cur = con.cursor()

templates = Jinja2Templates(directory="templates")



@app.get("/")
async def index(request : Request):
    sql = '''select * from links'''
    rows = cur.execute(sql).fetchall()

    return templates.TemplateResponse("index.html", {"request": request, "news": rows})


@app.get("/Text/{id}")
async def news_detail(request : Request, id):
    cur.execute('''select id,text from texts where id = ?  ''',(id,))
    row = cur.fetchone()

    return templates.TemplateResponse("text.html", {"request": request, "new": row})
# @app.get("/positive_new")
# def get_news():
#     return 'yo'
#
# @app.post("/articles")
# def post_news(db: list):
#     return db
