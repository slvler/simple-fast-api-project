from fastapi import FastAPI, Request

from routers.auth import auth_router
from routers.blog import blog_router
from routers.profile import profile_router
from routers.category import category_router

app = FastAPI()


# @app.middleware('http')
# async def roleControl(request: Request, next):
#     if request.headers.get('Authorization'):
#         HttpRequestUtil.set_current_user_context(request=request)
#
#     return await next(request)
#
#
# class HttpRequestUtil():
#
#     def get_bearer_token(request: Request):
#         auth_token = request.headers.get('Authorization')
#         if 'Bearer' in auth_token:
#             bearer_token: str = auth_token.split('Bearer')[1].strip()
#             return bearer_token
#     def set_current_user_context(request: Request):
#         jwt_token = HttpRequestUtil.get_bearer_token(request)
#         print(jwt_token)


app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(category_router)
app.include_router(blog_router)