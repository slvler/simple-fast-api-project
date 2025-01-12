from fastapi import Request, HTTPException

async def router_middleware(request: Request):
    True
    # token = request.headers.get("Authorization")
    # if not token or token != "Bearer mysecuretoken":
    #     raise HTTPException(status_code=403, detail="Unauthorized")
