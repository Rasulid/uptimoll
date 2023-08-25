from fastapi import FastAPI
from api.auth.admin_auth import router as auth_router
from api.router.admin_router import router as admin_router
from api.router.start_group_router import router as start_group_router
from api.router.course_router import router as course_router
from api.router.learning_format_router import router as learning_format_router
from api.router.student_work_router import router as student_work_router
from api.router.for_who_router import router as for_who_router

app = FastAPI(title="MIT",
              version="2.0")


app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(course_router)
app.include_router(start_group_router)
app.include_router(learning_format_router)
app.include_router(student_work_router)
app.include_router(for_who_router)

