from fastapi import FastAPI
from .crud.application_for_course import crud
app = FastAPI(title="UpTemAll-V2",
              docs_url='/',
              version='2.0')

app.include_router(crud.router)  # application_for_course


@app.get("/root")
async def root():
    return {'msg': "msg"}
