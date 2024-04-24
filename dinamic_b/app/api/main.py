from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from api.auth.admin_auth import router as auth_router
from api.router.admin_router import router as admin_router
from api.router.course_router import router as course_router
from api.router.for_who_router import router as for_who_router
from api.router.learning_format_router import router as learning_format_router
from api.router.start_group_router import router as start_group_router
from api.router.student_work_router import router as student_work_router
from api.super_user import router as super_user
from api.router.teacher_router import router as teacher_router

from api.CRM.amo import router as amo_router


app = FastAPI(title="MIT",
              version="2.0")

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(course_router)
app.include_router(start_group_router)
app.include_router(learning_format_router)
app.include_router(student_work_router)
app.include_router(for_who_router)
app.include_router(teacher_router)

app.include_router(amo_router)

app.mount('/static/image',
          StaticFiles(directory="static/image"), name="media")

app.mount("/super-user", super_user)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains
    allow_credentials=False,  # Must be False if origins are set to "*"
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Specifying allowed methods
    allow_headers=["Authorization", "Content-Type"],  # Specifying allowed headers
)

