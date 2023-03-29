from fastapi import FastAPI

app = FastAPI(title="UpTemAll-V2",
              docs_url='/',
              version='2.0')


@app.get("/root")
async def root():
    return {'msg': "msg"}
