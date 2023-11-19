from fastapi import FastAPI

from routers.auth import auth_router
from routers.blog import blog_router
from routers.profile import profile_router
from routers.category import category_router

app = FastAPI()



app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(category_router)
app.include_router(blog_router)