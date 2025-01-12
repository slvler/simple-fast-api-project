from fastapi import FastAPI

from routers import user_router, bank_account_router, saved_wallet_router


app = FastAPI()

app.include_router(user_router.user_router)
app.include_router(bank_account_router.bank_router)
app.include_router(saved_wallet_router.saved_wallet)

@app.get("/asdasd")
def all():
    return "hello world11122"

@app.get("/hello-world")
def hello_world():
    return "asdasdasd11"