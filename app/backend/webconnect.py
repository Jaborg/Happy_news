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



#orm



@app.get("/")
async def index(request : Request):
    sql = '''select count(distinct link) Total,ROUND(avg(polarity),2) Average from links l
                    inner join polarity p on p.id = l.id where length > 0 and News = 'BBC' '''
    bbc = cur.execute(sql).fetchone()

    sql = '''select count(distinct link) Total,ROUND(avg(polarity),2) Average from links l
                        inner join polarity p on p.id = l.id where length > 0 and News = 'Guardian' '''
    guardian = cur.execute(sql).fetchone()

    sql = '''select count(distinct link) Total,ROUND(avg(polarity),2) Average from links l
                            inner join polarity p on p.id = l.id where length > 0 and News = 'DailyMail' '''
    daily = cur.execute(sql).fetchone()


    return templates.TemplateResponse("frontpage.html",
        {"request":request ,
        "bbc": bbc,
        "guardian" : guardian,
        "daily" : daily})



@app.get("/repository")
async def index(request : Request):
    sql = '''select * from links l inner join polarity p on p.id = l.id where length > 0'''
    rows = cur.execute(sql).fetchall()

    return templates.TemplateResponse("links.html", {"request": request, "news": rows})



@app.get("/Text/{id}")
async def news_detail(request : Request, id):
    cur.execute('''select id,text from texts where id = ?
    ''',(id,))
    row = cur.fetchone()

    cur.execute('''select ROUND(polarity,2) polarity,length from polarity where id = ?
    ''',((id,)))

    pol = cur.fetchone()

    return templates.TemplateResponse("text.html",
    {"request": request,
    "news": row,
    "polarity" : pol})
