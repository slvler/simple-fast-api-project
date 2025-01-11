from fastapi import FastAPI

from routers import user_router

app = FastAPI()

app.include_router(user_router.user_router)


@app.get("/asdasd")
def all():
    return "hello world11122"

@app.get("/hello-world")
def hello_world():
    return "asdasdasd11"