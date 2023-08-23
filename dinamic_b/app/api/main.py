from fastapi import FastAPI
from api.auth.admin_auth import router as auth_router
from api.router.admin_router import router as admin_router

app = FastAPI(title="MIT",
              version="2.0")


app.include_router(auth_router)
app.include_router(admin_router)
