from fastapi import FastAPI

app = FastAPI()






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
