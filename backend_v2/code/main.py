from fastapi import FastAPI
from code.auth.router import router as auth_router
from code.site.router import router as site_router
from code.tasks.router import router as tasks_router
from code.course_applic.routers import router as course_router

app = FastAPI(title="UpTemAll",
              docs_url="/",
              version="2.0")

app.include_router(auth_router)
app.include_router(site_router)
app.include_router(tasks_router)
app.include_router(course_router)
