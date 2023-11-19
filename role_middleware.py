from fastapi import Request

async def roleControl(request: Request, next):
    print("start")
    response = await next(request)
    print("contuines")
