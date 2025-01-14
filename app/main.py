from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home_page():
    return {
        "message": "Добро пожаловать! Пусть эта заготовка станет удобным инструментом для вашей работы и "
                   "приносит вам пользу!"
    }
