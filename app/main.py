from fastapi import FastAPI

from app.users.router import router as router_user

app = FastAPI()


@app.get("/")
def home_page():
    return {
        "message": "Добро пожаловать! Пусть эта заготовка станет удобным инструментом для вашей работы и "
                   "приносит вам пользу!"
    }

app.include_router(router_user)
