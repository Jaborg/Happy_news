from fastapi import FastAPI

app = FastAPI()



db = ['yop']

@app.get("/")
async def root():
    return {"message": "Abdullah is happy"}


@app.get("/positive_new")
def get_news():
    return db
