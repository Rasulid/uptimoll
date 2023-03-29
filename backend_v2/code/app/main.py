from fastapi import FastAPI
import asyncpg
from .db.database import POSTGRESQL_URL

app = FastAPI(title="UpTemAll-V2",
              docs_url='/',
              version='2.0')


@app.on_event("startup")
async def startUp():
    app.db = await asyncpg.connect(POSTGRESQL_URL)


@app.on_event("shutdown")
async def shutDown():
    await app.db.close()


@app.get("/root")
async def root():
    return {'msg': "msg"}
